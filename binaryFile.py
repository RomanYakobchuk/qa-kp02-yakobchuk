from directory import Directory


class BinaryFile:
    def __init__(self, fileName, information=None, parent=None):
        self.name = fileName
        self.information = information
        self.parent = parent
        if self.parent is not None:
            self.parent.elements += 1
            parent.list.append(self)

    def __delete__(self):
        print('File was deleted ' + self.name)
        del self
        return

    def __move__(self, path):
        if path.elements >= path.DIR_MAX_ELEMS + 1:
            print('Target directory is full')
            return

        if self.parent is not None:
            self.parent.elements -= 1
            self.parent.list.pop(self.parent.list.index(self))

        self.parent = path
        self.parent.list.append(self)
        self.parent.elements += 1
        return

    def __read__(self):
        return self.information
