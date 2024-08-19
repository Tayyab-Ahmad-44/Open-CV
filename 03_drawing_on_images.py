import cv2

img = cv2.imread('tyb.jpg', 1)

img = cv2.line(img, (0, 0), (233, 233), (255, 0, 0), 8)
img = cv2.arrowedLine(img, (233, 0), (233, 233), (0, 0, 255), 8)
img = cv2.rectangle(img, (25, 25), (290, 60), (0, 255, 0), 8)
img = cv2.circle(img, (300, 300), 30, (0, 0, 0), 8)

cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()