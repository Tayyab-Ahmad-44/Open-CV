import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)
pTime = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(static_image_mode=False, max_num_faces=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
drawSpecs = mpDraw.DrawingSpec(thickness=1, circle_radius=2)

while True:
    _, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    results = faceMesh.process(imgRGB)
    ih, iw, ic = img.shape

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mp.solutions.face_mesh_connections.FACEMESH_TESSELATION, drawSpecs, drawSpecs)
            
            for id, lms in enumerate(faceLms.landmark):
                x, y = int(lms.x*iw), int(lms.y*ih)
                
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (70, 40), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)    

    cv.imshow('Video', img)
    if cv.waitKey(1) == 27:
        break
    
cv.destroyAllWindows()