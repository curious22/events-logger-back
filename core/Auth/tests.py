from dateutil.relativedelta import relativedelta
from django.test import TestCase
from django.utils import timezone

from .models import Token


class TokenTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        cls.token = Token.create_token(name="Test Token")
        cls.now = timezone.now()

    def test_is_token_exists(self):
        # Проверяем существует ли токен
        token = Token.create_token(name="Token to check")
        exists = Token.is_token_exists(token.data)
        self.assertTrue(exists)

    def test_create_token(self):
        data = {"name": "Test Token"}

        token = Token.objects.create(**data)

        self.assertTrue(Token.objects.filter(pk=token.pk).exists())
        self.assertEqual(token.name, data["name"])
        self.assertTrue(token.is_active)
        self.assertIsNone(token.expired_at)
        self.assertEqual(len(token.data), 64)

    def test_is_token_exists_not_exists(self):
        self.assertFalse(Token.is_token_exists(data_value="some-value"))

    def test_is_token_exists_not_active(self):
        Token.objects.filter(pk=self.token.pk).update(is_active=False)

        self.assertFalse(Token.is_token_exists(data_value=self.token.data))

    def test_is_token_exists_expired_by_date(self):
        yesterday = (self.now - relativedelta(days=1)).date()
        Token.objects.filter(pk=self.token.pk).update(expired_at=yesterday)

        self.assertFalse(Token.is_token_exists(data_value=self.token.data))
