from django.db import models
from django.contrib.auth.models import User
from faculty_portal.models import Candidate,Application

# Create your models here.

class FacultyStaff(models.Model):
	user = models.OneToOneField(User)
	def __str__(self):
		return self.user.username
