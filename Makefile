freeze:
	pip3 freeze > requirements.txt

install:
	pip3 install -r requirements.txt

test:
	pytest