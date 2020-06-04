from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from users.models import UserProfile
from .models import Events
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from allauth.account.decorators import verified_email_required
from django.contrib import messages
from teams.models import Team

 
# Create your views here.

def getUserProfile( request ):
    if request.user.is_authenticated:
        user = request.user
        try:
            profile = UserProfile.objects.get( user=user )
        except UserProfile.DoesNotExist:
            profile = None
    else:
        profile = None
    return profile

def getUserName( request ):
    profile = getUserProfile( request )
    if profile == None:
        if request.user.is_authenticated:
            name = request.user.email
        else:
            name = "Guest"
    else:
        name = f"{profile.first_name}  {profile.last_name}"
    return name
    
def home( request ):
    name = getUserName( request )
    context = {
        "events" : Events.objects.all(),
        "name" : name,
    }
    return render( request, "home.html", context )

def event( request, event_id ):
    try:
        event = Events.objects.get( pk=event_id )
    except Events.DoesNotExist:
        raise Http404( "Event Does Not Exist" )
    profile = getUserProfile( request )
    if profile == None:
        registered = False
        teams_managed = None
    else:
        if event.team_event:
            teams_registered = event.teams.all()
        else:
            teams_registered = None
        teams_managed = profile.team_manager.all()
        if profile.registrants.filter( pk=event_id ).count() == 1:
            registered = True
        else:
            registered = False
    name = getUserName( request )
    context = {
        "name" : name,
        "event" : event,
        "profile" : profile,
        "registered" : registered,
        "teams_managed" : teams_managed,
        "teams_registered" : teams_registered,
    }
    return render( request, "event.html", context )

@verified_email_required
def register( request, event_id ):
    event = get_object_or_404( Events, pk=event_id )
    profile = getUserProfile( request )
    if profile == None:
        message = "Please complete your profile <a href='{% url 'profileView' %}'>here</a> before registering for an event"
        name = getUserName( request )
        context = {
            "name" : name,
            "event" : event,
        }
        messages.add_message( request, messages.INFO, message )
        return render( request, "event.html", context)
    else:
        if profile.registrants.filter( pk=event_id ).count() == 1:
            message = f"You are already Registered to this event"
            messages.add_message( request, messages.INFO, message )
            return event( request, event_id )
        else:
            email = request.user.email
            event_name = event.title
            event_date = event.date
            name = f"{profile.first_name} {profile.last_name}"
            subject =  "Registration Confirmation"
            message = f"Hello {name}, \n You are now registered to {event_name} to be held on {event_date} "
            email_from = "matthew.mridha@gmail.com"
            email_to = email
            event.registrants.add( profile )
            send_mail(
                subject,
                message,
                email_from,
                [email_to],
                fail_silently=False,
            )
            message = f"Registered to {event_name} successfully"
            messages.add_message( request, messages.INFO, message )
            return home( request )
    
@verified_email_required
def unregister( request, event_id ):
    event = get_object_or_404( Events, pk=event_id )
    profile = getUserProfile( request )
    if profile == None:
        message = "Please complete your profile <a href='{% url 'profileView' %}'>here</a> before registering for an event"
        messages.add_message( request, messages.INFO, message )
        return event( request, event_id )
    else:
        if profile.registrants.filter( pk=event_id ).count() == 1:
            event.registrants.remove( profile )
            email = request.user.email
            event_name = event.title
            event_date = event.date
            name = f"{profile.first_name} {profile.last_name}"
            subject =  f"Unregisterd from {event_name}"
            message = f"Hello {name}, \n You have unregistered from {event_name} to be held on {event_date} "
            email_from = "matthew.mridha@gmail.com"
            email_to = email
            send_mail(
                subject,
                message,
                email_from,
                [email_to],
                fail_silently=False,
            )
            message = f"You have unregisterd from {event.title}"
            messages.add_message( request, messages.INFO, message )
            return home( request )
        else:
            message="Oops... Something went wrong. Please contact us."
            messages.add_message( request, messages.INFO, message )
            return event( request, event_id )

@verified_email_required
def register_team( request, event_id ):
    if request.method == "POST":
        event_id = event_id
        team_id = request.POST.get( "team_select" )
        event = get_object_or_404( Events, pk=event_id )
        team = get_object_or_404( Team, pk=team_id )
        team_members = team.members.all()
        event.teams.add(team)
        for member in team_members:
            name = f"{member.first_name} {member.last_name}"
            subject =  f"Registerd to {event.title}"
            message = f"Hello {name}, \n Your team {team.name} have been registered to {event.title} "
            email_from = "matthew.mridha@gmail.com"
            email_to = member.user.email
            send_mail(
                subject,
                message,
                email_from,
                [email_to],
                fail_silently=False,
            )
        message=f"Registered to {event.title}"
        messages.add_message( request, messages.INFO, message )
        return HttpResponseRedirect( reverse( "event", args=[ event_id ] ) )
    else:
        return HttpResponseRedirect( reverse( "home" ) )

@verified_email_required
def unregister_team( request, event_id, team_id ):
    event = get_object_or_404( Events, pk=event_id )
    team = get_object_or_404( Team, pk=team_id )
    event.teams.remove( team )
    return HttpResponseRedirect( reverse("team_view", args=[ team_id ]) )
