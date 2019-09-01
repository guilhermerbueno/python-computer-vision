import numpy as n
import matplotlib
import tkinterp
import cv2

img = np.zeros([640, 480, 3], np.uint8) #cv2.imread('lena.jpg',1)

img = cv2.line(img, (0,0),(255,255), (0,0,255), 5)
img = cv2.arrowedLine(img, (0,255),(255,255),(255,0,0), 5)

img = cv2.rectangle(img, (380,0), (510,128), (0,255,0), -5)
img = cv2.circle(img, (305,255), 50, (0,0,0), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OpenCV', (10,500), font, 4, (255,255,255), 10, cv2.LINE_AA)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()