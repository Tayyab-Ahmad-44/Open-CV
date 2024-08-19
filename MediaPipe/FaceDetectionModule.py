import cv2 as cv
import mediapipe as mp
import time
    
class FaceDetector():
    def __init__(self, minDetectCon=0.5):
        self.detectCon = minDetectCon
        self.mpFaceDetetction = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetetction.FaceDetection(self.detectCon)

    def findFaces(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        bboxs = []
        
        
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                ih, iw, c = img.shape
                bboxC = detection.location_data.relative_bounding_box
                bbox =  int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                
                bboxs.append([id, bbox, detection.score[0]])
                if draw:    
                    img = self.fancyDraw(img, bbox)
                    cv.putText(img, str(detection.score[0] * 100), (bbox[0], bbox[1] - 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
        
        return img, bboxs
    
    def fancyDraw(self, img, bbox, l=30, t=5, rt=1):
        x, y, w, h = bbox
        x1, y1 = x+w, y+h
        
        cv.rectangle(img, (bbox[0], bbox[1]), (bbox[0]+bbox[2], bbox[1]+bbox[3]), (255, 0, 255), rt)

        # Top Left
        cv.line(img, (x, y), (x+l, y), (255, 0, 255), t)
        cv.line(img, (x, y), (x, y+l), (255, 0, 255), t)
        # Top Right
        cv.line(img, (x+w-l, y), (x+w, y), (255, 0, 255), t)
        cv.line(img, (x+w, y), (x+w, y+l), (255, 0, 255), t)
        # Bottom Left
        cv.line(img, (x, y+h-l), (x, y+h), (255, 0, 255), t)
        cv.line(img, (x, y+h), (x+l, y+h), (255, 0, 255), t)
        # Bottom Right
        cv.line(img, (x+w-l, y+h), (x+w, y+h), (255, 0, 255), t)
        cv.line(img, (x+w, y+h-l), (x+w, y+h), (255, 0, 255), t)

        return img


def main():
    cap = cv.VideoCapture(0)
    pTime = 0

    detector = FaceDetector()
    while True:
        _, img = cap.read()
        img, bboxs = detector.findFaces(img)
        
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv.putText(img, str(int(fps)), (70, 40), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)

        cv.imshow('Video', img)
        if cv.waitKey(1) == 27:
            break

    cap.release()
    cv.destroyAllWindows()
    

if __name__ == "__main__":
    main()