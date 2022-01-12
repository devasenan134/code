#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from google.colab import drive
drive.mount('/content/drive')

# path = "/content/drive/MyDrive/ColabNotebooks/ML/opencv/"


# In[1]:


import cv2
import numpy as np
# from google.colab.patches import cv2_imshow


# In[12]:


img = cv2.imread("assets/familyPic.jpg")

cv2.imshow("win", img)
k = cv2.waitKey(0)
if k == ord('q'):
    cv2.destroyAllWindows()


# In[11]:


face_classifier = cv2.CascadeClassifier("haarcascades_data/haarcascades/haarcascade_frontalface_default.xml")

img = cv2.imread("assets/familyPic.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(gray, 1.3, 5)

if faces is None:
  print("No faces found")

for (x,y,w,h) in faces:
  cv2.rectangle(img, (x,y), (x+w, y+h), (127,0,255), 2)
cv2.imshow("win", img)
k = cv2.waitKey(0)
if k == ord('q'):
    cv2.destroyAllWindows()


# In[ ]:




