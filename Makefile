setup:
	poetry install --no-root
	poetry run pre-commit install --config .pre-commit-config.yml

pytest:
	poetry run pytest

lint:
	poetry run pre-commit run --all-files -c .pre-commit-config.yml
