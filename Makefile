runserver:
	python manage.py runserver

tests:
	python manage.py test -v 2 --keepdb

format:
	black -l 120 .
	isort -l 120 -m 5 .