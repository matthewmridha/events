from django.db import models
from users.models import UserProfile, Sport
from teams.models import Team

# Create your models here.
class HostName(models.Model):
    name = models.CharField( max_length=164 )
    logo = models.FileField( upload_to='media', blank=True )
    def __str__(self):
        return self.name

class EventType(models.Model):
    name = models.CharField( max_length=164 )

    def __str__(self):
        return self.name

class Events(models.Model):
    host = models.ForeignKey( HostName, on_delete=models.CASCADE, null=True )
    event_type = models.ForeignKey( EventType, on_delete=models.CASCADE, null=True )
    team_event = models.BooleanField( default=False )
    min_team = models.IntegerField(  blank=True )
    max_team = models.IntegerField( blank=True )
    sport = models.CharField( blank=True, null=True, max_length=64 )
    title = models.CharField( max_length=256 )
    description = models.TextField( blank=True )
    date = models.DateField( blank=True )
    time = models.TimeField( blank=True )
    end_date = models.DateField( blank=True, null=True )
    end_time = models.TimeField( blank=True, null=True )
    location = models.CharField( max_length=256 )
    city = models.CharField( max_length=120, blank=True )
    address = models.CharField( max_length=16, blank=True )
    banner = models.ImageField( upload_to='media', blank=True )
    poster = models.ImageField( upload_to='media', blank=True )
    registrants = models.ManyToManyField( UserProfile, blank=True, related_name='registrants' )
    teams = models.ManyToManyField( Team, blank=True, related_name='registered_teams')
    payment_required = models.BooleanField( default=False )
    price = models.DecimalField( blank=True, null=True, max_digits=6, decimal_places=2 )
    event_created = models.DateTimeField( auto_now=True )
    def __str__( self ):
        return self.title
