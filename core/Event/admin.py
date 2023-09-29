from django.contrib import admin

from .models import Event

from .models import EventLog

# Register your models here.

admin.site.register(Event)

admin.site.register(EventLog)
