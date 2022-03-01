import cv2
import numpy as np

car_classifier = cv2.CascadeClassifier("haarcascades_data/haarcascades/haarcascade_car.xml")

cap = cv2.VideoCapture("krish\krish_data\image_examples_cars.avi")

while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_classifier.detectMultiScale(gray, 1.3, 2)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow("video", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
