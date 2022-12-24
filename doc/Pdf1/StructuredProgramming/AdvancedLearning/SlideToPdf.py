import glob
from pptx import Presentation
from pptx.util import Inches
import os


slideFiles = glob.glob("*.pptx")

slideFiles.sort()


for iterator in range(len(slideFiles) - 1):


  # Create a PDF file object


  pdf_file_name = os.path.basename(iterator).split(".")[0]

  pdf_file_name = pdf_file_name+".pdf"
  pdf_file = open(pdf_file_name, "wb")




  # Save the PowerPoint to the PDF file
  iterator.save(pdf_file)

  # Close the PDF file
  pdf_file.close()

