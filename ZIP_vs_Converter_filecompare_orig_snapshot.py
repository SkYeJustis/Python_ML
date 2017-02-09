# -*- coding: utf-8 -*-
"""
Check ZIP against SVG Converter output directories
Converter output includes: PDI, Black SVG, White SVG, Black PDF, White PDF, and Visio

@author: leungs
"""

#==============================================================================
#==============================================================================
# # Creating lists of files available in ZIP / Converter directories for testing
#==============================================================================
#==============================================================================

import os
import time
import pandas as pd
from time import strftime
#fp = "C:/Users/leungs/Documents/Onelines_SVG/Termination_Hyperlinking_Testing/pisvg_AC1_20161214232228_orig/AE/ABSECON.svg"
#
#time.ctime(os.path.getctime(fp))
#os.path.getctime(fp)
#==============================================================================
# ## Getting ZIP filenames and other testing info
#==============================================================================

main_dir = "C:/Users/leungs/Documents/Onelines_SVG/Termination_Hyperlinking_Testing/01_SET/zip__conditions/"

zip_directory = main_dir + "pisvg_AC1_20170122230237"

zip_list = []
zip_clist = []
non_rawsvg = [] 
zip_ts = pd.DataFrame()

for folder in os.listdir(zip_directory):
    if folder.endswith(".csv") or folder.endswith(".CSV"):
        continue #do nothing
    else:
        #print os.path.join(directory, folder)
        #print "FOLDER" + " " + folder
        for filename in os.listdir(os.path.join(zip_directory, folder)):
            if filename.endswith(".svg") or filename.endswith(".SVG"): 
                print folder + " has " + filename
                print filename[:-4] #remove the .svg suffix
                zip_clist.append(folder + " has " + filename[:-4])
                zip_list.append(folder.upper() + " has " + filename[:-4].upper() ) #does case matter?
                
                zip_ts = zip_ts.append({'FOLDER': folder, 
                                        'SVG': filename[:-4].upper(),
                                        'TS_NUM': os.path.getctime(os.path.join(zip_directory, folder, filename)), 
                                        'TS': time.ctime(os.path.getctime(os.path.join(zip_directory, folder, filename))) }, ignore_index=True)
                continue
            else:
                non_rawsvg.append(filename + " in " + folder)
                continue
        continue
    
print len(zip_list)  #9527


zip_ts = zip_ts.sort(['TS_NUM'], ascending=False ) # Order by DESC




zip_ts.to_csv(main_dir + "zip_ts" + strftime("_%Y%m%d_%H%M") + ".csv")

# output zip file entries for another test
outputfile = open(main_dir + 'zipquery.txt', 'w')
for entry in zip_list:
    #thefile.write("%s/n" % entry)
    outputfile.write("SELECT '%s' as var FROM DUAL union all \n" % entry)
outputfile.close()

#outputfile = open('C:/Users/leungs/Documents/Onelines_SVG/Termination_Hyperlinking_Testing/zipcfilelist.txt', 'w')
#for entry in zip_clist:
#    outputfile.write("'%s' \n" % entry)
#outputfile.close()


#==============================================================================
# ## Getting PDI filenames and other testing info
#==============================================================================

pdi_directory = main_dir + "RTDATA/RTDATA"
    
pdi_list = []
pdi_clist = []
non_pdilist = []
pdi_ts = pd.DataFrame()

for folder in os.listdir(pdi_directory):
    if folder.endswith(".csv") or folder.endswith(".CSV") or folder.endswith(".xml") or folder.endswith(".XML"):
        continue #do nothing
    else: 
        for filename in os.listdir(os.path.join(pdi_directory, folder)):
            if filename.endswith(".pdi") or filename.endswith(".PDI"):
                print folder + " has " + filename
                print filename[:-4] #remove .pdi suffix
                pdi_list.append(folder.upper() + " has " + filename[:-4].upper() )
                pdi_clist.append(folder + " has " + filename[:-4])
                pdi_ts = pdi_ts.append({'FOLDER': folder, 
                                        'SVG': filename[:-4].upper(),
                                        'TS_NUM': os.path.getctime(os.path.join(pdi_directory, folder, filename)), 
                                        'TS': time.ctime(os.path.getctime(os.path.join(pdi_directory, folder, filename))) }, ignore_index=True)          
                continue
            else:
                non_pdilist.append(filename + " in " + folder)
                continue
    continue
              
