class Directory:
    def __init__(self, directoryName, maxElements=0, parent=None):
        self.parent = parent
        self.name = directoryName
        self.DIR_MAX_ELEMS = maxElements
        self.elements = 0
        self.list = []
        self.delete = False

    def __delete__(self):
        if self.delete is False:
            self.delete = True
            return {
                'Message': 'Directory [' + self.name + '] was deleted'
            }
        else:
            return {
                'Error': 'The directory does not exist'
            }

    def __list__(self):
        tab = ''
        for li in self.list:
            if type(li) is Directory:
                tab += '==='
                tab += li.__list__()
                tab += '==='
            else:
                tab += li.name
                tab += ', '

        return tab

    def __move__(self, path):
        if path.elements >= path.DIR_MAX_ELEMS + 1:
            return {
                'Error': 'The current directory is full'
            }
        if self.parent is not None:
            self.parent.elements -= 1
            self.parent.list.pop(self.parent.list.index(self))
        self.parent = path
        self.parent.list.append(self)
        self.parent.elements += 1
        return {
            'Message': 'The directory was moved successfully'
        }
