import cv2
import numpy as np

def click_event(event, x, y, flag, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (255, 0, 0), -1)
        pts.append((x, y))
        if len(pts) >= 2:
            cv2.arrowedLine(img, pts[-2], pts[-1], (255, 0, 0), 3)
        cv2.imshow("imgWin", img)


img = np.zeros([480, 640, 3], dtype=np.uint8)
cv2.imshow("imgWin", img)
pts = []
cv2.setMouseCallback("imgWin", click_event)

k = cv2.waitKey(0)
if k == ord("q"):
    cv2.destroyAllWindows()
