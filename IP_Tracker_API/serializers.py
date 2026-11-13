from rest_framework import serializers
from IP_Tracker_API.models import IP_Tracker

class Ip_TrackerSerializers(serializers.ModelSerializer):
    class Meta:
        model = IP_Tracker
        fields = '__all__'