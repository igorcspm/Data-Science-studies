from http.client import FOUND
import cv2
from time import sleep
from barcode_scanner import extract_barcode

def live_barcode_scanner():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (640, 480))
        if not ret:
            print("Can't receive frame.")
            break

        barcode_data = extract_barcode(frame=frame)
        barcode_found = None
        if barcode_data != None:
            barcode_found = barcode_data
        
        cv2.imshow("Frame", frame)

        if barcode_found:
            break

        key = cv2.waitKey(1)
        if key == ord("q"):
            break    
    cap.release()
    cv2.destroyAllWindows()

    return barcode_found