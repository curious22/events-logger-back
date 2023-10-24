import secrets

from django.db import models


class Token(models.Model):
    name = models.CharField(max_length=100)
    data = models.CharField(max_length=64, default=secrets.token_hex, unique=True)
    is_active = models.BooleanField(default=True)
    expired_at = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "tokens"

    @classmethod
    def create_token(cls, name, expired_at=None):
        data = cls(name=name)
        if expired_at:
            data.expired_at = expired_at
        while True:
            new_data = secrets.token_hex()
            if not cls.objects.filter(data=new_data).exists():
                data.data = new_data
                break
        data.save()
        return data

    @classmethod
    def is_token_exists(cls, data_value):
        return cls.objects.filter(data=data_value, is_active=True).exists()
