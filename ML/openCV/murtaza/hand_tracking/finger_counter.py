import cv2
import mediapipe as mp
import time
import os
import hand_tracking_module as htm



#################################################
w_cam, h_cam = 640, 480
#################################################

cap = cv2.VideoCapture(0)
cap.set(3, w_cam)
cap.set(4, h_cam)
p_time = 0




folder_path = "finger_imgs"
os.chdir("murtaza\hand_tracking")
my_list = os.listdir(folder_path)

overlay_list = []

for im_path in my_list:
    finger_img = cv2.imread(f"{folder_path}/{im_path}")
    # print(f"{folder_path}/{im_path}")
    overlay_list.append(cv2.resize(finger_img, (150, 150)))



detector = htm.HandDetector()

tip_id = [4, 8, 12, 16, 20]

while True:
    ret, frame = cap.read()

    frame = detector.find_hands(frame)
    lm_list = detector.find_position(frame, hand_no=2, draw=False)
    

    if len(lm_list) != 0:
        # print(lm_list)
        fingers = []
        for hand_no in lm_list:
            hand = lm_list[hand_no]

            # check if right or left hand
            if hand[tip_id[0]][1] > hand[tip_id[-1]][1]: 
                # for right thumb 
                if hand[tip_id[0]][1] > hand[tip_id[0]-1][1]:
                    print("right thumb is open")
                    fingers.append(1)
                else:
                    print("right thumb is close")
                    fingers.append(0)
            else:
                # for left thumb 
                if hand[tip_id[0]][1] < hand[tip_id[0]-1][1]:
                    print("left thumb is open")
                    fingers.append(1)
                else:
                    print("left thumb is close")
                    fingers.append(0)

            # for other fingers
            for id in range(1, 5):
                if hand[tip_id[id]][2] < hand[tip_id[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

        count = sum(fingers)
        cv2.putText(frame, f"{count}", (500, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        # y, x = overlay_list[count].shape[:2]
        # frame[0:y, 0:x] = overlay_list[count]


    c_time = time.time()
    fps = 1/(c_time - p_time)
    p_time = c_time
    cv2.putText(frame, f"FPS: {int(fps)}", (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Video", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
