""" fichier main test """
from flask import Flask

APP = Flask(__name__)

@APP.route('/')
def hello():
    """ doc """
# commentaire à ajouter
    return "Hello world!"
# Listen
if __name__ == '__main__':
    APP.run(host="0.0.0.0")
