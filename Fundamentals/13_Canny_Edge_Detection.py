import cv2 as cv
import matplotlib.pyplot as plt

def whatever(x):
    pass

img = cv.imread('messi.jpg')
# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.namedWindow('canny')

cv.createTrackbar('t1', 'canny', 0, 400, whatever)
cv.createTrackbar('t2', 'canny', 0, 400, whatever)

while(1):    
    t1 = cv.getTrackbarPos('t1', 'canny')
    t2 = cv.getTrackbarPos('t2', 'canny')
    
    canny = cv.Canny(img, t1, t2, apertureSize=3)

    cv.imshow('image', img)
    cv.imshow('canny', canny)
    
    k = cv.waitKey(1) & 0xFF
    
    if k == 27:
        break

cv.destroyAllWindows()



# titles = ['image', 'canny']
# images = [img, canny]

# for i in range(len(images)):
#     plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])

# plt.show()