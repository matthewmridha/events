from django.urls import path, include
from . import views

urlpatterns = [
    path( "", views.data_view, name="data_view" ),
    path( "download", views.download, name="download"),
]