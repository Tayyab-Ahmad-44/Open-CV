from datetime import datetime
import cv2 as cv
import mediapipe as mp
import HandTrackingModule as htm

cap = cv.VideoCapture(0)
ptime = datetime.now()
ctime = datetime.now()

detector = htm.HandDetector()
while True:
    _, img = cap.read()
    
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img)
    
    ctime = datetime.now()
    fps = 1 / (ctime - ptime).total_seconds()
    ptime = ctime
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    cv.imshow('Image', img)
    if cv.waitKey(1) & 0xFF == 27:
        break
    
cv.destroyAllWindows()