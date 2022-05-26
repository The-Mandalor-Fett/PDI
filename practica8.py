import cv2
import numpy as np

img = cv2.imread('A.png',0)
kernel = np.ones((3,3),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)