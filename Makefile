freeze-requirements:
	pip3 freeze > requirements.txt

install-requirements:
	pip3 install -r requirements.txt

start-tests:
	pytest