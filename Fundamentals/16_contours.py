import cv2 as cv

img = cv.imread('smarties.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(gray, 100, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

print("Number of Contours: " + str(len(contours)))

cv.drawContours(img, contours, -1, (0, 233, 0), 4)

cv.imshow('Threshold', thresh)
cv.imshow('Contoured', img)

cv.waitKey(0)
cv.destroyAllWindows()