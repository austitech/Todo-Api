
from flask import Flask

from flask_restful import Api
from flask_migrate import Migrate

from .models import db
from .api import HelloWorld


def factory():
    app = Flask(__name__)
    api = Api(app)

    # register extensions
    db.init_app(app)
    migrate = Migrate(app, db)

    # register endpoints
    api.add_resource(HelloWorld, '/')

    return app
