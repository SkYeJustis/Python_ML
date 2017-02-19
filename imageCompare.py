# -*- coding: utf-8 -*-
"""
Comparing image similarity for SVGs, PDFs, and VSDs

Note: 
- SVG, PDF, and VSD files are converted to an image filetype (PNG) 
for the structural similarity score function in sci-kit image.
- Due to .exe installation for the ImageMagick module alternative modules and an Rscript 
was used to convert the filetypes
"""

from skimage.measure import compare_ssim as ssim
import cv2
import cairosvg
import os

# Main directory that contains files in different subfolders according to filetype
os.chdir('C:/Users/skye/.spyder2')

#==============================================================================
# # Convert SVG -> PNG
#==============================================================================


directory = "samplesvgs\\"
nm = []
for filename in os.listdir(directory):
    if filename.endswith(".svg") or filename.endswith(".SVG"): 
        nm = filename[:-4] + ".png"
        cairosvg.svg2png(
            url= os.path.join(directory, filename), 
            write_to= os.path.join("samplepngs\\", nm) )
        continue
    else:
        continue    


#==============================================================================
# # Convert VISIO -> PNG
#==============================================================================
from visio2img import visio2img


                     
directory = "samplevsd/"
nm = []
for filename in os.listdir(directory):
    if filename.endswith(".vsd") or filename.endswith(".VSD"):
        # Remove ending from the previous file name and replace with .png
        nm = filename[:-4] + ".png" 
        visio2img.export_img( os.path.join(directory, filename),
                             os.path.join("samplepngs/", nm),
                             pagenum = 1)
        continue
    else:
        continue   

#==============================================================================
# Convert PDFs -> PNG using an R script
#==============================================================================
import subprocess

#Call R script
subprocess.call (['C:/Program Files/R/R-3.2.0/bin/x64/Rscript.exe', '--vanilla', 'convert_pdfs_to_pngs.R']) 


#==============================================================================
# # Get similarity scores 
# # From converted SVGs (Python) and PDFs (R)
#==============================================================================
directory = "samplepngs/"
image1 = []
image1_nm = []
image2 = []
image2_nm = []
results = []


for filename in os.listdir(directory):
    if "_1.png" in filename:
        image1_nm = filename[:-6]
        image1 = cv2.imread(os.path.join(directory, filename))
        continue            
    elif "_2.png" in filename: 
        image2_nm = filename[:-6]
        image2 = cv2.imread(os.path.join(directory, filename))
        
        if image1 != None and image2 != None and image1_nm == image2_nm:
            #print image1_nm + " sim. score: " + str(ss)
            try:
                results.append(image1_nm + " similarity score: " + str(ssim(image1, image2, multichannel=True)))
                continue #looping to next instance
            except ValueError as e:
                results.append(image1_nm + "-- Please check manually. ERROR: " + str(e) ) #Value error indicated different image dimensions
                continue #looping to next instance
            continue
        else:
            print "Calculation for " + image1_nm + "not successful"
            continue
        continue
    else:
        print filename + " is not named correctly"
        continue    


#==============================================================================
# Print results in a readable format
#==============================================================================
print('\n'.join('{}: {}'.format(*k) for k in enumerate(results)))

