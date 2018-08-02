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
- [ ] Create Date Import method
- [ ] Create 2 frames for organizing GUI
- [ ] Clean up the look of GUI
- [ ] Continue building on classes for future functions
