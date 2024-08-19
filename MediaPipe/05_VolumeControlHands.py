from operator import length_hint
import cv2 as cv
import mediapipe as mp
import numpy as np
import time
import math
import HandTrackingModule as htm
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

##########################################
camWidth, camHeight = 640, 480 
##########################################

cap = cv.VideoCapture(0)
cap.set(3, camWidth)
cap.set(4, camHeight)
pTime = 0

detector = htm.HandDetector()

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol, maxVol = volRange[0], volRange[1]
print(volRange)

volBar = 400

while True:
    _, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    
    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2) // 2, (y1+y2) // 2

        cv.circle(img, (x1, y1), 15, (255, 0, 255), -1)
        cv.circle(img, (x2, y2), 15, (255, 0, 255), -1)

        cv.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv.circle(img, (cx, cy), 15, (255, 0, 255), -1)
        
        lineLength = math.hypot(x2-x1, y2-y1) 
        
        if lineLength < 50:
            cv.circle(img, (cx, cy), 15, (0, 255, 0), -1)
        
        cv.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
        cv.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv.FILLED)
        
        # Hand Range 50 to 300
        # Volume Range -65 to 0
        vol = np.interp(lineLength, [50, 300], [minVol, maxVol])
        volBar = np.interp(lineLength, [50, 300], [400, 150])
        volPer = np.interp(lineLength, [50, 300], [0, 100])
        volume.SetMasterVolumeLevel(vol, None)    
        
        cv.putText(img, f'{int(volPer)}', (40, 450), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2) 

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, f'FPS: {int(fps)}', (40, 50), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2) 

    cv.imshow("Cam", img)
    if cv.waitKey(1) == 27:
        break
    
cap.release()
cv.destroyAllWindows()