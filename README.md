# events_logger
Boilerplate contains all the boilerplate you need to create a django REST API.


## Project requirements:
- Django >= 4.2
- django-rest-framework >= 3.14.0

## Dev setup:
Create *configs/settings.py* file with following content:
```python
from default_settings import *

SECRET_KEY = "some-long-key"  # key can be generated here https://djecrety.ir/
DEBUG = True
```

- Apply migrations: `python manage.py migrate`
- Run tests: `make tests`
- Start: `make runserver`
