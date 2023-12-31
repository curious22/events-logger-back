# Generated by Django 4.2 on 2023-09-29 12:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Participant", "0001_initial"),
        ("Event", "0002_alter_event_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_stamp", models.DateTimeField(auto_now_add=True)),
                (
                    "event",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="Event.event"),
                ),
                (
                    "participant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Participant.participant",
                    ),
                ),
            ],
            options={
                "db_table": "event_logs",
            },
        ),
    ]
