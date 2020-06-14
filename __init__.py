
from flask import Flask
from flask_restful import Api
from .views import HelloWorld


def factory():
    app = Flask(__name__)
    api = Api(app)

    # register endpoints
    api.add_resource(HelloWorld, '/')

    return app
