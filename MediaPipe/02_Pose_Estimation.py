import cv2 as cv
import mediapipe as mp
import time
import PoseDetectionModule as psm

cap = cv.VideoCapture(0)
pTime = 0

detector = psm.PoseDetector()
    
while True:
    _, img = cap.read()
    
    img = detector.findPose(img)
    lmList = detector.findPosition(img)
    
    print(lmList)
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    cv.putText(img, str(int(fps)), (70, 40), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
    cv.imshow('Video', img)
    if cv.waitKey(1) == 27:
        break
    
cap.release()
cv.destroyAllWindows()