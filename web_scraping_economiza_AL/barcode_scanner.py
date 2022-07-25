import cv2
from pyzbar import pyzbar

def extract_barcode(image_path=None, frame=None):
    if image_path:
        img = cv2.imread(image_path)
    else:
        img = frame

    try:
        barcode = pyzbar.decode(img)
        barcode_data = barcode[0].data.decode('utf-8')
  
        return barcode_data
        
    except:
        return None
    