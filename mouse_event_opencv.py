import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in i] #captura todos os eventos da biblioteca cv2
#print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
#        print(x, ',', y)
#        font = cv2.FONT_HERSHEY_SIMPLEX
#        strXY = str(x) + ', ' + str(y)
#        cv2.putText(img, strXY, (x,y), font, .5, (255,255,0), 2)
#        cv2.circle(img, (x,y), 3, (0,0,255), -1, cv2.LINE_AA)
#        points.append((x,y))
#        if len(points) >= 2:
#            cv2.line(img, points[-1], points[-2], (255,0,0), 5, cv2.LINE_AA)
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img, (x,y), 3, (0,0,255, 1))
        mycolorImage = np.zeros((512,512,3), np.uint8)
        mycolorImage[:] = [blue,green,red]
#        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.imshow('color',mycolorImage)

#    if event == cv2.EVENT_RBUTTONDOWN:
#        blue = img[y,x,0]
#        green = img[y,x,1]
#        red = img[y,x,2]
#        font = cv2.FONT_HERSHEY_SIMPLEX
#        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
#        cv2.putText(img, strBGR, (x,y), font, .5, (0,255,255), 2)
#        cv2.imshow('image', img)

#img = np.zeros([512,512,3], np.uint8)
img = cv2.imread('images/lena.jpg')
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()