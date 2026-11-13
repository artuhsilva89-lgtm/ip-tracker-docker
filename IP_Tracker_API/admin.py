from django.contrib import admin
from IP_Tracker_API.models import IP_Tracker

@admin.register(IP_Tracker)
class IP_TrackerAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'vlan','device', 'status')
    






