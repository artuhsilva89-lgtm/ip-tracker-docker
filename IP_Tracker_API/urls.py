from django.urls import path
from . import views

urlpatterns = [
    
    path('ips/', views.IpTrackerListCreateView.as_view(), name='IpTracker_create_list'),
    path('ips/<int:pk>/', views.IpTrackRetrieveUpdateDestroyView.as_view(), name='IpTracker_retrieve_update_destroy'),
]
