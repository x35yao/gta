import numpy as np
from PIL import ImageGrab
import cv2
import time

def process_img(original_img):
    processed_img = cv2.cvtColor(original_img,cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1 = 200, threshold2 = 300)
    return processed_img
last_time = time.time()
while(True):
    # window size 800*640
    screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    new_screen = process_img(screen)
    # printscreen_numpy =  np.array(printscreen_pil.getdata(),dtype='uint8') 
    print('loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    cv2.imshow('window', new_screen)
    # cv2.imshow('window2',cv2.cvtColor(np.array(screen),cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break