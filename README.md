# PhotoDir - Importer of Media
This python based application will be used to create a specific folder structure and import media from SD cards. 
- It can create a directory structure like this:
```
Parent
|_Photos
|     |_Final
|     |_RAW
|
|_Videos
      |_Final
      |_Working
      |       |_ProjectFiles
      |       |_Music
      |       |_FusionClips
      |_RAW

```
- Scan and detect media files from external devices (USB drives, SD cards, etc.)
- Move files into correct folders from above by three methods
    - Manual Import: Select individual files to import
    - Auto Import: Automatically moves all files on device to folders
    - Date Import: Automatically moves files select based on date to folders

## TODO (8/1/2018):
- [x] Create Date Import method
- [x] Create 2 frames for organizing GUI
- [x] Clean up the look of GUI
- [ ] Continue building on classes for future functions

## TODO (8/2/2018):
- [ ] Create Import Date button functionality
- [ ] Remove 'Move' button from GUI
- [ ] Change 'Find' to 'Manual Import' and shift to the right
- [ ] Move 'quit' button to bottom right
- [ ] ClearQueue after copy job
- [ ] Refresh button next to device dropdown

**Ideas:**
- Display each section on the fly
  - First is the browse/create
  - Then Manual or Device choose
  - Lastly bottom frames
- Lastly, start over
