from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json

from directory import Directory
from binaryFile import BinaryFile
from logTextFile import LogTextFile
from bufferFile import BufferFile

app = Flask(__name__)
api = Api(app)

parentDirectory = Directory('root')

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
    def get(self):
        return "Server work"


class ApiDirectory(Resource):
    def __init__(self):
        self.directory = directory

    def post(self):
        data = request.get_json()
        self.directory = Directory(data["name"], data["maxElements"])
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
        data = request.get_json()
        parent_directory = Directory(data["parent"])
        self.binary = BinaryFile(data["name"], data["information"], parent_directory)
        return jsonify({
            'Message': 'The BinaryFile was created successfully'
        })

    def put(self):
        data = request.get_json()
        parent_directory = Directory(data["parent"])
        return self.binary.__move__(parent_directory)

    def delete(self):
        return self.binary.__delete__()


api.add_resource(ApiServerWork, '/')
api.add_resource(ApiDirectory, '/directory')
api.add_resource(ApiBinary, '/binary')


if __name__ == '__main__':
    app.run(debug=True)
