import numpy as np
import cv2

# img = cv2.imread('assets/dry node.jpg')

img = np.zeros([1080, 1920, 3], np.uint8)


# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.arrowedLine(img, (0,255), (255, 255), (147, 0, 0), 5)
img = cv2.rectangle(img, (355, 255), (610, 510), (0, 255, 0), 10)
img = cv2.circle(img, (850, 450), 100, (0, 0, 255), -1)
font = cv2.FONT_HERSHEY_DUPLEX
img = cv2.putText(img, 'OpenCV', (10, 200), font, 4, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('imgWindow', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
