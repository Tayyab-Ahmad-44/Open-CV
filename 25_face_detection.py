import cv2 as cv


face_cascade = cv.CascadeClassifier()
eye_cascade = cv.CascadeClassifier()
face_cascade.load('classifiers/haarcascade_frontalface_default.xml')
eye_cascade.load('classifiers/haarcascade_eye_tree_eyeglasses.xml')

cap = cv.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_img = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 3)

    cv.imshow('Picture', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()