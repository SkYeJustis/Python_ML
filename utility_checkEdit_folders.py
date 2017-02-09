# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 11:00:15 2017

@author: leungs
"""

import os

#fp = "C:\Users\leungs\Documents\Onelines_SVG\Termination_Hyperlinking_Testing\pisvg_AC1_20161214232228_orig\AE\ABSECON.svg"
#
#time.ctime(os.path.getctime(fp))
#os.path.getctime(fp)
#==============================================================================
# ## Getting ZIP filenames and other testing info
#==============================================================================

zip_directory = "C:/Users/leungs/Documents/Onelines_SVG/Termination_Hyperlinking_Testing/01_SET/pisvg_AC1_20170117230739"

zip_list = []
zip_clist = []
non_rawsvg = [] 


for folder in os.listdir(zip_directory):
    if folder.endswith(".csv") or folder.endswith(".CSV"):
        continue #do nothing
    else:
        #print os.path.join(directory, folder)
        print "FOLDER" + " " + folder
        for filename in os.listdir(os.path.join(zip_directory, folder)):
            if filename.endswith(".svg") or filename.endswith(".SVG"): 

                print folder + " has " + filename
                print filename[:-4] #remove the .svg suffix
                zip_clist.append(folder + " has " + filename[:-4])

                continue
            else:
                non_rawsvg.append(filename)
                continue
        continue
    
zip_clist

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

time.ctime( time.mktime( time.localtime()) )
time.ctime( time.mktime( time.localtime()- 3600)  ) # one hour ago
time.ctime( time.mktime( time.localtime()- 86400)  ) # one day ago

time.ctime( time.mktime( time.localtime()) + 216000 ) # one day ago
           
# Set modified and accessed time
os.utime('C:/Users/leungs/Documents/Onelines_SVG/Termination_Hyperlinking_Testing/01_SET/zip__conditions/INPUT_ZIP_TESTING/scenario_37_svgdba_dates/AC2/pisvg_AC2_20170118235625.zip',
         (time.mktime( time.localtime()), time.mktime( time.localtime())) )

#==============================================================================
# Delete files from a zip archive
#==============================================================================

import zipfile
main_dir = "C:/Users/leungs/Documents/Onelines_SVG/Termination_Hyperlinking_Testing/01_SET/zip__conditions/INPUT_ZIP_TESTING/scenario_38_entry_mismatch/AC2/"
zin = zipfile.ZipFile (main_dir + 'pisvg_AC2_20170118235625.zip',
                       'r')
zout = zipfile.ZipFile (main_dir + 'pisvg_AC2_20170118235625_new.zip',
                        'w')

##Check file directory
#ziplist = [] 
#for folder in zin.infolist():
#    print folder.filename #ignores folders
#    ziplist.append(folder.filename)

for item in zin.infolist():
    buffer = zin.read(item.filename)
#    if (item.filename[-4:] != '.svg'): #if an empty folder is needed
#        zout.writestr(item, buffer)

    zout.writestr(item, buffer)         #if non-empty folder is needed


#zout.write("NULL2/NULL_NULL2.svg")
zout.write("SVGDBA.csv")

zout.close()
zin.close()

#Write an SVGDBA to an existing zip archive
#for item in zin.infolist():
#    buffer = zin.read(item.filename)
#    if (item.filename[-4:] != '.svg') and (item.filename[-4:] != '.csv'):
#        #do not write svg or csv files into the new archive
#        zout.writestr(item, buffer)

#with zipfile.ZipFile('spam.zip', 'w') as myzip:
#    myzip.write('eggs.txt')