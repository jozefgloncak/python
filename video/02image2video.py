# https://www.tutorialspoint.com/opencv_python/opencv_python_video_images.htm
import cv2
import os
import datetime


DIR = "./screen_shot"
first = True
counter = 0
for file in os.listdir(DIR):
    counter += 1
    if (counter == 100):
        break
    print(file)
    file_path = os.path.join(DIR, file)
    img = cv2.imread(file_path)
    img = cv2.resize(img, (640, 480))
    if first:
        height, width, layers = img.shape
        size = (width,height)
        file_name = datetime.datetime.now().strftime("%Y-%m-%dT%H_%M_%S") + ".avi"
        out = cv2.VideoWriter(file_name, cv2.VideoWriter_fourcc(*'DIVX'), 30, size)
        first = False


    out.write(img)
out.release()
