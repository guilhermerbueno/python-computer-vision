import cv2 as cv
import numpy as np

img = cv.imread("images/lena.jpg")

def gaussianPyramid(showImages):
    layer = img.copy()
    gp = [layer]

    for i in range(6):
        layer = cv.pyrDown(layer)
        gp.append(layer)
        if showImages == True:
            cv.imshow(str(i), layer)

    return gp

def pyrDownsUps():
    lr = cv.pyrDown(img) #low resolution
    lr1 = cv.pyrDown(lr)
    hr2 = cv.pyrUp(img)
    cv.imshow("Low resolution", lr)
    cv.imshow("pyr down 2 image", lr1)
    cv.imshow("pyr up 1", hr2)

def laplacianPyramid(gp):
    layer = gp[5]
    lp = [layer]

    for i in range(5, 0, -1):
        gaussian_extended = cv.pyrUp(gp[i])
        laplacian = cv.subtract(gp[i-1],gaussian_extended)
        cv.imshow(str(i), laplacian)

gp = gaussianPyramid(False)
laplacianPyramid(gp)

cv.imshow("Original image", img)
cv.waitKey(0)
cv.destroyAllWindows()