import secrets

import factory

from .models import Token


class TokenFactory(factory.Factory):
    name = factory.Faker("name")
    data = factory.LazyFunction(lambda: secrets.token_hex())  

    class Meta:
        model = Token
