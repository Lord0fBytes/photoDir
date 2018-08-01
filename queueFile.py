# import importQueue
import datetime, os

class queueFile(object):

    def __init__(self, filename):
        self.fullname = filename
        self.filename = os.path.basename(filename)
        self.extension = os.path.splitext(filename)[1]
        self.type = self.getType(self.filename)
        #self.date = datetime.datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y-%m-%d')

    def getFullName(self):
        return self.type

    def getType(self, file):
        file = file.lower()
        if '.jpg' in file or '.cr2' in file:
            return 'Photo'
        elif '.mov' in file or '.mp4' in file or '.m4v' in file:
            return 'Video'
        else:
            return 'Error'

    def getAttribute(self, attrib):
        if attrib == 'full':
            return self.fullname
        elif attrib == 'file':
            return self.filename
        elif attrib == 'ext':
            return self.extension
        elif attrib == 'type':
            return self.type
        elif attrib == 'date':
            return self.date
        else:
            return 'Error in getAttribute'
