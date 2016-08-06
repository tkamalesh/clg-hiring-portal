from django.contrib import admin

# Register your models here.
from .models import Candidate,Application

admin.site.register(Candidate)
admin.site.register(Application)