print len(pdi_list) #9525

pdi_ts = pdi_ts.sort(['TS_NUM'], ascending=False ) # Order by DESC

pdi_ts.to_csv(main_dir + "pdi_ts" + strftime("_%Y%m%d_%H%M") + ".csv")



#==============================================================================
# Get Blacksvg file names -converted and other testing info
#==============================================================================
bsvg_directory = main_dir + "NODATA/NODATA/svg"
    
bsvg_list = []
non_bsvglist = []
bsvg_clist = []
bsvg_ts = pd.DataFrame()

for folder in os.listdir(bsvg_directory):
    if folder.endswith(".csv") or folder.endswith(".CSV"):
        continue #do nothing
    else: 
        for filename in os.listdir(os.path.join(bsvg_directory, folder)):
            if filename.endswith(".svg") or filename.endswith(".SVG"):
                print folder + " has " + filename
                print filename[:-4] #remove .svg suffix
                bsvg_list.append(folder.upper() + " has " + filename[:-4].upper() )
                bsvg_clist.append(folder + " has " + filename[:-4])
                bsvg_ts = bsvg_ts.append({'FOLDER': folder, 
                                        'SVG': filename[:-4].upper(),
                                        'TS_NUM': os.path.getctime(os.path.join(bsvg_directory, folder, filename)), 
                                        'TS': time.ctime(os.path.getctime(os.path.join(bsvg_directory, folder, filename))) }, ignore_index=True)          
                
                continue
            else:
                non_bsvglist.append(filename + " in " + folder)
                continue
    continue
              
print len(bsvg_list) #9527

bsvg_ts = bsvg_ts.sort(['TS_NUM'], ascending=False ) # Order by DESC

bsvg_ts.to_csv(main_dir + "bsvg_ts" + strftime("_%Y%m%d_%H%M") + ".csv")


#==============================================================================
# Get Whitesvg file names -converted and other testing info
#==============================================================================
wsvg_directory = main_dir + "ModelManagement/ModelManagement/svg"
    
wsvg_list = []
wsvg_clist = []
non_wsvglist = []
wsvg_ts = pd.DataFrame()

for folder in os.listdir(wsvg_directory):
    if folder.endswith(".csv") or folder.endswith(".CSV"):
        continue #do nothing
    else: 
        for filename in os.listdir(os.path.join(wsvg_directory, folder)):
            if filename.endswith(".svg") or filename.endswith(".SVG"):
                print folder + " has " + filename
                print filename[:-4] #remove .svg suffix
                wsvg_list.append(folder.upper() + " has " + filename[:-4].upper() )
                wsvg_clist.append(folder + " has " + filename[:-4])
                wsvg_ts = wsvg_ts.append({'FOLDER': folder, 
                                        'SVG': filename[:-4].upper(),
                                        'TS_NUM': os.path.getctime(os.path.join(wsvg_directory, folder, filename)), 
                                        'TS': time.ctime(os.path.getctime(os.path.join(wsvg_directory, folder, filename))) }, ignore_index=True)          
 
                continue
            else:
                non_wsvglist.append(filename + " in " + folder)
                continue
    continue
           
   
print len(wsvg_list) #9527

wsvg_ts = wsvg_ts.sort(['TS_NUM'], ascending=False ) # Order by DESC

wsvg_ts.to_csv(main_dir + "wsvg_ts" + strftime("_%Y%m%d_%H%M") + ".csv")


