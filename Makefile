test:
	pre-commit run -a
	pytype
	pytest -svv --log-cli-level=INFO --cov=pytry/ tests/
