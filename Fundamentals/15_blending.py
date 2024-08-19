import cv2 as cv
import numpy as np

apple = cv.imread('apple.jpg')
orange = cv.imread('orange.jpg')
a_o = np.hstack((apple[:, :256], orange[:, 256:]))

# 1- Load Images
# 2- Find Gausian Pyramids for apple and orange
# 3- From Gausian Pyramids, find laplacian pyramids
# 4- Now join left half of apple and right half of orange in each level of laplacian pyramids.
# 5- Finally from this joint image pyramids, reconstruct the original image.

# Gausian Pyramids for apple
apple_layer = apple.copy()
gp_apple = [apple_layer]

for i in range(6):
    apple_layer = cv.pyrDown(apple_layer)
    gp_apple.append(apple_layer)


# Gausian Pyramids for Orange
orange_layer = orange.copy()
gp_orange = [orange_layer]

for i in range(6):
    orange_layer = cv.pyrDown(orange_layer)
    gp_orange.append(orange_layer)


# laplacian pyramid for Apple
apple_layer = gp_apple[5]
lp_apple = [apple_layer]

for i in range(5, 0, -1):
    gaussian_extended = cv.pyrUp(gp_apple[i])
    laplacian = cv.subtract(gp_apple[i-1], gaussian_extended)
    lp_apple.append(laplacian)

    
# laplacian pyramid for Orange
orange_layer = gp_orange[5]
lp_orange = [orange_layer]

for i in range(5, 0, -1):
    gaussian_extended = cv.pyrUp(gp_orange[i])
    laplacian = cv.subtract(gp_orange[i-1], gaussian_extended)
    lp_orange.append(laplacian)


# Join left half of apple and right half of orange in each level
a_o_pyramid = []

for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    cols, rows , ch = apple_lap.shape    
    laplacian = np.hstack((apple_lap[:, :int(cols/2)], orange_lap[:, int(cols/2):]))
    a_o_pyramid.append(laplacian)

# Now Reconstruct 
a_o_reconstruct = a_o_pyramid[0]

for i in range(1, 6):
    a_o_reconstruct = cv.pyrUp(a_o_reconstruct)
    a_o_reconstruct = cv.add(a_o_pyramid[i], a_o_reconstruct)
    
    
cv.imshow('Apple_Orange', a_o)
cv.imshow('Apple_Orange_Reconstruct', a_o_reconstruct)

cv.waitKey(0)
cv.destroyAllWindows()
