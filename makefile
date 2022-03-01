VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip


run: $(VENV)/bin/activate
	$(PYTHON) app.py


install: # install dependencies
	@echo "Installing dependencies ..."
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

flake8: $(VENV)/bin/activate 
	flake8

pytest:
	pytest

clean:
	rm -rf __pycache__
	rm -rf $(VENV)