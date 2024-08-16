install:
	python3 -m venv .venv
	python3 -m pip install flask --break-system-packages

run:
	python3 example-server.py