#==============================================================================
# Get WhitePDF file names -converted and other testing info
#==============================================================================
wpdf_directory = main_dir + "ModelManagement/ModelManagement/pdf"
    
wpdf_list = []
wpdf_clist = []
non_wpdflist = []
wpdf_ts = pd.DataFrame()

for folder in os.listdir(wpdf_directory):
    if folder.endswith(".csv") or folder.endswith(".CSV"):
        continue #do nothing
    else: 
        for filename in os.listdir(os.path.join(wpdf_directory, folder)):
            if filename.endswith(".pdf") or filename.endswith(".PDF"):
                print folder + " has " + filename
                print filename[:-4] #remove .pdf suffix
                wpdf_list.append(folder.upper() + " has " + filename[:-4].upper() )
                wpdf_clist.append(folder + " has " + filename[:-4])
                wpdf_ts = wpdf_ts.append({'FOLDER': folder, 
                                        'SVG': filename[:-4].upper(),
                                        'TS_NUM': os.path.getctime(os.path.join(wpdf_directory, folder, filename)), 
                                        'TS': time.ctime(os.path.getctime(os.path.join(wpdf_directory, folder, filename))) }, ignore_index=True)          
 
                continue
            else:
                non_wpdflist.append(filename + " in " + folder)
                continue
    continue
               
print len(wpdf_list) #9526

wpdf_ts = wpdf_ts.sort(['TS_NUM'], ascending=False ) # Order by DESC
wpdf_ts.to_csv(main_dir + "wpdf_ts" + strftime("_%Y%m%d_%H%M") + ".csv")


#==============================================================================
# Get BlackPDF file names -converted and other testing info
#==============================================================================
bpdf_directory = main_dir + "NODATA/NODATA/pdf"
    
bpdf_list = []
bpdf_clist = []
non_bpdflist = []
bpdf_ts = pd.DataFrame()

for folder in os.listdir(bpdf_directory):
    if folder.endswith(".csv") or folder.endswith(".CSV"):
        continue #do nothing
    else: 
        for filename in os.listdir(os.path.join(bpdf_directory, folder)):
            if filename.endswith(".pdf") or filename.endswith(".PDF"):
                print folder + " has " + filename
                print filename[:-4] #remove .pdf suffix
                bpdf_list.append(folder.upper() + " has " + filename[:-4].upper() )
                bpdf_clist.append(folder + " has " + filename[:-4])
                bpdf_ts = bpdf_ts.append({'FOLDER': folder, 
                                        'SVG': filename[:-4].upper(),
                                        'TS_NUM': os.path.getctime(os.path.join(bpdf_directory, folder, filename)), 
                                        'TS': time.ctime(os.path.getctime(os.path.join(bpdf_directory, folder, filename))) }, ignore_index=True)          
                continue
            else:
                non_bpdflist.append(filename + " in " + folder)
                continue
    continue
           
   
print len(bpdf_list) #9526

bpdf_ts = bpdf_ts.sort(['TS_NUM'], ascending=False ) # Order by DESC
bpdf_ts.to_csv(main_dir + "bpdf_ts" + strftime("_%Y%m%d_%H%M") + ".csv")


#==============================================================================
# Get VSD file names -converted and other testing info
#==============================================================================
vsd_directory = main_dir + "ModelManagement/ModelManagement/vsd"
    
vsd_list = []
vsd_clist = []
non_vsdlist = []
vsd_ts = pd.DataFrame()

for folder in os.listdir(vsd_directory):
    if folder.endswith(".csv") or folder.endswith(".CSV"):
        continue #do nothing
    else: 
        for filename in os.listdir(os.path.join(vsd_directory, folder)):
            if filename.endswith(".vsd") or filename.endswith(".VSD"):
                print folder + " has " + filename
                print filename[:-4] #remove .vsd suffix
                vsd_list.append(folder.upper() + " has " + filename[:-4].upper() )
                vsd_clist.append(folder + " has " + filename[:-4])
                vsd_ts = vsd_ts.append({'FOLDER': folder, 
                                        'SVG': filename[:-4].upper(),
                                        'TS_NUM': os.path.getctime(os.path.join(vsd_directory, folder, filename)), 
                                        'TS': time.ctime(os.path.getctime(os.path.join(vsd_directory, folder, filename))) }, ignore_index=True)          

                continue
            else:
                non_vsdlist.append(filename + " in " + folder)
                continue
    continue
           
   
