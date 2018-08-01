class importFiles(object):

    def __init__(self):
        self.files = []
        pass

    def getFiles(self):
        return self.files

    def setFiles(self, files):
        self.files = files

    def addFile(self, file):
        self.files.append(file)

    def numFiles(self):
        return len(self.files)

    def clearQueue(self):
        del self.files[:]

    def getPhotos(self):
        photos = []
        for photo in self.files:
            photo = photo.lower()
            if self.isPhotoVideo(photo) == 'Photo':
                photos.append(photo)
        return photos

    def getVideos(self):
        videos = []
        for video in self.files:
            video = videos.lower()
            if self.isPhotoVideo(video) == 'Video':
                videos.append(video)
        return videos

    def fileCount(self):
        count = [0,0,0]
        for file in self.files:
            if self.isPhotoVideo(file) == 'Photo':
                count[0] += 1
            elif self.isPhotoVideo(file) == 'Video':
                count[1] += 1
            else:
                # Not sure why, but this needs to be here #
                count[2] += 1
        return count

    def isPhotoVideo(self, file):
        file = file.lower()
        if '.jpg' in file or '.cr2' in file:
            return 'Photo'
        elif '.mov' in file or '.mp4' in file or '.m4v' in file:
            return 'Video'
        else:
            return 'Error'
