import cv2 as cv
import mediapipe as mp
import time

class FaceMeshDetector():
    def __init__(self, static_image_mode=False, max_num_faces=2, refine_landmarks=False, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.static_image_mode = static_image_mode
        self.max_num_faces = max_num_faces
        self.refine_landmarks = refine_landmarks
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(static_image_mode=self.static_image_mode, max_num_faces=self.max_num_faces, refine_landmarks=self.refine_landmarks, 
                                            min_detection_confidence=self.min_detection_confidence, min_tracking_confidence=self.min_tracking_confidence)
        self.drawSpecs = self.mpDraw.DrawingSpec(thickness=1, circle_radius=2)
        
    def findFaceMesh(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        self.results = self.faceMesh.process(imgRGB)
        ih, iw, ic = img.shape

        faces = []
        
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, mp.solutions.face_mesh_connections.FACEMESH_TESSELATION, self.drawSpecs, self.drawSpecs)
                face = []        
                for id, lms in enumerate(faceLms.landmark):
                    x, y = int(lms.x*iw), int(lms.y*ih)
                    face.append([id, x, y])
                faces.append(face)
                
        return img, faces

def main():
    cap = cv.VideoCapture(0)
    pTime = 0
    
    detector = FaceMeshDetector()
    
    while True:
        _, img = cap.read()
        img, faces = detector.findFaceMesh(img)
        
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv.putText(img, str(int(fps)), (70, 40), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)    

        cv.imshow('Video', img)
        
        if cv.waitKey(1) == 27:
            break
        
    cv.destroyAllWindows()
    
if __name__ == "__main__":
    main()