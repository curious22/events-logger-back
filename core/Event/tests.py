from django.db.models.deletion import ProtectedError
from django.test import TestCase

from core.Participant.factories import ParticipantFactory

from . import models
from .factories import EventFactory, EventLogFactory


class TestEventModels(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        cls.participant = ParticipantFactory()
        cls.event = EventFactory(name="Reading")
        cls.participant.events.add(cls.event)
        cls.event_log = EventLogFactory(participant=cls.participant, event=cls.event)

    def test_create_event(self):
        name = "Sleep"

        event = models.Event.objects.create(name=name)

        self.assertTrue(models.Event.objects.filter(pk=event.pk).exists())
        self.assertEqual(event.name, name)

    def test_delete_linked_event_fail(self):
        with self.assertRaises(ProtectedError):
            self.event.delete()
        self.assertTrue(models.Event.objects.filter(pk=self.event.pk).exists())

    def test_delete_event_without_references(self):
        new_event = EventFactory(name="Boxing")
        pk = new_event.pk
        self.assertTrue(models.Event.objects.filter(pk=pk).exists())

        new_event.delete()

        self.assertFalse(models.Event.objects.filter(pk=pk).exists())

    def test_create_event_log(self):
        new_event = EventFactory(name="Run")

        event_log = models.EventLog.objects.create(event=new_event, participant=self.participant)

        self.assertTrue(models.EventLog.objects.filter(pk=event_log.pk).exists())
        self.assertEqual(event_log.event, new_event)
        self.assertEqual(event_log.participant, self.participant)
        self.assertIsNotNone(event_log.created_stamp)

    def test_delete_event_log(self):
        pk = self.event_log.pk

        self.event_log.delete()

        self.assertFalse(models.EventLog.objects.filter(pk=pk).exists())
