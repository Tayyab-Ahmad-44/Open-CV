import cv2 as cv
import numpy as np

img = cv.imread('orange.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)

circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=40, maxRadius=0)

det_circles = np.uint16(np.around(circles))

for (x, y, r) in det_circles[0, :]:
    cv.circle(img, (x, y), r, (0, 0, 0), 2)
    cv.circle(img, (x, y), 2, (123, 156, 178), 4)

cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
