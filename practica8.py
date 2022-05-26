import cv2
import numpy as np
import random


img = cv2.imread("./img/engranes.png",0)
kernel = np.ones((9,9),np.uint8)
kernel2 = np.ones((7,7),np.uint8)
kernel3 = np.ones((5,5),np.uint8)
kernel4 = np.ones((3,3),np.uint8)

#Erosión
imgErosion = cv2.erode(img,kernel,iterations = 1)
#Dilatación
imgDilatacion = cv2.dilate(img,kernel,iterations = 1)

img2= cv2.imread("./img/formas.jpg",0)
def ruido(img2,probabilidad):
    imgSalida=np.zeros(img2.shape,np.uint8)
    umbral = 1-probabilidad
    for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            aleatorio = random.random()
            if aleatorio < probabilidad:
                imgSalida[i][j] = 0
            elif aleatorio > umbral:
                imgSalida[i][j] = 255
            else :
                imgSalida[i][j] = img2[i][j] 
    return imgSalida

imgRuidosa =ruido(img2, 0.02)
imgApertura = cv2.morphologyEx(imgRuidosa, cv2.MORPH_OPEN, kernel)
#Cierre
imgCierre = cv2.morphologyEx(imgApertura, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Imagen Erosión",imgErosion)
cv2.imshow("Imagen Dilatación",imgDilatacion)
cv2.imshow("Imagen Apertura",imgApertura)
cv2.imshow("Imagen Cierre",imgCierre)
cv2.waitKey(0)
cv2.destroyAllWindows()
#https://es.acervolima.com/erosion-y-dilatacion-de-imagenes-usando-opencv-en-python/
#https://unipython.com/transformaciones-morfologicas/
#https://www.youtube.com/watch?v=eN2p374g-rM
#https://programmerclick.com/article/96751091306/