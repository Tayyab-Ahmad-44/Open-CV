import numpy as np
import cv2

def mouseEvent(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 2, (255, 255, 255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[0], points[1], (0, 0, 255), 2)    
            points.clear()    

        
        cv2.imshow('image', img)
        
        
img = np.zeros((786, 786, 3), np.uint8)

points = []

cv2.imshow('image', img)
cv2.setMouseCallback('image', mouseEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()