print len(vsd_list) #9215

vsd_ts = vsd_ts.sort(['TS_NUM'], ascending=False ) # Order by DESC
vsd_ts.to_csv(main_dir + "vsd_ts" + strftime("_%Y%m%d_%H%M") + ".csv")


###############################################################################

#==============================================================================
#==============================================================================
# # TESTING: Checking for file extension errors
#==============================================================================
#==============================================================================
outputfile = open(main_dir + 'filetype_chk.txt', 'w')

outputfile.write("Non Raw SVGs in ZIP folder")
outputfile.write(str(non_rawsvg))
outputfile.write("\n")

outputfile.write("Non PDIs in PDI folder")
outputfile.write(str(non_pdilist))
outputfile.write("\n")

outputfile.write("Non Black SVGs in Black SVG folder")
outputfile.write(str(non_bsvglist))
outputfile.write("\n")

outputfile.write("Non White SVGs in White SVG folder")
outputfile.write(str(non_wsvglist))
outputfile.write("\n")

outputfile.write("Non White PDFs in White PDF folder")
outputfile.write(str(non_wpdflist))
outputfile.write("\n")

outputfile.write("Non Black PDFs in Black PDF folder")
outputfile.write(str(non_bpdflist))
outputfile.write("\n")

outputfile.write("Non Visios in Visio folder")
outputfile.write(str(non_vsdlist))
outputfile.write("\n")


outputfile.close()

#==============================================================================
#==============================================================================
# # TESTING: Check whether any lists have duplicates
#==============================================================================
#==============================================================================
import collections

#a = [1,2,3,2,1,5,6,5,5,5]
#print [item for item, count in collections.Counter(a).items() if count > 1]

outputfile = open(main_dir + 'duplicates.txt', 'w')

#All caps
outputfile.write("Not Case Sensitive \n")
outputfile.write("Duplicates in ZIP  \n")
outputfile.write( str([item for item, count in collections.Counter(zip_list).items() if count > 1] ) )
outputfile.write("\n")
outputfile.write("Duplicates in PDI \n")
outputfile.write( str([item for item, count in collections.Counter(pdi_list).items() if count > 1]) )
outputfile.write("\n")
outputfile.write("Duplicates in Black SVG \n")
outputfile.write( str([item for item, count in collections.Counter(bsvg_list).items() if count > 1]) )
outputfile.write("\n")
outputfile.write("Duplicates in White SVG \n")
outputfile.write( str([item for item, count in collections.Counter(wsvg_list).items() if count > 1]) )
outputfile.write("\n")
outputfile.write("Duplicates in White PDF \n")
outputfile.write( str([item for item, count in collections.Counter(wpdf_list).items() if count > 1]) )
outputfile.write("\n")
outputfile.write("Duplicates in Black PDF \n")
outputfile.write( str([item for item, count in collections.Counter(bpdf_list).items() if count > 1]) )
outputfile.write("\n")
outputfile.write("Duplicates in Visio \n")
outputfile.write( str([item for item, count in collections.Counter(vsd_list).items() if count > 1]) )
outputfile.write("\n")

