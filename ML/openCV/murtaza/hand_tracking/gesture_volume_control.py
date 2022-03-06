import cv2
import numpy as np
import time
import hand_tracking_module as htm
import math

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume



devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# volume.GetMute()
# volume.GetMasterVolumeLevel()
vol_range = volume.GetVolumeRange()
min_vol = vol_range[0]
max_vol = vol_range[1]

vol = volume.GetMasterVolumeLevel()
vol_bar = np.interp(vol, [-65, 0], [400, 150])
vol_per = np.interp(vol, [-65, 0], [0, 100])


#################################################
w_cam, h_cam = 640, 480
#################################################


cap = cv2.VideoCapture(0)
cap.set(3, w_cam)
cap.set(4, h_cam)
p_time = 0

detector = htm.HandDetector()

while cap.isOpened():
    ret, frame = cap.read()
    frame = detector.find_hands(frame)
    lm_list = detector.find_position(frame, ldm=[0, 4, 8])
    if len(lm_list) != 0:
        # print(lm_list[4], lm_list[8])
        x1, y1 = lm_list[4][1:]
        x2, y2 = lm_list[8][1:]
        cx, cy = (x1+x2)//2, (y1+y2)//2

        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(frame, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        
        length = math.hypot(x2-x1, y2-y1)
        
        # hand range 50 to 300
        # volume range -65 to 0
        
        vol = np.interp(length, [20, 200], [min_vol, max_vol])
        vol_bar = np.interp(length, [20, 200], [400, 150])
        vol_per = np.interp(length, [20, 200], [0, 100])
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(frame, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(frame, (50, 150), (85, 400), (0, 255, 0), 3)
    cv2.rectangle(frame, (50, int(vol_bar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(frame, f"Vol: {int(vol_per)}", (40, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    c_time = time.time()
    fps = 1/(c_time - p_time)
    p_time = c_time

    cv2.putText(frame, f"FPS: {int(fps)}", (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 150, 0), 3)
    # cv2.imshow("img", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()