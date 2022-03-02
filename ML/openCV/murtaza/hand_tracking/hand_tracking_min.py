import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    ret, frame = cap.read()



    cv2.imshow("Video", frame)
    cv2.waitKey(1)