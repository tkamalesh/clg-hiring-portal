from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from time import time
from userroles.models import UserRole
# Create your models here.



#For uploading files

def get_upload_filename_resume(instance,filename):
	return "uploaded_files/resume/%s_%s" % (str(time()).replace('.','_'),filename)

def get_upload_filename_cover(instance,filename):
	return "uploaded_files/coverletter/%s_%s" % (str(time()).replace('.','_'),filename)

def get_upload_filename_pub(instance,filename):
	return "uploaded_files/publications/%s_%s" % (str(time()).replace('.','_'),filename)


class Application(models.Model):
	name = models.CharField(max_length=100)
	status = models.IntegerField(default=0)
	candidate = models.OneToOneField('Candidate',blank=True)
	

	#0 - When the application is with the Staff.
	#1 - Application is validated and goes to Hiring Committee. HC can view it now.
	#2 - Hiring Committee forwards it to Faculty. The Faculty can now view this application.
	#-1 - The application is rejected by Staff.
	ResearchLabList=(("SPCRC","Signal Processing and Communications Research Center"),("CDE","Center for Data Engineering"),("LTRC","Language Technologies Research Center"),("RRC","Robotics Research Center"),("CSTAR","Center for Security, Theory and Algorithms"),("SERC","Software Engineering Research Center"),
	)
	applied_researchLab = models.CharField(max_length=100,choices=ResearchLabList,blank=False)
	summarysheet = models.CharField(max_length=100,blank=True)	
	allowed_level = models.IntegerField(default=0)
	applied_creation_time = models.DateTimeField(default=timezone.now)	
	stage_waiting_time = models.DateTimeField(default=timezone.now)	
	#-1 is the rejection by Staff
	#0 is the initial stage when he doesen't fill his profile.
	#1 is the stage where the Staff can view the profile.
	#2 is the stage where the Hiring Committee can view the profile.
	#3 is the stage where the Faculty can see it.
	# 4 is the stage when all the Faculty have filled the review
	# 5 is the stage where the application is in INTERVIEW stage.
	#-2 is rejection by Hiring Committee	

	def __unicode__(self):
		return self.name


class Candidate(models.Model):
	#Relation with other models
	user = models.OneToOneField(User) 
	#staff = models.ForeignKey('Staff.FacultyStaff',blank=True)
	#role = models.OneToOneField(UserRole,unique = False, blank=True)
	
	#Custom candidate fields
	givenname = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	age = models.SmallIntegerField()
	current_affliation = models.CharField(max_length=100)
	
	Complete = 'complete'
	Ongoing = 'ongoing'
	ABD = 'abd'
	NONE = 'none'
	PHD_STATUS = (
	    (Complete, 'Completed'),
	    (Ongoing, 'Ongoing'),
	    (ABD, 'All but dissertation'),
	    (NONE, 'None'),
	)
	status_of_phd = models.CharField(max_length=21,
                                  choices=PHD_STATUS,
                                  default=Complete)
	institue_of_phd = models.CharField(max_length=100,blank=True)
	date_of_completion = models.DateField(auto_now=False,default=datetime.date.today,blank=True)
	expected_date_of_completion = models.DateField(auto_now=False,default=datetime.date.today,blank=True)
	
	experience_place = models.CharField(max_length=100,blank=True)
	experience_position = models.CharField(max_length=100,blank=True)
	experience_duration = models.CharField(max_length=20,blank=True)

	resume = models.FileField(upload_to=get_upload_filename_resume,blank=True)  #RESUME' IS COMPULSORY
	cover_letter = models.FileField(upload_to=get_upload_filename_cover,blank=True)

	publication1 = models.FileField(upload_to=get_upload_filename_pub,blank=True)
	publication2 = models.FileField(upload_to=get_upload_filename_pub,blank=True)
	publication3 = models.FileField(upload_to=get_upload_filename_pub,blank=True)
	publication4 = models.FileField(upload_to=get_upload_filename_pub,blank=True)
	publication5 = models.FileField(upload_to=get_upload_filename_pub,blank=True)
	
	pub_title1 = models.CharField(max_length=100,blank=True)
	pub_title2 = models.CharField(max_length=100,blank=True)
	pub_title3 = models.CharField(max_length=100,blank=True)
	pub_title4 = models.CharField(max_length=100,blank=True)
	pub_title5 = models.CharField(max_length=100,blank=True)
	
	def __unicode__(self):
		return self.givenname


