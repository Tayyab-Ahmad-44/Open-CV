import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def clickEvent(event, x, y, flags, param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        print(x, ' , ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ' , ' + str(y)
        cv2.putText(img, strXY, (x, y), font, 1, (255, 255, 0), 1)
        cv2.imshow('image', img)
        
    if event == cv2.EVENT_FLAG_RBUTTON:
        font = cv2.FONT_HERSHEY_SIMPLEX
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 1, (255, 255, 0), 1)
        cv2.imshow('image', img)

# img = np.zeros((786, 1024, 3), np.uint8)
img = cv2.imread('messi.jpg')


cv2.imshow('image', img)
cv2.setMouseCallback('image', clickEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()
