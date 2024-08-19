import cv2 as cv
import numpy as py

cap = cv.VideoCapture('data/test.mp4')
fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
# fgbg = cv.createBackgroundSubtractorKNN()

while cap.isOpened():
    _, frame = cap.read()
    
    blur = cv.blur(frame, (5, 5))

    fgmask = fgbg.apply(frame)

    cv.imshow("Frame", frame)
    cv.imshow("FG Mask", fgmask)
    if cv.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()