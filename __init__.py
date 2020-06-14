
from flask import Flask

from flask_restful import Api
from flask_migrate import Migrate

from .config import Development, Testing
from .models import db
from .api import CreateListView, GetUpdateDeleteView


def factory(testing=False):
    app = Flask(__name__)
    api = Api(app)

    # configure app
    app.config.from_object(Development)
    if testing:
        app.config.from_object(Testing)

    # register extensions
    db.init_app(app)
    migrate = Migrate(app, db)

    # register endpoints
    api.add_resource(GetUpdateDeleteView, '/todo/api/v1/<string:todo_id>')
    api.add_resource(CreateListView, '/todo/api/v1/')

    return app
