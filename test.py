import pytest

from directory import Directory
from binaryFile import BinaryFile
from logTextFile import LogTextFiles
from bufferFile import BufferFile
from types import NoneType


class TestDirectory:
    parentDirectory = Directory('parentDirectory', 10)

    def testCreatDirectory(self):
        maxElements = 10
        directoryName = 'item_1'
        directory = Directory(directoryName, maxElements)

        assert directory.name == directoryName
        assert directory.DIR_MAX_ELEMS == maxElements
        assert directory.elements == 0

    def testMoveDirectory(self):
        directory = Directory('directory')

        assert type(directory.parent) is NoneType

        directory.__move__(self.parentDirectory)

        assert directory.parent == self.parentDirectory

    def testDeleteDirectory(self):
        directory = Directory('directory')

        directory.__delete__()

        assert pytest.raises(Exception)

    def testListDirectory(self):
        directory = Directory("parent")
        binary = directory.__list__()

        assert type(binary) == str

        directory.list = ['item_1', Directory('1')]

        binary = directory.__list__()
        assert type(binary) == str


class TestBinary:
    parentDirectory = Directory('parentDirectory', 10)
    secondDirectory = Directory('secondDirectory', 10)

    def testCreateBinary(self):
        fileName = 'item_1'
        information = 'Lorem Ipsum has been the industry'
        binary = BinaryFile(fileName, information, self.parentDirectory)

        assert binary.name == fileName
        assert binary.information == information
        assert binary.parent == self.parentDirectory

    def testMoveBinary(self):
        directory = Directory("directory")
        fileName = 'item_1'
        binary = BinaryFile(fileName, directory)

        binary.__move__(self.secondDirectory)

        assert any(binary in self.secondDirectory.list for binary in self.secondDirectory.list) is True

    def testDeleteBinary(self):
        binary = BinaryFile('binary')
        binary.__delete__()
        assert pytest.raises(Exception)


class TestBuffer:
    parentDirectory = Directory('parentDirectory', 10)

    def testCreateBuffer(self):
        fileName = 'item_1'
        size = 10
        buffer = BufferFile(fileName, size, self.parentDirectory)

        assert buffer.name == fileName
        assert buffer.MAX_BUF_FILE_SIZE == size
        assert pytest.raises(OverflowError)
        assert buffer.parent == self.parentDirectory

    def testMoveBuffer(self):
        fileName = 'item_1'
        information = 'Lorem Ipsum has been the industry'
        buffer = BufferFile(fileName, information)

        buffer.__move__(self.parentDirectory)

        assert buffer.parent == self.parentDirectory

    def testDeleteBuffer(self):
        buffer = BufferFile('buffer')

        del buffer

        assert 'buffer' not in locals()

    def testAddConsumeBuffer(self):
        fileName = 'item_1'
        size = 10
        line1 = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
        line2 = 'Lorem Ipsum has been the industry'
        buffer = BufferFile(fileName, size)

        buffer.__push__(line1)
        buffer.__push__(line2)

        assert buffer.__consume__() == line1
        assert buffer.__consume__() == line2
        assert pytest.raises(OverflowError)


class TestLog:
    parentDirectory = Directory('parentDirectory', 10)

    def testCreateLog(self):
        fileName = 'item_1'
        log = LogTextFiles(fileName, self.parentDirectory)

        assert log.name == fileName
        assert log.__read__() == ''
        assert log.parent == self.parentDirectory

    def testMoveLog(self):
        fileName = 'item_1'
        log = LogTextFiles(fileName)
        assert type(log.parent) is NoneType

        log.__move__(self.parentDirectory)

        # assert
        assert log.parent == self.parentDirectory

    def testDeleteLog(self):
        log = LogTextFiles('log')

        del log

        assert 'log' not in locals()

    def testAddReadLog(self):
        fileName = 'item_1'
        line1 = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
        line2 = 'Lorem Ipsum has been the industry'
        log = LogTextFiles(fileName)

        log.__addLineToTheEnd__(line1)
        log.__addLineToTheEnd__(line2)

        assert log.__read__() == line1 + '\n' + line2 + '\n'
