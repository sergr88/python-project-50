install:
	uv sync

lint:
	uv run flake8 gendiff tests

test:
	uv run pytest

test-coverage:
	uv run pytest --cov --cov-report=term-missing

test-coverage-all:
	uv run pytest --cov=gendiff --cov-report=term-missing

test-coverage-xml:
	uv run pytest --cov --cov-report xml