#Not all caps
outputfile.write("Case Sensitive  \n")
outputfile.write("Duplicates in ZIP - case sensitive  \n")
outputfile.write( str([item for item, count in collections.Counter(zip_clist).items() if count > 1]) )
outputfile.write("\n")
outputfile.write("Duplicates in PDI - case sensitive  \n")       
outputfile.write( str([item for item, count in collections.Counter(pdi_clist).items() if count > 1]) )
outputfile.write("\n")
outputfile.write("Duplicates in Black SVG - case sensitive  \n")
outputfile.write( str([item for item, count in collections.Counter(bsvg_clist).items() if count > 1]) )
outputfile.write("\n")
outputfile.write("Duplicates in White SVG - case sensitive  \n")
outputfile.write( str([item for item, count in collections.Counter(wsvg_clist).items() if count > 1]) )
outputfile.write("\n")
outputfile.write("Duplicates in White PDF - case sensitive  \n")
outputfile.write( str([item for item, count in collections.Counter(wpdf_clist).items() if count > 1]) )
outputfile.write("\n")
outputfile.write("Duplicates in Black PDF - case sensitive  \n")
outputfile.write( str([item for item, count in collections.Counter(bpdf_clist).items() if count > 1]) )
outputfile.write("\n")
outputfile.write("Duplicates in Visio - case sensitive  \n")
outputfile.write( str([item for item, count in collections.Counter(vsd_clist).items() if count > 1]) )
outputfile.write("\n")

outputfile.close()
 
#==============================================================================
#==============================================================================
# # TESTING: Find differences in arrays
#==============================================================================
#==============================================================================
# Testing code that highlights differences

#temp1 = ['One', 'Two', 'Three', 'Four']
#temp2 = ['One', 'Two']
#list(set(temp1) - set(temp2))
#
#set([1, 2]) - set([2, 3])
#
## Order should not matter - good
#list(set([1, 2]) - set([2, 1]))
#list(set([1, 2]) - set([1, 2]))
#
## duplicates should not matter
## 2 should be found -good
#list(set([1, 2]) - set([1, 1]))


#==============================================================================
### Case insensitive: PDI differences
#==============================================================================
pdi_difflist = []
msg = None

if len(list(set(zip_list) - set(pdi_list))) > len(list(set(pdi_list) - set(zip_list))):
    pdi_difflist = list(set(zip_list) - set(pdi_list))
    print "Chose ZIP list"
    msg = "Chose ZIP list"
    print "Difference between ZIP and PDI: "+ str(len(zip_list) - len(pdi_list))

else:
    pdi_difflist = list(set(pdi_list) - set(zip_list))
    print "Chose PDI list"
    msg = "Chose PDI list"
    print "Difference between PDI and ZIP: "+ str(len(pdi_list) - len(zip_list))

pdi_difflist.sort() #ascending order

pdi_difflist

outputfile = open(main_dir + 'pdi_difflist.txt', 'w')

outputfile.write( msg + "\n" )

for entry in pdi_difflist:
    #thefile.write("%s/n" % entry)
    outputfile.write(" '%s' \n" % entry)

outputfile.write( str(len(pdi_difflist)) )

outputfile.close()
#==============================================================================
### Case insensitive: BSVG differences
#==============================================================================
bsvg_difflist = []
msg = None

if len(list(set(zip_list) - set(bsvg_list))) > len(list(set(bsvg_list) - set(zip_list))):
    bsvg_difflist = list(set(zip_list) - set(bsvg_list))
    print "Chose ZIP list"
    msg = "Chose ZIP list"
    print "Difference between ZIP and bsvg: "+ str(len(zip_list) - len(bsvg_list))

else:
    bsvg_difflist = list(set(bsvg_list) - set(zip_list))
    print "Chose bsvg list"
    msg = "Chose bsvg list"
    print "Difference between bsvg and ZIP: "+ str(len(bsvg_list) - len(zip_list))

bsvg_difflist.sort() #ascending order

bsvg_difflist
outputfile = open(main_dir + 'bsvg_difflist.txt', 'w')

outputfile.write( msg + "\n" )
for entry in bsvg_difflist:
    #thefile.write("%s/n" % entry)
    outputfile.write(" '%s' \n" % entry)

