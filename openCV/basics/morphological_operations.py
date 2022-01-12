import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../assets/gems.png", 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

_, mask = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((2,2), np.uint8)

# 4 basic morphological operations
dilation = cv2.dilate(mask, kernal, iterations=1)
erosion = cv2.erode(mask, kernal, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)    # opening - first erosion then dilation is applied
closing = cv2.morphologyEx(mask, cv2.MORPH_CROSS, kernal)   # closing - first dilation then erosion is applied

# extra morph operations
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)     # difference between dilation and erosion
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)       # difference between src and opening


titles = ["img", "mask", "dilation", "erosion", "opening", "closing", "mg", "th"]
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()