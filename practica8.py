import cv2
import numpy as np


img = cv2.imread("./img/estrella.jpg",0)
kernel = np.ones((3,3),np.uint8)
#Erosión
imgErosion = cv2.erode(img,kernel,iterations = 1)
#Dilatación
imgDilatacion = cv2.dilate(img,kernel,iterations = 1)

img2= cv2.imread("./img/figura-2.jpg")
#Apertura
imgApertura = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)
#Cierre
imgCierre = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Imagen Erosión",imgErosion)
cv2.imshow("Imagen Dilatación",imgDilatacion)
cv2.imshow("Imagen Apertura",imgApertura)
cv2.imshow("Imagen Cierre",imgCierre)
cv2.waitKey(0)
cv2.destroyAllWindows()