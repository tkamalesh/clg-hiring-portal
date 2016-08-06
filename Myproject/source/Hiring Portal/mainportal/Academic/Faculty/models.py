from django.db import models
from django.contrib.auth.models import User
from faculty_portal.models import Application
# Create your models here.

class Review(models.Model):
	RatingScale = ((1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"),(5,"6"),(7,"7"),(8,"8"),(9,"9"),(10,"10"),)
	strength = models.IntegerField(choices=RatingScale)
	area_of_expertize = models.IntegerField(choices=RatingScale)
	appropriateness = models.IntegerField(choices=RatingScale,blank=True)
	recommendation = models.IntegerField(choices=RatingScale)
	specific_recommendation = models.CharField(max_length=200,blank=True)
	comments = models.CharField(max_length=100) 
	applications = models.ForeignKey(Application)

class FacultyReview(models.Model):
	class Meta:
		unique_together = (('faculty', 'application'),)
	faculty = models.ForeignKey(User)
	application = models.ForeignKey(Application)
	filled_status = models.BooleanField(default = False)
