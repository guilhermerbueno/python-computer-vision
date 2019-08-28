#the steps of canny edge detection are:
#1. noise detection
#2. gradient calculation
#3. nom maximum suppression
#4. double treshold
#5. edge tracking by histeresis
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/messi5.jpg', 0)
canny = cv.Canny(img, 100, 200)

titles = ['original', 'canny']
images = [img, canny]

for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()