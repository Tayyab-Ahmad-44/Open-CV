import cv2 as cv

img = cv.imread('orange.jpg')
imgGrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, tresh = cv.threshold(imgGrey, 200, 255, cv.THRESH_BINARY_INV)

dilate = cv.dilate(tresh, (5, 5), iterations=20)

contours, _ = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
    cv.drawContours(img, [approx], 0, (0, 0, 0), 2)

    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 3:
        cv.putText(img, "Triangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
    
    elif len(approx) == 4:
        x1, y1, w, h = cv.boundingRect(approx)
        aspectRatio = float(w) / h
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv.putText(img, "Square", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
        else:
            cv.putText(img, "Rectangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)

    elif len(approx) == 5: 
        cv.putText(img, "Pentagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)

    elif len(approx) == 10: 
        cv.putText(img, "Star", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)

    else:
        cv.putText(img, "Circle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
        

cv.imshow('Grey Image', imgGrey)
cv.imshow('Treshold Image', tresh)
cv.imshow('Dilate Image', dilate)
cv.imshow('Image', img)

cv.waitKey(0)
cv.destroyAllWindows()