from django.db import models
from users.models import UserProfile
from users.models import Sport

# Create your models here.

class Team(models.Model):
    name = models.CharField( max_length=164 )
    logo = models.ImageField( upload_to='media', blank=True )
    description = models.TextField( blank=True, )
    sport = models.ForeignKey( Sport, on_delete=models.CASCADE, default=1 )
    manager = models.ForeignKey( UserProfile, related_name='team_manager', on_delete=models.CASCADE )
    members = models.ManyToManyField( UserProfile, blank=True, related_name='team_member' )
    password = models.CharField( max_length=50 )

    def __str__(self):
        return self.name

