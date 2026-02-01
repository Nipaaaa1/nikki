dev:
	uv run app/manage.py runserver

migration:
	uv run app/manage.py makemigrations

migrate:
	uv run app/manage.py migrate