outputfile.write( str(len(bsvg_difflist)) )
outputfile.close()
#==============================================================================
### Case insensitive: wsvg differences
#==============================================================================

wsvg_difflist = []
msg = None

if len(list(set(zip_list) - set(wsvg_list))) > len(list(set(wsvg_list) - set(zip_list))):
    wsvg_difflist = list(set(zip_list) - set(wsvg_list))
    print "Chose ZIP list"
    msg = "Chose ZIP list"
    print "Difference between ZIP and wsvg: "+ str(len(zip_list) - len(wsvg_list))

else:
    wsvg_difflist = list(set(wsvg_list) - set(zip_list))
    print "Chose wsvg list"
    msg = "Chose ZIP list"
    print "Difference between wsvg and ZIP: "+ str(len(wsvg_list) - len(zip_list))

wsvg_difflist.sort() #ascending order

wsvg_difflist

outputfile = open(main_dir + 'wsvg_difflist.txt', 'w')
outputfile.write( msg + "\n" )

for entry in wsvg_difflist:
    #thefile.write("%s/n" % entry)
    outputfile.write(" '%s' \n" % entry)
    
outputfile.write( str(len(wsvg_difflist)) )
outputfile.close()

#==============================================================================
### Case insensitive: wpdf differences
#==============================================================================

wpdf_difflist = []
msg = None
if len(list(set(zip_list) - set(wpdf_list))) > len(list(set(wpdf_list) - set(zip_list))):
    wpdf_difflist = list(set(zip_list) - set(wpdf_list))
    print "Chose ZIP list"
    msg = "Chose ZIP list"
    print "Difference between ZIP and wpdf: "+ str(len(zip_list) - len(wpdf_list))

else:
    wpdf_difflist = list(set(wpdf_list) - set(zip_list))
    print "Chose wpdf list"
    msg = "Chose wpdf list"
    print "Difference between wpdf and ZIP: "+ str(len(wpdf_list) - len(zip_list))

wpdf_difflist.sort() #ascending order

wpdf_difflist

outputfile = open(main_dir + 'wpdf_difflist.txt', 'w')
outputfile.write( msg + "\n" )
for entry in wpdf_difflist:
    #thefile.write("%s/n" % entry)
    outputfile.write(" '%s' \n" % entry)
    
outputfile.write( str(len(wpdf_difflist)) )
outputfile.close()

#==============================================================================
### Case insensitive: bpdf differences
#==============================================================================

bpdf_difflist = []
msg = None

if len(list(set(zip_list) - set(bpdf_list))) > len(list(set(bpdf_list) - set(zip_list))):
    bpdf_difflist = list(set(zip_list) - set(bpdf_list))
    print "Chose ZIP list"
    msg = "Chose ZIP list"
    print "Difference between ZIP and bpdf: "+ str(len(zip_list) - len(bpdf_list))

else:
    bpdf_difflist = list(set(bpdf_list) - set(zip_list))
    print "Chose bpdf list"
    msg = "Chose bpdf list"
    print "Difference between ZIP and bpdf: "+ str(len(bpdf_list) - len(zip_list))

bpdf_difflist.sort() #ascending order

bpdf_difflist 

outputfile = open(main_dir + 'bpdf_difflist.txt', 'w')

outputfile.write( msg + "\n" )
for entry in bpdf_difflist:
    #thefile.write("%s/n" % entry)
    outputfile.write(" '%s' \n" % entry)

outputfile.write( str(len(bpdf_difflist)) )
outputfile.close()

#==============================================================================
### Case insensitive: vsd differences
#==============================================================================

vsd_difflist = []
msg = None

if len(list(set(zip_list) - set(vsd_list))) > len(list(set(vsd_list) - set(zip_list))):
    vsd_difflist = list(set(zip_list) - set(vsd_list))
    print "Chose ZIP list"
    msg = "Chose ZIP list"
    print "Difference between ZIP and vsd: "+ str(len(zip_list) - len(vsd_list))

