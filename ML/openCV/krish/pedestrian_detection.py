import cv2
import numpy as np

body_classifier = cv2.CascadeClassifier("haarcascades_data/haarcascades/haarcascade_fullbody.xml")

cap = cv2.VideoCapture("krish\krish_data\walking.avi")

while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodies = body_classifier.detectMultiScale(gray, 1.3, 3)

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow("video", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
