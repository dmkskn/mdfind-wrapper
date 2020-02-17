build:
	python setup.py sdist bdist_wheel

publish:
	twine upload dist/*

pre-commit:
	pre-commit install

mypy:
	mypy mdfind

test:
	pytest --exitfirst tests/
	pytest --cov --cov-fail-under=100

format:
	black mdfind tests
	isort -y

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
	black --check mdfind tests/
	mypy mdfind
	pytest --exitfirst tests/
	pytest --cov --cov-fail-under=100
