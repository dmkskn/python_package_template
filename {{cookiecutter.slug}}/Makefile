init: update install pre-commit

install:
	poetry install

update:
	poetry update

pre-commit:
	poetry run pre-commit install

test:
	poetry run pytest --exitfirst tests/

lint:
	poetry run flake8 {{ cookiecutter.slug }} tests

format:
	poetry run black {{ cookiecutter.slug }} tests
	poetry run isort -y

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

ci:
	poetry run black --check {{ cookiecutter.slug }}/ tests/
	poetry run flake8 {{ cookiecutter.slug }} tests
	poetry run pytest --exitfirst tests/
	poetry run pytest --cov --cov-fail-under=100
