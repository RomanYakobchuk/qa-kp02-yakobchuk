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


api.add_resource(ApiServerWork, '/')


if __name__ == '__main__':
    app.run(debug=True)
