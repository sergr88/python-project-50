install:
	poetry install

lint:
	poetry run flake8 gendiff tests

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov

test-coverage-all:
	poetry run pytest --cov=gendiff

test-coverage-xml:
	poetry run pytest --cov --cov-report xml
