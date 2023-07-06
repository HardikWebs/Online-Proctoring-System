import cv2
import numpy as np


img = cv2.imread('photos/Kurapika.png', -1)
img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([15,0,0])
upper_yellow = np.array([36,255,255])
lower_blue = np.array([90,50,50])
upper_blue = np.array([130,255,255])

mask1 = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask2 = cv2.inRange(hsv, lower_blue, upper_blue)
appliedMask = cv2.bitwise_or(mask1, mask2)

target = cv2.bitwise_and(img, img, mask = appliedMask)

while True:
    cv2.imshow('kurapika', target)
    cv2.imshow('mask1', mask1)
    cv2.imshow('mask2', mask2)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()