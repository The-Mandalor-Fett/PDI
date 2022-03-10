from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt

def abrir(img):#SE LE PASA EL nombre DE LA IMAGEN COMO PARÁMETRO

    #EL NOMBRE DE LA IMAGEN SERA INTRODUCIDA EN LA VARIABLE img
    #POR ESO SE CONCATENA
    rutaArchivo=("./img/"+img) #./ ES PARA LA RUTA ACTUAL EN LA QUE ESTAMOS

    img= Image.open(rutaArchivo) #ABRE LA IMAGEN DESDE LA RUTA OBTENIDA

    img.show() #MUESTRA LA IMAGEN EN TU EXPLORADOR DEFALUT
    print(rutaArchivo)#MUESTRA LA RUTA DEL ARCHIVO

#COMO NO QUIERO TRABAJAR CON OTRA IMAGEN EN GRISES CONVERTIRÉ LA IMAGEN ORIGINAL EN GRISES
#NO FUNCIONO Y NO GUARDA LA IMAGEN CORRECTAMENTE xd
def escala_grises(img): #SE LE PASA EL nombre DE LA IMAGEN COMO PARÁMETRO

    rutaArchivo=("./img/"+img)
    img= Image.open(rutaArchivo)
    img.show() #MUESTRA LA IMAGEN EN TU EXPLORADOR DEFALUT
    #AHORA NECESITAMOS CREAR UNA NUEVA VARIABLE QUE CONTENGA LA NUEVA IMAGEN EN
    #ESCALA DE GRISES, LO HAREMOS CAMBIANDO CADA PIXEL DE LA IMAGEN CON SU CORRESPONDIENTE EN RGB
    #Y SACANDO SU PROMEDIO
    imgris = img
    i = 0
    while i < imgris.size[0]: #.size ES PARA EL TAMAÑO DEL arreglo Y [0] ES PARA LAS FILAS
        j = 0
        while j < imgris.size[1]:
            r, g , b = imgris.getpixel((i,j)) #OBTIENE EL PIXEL DE LA POSICIÓN [i,j]

            #PARA OBTENER LA IMAGEN EN GRISES DEBAMOS SACAR SU PORMEDIO COMO ENTERO
            gris = int((r + g + b)/3)
            #PARA PONER EL PIXEL EN GRISES NECESITAMOS UNA TUPLA QUE CONTENGA LOS 3 NIVELES DE GRIS
            tupla = (gris,gris,gris)#GUARDAMOS LOS VALORES DE GRIS EN UNA TUPLA
            #print(tupla)
            imgris.putpixel((i,j),tupla)#COLOCAMOS LOS VALORES DE GRIS EN LOS PIXELES
            print("Niveles de gris en la posicion ["+str(i)+" "+str(j)+"] = "+str(gris))
            j += 1
        i += 1   #AUMENTAMOS EN CADA ITERACIÓN PARA CAMBIAR CADA UNO DE LOS PIXELES
    imgris.save("./img/escalagris.jpg")
    imgris.show()
   
#MÉTODO QUE DA EL NEGATIVO EN ESCALA DE GRISES
def negativo_grises(img):
    rutaArchivo=("./img/"+img)
    img= Image.open(rutaArchivo)
    img.show()
    imgnegativo = img
    ''' PARA OBTENER EL NEGATIVO DEBEMOS RESTAR EL VAMOR MÁXIMO DE GRIS 255 POR
    EL VALOR ACTUAL DEL PIXEL 255-valoractual'''
    i = 0
    while i < imgnegativo.size[0]: #.size ES PARA EL TAMAÑO DEL arreglo Y [0] ES PARA LAS FILAS
        j = 0
        while j < imgnegativo.size[1]:
            gris1,gris2,gris3 = imgnegativo.getpixel((i,j))
            valorActual = int((gris1 + gris2 + gris3) / 3) #OBTIENE EL VALOR ACTUAL DE GRIS
            negativo = 255 - valorActual #OBTIENE SU NEGATIVO
            tupla = (negativo,negativo,negativo)
            print("Valores actuales de gris en la imagen = ["+str(gris1)+", "+str(gris2)+", "+str(gris3)+"]")
            print("Nuevo valor obtenido "+str(negativo))
            imgnegativo.putpixel((i,j),tupla)
            j += 1
        i += 1
    imgnegativo.save("./img/negativo.jpg")#GUARDA LA IMAGEN EN NEGATIVO EN LA CARPETA DE img
    imgnegativo.show()