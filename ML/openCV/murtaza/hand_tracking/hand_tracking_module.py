import cv2
import mediapipe as mp
import time


class HandDetector():
    def __init__(self, mode=False, max_hands=2, detection_confidence=1, track_confidence=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_confidence = detection_confidence
        self.track_confidence = track_confidence
        
        self.mp_hands = mp.solutions.hands
        self.hands =self.mp_hands.Hands(self.mode, self.max_hands, self.detection_confidence, self.track_confidence)
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, frame, draw=True):
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(frame, hand_lms, self.mp_hands.HAND_CONNECTIONS)
        return frame

    def find_position(self, frame, hand_no=1, ldm=[], draw=True):
        lm_list = {}
        
        if self.results.multi_hand_landmarks:
            for hand_id, hand_lms in enumerate(self.results.multi_hand_landmarks[:hand_no]):
                # my_hand = self.results.multi_hand_landmarks[hand_no]
                lms = []
                for id, lm in enumerate(hand_lms.landmark):
                    h, w = frame.shape[:-1]
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    lms.append([id, cx, cy])
                    if draw:
                        if ldm == []:
                            cv2.circle(frame, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
                        else:
                            if id in ldm:
                                cv2.circle(frame, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
                lm_list[hand_id] = lms
        return lm_list



def main():
    
    cap = cv2.VideoCapture(0)
    p_time = 0
    c_time = 0

    detector = HandDetector()
    while True:
        ret, frame = cap.read()
        frame = detector.find_hands(frame)
        
        lm_list = detector.find_position(frame, draw=True)
        
        if len(lm_list) != 0:
            print(lm_list)
        
        c_time = time.time()
        fps = 1/(c_time - p_time)
        p_time = c_time

        cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 2)

        cv2.imshow("Video", frame)
        if cv2.waitKey(1) == ord("q"):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()