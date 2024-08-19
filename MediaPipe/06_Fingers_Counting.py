import cv2 as cv
import HandTrackingModule as htm
import time
import os

cap = cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

folderPath = 'FingerImages'
myList = os.listdir(folderPath)
overlayList = []
for imgPath in myList:
    img = cv.imread(f'{folderPath}/{imgPath}')
    overlayList.append(img)

detector = htm.HandDetector()
pTime = 0 

tipIds = [4, 8, 12, 16, 20]

while cap.isOpened():
    _, img = cap.read()
    
    img = detector.findHands(img)
    lmList = detector.findPosition(img=img, draw=False)

    if len(lmList) != 0:
        fingers = []
        
        ## For Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
            fingers.append(1)
        
        ## For the rest of fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            
        openFingers = len(fingers)

        # To show image on screen
        h, w, c = overlayList[openFingers].shape
        img[0:h, 0:w] = overlayList[openFingers]
        

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, f'FPS: {int(fps)}', (500, 30), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2) 
    
    
    cv.imshow("Cam", img)
    if cv.waitKey(1) == 27:
        break
    
cap.release()
cv.destroyAllWindows()