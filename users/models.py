from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class CustomUser(AbstractUser):
    # add additional fields in here

    def __str__(self):
        return self.email

class Area(models.Model):
    area = models.CharField( max_length=164, unique=True)

    def __str__(self):
        return self.area

class Sport(models.Model):
    sport = models.CharField( max_length=164, unique=True)

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
    phone = models.CharField( max_length=17, blank=True )
    first_name = models.CharField( max_length=64 )
    last_name = models.CharField( max_length=64 )
    gender = models.CharField( choices=GENDER_CHOICES, max_length=8, blank=False, default='Unspecified' )
    birthday = models.DateField ( auto_now=False, auto_now_add=False )
    area = models.ForeignKey( Area, on_delete=models.CASCADE )
    city = models.CharField( max_length=164 )
    country = models.CharField( max_length=164 )
    sport = models.ManyToManyField( Sport )
    communication = models.BooleanField( default=True )
    extra = models.CharField( max_length=250, null=True, blank=True )
    profile_created = models.DateTimeField( auto_now=True, auto_now_add=False )

    def __str__(self):
        return (f"{self.user.email}")

    



    