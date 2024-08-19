import cv2 as cv
import numpy as np

img = cv.imread('messi.jpg')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
template = cv.imread('messi_face.png', 0)

w, h = template.shape[::-1]

res = cv.matchTemplate(imgGray, template, cv.TM_CCORR_NORMED)

threshold = 0.927

loc = np.where(res > threshold)

print(loc)
# whatever = res.ravel()
# print(max(whatever))

for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 255, 0), 1)

cv.imshow('Image', img)
cv.imshow('Imag', template)
cv.waitKey(0)
cv.destroyAllWindows()


