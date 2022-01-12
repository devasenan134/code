import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("assets/banff dryer.jpg", 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 200, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 200, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 200, 255, cv2.THRESH_TOZERO_INV)

titles = ["img", "th1", "th2", "th3", "th4", "th5"]
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
