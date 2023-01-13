class BufferFile:
    def __init__(self, fileName, maxFileSize=0, parent=None):
        self.name = fileName
        self.MAX_BUF_FILE_SIZE = maxFileSize
        self.parent = parent
        self.information = []
        self.delete = False
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

    def __push__(self, item):
        if len(self.information) >= self.MAX_BUF_FILE_SIZE:
            return {
                'Error': 'Buffer is full'
            }
        self.information.append(item)
        return {
            'Information': self.information
        }

    def __consume__(self):
        if len(self.information) >= 1:
            item = self.information[0]
            self.information.pop(0)
            return {
                'Consumed Information': item
            }
        return {
            'Error': 'Information is empty'
        }
