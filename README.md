# Theater-Seating-Algorithm-API
1. Create a datastructure that defines a seating layout for a hall in a venue:     
different sections (main hall, 1st balcony, 2nd balcony)     
different ranks defined across sections (1st rank, 2nd rank 3rd rank)      
so the 1st rank could be on both the main hall and 1st balcony - they're not restricted by section      
rows of seats, numbered by row, seat. Seats can be differently numbered: sometimes 1 .. 6, 
sometimes 1,3,5,6,4,2​​     
bonus:      Support additional properties on seats:         
aisle seat         
frontrow seat         
high seat (e.g. on balcony) 

2. Create an algorithm that given a list of "groups of users" per rank (basically sizes,
e.g. (1, 3, 4, 4, 5, 1, 2, 4) in a specific order, tries to place the users in their seats, 
e.g.   1 2 2 2 3 3 3 3  
       5 5 5 5 4 4 4 4  
       5 6 7 7 8 8 8 8  
 So the group of size 1 at index 1 gets the frontmost left seat. 
 Then the group at index 2 of 3 people next to it, until the row fills and wraps to the next row and fills in the other direction.  
 You can assume that sum(groups_of_users_for_rank) &lt;= seats_in_that_rank      
 
 Bonus: take preferences into account based on seat properties.
 E.g. ("aisle", 2) would mean a group of 2 where one of the members whishes to be near the aisle      
 
 Bonus: Allow seats to be blocked (e.g. for technical purposes). 
 This means a group should not be split across such a block   
 
 3. Improve the algorithm in such a way that no individual people sit alone. 
 In the above example this happened with the group​ ​at index 5 where a single individual sits on the
 3rd row (eventhough the rest of the group is in front of him)   
 1 2 2 2 3 3 3 3  
 8 8 8 8 4 4 4 4  
 5 5 5 5 5 6 7 7   
 would be a better solution. 
 Try to preserve the order as much as possible because the lowest numbers should get the "best" (frontmost) seats  
 
 4. Create a django model to store the seating layout (generically) and the seating allocation. 
 The allocation should be separate (think of different shows in the same theater) 
 
 5. Design / Create a REST API to retrieve the layout the allocations. 
 Authentication / security is not a requirement (everything public)  
 
 6. Create a simple consumer of this API that renders the allocations to a visually understandable HTML layout 

