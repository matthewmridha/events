from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    # add additional fields in here

    def __str__(self):
        return self.email

class Area(models.Model):
    area = models.Charfield( max_length=164 )

    def __str(self):
        return self.area

class Sport(models.Model):
    sport = models.Charfield( max_length=164 )

    def __str__(self):
        return self.sport

class UserProfile(models.Model):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'
    GENDER_CHOICES = (
        ( Male, 'Male' ),
        ( Female, 'Female' ),
        ( Other, 'Other' )
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField( max_length=120 )
    phone = models.Charfield( max_length=16 )
    first_name = models.CharField( max_length=64 )
    last_name = models.CharField( max_length=64 )
    gender = models.CharField( choices=GENDER_CHOICES, max_length=8 )
    area = models.ForeignKey( Area, on_delete=models.CASCADE )
    sport = models.ManyToManyField( Sport )
    extra = models.CharField( max_length=250, null=True, blank=True )
    profile_complete = models.BooleanField( default=False )



    