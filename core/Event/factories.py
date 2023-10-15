from factory import django, fuzzy

from . import models


class EventFactory(django.DjangoModelFactory):
    name = fuzzy.FuzzyText(length=15)

    class Meta:
        model = models.Event
