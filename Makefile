install:
	uv sync

build:
	uv build

package-install:
	uv tool install .

package-uninstall:
	uv tool uninstall hexlet-code

lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

format:
	uv run ruff format

test:
	uv run pytest

test-coverage:
	uv run pytest --cov --cov-report=term-missing

test-coverage-all:
	uv run pytest --cov=gendiff --cov-report=term-missing

test-coverage-xml:
	uv run pytest --cov --cov-report xml