else:
    vsd_difflist = list(set(vsd_list) - set(zip_list))
    print "Chose vsd list"
    msg = "Chose vsd list"
    print "Difference between ZIP and vsd: "+ str(len(vsd_list) - len(zip_list))

vsd_difflist.sort() #ascending order

vsd_difflist 

outputfile = open(main_dir + 'vsd_difflist.txt', 'w')
outputfile.write( msg + "\n" )

for entry in vsd_difflist :
    #thefile.write("%s/n" % entry)
    outputfile.write(" '%s' \n" % entry)

outputfile.write( str(len(vsd_difflist)) )
outputfile.close()

###############################################################################
###############################################################################
###############################################################################

#==============================================================================
### Case sensitive: PDI differences
#==============================================================================
pdi_cdifflist = []
msg = None

if len(list(set(zip_clist) - set(pdi_clist))) > len(list(set(pdi_clist) - set(zip_clist))):
    pdi_cdifflist = list(set(zip_clist) - set(pdi_clist))
    print "Chose ZIP list"
    msg = "Chose ZIP list"
    print "Difference between ZIP and PDI: "+ str(len(zip_clist) - len(pdi_clist))

else:
    pdi_cdifflist = list(set(pdi_clist) - set(zip_clist))
    print "Chose PDI list"
    msg = "Chose PDI list"
    print "Difference between PDI and ZIP: "+ str(len(pdi_clist) - len(zip_clist))

pdi_cdifflist.sort() #ascending order

pdi_cdifflist

outputfile = open(main_dir + 'pdi_cdifflist.txt', 'w')

outputfile.write( msg + "\n" )
for entry in pdi_cdifflist :
    #thefile.write("%s/n" % entry)
    outputfile.write(" '%s' \n" % entry)
outputfile.write( str(len(pdi_cdifflist)) )
outputfile.close()

#==============================================================================
### Case sensitive: BSVG differences
#==============================================================================

bsvg_cdifflist = []
msg = None

if len(list(set(zip_clist) - set(bsvg_clist))) > len(list(set(bsvg_clist) - set(zip_clist))):
    bsvg_cdifflist = list(set(zip_clist) - set(bsvg_clist))
    print "Chose ZIP list"
    msg = "Chose ZIP list"
    print "Difference between ZIP and bsvg: "+ str(len(zip_clist) - len(bsvg_clist))

else:
    bsvg_cdifflist = list(set(bsvg_clist) - set(zip_clist))
    print "Chose bsvg list"
    msg = "Chose bsvg list"
    print "Difference between bsvg and ZIP: "+ str(len(bsvg_clist) - len(zip_clist))

bsvg_cdifflist.sort() #ascending order

bsvg_cdifflist

outputfile = open(main_dir + 'bsvg_cdifflist.txt', 'w')
outputfile.write( msg + "\n" )
for entry in bsvg_cdifflist :
    #thefile.write("%s/n" % entry)
    outputfile.write(" '%s' \n" % entry)
    
outputfile.write( str(len(bsvg_cdifflist)) )
outputfile.close()

#==============================================================================
### Case sensitive: wsvg differences
#==============================================================================

wsvg_cdifflist = []
msg = None

if len(list(set(zip_clist) - set(wsvg_clist))) > len(list(set(wsvg_clist) - set(zip_clist))):
    wsvg_cdifflist = list(set(zip_clist) - set(wsvg_clist))
    print "Chose ZIP list"
    msg = "Chose ZIP list"
    print "Difference between ZIP and wsvg: "+ str(len(zip_clist) - len(wsvg_clist))

else:
    wsvg_cdifflist = list(set(wsvg_clist) - set(zip_clist))
    print "Chose wsvg list"
    msg = "Chose wsvg list"
    print "Difference between wsvg and ZIP: "+ str(len(wsvg_clist) - len(zip_clist))

wsvg_cdifflist.sort() #ascending order

wsvg_cdifflist

