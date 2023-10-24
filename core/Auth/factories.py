import factory
import secrets
from .models import Token

class TokenFactory(factory.Factory):
    class Meta:
        model = Token

    name = factory.Faker('name') 
    data = factory.LazyFunction(lambda: secrets.token_hex()) 
    is_active = True
    expired_at = None