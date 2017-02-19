# -*- coding: utf-8 -*-
"""
Comparing folder directories: aDirectory and aDirectory2

@author: SkyeJustIs
"""

#==============================================================================
#==============================================================================
# # Creating lists of files available aDirectory and aDirectory2
#==============================================================================
#==============================================================================

import os
import time
import pandas as pd
from time import strftime

#==============================================================================
# ## Getting ZIP filenames and other testing info
#==============================================================================

main_dir = "C:/Users/skye/Documents/fileDirectories/"

a_directory = main_dir + "aDirectory"

aDir_list = []
aDir_clist = []
non_filetype = [] 
aDir_ts = pd.DataFrame()

for folder in os.listdir(a_directory):
    if folder.endswith(".csv") or folder.endswith(".CSV"):
        continue #do nothing - ignore this file a the top of the directory
    else:

        for filename in os.listdir(os.path.join(a_directory, folder)):
            if filename.endswith(".jpeg") or filename.endswith(".jpeg"): 
                print folder + " has " + filename
                print filename[:-4] #remove the .svg suffix
                aDir_clist.append(folder + " has " + filename[:-4])
                aDir_list.append(folder.upper() + " has " + filename[:-4].upper() ) #does case matter?
                
                aDir_ts = aDir_ts.append({'FOLDER': folder, 
                                        'FILE': filename[:-4].upper(),
                                        'TS_NUM': os.path.getctime(os.path.join(a_directory, folder, filename)), 
                                        'TS': time.ctime(os.path.getctime(os.path.join(a_directory, folder, filename))) }, ignore_index=True)
                continue
            else:
                non_filetype.append(filename + " in " + folder)
                continue
        continue
    
#Get the length of directory
print len(aDir_list) 

# Order the file names by DESC -- latest modified files will appear a the top
aDir_ts = aDir_ts.sort(['TS_NUM'], ascending=False ) 


#Output a csv that contains the modified date of the file, the folder name, and a file name
aDir_ts.to_csv(main_dir + "a_directory_ts" + strftime("_%Y%m%d_%H%M") + ".csv")


#==============================================================================
# ## Getting filenames and other file info from aDir2
#==============================================================================

a2_directory = main_dir + "aDir2"
    
adir2_list = []
adir2_clist = []
non_filetype2 = []
adir2_ts = pd.DataFrame()

for folder in os.listdir(a2_directory):
    if folder.endswith(".csv") or folder.endswith(".CSV") or folder.endswith(".xml") or folder.endswith(".XML"):
        continue #do nothing - ignore this file a the top of the directory
    else: 
        for filename in os.listdir(os.path.join(a2_directory, folder)):
            if filename.endswith(".png") or filename.endswith(".PNG"):
                print folder + " has " + filename
                print filename[:-4] #remove .pdi suffix
                adir2_list.append(folder.upper() + " has " + filename[:-4].upper() )
                adir2_clist.append(folder + " has " + filename[:-4])
                adir2_ts = adir2_ts.append({'FOLDER': folder, 
                                        'FILE': filename[:-4].upper(),
                                        'TS_NUM': os.path.getctime(os.path.join(a2_directory, folder, filename)), 
                                        'TS': time.ctime(os.path.getctime(os.path.join(a2_directory, folder, filename))) }, ignore_index=True)          
                continue
            else:
                non_filetype2.append(filename + " in " + folder)
                continue
    continue
              
print len(adir2_list) 

#Order the file names by DESC -- latest modified files will appear a the top
adir2_ts = adir2_ts.sort(['TS_NUM'], ascending=False )

#Output a csv that contains the modified date of the file, the folder name, and a file name
adir2_ts.to_csv(main_dir + "a_directory2_ts" + strftime("_%Y%m%d_%H%M") + ".csv")




#==============================================================================
#==============================================================================
# # TESTING: Checking for file extension errors
#==============================================================================
#==============================================================================
outputfile = open(main_dir + 'filetype_chk.txt', 'w')

outputfile.write("Non FileTypes in aDirectory folder")
outputfile.write(str(non_filetype))
outputfile.write("\n")

outputfile.write("Non FileTypes in aDirectory2 folder")
outputfile.write(str(non_filetype2))
outputfile.write("\n")

outputfile.close()

#==============================================================================
#==============================================================================
# # TESTING: Check whether any lists have duplicates
#==============================================================================
#==============================================================================
import collections

outputfile = open(main_dir + 'duplicates.txt', 'w')

#All caps
outputfile.write("Not Case Sensitive \n")
outputfile.write("Duplicates in aDirectory  \n")
outputfile.write( str([item for item, count in collections.Counter(aDir_list).items() if count > 1] ) )
outputfile.write("\n")
outputfile.write("Duplicates in aDirectory2 \n")
outputfile.write( str([item for item, count in collections.Counter(adir2_list).items() if count > 1]) )

#Not all caps
outputfile.write("Case Sensitive  \n")
outputfile.write("Duplicates in aDirectory - case sensitive  \n")
outputfile.write( str([item for item, count in collections.Counter(aDir_list).items() if count > 1]) )
outputfile.write("\n")
outputfile.write("Duplicates in aDirectory2 - case sensitive  \n")       
outputfile.write( str([item for item, count in collections.Counter(adir2_list).items() if count > 1]) )

outputfile.close()
 
#==============================================================================
#==============================================================================
# # TESTING: Find differences in arrays
#==============================================================================
#==============================================================================

#==============================================================================
### Case insensitive: Folder directory differences
### Outputs a text file listing the differences and the number of differences
#==============================================================================
dir_difflist = []
msg = None


outputfile = open(main_dir + 'dir_difflist.txt', 'w')

msg = "Differences only in aDirectory (not in aDirectory2)"
outputfile.write( msg + "\n" )
dir_difflist = list(set(aDir_list) - set(adir2_list))
dir_difflist.sort() #sort list in ascending order
for entry in dir_difflist :
    #thefile.write("%s/n" % entry)
    outputfile.write(" '%s' \n" % entry)
outputfile.write( str(len(dir_difflist)) )

msg = "Differences only in aDirectory2 (not in aDirectory)"
outputfile.write( msg + "\n" )
dir_difflist = list(set(adir2_list) - set(aDir_list))
dir_difflist.sort() #sort list in ascending order
for entry in dir_difflist :
    #thefile.write("%s/n" % entry)
    outputfile.write(" '%s' \n" % entry)
outputfile.write( str(len(dir_difflist)) )

outputfile.close()

#==============================================================================
### Case sensitive: Folder directory differences
### Outputs a text file listing the differences and the number of differences
#==============================================================================
dir_cdifflist = []
msg = None


outputfile = open(main_dir + 'dir_cdifflist.txt', 'w')

msg = "Differences only in aDirectory (not in aDirectory2)"
outputfile.write( msg + "\n" )
dir_cdifflist = list(set(aDir_clist) - set(adir2_clist))
dir_cdifflist.sort() #sort list in ascending order
for entry in dir_cdifflist :
    #thefile.write("%s/n" % entry)
    outputfile.write(" '%s' \n" % entry)
outputfile.write( str(len(dir_cdifflist)) )

msg = "Differences only in aDirectory2 (not in aDirectory)"
outputfile.write( msg + "\n" )
dir_cdifflist = list(set(adir2_clist) - set(aDir_clist))
dir_cdifflist.sort() #sort list in ascending order
for entry in dir_cdifflist :
    #thefile.write("%s/n" % entry)
    outputfile.write(" '%s' \n" % entry)
outputfile.write( str(len(dir_cdifflist)) )

outputfile.close()

