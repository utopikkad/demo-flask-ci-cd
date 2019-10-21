build :
	pipenv install

test :
	pipenv run pylint main.py
