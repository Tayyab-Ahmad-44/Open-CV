import numpy as np
import cv2 as cv

def whatever(x):
    print(x)
    
cv.namedWindow('image')

cv.createTrackbar('CP', 'image', 10, 400, whatever)

switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, whatever)


while(1):
    img = cv.imread('messi.jpg')
    pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_COMPLEX
    cv.putText(img, str(pos), (50, 150), font, 4, (0, 0, 255), 2)

    k = cv.waitKey(1) & 0xFF
    
    if k == 27:
        break
    
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)            

    img = cv.imshow('image',img)
    
cv.destroyAllWindows()
