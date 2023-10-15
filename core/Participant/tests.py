from django.test import TestCase

from core.Event import factories as event_factories

from .factories import ParticipantFactory
from .models import Participant


class TestParticipantModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        cls.participant = ParticipantFactory()
        cls.event = event_factories.EventFactory(name="Reading")
        cls.participant.events.add(cls.event)

    def test_create(self):
        data = {"name": "John", "telegram_id": "123456789"}

        participant = Participant.objects.create(**data)

        self.assertTrue(Participant.objects.filter(pk=participant.pk).exists())
        self.assertIsNotNone(participant.joined_stamp)
        self.assertEqual(participant.name, data["name"])
        self.assertEqual(participant.telegram_id, data["telegram_id"])

    def test_delete(self):
        pk = self.participant.pk

        self.participant.delete()

        self.assertFalse(Participant.objects.filter(pk=pk).exists())
