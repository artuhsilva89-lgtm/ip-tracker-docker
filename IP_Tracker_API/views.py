from rest_framework import generics
from IP_Tracker_API.serializers import Ip_TrackerSerializers
from IP_Tracker_API.models import IP_Tracker

class IpTrackerListCreateView(generics.ListCreateAPIView):
    queryset = IP_Tracker.objects.all()
    serializer_class = Ip_TrackerSerializers
    
class IpTrackRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IP_Tracker.objects.all()
    serializer_class = Ip_TrackerSerializers

# Create your views here.