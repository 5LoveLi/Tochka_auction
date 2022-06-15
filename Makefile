create:
	python3 -m venv env

install:
	pip install -r requirements.txt

activate:
	@echo "source env/Scripts/Activate"

run:
	FLASK_ENV=development TEMPLATES_AUTO_RELOAD=true flask run
