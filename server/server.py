from flask import Flask

srv = Flask(__name__)

@srv.route('/')
def hello_world():
    return "Hello, world!"
