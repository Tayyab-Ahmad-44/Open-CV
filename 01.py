import cv2

img = cv2.imread('tyb.jpg')

cv2.imshow('image', img)

key = cv2.waitKey(20000)

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('tyb_copy.jpg', img)
    cv2.destroyAllWindows()
