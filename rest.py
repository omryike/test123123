from flask import Flask, request
from flask_restful import Resource, Api
from tinydb import TinyDB, Query

app = Flask(__name__)
api = Api(app)
db = TinyDB('db.json')


class HelloWorld(Resource):
    def get(self):
        table = db.table('todos')

        return table.all()

    def post(self):
        table = db.table('todos')
        return table.insert(request.get_json()), 201


class Multi(Resource):
    def get(self, num):
        return {'result': num * 10}


api.add_resource(HelloWorld, '/')
api.add_resource(Multi, '/multi/<int:num>')


if __name__ == '__main__':
    app.run(debug=True)
