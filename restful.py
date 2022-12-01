import requests
import json
from flask import Flask, request
from flask_restful import Api, reqparse, Resource, abort

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('id', type=int, help="No id passed")
parser.add_argument('state', type=str, help="Need address state")
parser.add_argument('hobbies', type=str, help="No list passed")

data = {}

def abort_no_name(name):
    if name not in data:
        abort("No name currently exists")

class getName(Resource):
    def get(self, name):
        return data[name]

    def put(self, name):
        args = parser.parse_args()
        data[name] = args
        return data[name]

class landingPage(Resource):
    def get(self):
        return "<html><h1>Hello World</h1><html>"


api.add_resource(getName, "/<string:name>")
api.add_resource(landingPage, "/")

if __name__ == '__main__':
    app.run(debug=True)