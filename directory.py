class Directory:
    def __init__(self, directoryName, maxElements=0, parent=None):
        self.DIR_MAX_ELEMS = maxElements
        self.parent = parent
        self.name = directoryName
        self.elements = 0
        self.list = []

    def __delete__(self) -> None:
        print('Directory was deleted ' + self.name)
        del self
        return

    def __list__(self):
        if len(self.list) == 0:
            return 'Directory: ' + self.name + 'is empty'

        elem = self.name + '\n'
        for item in self.list:
            if type(item) == Directory:
                elem += item.name + '\n'
            else:
                elem += item + '\n'
        return elem

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
