import sys
import cv2 as cv

imgOriginal = ("./img/1-img-promedio.jpg")
img = cv.imread(imgOriginal,0)

cv.imshow("Imagen Original",img)

#Filtro Promedio

imgProm = cv.blur(img,(3,3))

cv.imshow("Imagen Promedio",imgProm)

#Filtro Mediana

imgMed = cv.medianBlur(img, ksize=3)

cv.imshow("Imagen Mediana",imgMed)

#Filtro Laplaciano
imgOriginal = ("./img/4-img-Laplaciano.jpg")
src = cv.imread(imgOriginal, 0)

srcG = cv.GaussianBlur(src, (3, 3), 0)

#src_gray = cv.cvtColor(srcG, cv.COLOR_BGR2GRAY)

lapFilt = cv.Laplacian(srcG, cv.CV_16S, ksize=3)

laplac = cv.convertScaleAbs(lapFilt)

cv.imshow("Imagen Laplaciano", laplac)

#Filtro Sobel
imgSobel = ("./img/7-img-Sobel.jpg")
src = cv.imread(imgSobel, 0)
srcG2 = cv.GaussianBlur(src, (3, 3), 0)
sobelX = cv.Sobel(srcG2, cv.CV_16S,  1, 0, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)

sobelY = cv.Sobel(srcG2, cv.CV_16S,  0, 1, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)

absSobelX = cv.convertScaleAbs(sobelX)

absSobelY = cv.convertScaleAbs(sobelY)

sobel = cv.addWeighted(absSobelX, 0.5, absSobelY, 0.5, 0)

cv.imshow("Imagen Sobel", sobel)

cv.waitKey(0)
cv.destroyAllWindows()