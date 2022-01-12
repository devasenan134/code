import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20, (640, 480))

i = 0
j = 10
while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        frame = cv2.circle(frame, (i, 20), 10, (0, 255, 0), -1)
        cv2.imshow("imgWin", frame)
        out.write(frame)
        if i < 640:
            i += 5
            j += 5
        else:
            i -= 5
            j -= 5
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

