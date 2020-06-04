from django.contrib import admin
from .models import Events, HostName, EventType
# Register your models here.

admin.site.register( Events )
admin.site.register( HostName )
admin.site.register( EventType )
