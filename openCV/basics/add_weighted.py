import cv2
import numpy as np


img = cv2.imread("../assets/banff dryer.jpg")
img2 = cv2.imread("../assets/branch nodes.jpg")

print(img.shape)
print(img.size)
print(img.dtype)
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

button = img[55:134, 692:765]

img = cv2.resize(img, (1024, 512))
img2 = cv2.resize(img2, (1024, 512))
res = cv2.addWeighted(img, 0.7, img2, 0.3, 0)

cv2.imshow("imgWin", res)
k = cv2.waitKey(0)
if k == ord("q"):
    cv2.destroyAllWindows()
