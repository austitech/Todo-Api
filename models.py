import datetime

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    task = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __str__(self):
        return "<Todo: {}>".format(self.id)
