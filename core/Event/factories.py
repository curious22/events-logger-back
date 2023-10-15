from factory import SubFactory, django, fuzzy

from core.Participant.factories import ParticipantFactory

from . import models


class EventFactory(django.DjangoModelFactory):
    name = fuzzy.FuzzyText(length=15)

    class Meta:
        model = models.Event


class EventLogFactory(django.DjangoModelFactory):
    participant = SubFactory(ParticipantFactory)
    event = SubFactory(EventFactory)

    class Meta:
        model = models.Event
