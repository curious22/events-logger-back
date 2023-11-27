from rest_framework import serializers
from core.Participant.models import Participant

class ParticipantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('telegram_id',)

    def validate_telegram_id(self, value):
        if Participant.objects.filter(telegram_id=value).exists():
            raise serializers.ValidationError("Участник с таким telegram_id уже существует.")
        return value
