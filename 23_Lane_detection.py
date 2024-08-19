import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Mask the whole area with balack color which is'nt needed
def masking(img, vertices):
    mask = np.zeros_like(img)
    # no_chnls = img.shape[0]
    # match_mask_color = (255,) * no_chnls # It is like a rgb(255, 255, 255) white color and will be used to fill region with white color
    match_mask_color = 255
    cv.fillPoly(mask, vertices, match_mask_color) # It will fill the interested region with white color for and operation
    masked_image = cv.bitwise_and(img, mask) # If something is and with 0 that will become 0 automatically and viceversa

    return masked_image

# Function to draw lines on image
def draw_lines(img, lines):
    img = np.copy(img)
    blank_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv.line(blank_img, (x1, y1), (x2, y2), (0, 255, 0), 5)
                    
    img = cv.addWeighted(img, 0.8, blank_img, 1, 0.0)
    
    return img
    
def process_image(img):  
    # print(img.shape)  
    height = img.shape[0] 
    width = img.shape[1]

    reg_of_int = [
        (0, height),
        (width/2, height/2),
        (width, height)
    ]

    # Detect the lines using Canny Edge Detector
    gray_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    blur = cv.GaussianBlur(gray_img, (5, 5), 0)
    canny = cv.Canny(gray_img, 100, 200)

    # Mask it
    masked_img = masking(canny, np.array([reg_of_int], np.int32))

    # Apply Hough Line Probibilistic Transform
    lines = cv.HoughLinesP(masked_img, rho=6, theta=np.pi/60, threshold=160, lines=np.array([]), minLineLength=20, maxLineGap=25)

    # Image with Lines
    img_wth_lines = draw_lines(img, lines)

    return img_wth_lines

cap = cv.VideoCapture('data/lane_video.mp4')

# _ , img = cap.read()
# img = process_image(img)

# plt.imshow(img)
# plt.show()

while cap.isOpened():
    _ , frame = cap.read()
    
    frame = process_image(frame)
    
    cv.imshow('Lane Detection', frame)
    if cv.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()