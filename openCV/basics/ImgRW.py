import cv2

img = cv2.imread("openCV/assets/purpleGroup.jpg", 1)

img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# img = cv2.rotate(img, cv2.cv2.ROTATE_180)

cv2.imshow("ImgWindow", img)
k = cv2.waitKey(0)

if k == ord('q'):
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("../out.jpg", img)
    cv2.destroyAllWindows()
