#set working directory
#getwd() 
setwd("C:/Users/leungs/.spyder2")

library("pdftools")


file.names = list.files(path="samplepdfs/", pattern="*.pdf", full.names=TRUE, recursive=FALSE)

title = NULL
fname = NULL
bitmap = NULL

# Loop through and convert all pdf files in one directory into png files within another directory
for(i in 1:length(file.names)){
  file = file.names[i]
  fname = gsub("(.*/)", "", file)
  title = as.character(gsub("(.pdf$)","",fname))

  # Read in file - dpi setting cannot be too high (too much data for algorithm to process)
  bitmap = pdf_render_page(file, page = 1, dpi = 100)
  title = paste0(title, ".png")
  print(title)

  # Convert file and put in different directory
  png::writePNG(bitmap, paste0("C:/Users/leungs/.spyder2/samplepngs/", title))
  
}
