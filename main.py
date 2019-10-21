from flask import Flask, escape, request

APP = Flask(__name__)

@APP.route('/')
def hello():
#     
    return "Hello world!"

if __name__ == '__main__':
    APP.run(host="0.0.0.0")


