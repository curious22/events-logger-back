from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "events"



class EventLog(models.Model):
    participan = models.ForeignKey("Participant", on_delete=models.CASCADE,)
    event = models.ForeignKey(on_delete=models.PROTECT)
    created_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "event_logs"