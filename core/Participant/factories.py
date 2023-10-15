from factory import django, fuzzy

from . import models


class ParticipantFactory(django.DjangoModelFactory):
    name = fuzzy.FuzzyText(length=15)
    telegram_id = fuzzy.FuzzyText(length=15)

    class Meta:
        model = models.Participant
