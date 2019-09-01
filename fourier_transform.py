import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('images/lena.jpg',0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrumDFT = 20*np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
magnitude_spectrum = 20*np.log(np.abs(fshift))

#rows, cols = img.shape
#crow,ccol = rows/2 , cols/2
#fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
#f_ishift = np.fft.ifftshift(fshift)
#img_back = np.fft.ifft2(f_ishift)
#img_back = np.abs(img_back)

images = [img,magnitude_spectrum, magnitude_spectrumDFT]
titles = ['original', 'spectrum', 'dft']

for i in range(3):
    plt.subplot(1,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()