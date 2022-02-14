VENV = census
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip


run: $(VENV)/bin/activate
	$(PYTHON) app.py


install: # install dependencies
	@echo "Installing dependencies ..."
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

lint: 
	pylint --disable=R,C main.py

test:
	pytest

clean:
	rm -rf __pycache__
	rm -rf $(VENV)