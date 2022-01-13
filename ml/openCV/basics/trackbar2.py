import cv2
import numpy as np


def nothing(x):
    print(x)


cv2.namedWindow("image")

cv2.createTrackbar("cp", "image", 10, 400, nothing)

switch = "color/gray"
cv2.createTrackbar(switch, "image", 0, 1, nothing)

while True:
    img = cv2.imread("assets/stone dicots.jpg")
    img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    cv2.imshow("image", img)

    pos = cv2.getTrackbarPos("cp", "image")
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(pos), (50, 150), font, 4, (0, 0, 255))

    s = cv2.getTrackbarPos(switch, "image")
    if s == 1:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    cv2.imshow("image", img)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()
