install:
	@pip install -r requirements.txt
	@python manage.py syncdb
	@python manage.py migrate
	@python manage.py runserver
