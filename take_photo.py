import cv2
import os

def take_photo():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        ret, frame = cap.read()
        cv2.resize(frame, (640, 480))
        if not ret:
            print("Can't receive frame.")
            break

        cv2.imshow('frame', frame)

        wait_key = cv2.waitKey(1)
        if wait_key == 27: # aperte Esc pra fechar a câmera
            break
        elif wait_key == 32: # aperte Espaço para tirar a foto
            directory_path = r'scanner_barcode\web_scraping_economiza_AL\barcode_photos'
            qnt_files = len(os.listdir(directory_path))
            
            image_name = f'barcode_0{qnt_files + 1}.png'
            image_path = fr'scanner_barcode\web_scraping_economiza_AL\barcode_photos\{image_name}'
            cv2.imwrite(image_path, frame)
            break
    cap.release()
    cv2.destroyAllWindows()
    
    if wait_key == 32:
        return image_path 
    else:
        return None