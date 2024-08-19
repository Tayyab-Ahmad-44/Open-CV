from datetime import datetime
import cv2 as cv
import mediapipe as mp  


class HandDetector():
    def __init__(self, mode=False, maxHands=2, detectCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectCon = detectCon
        self.trackCon =  trackCon
        
        self.mpHands = mp.solutions.hands
        
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectCon,
            min_tracking_confidence=self.trackCon
        )
        
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        self.results = self.hands.process(imgRGB)
        
        if draw:
            if self.results.multi_hand_landmarks:
                for handLms in self.results.multi_hand_landmarks:                
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                    
        return img
    
    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 7, (255, 0, 0), -1)  

        return lmList



def main():
    cap = cv.VideoCapture(0)
    ptime = datetime.now()
    ctime = datetime.now()
    
    detector = HandDetector()

    while True:
        _, img = cap.read()
        
        img = detector.findHands(img, draw=True)
        lmList = detector.findPosition(img)
        
        ctime = datetime.now()
        fps = 1 / (ctime - ptime).total_seconds()
        ptime = ctime
        cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

        cv.imshow('Image', img)
        if cv.waitKey(1) & 0xFF == 27:
            break
        
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
    