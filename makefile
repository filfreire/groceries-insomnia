install:
	python3 -m venv .venv
	python3 -m pip install --no-cache-dir -r requirements.txt

dev:
	python3 app.py

docker-build:
	docker build -t groceries-app .

docker-run:
	docker run -d --name groceries-app -p 5000:5000 groceries-app

docker-run-image:
	docker run -d --name groceries-app -p 5000:5000 ghcr.io/filfreire/groceries-insomnia:latest