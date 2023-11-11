from django.db.utils import IntegrityError
from django.test import TestCase
from django.utils import timezone

from .models import Token


class TokenTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        cls.token = Token.objects.create(name="Test Token")
        cls.token.is_active = True
        cls.token.expired_at = None
        cls.token.save()
        cls.now = timezone.now()

    def test_is_token_exists(self):
        print("Token Data:", self.token.data)  # Отладочный вывод
        exists = Token.is_token_exists(self.token.data)
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

    def test_data_is_unique(self):
        data = {"name": "New name", "data": self.token.data}  # data must be unique
        with self.assertRaises(IntegrityError):
            Token.objects.create(**data)