outputfile = open(main_dir + 'wsvg_cdifflist.txt', 'w')

outputfile.write( msg + "\n" )
for entry in wsvg_cdifflist:
    #thefile.write("%s/n" % entry)
    outputfile.write(" '%s' \n" % entry)
    
outputfile.write( str(len(wsvg_cdifflist)) )
outputfile.close()
#==============================================================================
### Case sensitive: wpdf differences
#==============================================================================

wpdf_cdifflist = []
msg = None

if len(list(set(zip_clist) - set(wpdf_clist))) > len(list(set(wpdf_clist) - set(zip_clist))):
    wpdf_cdifflist = list(set(zip_clist) - set(wpdf_clist))
    print "Chose ZIP list"
    msg = "Chose ZIP list"
    print "Difference between ZIP and wpdf: "+ str(len(zip_clist) - len(wpdf_clist))

else:
    wpdf_cdifflist = list(set(wpdf_clist) - set(zip_clist))
    print "Chose wpdf list"
    msg = "Chose wpdf list"
    print "Difference between wpdf and ZIP: "+ str(len(wpdf_clist) - len(zip_clist))

wpdf_cdifflist.sort() #ascending order

wpdf_cdifflist

outputfile = open(main_dir + 'wpdf_cdifflist.txt', 'w')
outputfile.write( msg + "\n" )

for entry in wpdf_cdifflist:
    #thefile.write("%s/n" % entry)
    outputfile.write(" '%s' \n" % entry)
outputfile.write( str(len(wpdf_cdifflist)) )
outputfile.close()

#==============================================================================
### Case sensitive: bpdf differences
#==============================================================================

bpdf_cdifflist = []
msg = None
if len(list(set(zip_clist) - set(bpdf_clist))) > len(list(set(bpdf_clist) - set(zip_clist))):
    bpdf_cdifflist = list(set(zip_clist) - set(bpdf_clist))
    print "Chose ZIP list"
    msg = "Chose ZIP list"
    print "Difference between ZIP and bpdf: "+ str(len(zip_clist) - len(bpdf_clist))

else:
    bpdf_cdifflist = list(set(bpdf_clist) - set(zip_clist))
    print "Chose bpdf list"
    msg = "Chose bpdf list"
    print "Difference between ZIP and bpdf: "+ str(len(bpdf_clist) - len(zip_clist))

bpdf_cdifflist.sort() #ascending order

bpdf_cdifflist 

outputfile = open(main_dir + 'bpdf_cdifflist.txt', 'w')
outputfile.write( msg + "\n" )
for entry in bpdf_cdifflist:
    #thefile.write("%s/n" % entry)
    outputfile.write(" '%s' \n" % entry)

outputfile.write( str(len(bpdf_cdifflist)) )
outputfile.close()
#==============================================================================
### Case sensitive: vsd differences
#==============================================================================

vsd_cdifflist = []
msg = None

if len(list(set(zip_clist) - set(vsd_clist))) > len(list(set(vsd_clist) - set(zip_clist))):
    vsd_cdifflist = list(set(zip_clist) - set(vsd_clist))
    print "Chose ZIP list"
    msg = "Chose ZIP list"
    print "Difference between ZIP and vsd: "+ str(len(zip_clist) - len(vsd_clist))

else:
    vsd_cdifflist = list(set(vsd_clist) - set(zip_clist))
    print "Chose vsd list"
    msg = "Chose vsd list"
    print "Difference between ZIP and vsd: "+ str(len(vsd_clist) - len(zip_clist))

vsd_cdifflist.sort() #ascending order

vsd_cdifflist

outputfile = open(main_dir + 'vsd_cdifflist.txt', 'w')
outputfile.write( msg + "\n" )
for entry in vsd_cdifflist:
    #thefile.write("%s/n" % entry)
    outputfile.write(" '%s' \n" % entry)
    
outputfile.write( str(len(vsd_cdifflist)) )
outputfile.close()