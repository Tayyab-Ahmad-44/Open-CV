import cv2 as cv

cap = cv.VideoCapture('people_walking.mp4')

# First find the absolute difference between two frames.
# Convert the difference to grayscale mode coz its easy to find contour in gray scale mode later.
# Apply Gaussian Blur to that gray scale frame
# Apply threshold to that gray scale image
# Dilate the thresholded image to fill in the holes to find better contours.
# Find contours on that dilated image
# Draw contours on original image


_, frame1 = cap.read()
_, frame2 = cap.read()

while cap.isOpened():
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilate = cv.dilate(thresh, None, iterations=5)
    contours, _ = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour)

        if cv.contourArea(contour) >= 700:
            cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv.putText(frame1, "Status: {}".format('Movement'), (10, 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    
    cv.imshow('Moving', frame1)
    frame1 = frame2
    _, frame2 = cap.read()

    if cv.waitKey(30) == 27:
        break

cv.destroyAllWindows()
cap.release()