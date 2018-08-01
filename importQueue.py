from queueFile import *

class importQueue(object):

    def __init__(self):
        self.queue = []

    def append(self, filename):
        self.queue.append(queueFile(filename))

    def getItem(self, index):
        return self.queue[index].getFullName()

    def getDateCount(self):
        # Gets the count for each date
        pass

    def getExtCount(self, filetype):
        # Gets teh count of each extension #
        counts = {}
        for file in self.queue:
            ext = file.getAttribute('ext').lower()
            if file.getAttribute('type') == filetype:
                if ext not in counts:
                    counts[ext] = 1
                else:
                    counts[ext] += 1
        return counts

    def getTypeCount(self):
        # Get the count for photos vs videos #
        counts = {'Photo':0, 'Video':0}
        for file in self.queue:
            if file.getAttribute('type') == 'Photo':
                counts['Photo'] += 1
            elif file.getAttribute('type') == 'Video':
                counts['Video'] += 1
            else:
                pass
        return counts
