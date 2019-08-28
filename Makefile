PIPENV          = pipenv
VENV            = .venv
BASEDIR         = charaPoster/
MAIN            = main.py

.PHONY: usage
usage:
	@echo "Usage: ${MAKE} Target"
	@echo ""
	@echo "Targets:"
	@echo "  run              run ${MAIN} script"
	@echo "  lint             run flake8"
	@echo "  format           run auto formatter"


${VENV}: Pipfile.lock
	${PIPENV} sync --dev
	touch ${VENV}

.env: .env.sample
	cp -n .env.sample .env

.PHONY: run
run: ${VENV} .env
	${PIPENV} run python ${MAIN}

.PHONY: lint
lint:
	${PIPENV} run flake8 ${BASEDIR}

.PHONY: format
format:
	${PIPENV} run autopep8 -ri ${BASEDIR}
	${PIPENV} run isort -rc ${BASEDIR}
