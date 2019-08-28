import numpy as np
import cv2

img = np.zeros([250,500,3], np.uint8)
img = cv2.rectangle(img, (250,0), (500,500), (255,255,255), -1)

#pic = cv2.imread('lena.jpg',0)
cv2.imshow('pic', img)
cv2.imwrite('image_1.png', img)

cv2.waitKey(0)
cv2.destroyAllWindows()