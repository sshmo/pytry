test:
	pytest -svv --log-cli-level=INFO --cov=pytry/ tests/

dev:
	pre-commit run -a
	mypy ../pytry
	pytype ../pytry
	radon cc -a -nb ../pytry
	pytest -svv --log-cli-level=INFO --cov=pytry/ tests/
