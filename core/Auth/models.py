import secrets

from django.db import models


class Token(models.Model):
    name = models.CharField(max_length=100)
    data = models.CharField(max_length=64, default=secrets.token_hex, unique=True)
    is_active = models.BooleanField(default=True)
    expared_at = models.DateField()

    class Meta:
        db_table = "tokens"

    @classmethod
    def create_token(name, expared_at=None):
        data = Token(name=name)
        if expared_at:
            data.expared_at = expared_at
        while True:
            new_data = secrets.token_hex()
            if not Token.objects.filter(token=new_data).exists():
                data.token = new_data
                break
        data.save()
        return data

    @classmethod
    def is_token_exists(cls, data_value):
        return cls.objects.filter(data=data_value, is_active=True).exists()
