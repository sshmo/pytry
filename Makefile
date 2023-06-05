test:
	pytest -svv --log-cli-level=INFO --cov=pytry/ tests/ --hypothesis-show-statistics

dev:
	pre-commit run -a
	mypy ../pytry --check-untyped-defs
	pytype ../pytry
	radon cc -a -nb ../pytry
	pytest -svv --log-cli-level=INFO --cov=pytry/ tests/ --hypothesis-show-statistics
