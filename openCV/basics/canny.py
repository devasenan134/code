import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("../assets/memoji.png", 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

"""
Canny Edge detector - steps:
1) Noise reduction
2) Gradient calculation
3) Non-maximum suppression
4) Double threshold
5) Edge tracking by Hysteresis
"""
cv2.namedWindow("canny")
cv2.createTrackbar("threshold1", "canny", 0, 255, lambda x: print(x))
cv2.createTrackbar("threshold2", "canny", 0, 255, lambda x: print(x))

while True:
    t1 = cv2.getTrackbarPos("threshold1", "canny")
    t2 = cv2.getTrackbarPos("threshold2", "canny")
    print(t1, t2)
    canny = cv2.Canny(img, t1, t2)
    cv2.imshow("canny", canny)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cv2.destroyAllWindows()








