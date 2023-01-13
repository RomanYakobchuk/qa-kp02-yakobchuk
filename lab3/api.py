from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json

from directory import Directory
from binaryFile import BinaryFile
from logTextFile import LogTextFile
from bufferFile import BufferFile

app = Flask(__name__)
api = Api(app)

parentDirectory = Directory('root', 100)

# directory
directoryName = 'item_1'
maxElements = 20
directory = Directory(directoryName, maxElements)

# binary
fileName = 'binary file'
information = 'binary information'
binary = BinaryFile(fileName, information, parentDirectory)

# logTextFile
fileName = 'item_1'
log = LogTextFile(fileName, parentDirectory)

# buffer
fileName = 'buffer_1'
maxFileSize = 20
buffer = BufferFile(fileName, maxFileSize)


class ApiServerWork(Resource):
    @staticmethod
    def get():
        return "Server work"


class ApiDirectory(Resource):
    def __init__(self):
        self.directory = directory

    @property
    def post(self):
        params = request.get_json()
        self.directory = Directory(params["name"], params["maxElements"])
        return jsonify({
            'Message': 'The Directory was created successfully'
        })


def put(self):
    data = request.get_json()
    parent_directory = Directory(data["parent"])
    return self.directory.__move__(parent_directory)


def delete(self):
    return self.directory.__delete__()


class ApiBinary(Resource):
    def __init__(self):
        self.binary = binary

    def get(self):
        return self.binary.__read__()

    def post(self):
        params = request.get_json()
        parent_directory = Directory(params["parent"])
        self.binary = BinaryFile(params["name"], params["information"], parent_directory)
        return jsonify({
            'Message': 'The BinaryFile was created successfully'
        })

    def put(self):
        params = request.get_json()
        parent_directory = Directory(params["parent"])
        return self.binary.__move__(parent_directory)

    def delete(self):
        return self.binary.__delete__()


class ApiLogTextFile(Resource):
    def __init__(self):
        self.logText = log

    def get(self):
        return self.logText.__read__()

    def post(self):
        params = request.get_json()
        parent_directory = Directory(params["parent"])
        self.logText = LogTextFile(params["name"], parent_directory)
        return jsonify({
            'Message': 'The LogTextFile was created successfully'
        })

    def put(self):
        params = request.get_json()
        parent_directory = Directory(params["parent"])
        return self.logText.__move__(parent_directory)

    def patch(self):
        params = request.get_json()
        return self.logText.__log__(params["line"])

    def delete(self):
        return self.logText.__delete__()


class ApiBuffer(Resource):
    def __init__(self):
        self.buffer = buffer

    def get(self):
        return self.buffer.__consume__()

    def post(self):
        params = request.get_json()
        parent_directory = Directory(params["parent"])
        self.buffer = BufferFile(params["name"], params["maxFileSize"], parent_directory)
        return jsonify({
            'Message': 'The BufferFile was created successfully'
        })

    def put(self):
        params = request.get_json()
        parent_directory = Directory(params["parent"])
        return self.buffer.__move__(parent_directory)

    def patch(self):
        params = json.loads(request.data)
        return self.buffer.__push__(params["element"])

    def delete(self):
        return self.buffer.__delete__()


api.add_resource(ApiServerWork, '/')
api.add_resource(ApiDirectory, '/directory')
api.add_resource(ApiBinary, '/binary')
api.add_resource(ApiLogTextFile, '/log')
api.add_resource(ApiBuffer, '/buffer')

if __name__ == '__main__':
    app.run(debug=True)
