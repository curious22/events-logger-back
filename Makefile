runserver:
	python manage.py runserver

tests:
	pytest -s

format:
	black -l 120 .
	isort -l 120 -m 5 .