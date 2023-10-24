import secrets

from django.test import TestCase

from .models import Token


class TokenTestCase(TestCase):
    def test_is_token_exists(self):
        # Проверяем существует ли токен
        token = Token.create_token(name="Token to check")
        exists = Token.is_token_exists(token.data)
        self.assertTrue(exists)
