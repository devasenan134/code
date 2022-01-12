import cv2
import numpy as np


def click_event(event, x, y, flag, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = img[y, x]
        pt_color = np.zeros((240, 320, 3), dtype=np.uint8)
        pt_color[:] = b, g, r

        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        cv2.imshow("imgWin", img)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pt_color, "Selected Color", (5, 15), font, 0.5, (100, 100, 100), 1)
        cv2.imshow("colWin", pt_color)


img = cv2.imread("../assets/banff dryer.jpg", 1)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
cv2.imshow("imgWin", img)
cv2.setMouseCallback("imgWin", click_event)

k = cv2.waitKey(0)
if k == ord("q"):
    cv2.destroyAllWindows()
