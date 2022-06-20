from django.contrib import admin

from .models import Map,Location,Event,NPC
# Register your models here.
admin.site.register(Map)
admin.site.register(Location)
admin.site.register(Event)
admin.site.register(NPC)
