import cv2
import numpy as np


def nothing(x):
    print(x)


cap = cv2.VideoCapture(0)

cv2.namedWindow("tracking")
cv2.createTrackbar("LH", "tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "tracking", 255, 255, nothing)
cv2.createTrackbar("US", "tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "tracking", 255, 255, nothing)

while True:
    # frame = cv2.imread("../assets/stone dicots.jpg")
    # frame = cv2.resize(img, (0, 0), fx=0.10, fy=0.10)
    _, frame = cap.read()
    print("Camera working: ", _)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "tracking")
    l_s = cv2.getTrackbarPos("LS", "tracking")
    l_v = cv2.getTrackbarPos("LV", "tracking")
    u_h = cv2.getTrackbarPos("UH", "tracking")
    u_s = cv2.getTrackbarPos("US", "tracking")
    u_v = cv2.getTrackbarPos("UV", "tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("image", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
