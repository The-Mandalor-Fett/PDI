import cv2
import numpy as np


img = cv2.imread("./img/estrella.jpg",0)
kernel = np.ones((3,3),np.uint8)
#Erosión
imgErosion = cv2.erode(img,kernel,iterations = 1)
#Dilatación
dilatacion = cv2.dilate(img,kernel,iterations = 1)
