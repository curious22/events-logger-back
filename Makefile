runserver:
	python manage.py runserver

tests:
	python manage.py tests

format:
	black -l 120 .
	isort -l 120 -m 5 .