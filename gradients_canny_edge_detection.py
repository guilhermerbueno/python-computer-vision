import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/sudoku.png', cv.IMREAD_GRAYSCALE)

#HIGH PASS FILTER is used to find edges in the image
laplacian = cv.Laplacian(img, cv.CV_64F, ksize=3)
laplacian = np.uint8(np.absolute(laplacian))

sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelCombine = cv.bitwise_or(sobelX, sobelY)

edges = cv.Canny(img, 100, 200)

titles = ['original','laplacian', 'sobel X', 'sobael Y', 'sobel combine','canny']
images = [img, laplacian, sobelX, sobelY, sobelCombine, edges]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()