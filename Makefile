build:
	pipenv run python setup.py sdist bdist_wheel

publish:
	pipenv run twine upload dist/*

pre-commit:
	pipenv run pre-commit install

mypy:
	pipenv run mypy mdfind.py

test:
	pipenv run pytest --exitfirst tests/
	pipenv run pytest --cov --cov-fail-under=100

format:
	pipenv run black mdfind.py setup.py tests
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
	pipenv run black --check mdfind.py setup.py tests/
	pipenv run mypy mdfind.py
	pipenv run pytest --exitfirst tests/
	pipenv run pytest --cov --cov-fail-under=100
