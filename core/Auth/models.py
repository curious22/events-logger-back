import secrets
from datetime import date

from django.db import models
from django.utils import timezone


class Token(models.Model):
    name = models.CharField(max_length=100)
    data = models.CharField(max_length=64, default=secrets.token_hex, unique=True)
    is_active = models.BooleanField(default=True)
    expired_at = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "tokens"

    @classmethod
    def is_token_exists(cls, data_value):
        filter_result = cls.objects.filter(
            data=data_value,
            is_active=True,
            expired_at__isnull=True,
        )
        print("Filter Result Count:", filter_result.count())  # Добавляем отладочный вывод
        return filter_result.exists()
