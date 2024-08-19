import cv2 as cv
import numpy as np
import HandTrackingModule as htm
import os

folderPath = 'PaintImages'
myList = os.listdir(folderPath)
overlayList = []
for imgPath in myList:
    img = cv.imread(f'{folderPath}/{imgPath}')
    overlayList.append(img)

cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.HandDetector(maxHands=1)

header = overlayList[0]
thumbTip = 4
indexTip = 8
color = (255, 77, 255)
xp = yp = 0
thickness = 3

imgCanvas = overlayList[5]
blackImg = np.zeros((720, 1280, 3), np.uint8)

while True:
    ## Import Image
    _, img = cap.read()
    img = cv.flip(img, 1)
    
    ## Find Landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, 0, False)
        
    ## Check which fingers are up
    if len(lmList) != 0:
        _, x1, y1 = lmList[indexTip]
        _, x2, y2 = lmList[thumbTip]

        ## If Selection-Mode -> Two fingers are up 
        if y1 < lmList[indexTip - 2][2] and x2 < lmList[thumbTip - 1][1]:
            xp = yp = 0
            cv.rectangle(img, (x1-10, y1-10), (x1+10, y1+10), color, -1)
            if y1 < 113:
                if x1 > 300 and x1 < 400:
                    header = overlayList[0]
                    color = (255, 77, 255)
                elif x1 > 490 and x1 < 577:
                    header = overlayList[1]
                    color = (255, 42, 0)
                if x1 > 680 and x1 < 760:
                    header = overlayList[2]
                    color = (51, 255, 51)
                if x1 > 860 and x1 < 950:
                    header = overlayList[3]
                    color = (0, 255, 255)
                if x1 > 1065 and x1 < 1160:
                    header = overlayList[4]
                    color = (255, 255, 255)
                            
        ## If Drawing-Mode -> Index Finger is up
        elif lmList[indexTip][2] < lmList[indexTip - 2][2]:
            if xp == yp == 0:
                xp, yp = x1, y1
                    
            if color == (255, 255, 255):
                cv.line(img, (xp, yp), (x1, y1), color, 50)
                cv.line(imgCanvas, (xp, yp), (x1, y1), color, 50)
                cv.line(blackImg, (xp, yp), (x1, y1), (0, 0, 0), 50)
                cv.circle(img, (x1, y1), 20, color, -1)
            else:
                cv.line(img, (xp, yp), (x1, y1), color, thickness)
                cv.line(imgCanvas, (xp, yp), (x1, y1), color, thickness)
                cv.line(blackImg, (xp, yp), (x1, y1), color, thickness)
                cv.circle(img, (x1, y1), 7, color, -1)
                
            xp, yp = x1, y1      
            
    ## Drawing on Original Image
    imgGray = cv.cvtColor(blackImg, cv.COLOR_BGR2GRAY)     
    _, thresholdImg = cv.threshold(imgGray, 50, 255, cv.THRESH_BINARY_INV)
    thresholdImg = cv.cvtColor(thresholdImg, cv.COLOR_GRAY2BGR)
    img = cv.bitwise_and(img, thresholdImg) 
    img = cv.bitwise_or(img, blackImg)
                        
    img[0:113,0:1280] = header
    
    cv.imshow("WebCam", img)
    cv.imshow("Drawing Board", imgCanvas)
    if cv.waitKey(1) == 27:
        break

cv.imwrite('saved/paint.png', imgCanvas)   
cap.release()
cv.destroyAllWindows()