from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView
from django import forms
from .forms import UserProfileForm
from django.utils import timezone
from allauth.account.decorators import verified_email_required
from .models import UserProfile
from events.views import getUserProfile, getUserName
from django.contrib import messages 
from datetime import datetime
from django.db.models import Q

# Create your views here.

@verified_email_required
def profileView( request ):
    name = getUserName( request )
    if request.method == "POST":
        if request.user.is_authenticated:
                form = UserProfileForm( request.POST )
                user = request.user
                if form.is_valid():
                    model_instance = form.save( commit=False )
                    model_instance.user = user
                    model_instance.save()
                    form.save_m2m()
                    messages.info( request, "Thank you for completing your profile" )
                    return HttpResponseRedirect(reverse("home"))
                else:
                    form = UserProfileForm()
                    context = {
                        "form" : form,
                        "name" : name
                    }
                    messages.error( request, "Please fill out all the Fields" )
                    return render( request, "profile.html", context )
    else:
        try:
            profile = UserProfile.objects.get( user=request.user )
        except ObjectDoesNotExist:
            form = UserProfileForm()
            context = {
                "form" : form,
                "name" : name
            }
            return render( request, "profile.html", context )
        now = datetime.now()
        upcoming_events = profile.registrants.filter(Q(date__gte=now.date())).order_by("-date", "-time") or None
        past_events =  profile.registrants.filter(Q(date__lt=now.date())) or None
        teams = profile.team_member.all() or None
        team_events = []
        if teams != None:
            for team in teams:
                for event in team.registered_teams.filter(Q(date__gte=now.date())):
                    team_events.append( event )
        managed_teams = profile.team_manager.all() or None
        context = {
            "profile" : profile,
            "name" : name, 
            "upcoming_events" : upcoming_events,
            "past_events" : past_events,
            "teams" : teams,
            "managed_teams" : managed_teams,
            "team_events" : team_events,
        }
        return render( request, "profile.html", context )          
