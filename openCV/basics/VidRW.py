import cv2
import numpy as np

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))            # identifier of width prop is 3
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))          # identifier of height prop is 4
print(width, height)

fourcc = cv2.VideoWriter_fourcc(*"XVID")        # same as ('X', '2', '6', '4')

# we could not use  h264 with mp4 format because by default opencv-python does not comes with it
# so we have to install openh264 in conda where that plugin is not available for windows

out = cv2.VideoWriter("output.avi", fourcc, 20, (width, height))

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        image = np.zeros(frame.shape, dtype=np.uint8)
        smallFrame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        h = height//2
        w = width//2
        # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        image[:h, :w] = smallFrame
        image[h:, :w] = smallFrame
        image[:h, w:] = smallFrame
        image[h:, w:] = smallFrame

        cv2.imshow("videoFrame", image)
        out.write(image)

        # print(cap.get(cv2.CAP_PROP_FPS))          # there are more other properties
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
