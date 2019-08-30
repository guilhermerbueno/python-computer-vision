import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/LinuxLogo.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

#homogeneous filter
kernel = np.ones((5,5), np.float32)/25
dst = cv.filter2D(img,-1,kernel) # it's a LOW PASS FILTER that helps to remove noise
blur = cv.blur(img,(5,5))
gaussianBlur = cv.GaussianBlur(img, (5,5), 0)
medianBlur = cv.medianBlur(img, 5)
bilateralFilter = cv.bilateralFilter(img, 9, 75, 75)

titles = ['original','2d convolution','blurred', 'gaussian blur','median blur', 'bilateral filter']
images = [img, dst, blur, gaussianBlur, medianBlur, bilateralFilter]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()