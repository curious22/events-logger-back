from django.db import models



class Token(models.Model):
    name = models.CharField(max_length=100)
    data = models.CharField(max_length=64, default=secrets.token_hex, unique=True)
    is_active = models.BooleanField(default=True)
    expared_at = models.DateField()


    class Meta:
        db_table = "tokens"

    @staticmethod
    def create_token(name, expires_at=None):
        token = Token(name=name)
        if expires_at:
            token.expires_at = expires_at
        while True:
            new_token = secrets.token_hex(32)
            if not Token.objects.filter(token=new_token).exists():
                token.token = new_token
                break
        token.save()
        return token

    @staticmethod
    def is_valid_token(token_value):
        try:
            token = Token.objects.get(token=token_value, is_active=True, expires_at__gt=timezone.now())
            return True
        except Token.DoesNotExist:
            return False
