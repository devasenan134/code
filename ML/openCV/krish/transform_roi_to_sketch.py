import cv2
import numpy as np


def sketch_transform(frame):
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_gray_blurred = cv2.GaussianBlur(img_gray, (7, 7), 0)
    img_canny = cv2.Canny(img_gray_blurred, 10, 80)
    _, mask = img_canny_inverted = cv2.threshold(img_canny, 30, 255, cv2.THRESH_BINARY_INV)
    return mask


cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    showCrosshair = False
    fromCenter = False
    r = cv2.selectROI("Image", frame, fromCenter, showCrosshair)
    break

while True:
    _, img_frame = cap.read()
    rect_img = img_frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    sketch_rect = rect_img
    sketch_rect = sketch_transform(sketch_rect)

    sketch_rect_rgb = cv2.cvtColor(sketch_rect, cv2.COLOR_GRAY2RGB)
    img_frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])] = sketch_rect_rgb

    cv2.imshow("sketch", img_frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
