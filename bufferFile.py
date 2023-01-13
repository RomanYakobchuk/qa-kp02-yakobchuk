class BufferFile:
    def __init__(self, fileName, maxBufFileSize=0, parent=None):
        self.MAX_BUF_FILE_SIZE = maxBufFileSize
        self.parent = parent
        self.name = fileName
        self.information = []

    def __delete__(self):
        print('File was deleted ' + self.name)
        del self
        return

    def __move__(self, path):
        if path.elements >= path.DIR_MAX_ELEMS + 1:
            print('Directory ' + '--' + self.name + '--' + ' is full')
            return

        if self.parent is not None:
            self.parent.elements -= 1
            self.parent.list.pop(self.parent.list.index(self))

        self.parent = path
        self.parent.list.append(self)
        self.parent.elements += 1
        return

    def __push__(self, element):
        if len(self.information) >= self.MAX_BUF_FILE_SIZE:
            print('Buffer is full')
            return
        self.information.append(element)

    def __consume__(self):
        if len(self.information) >= 1:
            temp = self.information[0]
            self.information.pop(0)
            return temp
        return None
