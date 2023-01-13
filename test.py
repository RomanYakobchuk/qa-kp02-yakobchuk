import pytest

from directory import Directory
from binaryFile import BinaryFile
from logTextFile import LogTextFile
from bufferFile import BufferFile


class TestDirectory:
    parentDirectory = Directory("root")

    def test_CreatDirectory(self):
        directoryName = 'item_1'
        maxElements = 200
        directory = Directory(directoryName, maxElements)

        assert directory.name == directoryName
        assert directory.DIR_MAX_ELEMS == maxElements
        assert directory.elements == 0
        assert pytest.raises(OverflowError)

    def test_MoveDirectory(self):
        directory = Directory('directory')
        assert pytest.raises(OverflowError)
        assert directory.__move__(self.parentDirectory) == {
            'Message': 'The directory was moved successfully'
        }

    def test_DeleteDirectory(self):
        directory = Directory('directory')

        assert directory.__delete__() == {
            'Message': 'Directory [' + directory.name + '] was deleted'
        }
        assert directory.__delete__() == {
            'Error': 'The directory does not exist'
        }


class TestBinary:
    parentDirectory = Directory('root')

    def test_CreateBinary(self):
        fileName = 'item_1'
        information = 'information for item_1'
        binary = BinaryFile(fileName, information, self.parentDirectory)

        assert binary.name == fileName
        assert binary.information == information
        assert binary.parent == self.parentDirectory
        assert binary.__read__() == {
            'Information': information
        }

    def test_MoveBinary(self):
        fileName = 'item_1'
        information = 'information for move'
        binary = BinaryFile(fileName, information)

        assert pytest.raises(OverflowError)
        assert binary.__move__(self.parentDirectory) == {
            'Message': 'The file was moved successfully'
        }

    def test_ReadBinary(self):
        fileName = 'item_1'
        information = 'information for read'
        binary = BinaryFile(fileName, information)

        assert pytest.raises(OverflowError)
        assert binary.__read__() == {
            'Information': 'information for read'
        }

    def test_DeleteBinary(self):
        binary = BinaryFile('binary')

        assert binary.__delete__() == {
            'Message': 'File [' + binary.name + '] was deleted'
        }
        assert binary.__delete__() == {
            'Error': 'The file does not exist'
        }


class TestLog:
    parentDirectory = Directory('root')

    def test_CreateLog(self):
        fileName = 'item_1'
        log = LogTextFile(fileName, self.parentDirectory)

        assert log.name == fileName
        assert pytest.raises(OverflowError)
        assert log.parent == self.parentDirectory

    def test_MoveLog(self):
        fileName = 'item_1'
        log = LogTextFile(fileName)
        assert pytest.raises(OverflowError)

        assert log.__move__(self.parentDirectory) == {
            'Message': 'The file was moved successfully'
        }

    def test_AddLog(self):
        fileName = 'item_1'
        line_1 = 'line_1'
        line_2 = 'line_2'
        log = LogTextFile(fileName)

        log.__log__(line_1)
        log.__log__(line_2)

        assert log.__read__() == {
            'Information': '\r\n' + line_1 + '\r\n' + line_2
        }

    def test_DeleteLog(self):
        log = LogTextFile('logTextFile')

        assert log.__delete__() == {
            'Message': 'File [' + log.name + '] was deleted'
        }
        assert log.__delete__() == {
            'Error': 'The file does not exist'
        }


class TestBuffer:
    parentDirectory = Directory('root')

    def test_CreateBuffer(self):
        fileName = 'item_1'
        maxFileSize = 20
        buffer = BufferFile(fileName, maxFileSize, self.parentDirectory)

        assert buffer.name == fileName
        assert buffer.MAX_BUF_FILE_SIZE == maxFileSize
        assert pytest.raises(OverflowError)
        assert buffer.parent == self.parentDirectory

    def test_MoveBuffer(self):
        fileName = 'item_1'
        information = 'information for buffer'
        buffer = BufferFile(fileName, information)

        assert pytest.raises(OverflowError)
        assert buffer.__move__(self.parentDirectory) == {
            'Message': 'The file was moved successfully'
        }

    def test_ConsumeBuffer(self):
        fileName = 'item_1'
        maxFileSize = 20
        line_1 = 'line_1'
        line_2 = 'line_2'
        buffer = BufferFile(fileName, maxFileSize)

        buffer.__push__(line_1)
        buffer.__push__(line_2)

        assert buffer.__consume__() == {
            'Consumed Information': line_1
        }
        assert buffer.__consume__() == {
            'Consumed Information': line_2
        }
        assert buffer.__consume__() == {
            'Error': 'Information is empty'
        }
        assert pytest.raises(OverflowError)

    def test_DeleteBuffer(self):
        buffer = BufferFile('buffer')

        assert buffer.__delete__() == {
            'Message': 'File [' + buffer.name + '] was deleted'
        }
        assert buffer.__delete__() == {
            'Error': 'The file does not exist'
        }
