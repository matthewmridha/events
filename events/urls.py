from django.urls import path, include
from . import views

urlpatterns = [
    path( "", views.home, name="home" ),
    path( "<int:event_id>", views.event, name="event" ),
    path( "<int:event_id>/register", views.register, name="register" ),
    path( "<int:event_id>/register_team", views.register_team, name="register_team" ),
    path( "<int:event_id>/unregister", views.unregister, name="unregister" ),
    path( "<int:event_id>,<int:team_id>/unregister_team", views.unregister_team, name="unregister_team")
]

