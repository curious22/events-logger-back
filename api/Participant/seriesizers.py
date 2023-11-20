from rest_framework import serializers
from core.Participant.models import Participant

class ParticipantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('telegram_id',)
