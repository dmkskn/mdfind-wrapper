pipenv:
	python -m pip install pipenv

install:
	pipenv install --dev --keep-outdated --skip-lock

build:
	pipenv run python setup.py sdist bdist_wheel

publish:
	pipenv run twine upload dist/*

pre-commit:
	pipenv run pre-commit install

mypy:
	pipenv run mypy mdfind

test:
	pipenv run pytest --exitfirst tests/
	pipenv run pytest --cov --cov-fail-under=100

format:
	pipenv run black mdfind setup.py tests
	pipenv run isort -y

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
	rm -f .coverage
	rm -fr .pytest_cache
	rm -fr .mypy_cache

ci:
	pipenv run black --check --verbose mdfind/ tests/ setup.py
	pipenv run mypy mdfind
	pipenv run pytest --exitfirst tests/
	pipenv run pytest --cov --cov-fail-under=100
