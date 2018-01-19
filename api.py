import copy
import collections

class Rank:
    def __init__(self, rankno, layout):
        self.id = rankno
        self.layout = copy.copy(layout)
        self.flags = collections.defaultdict(list)
        self.seating = copy.copy(layout)

        for i in range(len(self.seating)):
            for j in range(len(self.seating[i])):
                self.seating[i][j] = None


    def seat_preference(self, group, no_people, preference):
        lr = True
        seats = []
        pref_found = False

        if preference not in self.flags:
            return False

        for i in range(len(self.seating)):
            if lr:
                ran = range(len(self.seating[i]))
            else:
                ran = range(len(self.seating[i]) - 1, -1, -1)

            for j in ran:
                if (i, j) in self.flags["blocked"]:
                    seats = []
                    continue

                if self.seating[i][j] is None:
                    seats.append((i, j))

                if (i, j) in self.flags[preference]:
                    pref_found = True

                if len(seats) >= no_people:
                    if pref_found:
                        for i, j in seats:
                            self.seating[i][j] = group
                        return True
                    else:
                        seats.pop(0)

            lr = not lr

        if not pref_found:
            self.seat(group, no_people)

        return False

    def seat(self, group, no_people):
        lr = True
        seats = []

        for i in range(len(self.seating)):
            if lr:
                ran = range(len(self.seating[i]))
            else:
                ran = range(len(self.seating[i]) - 1, -1, -1)

            for j in ran:
                if (i, j) in self.flags["blocked"]:
                    seats = []
                    continue

                if self.seating[i][j] is None:
                    seats.append((i, j))

                if len(seats) >= no_people:
                    for i, j in seats:
                        self.seating[i][j] = group

                    return True

            lr = not lr

        return False

    def subsetsum(self, array, num):
        if num < 1:
            return None
        elif len(array) == 0:
            return None
        else:
            if array[0][1] == num:
                return [array[0]]
            else:
                with_v = self.subsetsum(array[1:],(num - array[0][1]))
                if with_v:
                    return [array[0]] + with_v
                else:
                    return self.subsetsum(array[1:],num)

    def seat_in_row(self, row, group, no_people):
        for seat in range(len(row)):
            if row[seat] is None:
                row[seat] = group
                no_people -= 1

            if no_people <= 0:
                return True

        return False

    def rank_seat(self, rank, groups):
        for group in range(len(groups)):
            no_people = groups[group]
            self.seat(group + 1, no_people)

    def rank_seat_preference(self, rank, groups):
        groups = list(zip(range(len(groups)), copy.copy(groups)))
        groups = sorted(groups, key = lambda x: x[1][0] if x[1][1] else 0)
        preference_groups = [x for x in groups if x[1][1]]
        rest_groups = [x for x in groups if not x[1][1]]


        for group, info in preference_groups:
            no_people = info[0]
            preference = info[1]
            self.seat_preference(group + 1, no_people, preference)

        for group, info in rest_groups:
            no_people = info[0]
            preference = info[1]

            self.seat(group + 1, no_people)

    def rank_seat_nowrap(self, rank, groups):
        groups = list(zip(range(len(groups)), copy.copy(groups)))

        for row in self.seating:
            subsetsum = self.subsetsum(groups, len(row))

            if subsetsum is []:
                #We could not fit these people in rows without a gap.
                #We will have to use the regular algorithm.
                return rank_seat(rank, groups)

            for group, no_people in subsetsum:
                self.seat_in_row(row, group + 1, no_people)

            groups = [x for x in groups if x not in subsetsum]

    def apply_flag(self, flag, row, seat):
        self.flags[flag].append((row - 1, seat - 1))
        return True

    def print_seating(self):
        for row in self.seating:
            for seat in row:
                print(seat, end= ' ')

            print()

a = [[1, 2, 3, 4, 5, 6, 7, 8],
 [1, 2, 3, 4, 5, 6, 7, 8],
 [1, 2, 3, 4, 5, 6, 7, 8]]

d = Rank(1, a)
for i in range(1, 4):
    d.apply_flag("aisle", i, 1)
    d.apply_flag("aisle", i, 8)

d.apply_flag("balcony", 3, 5)
#d.rank_seat(1, [1, 3, 4, 4, 5, 1, 2, 4])
#d.rank_seat_preference(1, [(1, None), (3, None), (4,  "aisle"), (4, None), (5,None), (1, None), (2, "balcony"), (4, None)])
d.rank_seat_nowrap(1, [1, 3, 4, 4, 5, 1, 2, 4])
d.print_seating()
