class LogTextFile:
    def __init__(self, fileName, parent=None):
        self.name = fileName
        self.parent = parent
        self.delete = False
        self.information = ''
        if self.parent is not None:
            parent.list.append(self)

    def __delete__(self):
        if self.delete is False:
            self.delete = True
            return {
                'Message': 'File [' + self.name + '] was deleted'
            }
        else:
            return {
                'Error': 'The file does not exist'
            }

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
            'Message': 'The file was moved successfully'
        }

    def __read__(self):
        return {
            'Information': self.information
        }

    def __log__(self, line):
        self.information += '\r\n'
        self.information += line
        return {
            'Information': self.information
        }
