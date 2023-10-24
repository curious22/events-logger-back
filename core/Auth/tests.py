import secrets

from django.test import TestCase

from .models import Token


class TokenTestCase(TestCase):
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
