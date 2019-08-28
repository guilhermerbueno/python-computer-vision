import cv2 as cv

img = cv.imread('images/gradient.png', 0)
_,th1 = cv.threshold(img, 127,255, cv.THRESH_BINARY)
_,th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
_,th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC) #freeze the pixel color after the threshold
_,th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) #less to threshold will be zero
_,th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV) #if the value of the pixel is greater than threshold it will be zero

cv.imshow("Threshold Trunc", th3)
cv.imshow("Threshold2", th2)
cv.imshow("Threshold", th1)
cv.imshow("Image",img)
cv.imshow("th4", th4)
cv.imshow("th5", th5)

cv.waitKey(0)
cv.destroyAllWindows()