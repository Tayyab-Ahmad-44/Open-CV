import cv2 as cv
import numpy as np

# 1- Edge Detection using Canny edge Detector
# 2- Mapping of Edge points to the Hough space and storage in an accumulator
# 3- Interpretation of the accumulator to yield lines of infinite length.
#    The interpretation is done by threshoulding and possibly other constraints.
# 4- Conversion of infinite lines to finite lines

 
img = cv.imread('data/sudoku.png')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,50,150,apertureSize = 3)
 
lines = cv.HoughLines(edges,1,np.pi/180,200)

for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
 
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
 
cv.imshow('Canny', edges)
cv.imshow('Image', img)

cv.waitKey(0)
cv.destroyAllWindows()