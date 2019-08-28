import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("images/smarties.png", cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

#kernel is basically a shape applied in image
kernel = np.ones((2,2), np.uint8)

dilation = cv.dilate(mask, kernel, iterations=2)
erosion = cv.erode(mask, kernel, iterations=1)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel) #it's the same that apply dilation and then erosion
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel) #it's the same that apply erosion and then dilation
morphGradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel)

titles = ['original', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'gradient', 'tophat']
images = [img, mask, dilation, erosion, opening, closing, morphGradient, tophat]

for i in range(8):
    plt.subplot(2,4,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()