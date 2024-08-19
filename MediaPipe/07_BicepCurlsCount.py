import cv2 as cv
import PoseDetectionModule as pdm
import time
import numpy as np

cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = pdm.PoseDetector()
dir = 0
count = 0

while True:
    _, img = cap.read() 
    
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    
    if len(lmList) != 0:
        angle = detector.findAngle(img, 12, 14, 16)
        # angle = detector.findAngle(img, 11, 13, 15)
        
        per = np.interp(angle, (40, 140), (0, 100))
        bar = np.interp(angle, (40, 140), (100, 650))
        
        if per == 100:
            if dir == 0:
                count += 0.5
                dir = 1
        
        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0    

        cv.rectangle(img, (1100, 100), (1175, 650), (0, 255, 0), 2)
        cv.rectangle(img, (1100, int(bar)), (1175, 650), (0, 255, 0), -1)                
        cv.putText(img, f'{abs(int(per)-100)}%', (1100, 75), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)    

        cv.rectangle(img, (0, 0), (200, 150), (0, 255, 0), -1)                
        cv.putText(img, f'{int(count)}', (75, 90), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)    
 
    cv.imshow('Video', img)
    if cv.waitKey(1) == 27:
        break
    
cap.release()   
cv.destroyAllWindows()
