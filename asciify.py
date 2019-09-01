import cv2 as cv
import numpy as np
import sys

def generateImage(asciify_image):
    output_img = np.array(
        [[[255, 255, 255] for m in range(len(asciify_image[0]) * 10)] for n in range(len(asciify_image) * 10)]).astype(np.uint8)
    font = cv.FONT_HERSHEY_SIMPLEX
    for j, line in enumerate(asciify_image):
        for i, symbol in enumerate(line):
            try:
                cv.putText(output_img, symbol, (i * 10, j * 10), font, 0.4, (0,0,0), 1)
            except:
                raise MemoryError("Input image is too large to convert. Try a smaller one, like 300 x 300 ...")
    return output_img

def reduceSize(result):
    gaussianPyramid = [result]
    for i in range(6):
        result = cv.pyrDown(result)
        gaussianPyramid.append(result)
    return gaussianPyramid

def convertToAscii(image, alphabet):
    alphabetSize = len(alphabet)
    h = image.shape[0]
    w = image.shape[1]
    size_ranges = 255 / alphabetSize
    asciify_image = np.zeros((h, w), dtype=str)

    for y in range(0, h):
        for x in range(0, w):
            asciify_image[y][x] = alphabet[int((image[y, x] - 1) / size_ranges)]

    return asciify_image

def showImages(images):
    for i in range(len(images)):
        cv.imshow("Image " + str(i), images[i])
        cv.imwrite("output/asciify"+str(i)+".jpg", images[i])

defaultAlphabet = "#@%=*:-. "
defaultImage = cv.imread("images/LinuxLogo.jpg", 0)

alphabet = defaultAlphabet
image = defaultImage
imageUrl = "images/LinuxLogo.jpg"

if len(sys.argv) >= 3:
    if sys.argv[1] != None:
        print(sys.argv[1])
        image = cv.imread(sys.argv[1],0)
    if sys.argv[2] != None:
        print(sys.argv[2])
        alphabet = sys.argv[2]

cv.imshow("original", image)

asciify_image = convertToAscii(image, alphabet)
result = generateImage(asciify_image)
smallSizes = reduceSize(result)
showImages(smallSizes)

cv.waitKey(0)
cv.destroyAllWindows()