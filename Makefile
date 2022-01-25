PYTHON ?= python3

ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

reformat:
	$(PYTHON) -m black $(ROOT_DIR)
	$(PYTHON) -m isort --profile black $(ROOT_DIR)
	$(PYTHON) -m autoflake --recursive --in-place, --remove-all-unused-imports, --remove-unused-variable $(ROOT_DIR)

install:
	pip install -U black isort autoflake
