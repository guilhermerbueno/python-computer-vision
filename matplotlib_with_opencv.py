import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('images/lena.jpg', -1)
#cv.imshow("image", img)

_,th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_,th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_,th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC) #freeze the pixel color after the threshold
_,th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) #less to threshold will be zero
_,th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = ['ORIGINAL', 'Binary', 'Binary inverse', 'Trunc', 'ToZero', 'ToZero inverse']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2,3, i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

#plt.imshow(img)
#plt.xticks([]), plt.yticks([])  #hide the axis
plt.show()

#cv.waitKey(0)
#cv.destroyAllWindows()