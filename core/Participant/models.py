from django.db import models

from core.Event.models import Event


# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=200)
    joined_stamp = models.DateTimeField(auto_now_add=True)
    telegram_id = models.CharField(max_length=64)
    events = models.ManyToManyField(Event)

    class Meta:
        db_table = "participants"
