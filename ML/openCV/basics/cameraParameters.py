import cv2

cap = cv2.VideoCapture(0)
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(w, h)

cap.set(3, 100)
cap.set(4, 100)

print(cap.get(3), cap.get(4))
while cap.isOpened():
    ret, frame = cap.read()
    if ret:

        gy = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("imShow", gy)

        if cv2.waitKey(1) == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()