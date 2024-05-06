.PHONY: install test coverage publish clean update lint format check

install:
	@poetry install --with dev

update:
	@poetry update

clean:
	@find . -type f -name '*.pyc' -exec rm -f {} +
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '.pytest_cache' -exec rm -rf {} +
	@find . -type d -name '.ruff_cache' -exec rm -rf {} +

lint:
	@poetry run ruff check $(SRC_DIR)
	@poetry run isort --check-only $(SRC_DIR)

format:
	@poetry run isort $(SRC_DIR)

check:
	@poetry run pyright

test:
	@poetry run pytest -s -vv

coverage:
	@poetry run pytest -s -vv --cov=Nexus --cov-report term --cov-report xml

publish:
	@poetry publish --build
