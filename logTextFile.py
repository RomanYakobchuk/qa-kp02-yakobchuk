class LogTextFiles:
    def __init__(self, fileName, parent=None):
        self.name = fileName
        self.parent = parent
        self.information = ''

    def __delete__(self):
        print('File was deleted ' + self.name)
        del self
        return

    def __move__(self, path):
        if path.elements >= path.DIR_MAX_ELEMS + 1:
            print('Directory is full')
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

    def __addLineToTheEnd__(self, line):
        self.information += line
        self.information += '\n'
