import  numpy as np
import cv2 as cv

img = cv.imread("images/opencv-logo.png")
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print("number of contours = " + str(len(contours)))

cv.drawContours(img, contours, -1, (0,255,0), 3)

cv.imshow('Original ', img)
cv.imshow("Image gray", imgray)
cv.waitKey(0)
cv.destroyAllWindows()