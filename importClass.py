class importFiles(object):

    def __init__(self):
        #self.files = files
        pass

    def getFiles(self):
        return self.files

    def setFiles(self, files):
        self.files = files

    def numFiles(self):
        return len(self.files)

    def clearQueue(self):
        del self.files[:]
