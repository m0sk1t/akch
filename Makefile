dev-start:
	sudo docker-compose -f docker-compose-dev.yml up

prod-start:
	sudo docker-compose -f docker-compose-prod.yml up

setup:
	. venv/bin/activate && pip install -r requirements.txt