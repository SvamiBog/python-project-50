install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	poetry build
	poetry publish --dry-run
	python -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl --force-reinstall

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
