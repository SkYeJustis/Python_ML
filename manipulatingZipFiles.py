# -*- coding: utf-8 -*-
"""
Examples of ways to manipulate ZIP folders via Python in seconds 
(Depends on file size-- script was created to manipulate 
zip folders with under 100 subfolders and under 10000 total files within the zip)
@author: SkyeJustIs
"""

#==============================================================================
### Getting ZIP filenames and other testing info
#==============================================================================

import os

# Open the zip file
## Get names of all files within the opened zip folder
zip_directory = "C:/Users/skye/Documents/ZipFolder/azip"

zip_list = []   #ignore capitalization
zip_clist = []  #preserver capitalization
non_jpeg = []   #non-type files expected in file


for folder in os.listdir(zip_directory):
    # If certain file types were to not be counted 
    if folder.endswith(".csv") or folder.endswith(".CSV"):
        continue #do nothing
    else:
        #print os.path.join(directory, folder)
        print "FOLDER" + " " + folder
        for filename in os.listdir(os.path.join(zip_directory, folder)):
            if filename.endswith(".jpeg") or filename.endswith(".JPEG"): 

                print folder + " has " + filename
                print filename[:-4] #remove the .svg suffix
                zip_clist.append(folder + " has " + filename[:-4])

                continue
            else:
                non_jpeg.append(filename)
                continue
        continue

#See file list
zip_clist
#See size of list
print len(zip_clist)

#See file list
zip_list
#See size of list
print len(zip_list)

#See file list of jpeg
non_jpeg
#See size of list
print len(non_jpeg)

#==============================================================================
# Change last modified date of a zip file
#==============================================================================
import os
import time
# Current numeric float time
time.localtime() 
time.gmtime()

time.mktime( time.gmtime() ) 

time.ctime( time.mktime( time.gmtime()))

time.mktime( time.localtime()) 
time.mktime( time.localtime()) 

# time.ctime( time.mktime( time.localtime()) - time.mktime( time.) ) 

time.ctime( time.mktime( time.localtime()) - 3600 )
time.ctime( time.mktime( time.localtime()) - 3600 ) # one hour ago
time.ctime( time.mktime( time.localtime()) - 86400 ) # one day ago

time.ctime( time.mktime( time.localtime()) + 259200 ) # set the file date to 3 days ahead
           
# Set modified and accessed time
os.utime('C:/Users/skye/Documents/zipFolders/aZip.zip',
         (time.mktime( time.localtime()) + 259200 , time.mktime( time.localtime())+ 259200) )

#==============================================================================
# Add or delete files from a zip archive (via a newly created one)
#==============================================================================

import zipfile

#Main directory that the files are in:
main_dir = "C:/Users/skye/Documents/zipFolders/"
zin = zipfile.ZipFile (main_dir + 'aZip.zip',
                       'r')
zout = zipfile.ZipFile (main_dir + 'aZip_new.zip',
                        'w')


for item in zin.infolist():
    buffer = zin.read(item.filename)
    if (item.filename[-4:] != '.csv'): #avoid adding certain type of files to the new zip folder
        zout.writestr(item, buffer)

    zout.writestr(item, buffer)        #add all other types of files to new zip


zout.write("NULL2/NULL_NULL2.jpeg")    #Add folder and a file not in old zip
                                       #Folder and file is located in python directory 
zout.close()
zin.close()

