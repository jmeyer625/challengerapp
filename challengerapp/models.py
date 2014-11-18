import datetime
from django.db import models

# Create your models here.

class Challenge(models.Model):
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	title = models.CharField(max_length=50)

	def __unicode__(self):
		return self.title

	def create_days(self, numdays):
		for i in range(0,numdays):
			day = Day(day_sequence=i+1, challenge=self)
			day.save()

class Day(models.Model):
	day_sequence = models.IntegerField()
	challenge = models.ForeignKey(Challenge)

	def __unicode__(self):
		return self.challenge.title+str(self.day_sequence)

class Post(models.Model):
	title = models.CharField(max_length=50)
	body = models.TextField()
	day = models.ForeignKey(Day)
	pub_date = models.DateTimeField('date published', null=True)

	def __unicode__(self):
		return self.title+'_'+self.day.challenge.title+'_'+str(self.day.day_sequence)

class Task(models.Model):
	description = models.CharField(max_length=200)
	day = models.ForeignKey(Day, default=None)
	challenge = models.ForeignKey(Challenge, default=None)
	post = models.ForeignKey(Post, default=None)
	completed = models.BooleanField(default=False)
	completed_at = models.DateTimeField(null=True)

	def __unicode__(self):
		return self.description