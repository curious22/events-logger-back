# Generated by Django 4.2 on 2023-09-25 11:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("Event", "0002_alter_event_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="Participant",
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
                ("name", models.CharField(max_length=200)),
                ("joined_stamp", models.DateTimeField(auto_now_add=True)),
                ("telegram_id", models.CharField(max_length=64)),
                ("events", models.ManyToManyField(to="Event.event")),
            ],
            options={
                "db_table": "participants",
            },
        ),
    ]
