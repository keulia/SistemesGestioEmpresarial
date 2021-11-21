import os;
import sys;
import cv2
from pyzbar.pyzbar import decode


def BarcodeReader(image):
     
    # reading the image using cv2
    img = cv2.imread(image)
    detectedBarcodes = decode(img) # Decoding out barcode image
      

    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
       
          # We go through each different barcode
        for barcode in detectedBarcodes: 
           
            # Locating the position of the barcode in the image
            (x, y, w, h) = barcode.rect
             
            
            if barcode.data!="":
               
            # Print the barcode data
                id = barcode.data.decode("utf-8") # fetching the id, We convert it into utf-8
                id = int(id[:12]) # We remove the last digit and turning it into an int
                return id


n = len(sys.argv)

studentList = []
if n > 1:
    dirPath =  sys.argv[1];
    print(dirPath)

for x in os.listdir(dirPath):
    if x.endswith(".png"):
        stuidentName =  x.replace('.png','')
        print(stuidentName)
        print(BarcodeReader(x))
