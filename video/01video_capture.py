# import numpy as np
import cv2
import time
import os

cap = cv2.VideoCapture("https://stream.profi-net.sk/donovaly/KASA_ZAHRADISTE.stream/chunklist_w462562441.m3u8")

count = 0
dir = os.path.join("screen_shot")
while(True):

    cap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
    ret, image = cap.read()
    print("read next frame", count)
    if ret:
        image = cv2.resize(image, (1024, 768))

        # Our operations on the frame come here
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        file_name = str(count).zfill(4) + ".jpeg"
        cv2.imwrite(os.path.join(dir, file_name), image)

    count += 1




# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()