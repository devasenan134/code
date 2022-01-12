import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../assets/memoji.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


"""
Smoothing and blurring is one of the most important preprocessing steps in all of computer vision and image processing. 
By smoothing an image prior to applying techniques such as edge detection or thresholding we are able to reduce the 
amount of high-frequency content, such as noise and edges (i.e., the “detail” of an image).

LPF(low pass filters) - helps in removing noises (reduces high frequency componenets)
HPF(high pass filters) - helps in finding edges in the images (reduces low frequency componenets)
"""

kernel = np.ones((5, 5), np.float32)/25

dst = cv2.filter2D(img, -1, kernel)                 # (LPF)Homogeneous blur - simplest filter, all pixel has equal weight
blur = cv2.blur(img, (5, 5))                        # Simple average blur
gauss = cv2.GaussianBlur(img, (5, 5), 0)            # (LPF)Gaussian blur
median = cv2.medianBlur(img, 5)                     # (ksize must be odd except 1)  # Median blur - great when dealing with salt and pepper noise
bilateral = cv2.bilateralFilter(img, 9, 75, 75)     # Bilateral blur - removes noise while keeping the edges sharp


titles = ["img", "2D Convolution", "Blur", "Gauss", "Median", "Bilateral"]
images = [img, dst, blur, gauss, median, bilateral]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()