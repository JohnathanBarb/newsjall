venv:
	uv sync --all-extras


test:
	uv run pytest . -s

run:
	uv run fastapi run src/main.py --reload

typecheck:
	uv run mypy .

check:
	uv run ruff format --check .
	uv run ruff check .

format:
	uv run ruff format .
	uv run ruff check --fix .
