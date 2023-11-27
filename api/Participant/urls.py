from django.urls import path 
from api.Participant.views import ParticipantView 

urlpatterns = [
    path('participants/', ParticipantView.as_view(), name='participant-list'),
]
