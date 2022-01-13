import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("../assets/sudoku.png", 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

sobelCombined = cv2.bitwise_or(sobelx, sobely)

titles = ["img", "lap", "sobelx", "sobely", "sobelCombined"]
images = [img, lap, sobelx, sobely, sobelCombined]

for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
