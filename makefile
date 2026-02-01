dev:
	uv run app/manage.py runserver

create-migration:
	uv run app/manage.py makemigrations

migrate:
	uv run app/manage.py migrate
