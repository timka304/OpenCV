# INVISIBILIY CLOAK 
import cv2
import numpy as np
import os
import time

original_video = cv2.VideoCapture("video.mp4")
time.sleep(3)
count = 0
background = 0

for i in range(60):
    return_val, background = original_video.read()
    if not return_val:
        print("Failed to capture background")
        continue

background = np.flip(background, axis=0)

#Video Processing frame by frame
while (original_video.isOpened()):
    return_val, img = original_video.read()
    if not return_val:
        print("Failed to read video frame")
        break
    count+=1
    img = np.flip(img, axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask = mask1 + mask2
    
    # Refining the Images
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations=1)
    mask2 = cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(background, background, mask = mask1)
    res2 = cv2.bitwise_and(img, img, mask = mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Invisible Cloak", final_output)
    key = cv2.waitKey(10)
    if key == 27:
        print("Exiting video processing")
        break