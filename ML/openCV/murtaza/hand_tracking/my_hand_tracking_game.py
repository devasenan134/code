import cv2
import mediapipe as mp
import time
import hand_tracking_module as htm


cap = cv2.VideoCapture(0)
p_time = 0
c_time = 0
detector = htm.HandDetector()

while True:
    ret, frame = cap.read()
    frame = detector.find_hands(frame)
    lm_list = detector.find_position(frame, hand_no=2)

    if len(lm_list) != 0:
        print(lm_list[0])
    
    c_time = time.time()
    fps = 1/(c_time - p_time)
    p_time = c_time
    cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 2)

    cv2.imshow("Video", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
