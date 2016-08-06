from django.db import models
from django.contrib.auth.models import User
import datetime
import django.utils.timezone
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=django.utils.timezone.now)
    first_timelogin = models.BooleanField(default=True)      
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural=u'User profiles'
