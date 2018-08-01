import os
from Tkinter import *
import tkFileDialog
import tkMessageBox
import shutil
import glob
from importClass import *
import time, datetime
from importQueue import *

def status_update(type, textInfo):
    lblStatus['text'] = '%s' % (textInfo)
    if type == 'warn':
        lblStatus['fg'] = 'Orange'
    if type == 'suc':
        lblStatus['fg'] = 'DarkGreen'
    if type == 'error':
        lblStatus['fg'] = 'Red'
    if type == 'debug':
        lblStatus['fg'] = 'Purple'

def displayFiles():
    status = ''
    for type in queue1.getTypeCount():
        status += "%ss: %s\n" % (type, queue1.getTypeCount()[type])
        for ext in queue1.getExtCount(type):
            status += "\t%s: %s\n" % (ext, queue1.getExtCount(type)[ext])
    return status

def create_directory():
   # Check to see if location exists
   # Create the folder structure if so
   directory = "/Users/justin/Pictures/%s/" % (e1.get())
   if not os.path.isdir(directory):
       os.makedirs(directory)
       os.makedirs(directory+"Photos/")
       os.makedirs(directory+"Photos/RAW")
       os.makedirs(directory+"Photos/Final")
       os.makedirs(directory+"Videos/")
       os.makedirs(directory+"Videos/RAW")
       os.makedirs(directory+"Videos/Final")
       os.makedirs(directory+"Videos/Working")
       os.makedirs(directory+"Videos/Working/Music")
       os.makedirs(directory+"Videos/Working/Sounds")
       os.makedirs(directory+"Videos/Working/Project")
       status_update('suc', 'Directory: %s has been created' % (directory))
   else:
       status_update('error','Directory cannot be empty')

def move_files():
    # Move the files from /Pictures/Staging to the location above
    # Sorts by file type
    #   .jpg/.cr2 -> photos/RAW
    #   .mp4/.mov -> videos/RAW
    # if e1.get() != "" and cFiles.numFiles() > 0:
    #     # dest_photo = "/Users/justin/Pictures/%s/Photos/RAW/" % (e1.get())
    #     # dest_video = "/Users/justin/Pictures/%s/Videos/RAW/" % (e1.get())
    #     for file in cFiles.getFiles():
    #         shutil.copy(file, "/Users/justin/Pictures/%s/%ss/RAW/" % (e1.get(),cFiles.isPhotoVideo(file)))
    #     # for photo in cFiles.getPhotos():
    #     #     shutil.copy(file, dest_photo)
    #     #     status_update('suc', 'Files have been successfully moved')
    #     # for video in cFiles.getVideos():
    #     #     shutil.copy(file, dest_video)
    #     #     status_update('suc', 'Files have been successfully moved')
    #     # Empty the queue after copying
    #     cFiles.clearQueue()
    # else:
    #     if e1.get() == "":
    #         status_update("error","Directory name cannot be blank.")
    #     elif cFiles.numFiles() <= 0:
    #         status_update("error","No media has been selected.")
    #     else:
    #         status_update('error', 'Unknown error has occurred')
    pass

def find_files():
    fdFiles = tkFileDialog.askopenfiles(parent=master,title='Choose a file')
    if len(fdFiles) <= 0:
        status_update('warn', 'No files have been selected')
        btn_move['state'] = 'disabled'
    else:
        for file in fdFiles:
            queue1.append(str(file).split('\'')[1])
        # status_update('suc',"Media loaded in queue: %s file(s)" % fdFiles)
        btn_move['state'] = 'normal'
        lblDeviceInfo['text'] = '%s' % (displayFiles())
        lblDeviceInfo['fg'] = 'red'
    # pass

master = Tk()
# Creates header label #
Label(master, text="Enter the Name of the Album").grid(row=0, columnspan=2)
# Create status label #
lblStatus = Label(master, text="Status:")
lblStatus.grid(row=2, column=0, sticky=W)
lblDeviceInfo = Label(master, text='')
lblDeviceInfo.grid(row=6, column=0, sticky=W)

# Textbox for Album name #
e1 = Entry(master)
e1.grid(row=1, column=0)

# Buttons on the form #
btn_quit = Button(master, text='Quit', command=master.quit)
btn_quit.grid(row=3, column=0, sticky=W, pady=4)
btn_create = Button(master, text='Create', command=create_directory)
btn_create.grid(row=1, column=2, pady=4, sticky=EW)
btn_browse = Button(master, text='Browse', command=create_directory)
btn_browse.grid(row=1, column=1, pady=4, sticky=EW)
btn_move = Button(master, text='Move Files', state=NORMAL, command=move_files)
btn_move.grid(row=3, column=2, sticky=E, pady=4)
btn_find = Button(master, text='Find Files', command=find_files)
btn_find.grid(row=3, column=1, sticky=W, pady=4)

#Finds removable media in /Volumes/
#Excludes certain volumes
vols = os.walk('/Volumes/').next()[1]
exclude = set(['OS X Base System','Macintosh HD','DROPME','TIMEMACHINE'])
vols[:] = [d for d in vols if d not in exclude]

# Create a Tkinter variable
tkvar = StringVar(master)

# Initiate import files variable #
# cFiles = importFiles()
queue1 = importQueue()

# Create the dropdown menu and label #
try:
    popupMenu = OptionMenu(master, tkvar, *vols)
except:
    popupMenu = OptionMenu(master, tkvar, 'None')
Label(master, text="---TESTING BEYOND THIS POINT!!!!---\n\nChoose a device to pull media from:  ").grid(row = 4, column = 0, columnspan=3, sticky=W)
popupMenu.grid(row = 5, column=0, columnspan=2, sticky=EW)

# on change dropdown value
def change_dropdown(*args):
    if tkvar.get() != 'None':
        for root, dirs, files in os.walk("/Volumes/%s/" % tkvar.get(), topdown=True):
            print root
            for name in files:
                # Ignore hidden files #
                if name.startswith('.'):
                    break
                else:
                    queue1.append(os.path.join(root, name))
        # Store as variable so for loop only runs once #

        lblDeviceInfo['text'] = '%s' % (displayFiles())
        lblDeviceInfo['fg'] = 'red'

# link function to change dropdown
tkvar.trace('w', change_dropdown)

####### Live testing area #######



mainloop( )
