import cv2 as cv
import numpy as np

img = cv.imread('data/chessboard4.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, 100, 0.01, 10)

corners = np.intp(corners)

for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x, y), 1, (255, 0, 0), 2)

cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
