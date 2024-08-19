import numpy as np
import cv2

img1 = cv2.imread('image_1.png')
img2 = np.zeros((250, 500, 3), np.uint8)

img2 = cv2.rectangle(img2, (200, 0), (300, 100), (255, 255, 255), -1)

bitAnd = cv2.bitwise_and(img1, img2)
# bitOr = cv2.bitwise_or(img1, img2)
bitXor = cv2.bitwise_xor(img1, img2)

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('BitWise Operation', bitXor)


cv2.waitKey(0)
cv2.destroyAllWindows()