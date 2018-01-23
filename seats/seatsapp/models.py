from django.db import models

class Layout(models.Model):

	class Meta:
		unique_together = (('rank'), ('row'), ('seat'))

	rank = models.IntegerField()
	row = models.IntegerField()
	seat = models.IntegerField()
	name = models.CharField(max_length=255)
	section = models.CharField(max_length=255, null=True)

class Flag(models.Model):
	class Meta:
		unique_together = (('seat'), ('flag'))

	seat = models.ForeignKey(Layout, on_delete=models.CASCADE)
	flag = models.CharField(max_length=255)

class Seating(models.Model):
	class Meta:
		unique_together = (('seat'), ('event'), ('occupant'))

	seat = models.ForeignKey(Layout, on_delete=models.CASCADE)
	event = models.IntegerField(primary_key=True)
	occupant = models.IntegerField(null=True)
