import cv2
import numpy as np


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        img[y:y+79, x:x+73] = button
        cv2.imshow("imgWin", img)


img = cv2.imread("../assets/banff dryer.jpg", 1)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

print(img.shape)
print(img.size)
print(img.dtype)
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

button = img[55:134, 692:765]

cv2.imshow("imgWin", img)
cv2.setMouseCallback("imgWin", click_event)
k = cv2.waitKey(0)
if k == ord("q"):
    cv2.destroyAllWindows()
