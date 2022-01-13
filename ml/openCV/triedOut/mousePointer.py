import cv2


cap = cv2.VideoCapture(0)


def click_event(event, x, y, flag, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(frame, (x,y), 30, (175,0,0), -1)
        cv2.imshow("win", frame)
        cv2.waitKey(100)


while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        cv2.imshow("win", frame)
        cv2.setMouseCallback('win', click_event)

        k = cv2.waitKey(1)
        if k == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
