from importQueue import *

queue1 = importQueue()
#print queue1.getItem()

queue1.append('/Test/path/file.jpg')
queue1.append('/Test/path/file2.jpg')
queue1.append('/Test/path/file3.cr2')
queue1.append('/Test/path/file21.mov')
queue1.append('/Test/path/file22.mov')
queue1.append('/Test/path/file23.mp4')
queue1.append('/Test/path/file24.mov')
queue1.append('/Test/path/file25.mp4')
for type in queue1.getTypeCount():
    print "%ss: %s" % (type, queue1.getTypeCount()[type])
    for ext in queue1.getExtCount(type):
        print "\t%s: %s" % (ext, queue1.getExtCount(type)[ext])
