VENV = census
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip



run: $(VENV)/bin/activate
	$(PYTHON) app.py


install: 
	$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

lint: 
	pylint --disable=R,C main.py

test:
	$(PYTHON) -m pytest -vv --cov= 
clean:
	rm -rf __pycache__
	rm -rf $(VENV)