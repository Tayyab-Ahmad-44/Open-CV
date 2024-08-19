import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('lena.jpg', 0)

# b, g, r = cv.split(img)

cv.imshow('Image', img)
# cv.imshow('B', b)
# cv.imshow('G', g)
# cv.imshow('R', r)

hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)

# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()