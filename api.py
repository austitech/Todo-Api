
from flask import request

from flask_restful import Resource
from flask_restful import reqparse

from .models import db, Todo


parser = reqparse.RequestParser()


class GetUpdateDeleteView(Resource):
    def get(self, todo_id):
        todo = Todo.query.get_or_404(todo_id)
        return {todo_id: todo.json_serialize()}, 200

    def put(self, todo_id):
        todo = Todo.query.get_or_404(todo_id)

        parser.add_argument("task", type=str)
        parser.add_argument("description", type=str)
        args = parser.parse_args()

        todo.task = args.get("task", todo.task)
        todo.description = args.get("description", todo.description)

        db.session.add(todo)
        db.session.commit()

        return {todo_id: todo.json_serialize()}, 203

    def delete(self, todo_id):
        todo = Todo.query.get_or_404(todo_id)
        db.session.delete(todo)
        db.session.commit()

        return {"status": "OK"}, 200


class CreateListView(Resource):
    def post(self):
        parser.add_argument("task", type=str)
        parser.add_argument("description", type=str)
        args = parser.parse_args()
        print(args)

        if all([args.get(field, False) for field in ["task", "description"]]):
            todo = Todo(
                task=args["task"],
                description=args["description"]
            )
            db.session.add(todo)
            db.session.commit()

            return {todo.id: todo.json_serialize()}, 201

        return {"status": "BAD REQUEST"}, 400

    def get(self):
        todo_list = Todo.query.all()
        todo_list = [todo.json_serialize() for todo in todo_list]
        return {"todo": todo_list}, 200
