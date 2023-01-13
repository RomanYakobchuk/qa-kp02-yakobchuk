from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json

from directory import Directory
from binaryFile import BinaryFile
from logTextFile import LogTextFile
from bufferFile import BufferFile

app = Flask(__name__)
api = Api(app)




class ApiServerWork(Resource):
    def get(self):
        return "Server work"


api.add_resource(ApiServerWork, '/')


if __name__ == '__main__':
    app.run(debug=True)
