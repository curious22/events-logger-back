from rest_framework import serializers
from .models import Participant

class ParticipantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('telegram_id',)
        