from django.shortcuts import render
from django.http import HttpResponse
from users.models import UserProfile
from events.models import Events
from events.views import getUserProfile, getUserName
from allauth.account.decorators import verified_email_required
from django.core.exceptions import PermissionDenied
import csv


# Create your views here.



def download( request ):
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(
        [ 
            'Created', 
            'Email', 
            'First Name', 
            'Last Name', 
            'Gender', 
            'Phone', 
            'Area', 
            'Sport'
        ]
    )
    for profile in UserProfile.objects.all():
        email = profile.user.email
        firstname = profile.first_name
        lastname = profile.last_name
        gender = profile.gender
        phone = profile.phone
        area = profile.area
        created = profile.profile_created.strftime("%c")
        sport = []
        for s in profile.sport.all():
            sport.append(s.sport)
        
        writer.writerow(
            [ 
                created,
                email, 
                firstname, 
                lastname, 
                gender, 
                phone, 
                area, 
                sport
            ] 
        )

    return response

@verified_email_required
def data_view( request ):
    user = request.user
    name = getUserName( request )
    if user.is_superuser or user.is_staff:
        staff = True
        events = Events.objects.all() or None
        
    else:
        raise PermissionDenied
    context = {
        "name" : name,
        "staff" : staff,
        "events" : events,
    }
    return render( request, "data_view.html", context )
    
