PYTHON ?= python3

ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

reformat:
	$(PYTHON) -m autoflake --in-place --remove-all-unused-imports --remove-unused-variable --recursive --exclude=__init__.py, $(ROOT_DIR)/src/
	$(PYTHON) -m isort --profile black $(ROOT_DIR)
	$(PYTHON) -m black $(ROOT_DIR)
update:
	$(PYTHON) -m pip install -U autoflake isort black
