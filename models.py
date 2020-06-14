import datetime

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    task = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __str__(self):
        return "<Todo: {}>".format(self.task)

    def converter(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.__str__()

    def json_serialize(self):
        todo = {}
        todo["id"] = self.id
        todo["task"] = self.task
        todo["description"] = self.description
        todo["created"] = self.converter(self.created)

        return todo
