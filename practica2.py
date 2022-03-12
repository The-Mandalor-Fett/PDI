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
    # PARA OBTENER EL NEGATIVO DEBEMOS RESTAR EL VAMOR MÁXIMO DE GRIS 255 POR
    #EL VALOR ACTUAL DEL PIXEL 255-valoractual
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

def histograma_grises(img):
    rutaArchivo=("./img/"+img)
    img = cv2.imread(rutaArchivo,0)#ABRE LA IMAGEN, EL CERO ES PARA IMAGENES A ESCALA DE GRISES, 1  PARA A COLOR
    #SI NO ESTÁ A COLOR NO VA A ABRIR LA PRIMERA FORMA DEL HISTOGRAMA
    img1 = Image.open(rutaArchivo)
    #d = list(img1.getdata())
    #print(d)
    #datos = np.array(d)
    #media2= int(datos.mean())#MEDIA DE CADA DATO DE LO PIXELES
    cv2.imshow("Imagen para histograma",img)
    ancho = img.shape[0] #OBTIENE EL ancho DE LA IMAGEN 
    largo = img.shape[1] #OBTIENE EL largo DE LA IMAGEN
    intensidadesDegris=[] 
    for i in range(256):
        intensidadesDegris.append(0) #RELLENA LOS 256 TIPOS DE INTENSIDAD DE GRIS CON 0

    for i in range(ancho):
        for j in range(largo):
            #LA intensidadDegris NOS VA A AYUDAR PARA OBTENER LOS VALORES DE GRIS EN CIERTA POSICIÓN
            #EL VALOR OBTENIDO LO COLOCA  EN LA POSICIÓN img.item(i,j) Y LE SUMA 1
            #POR EJEMPLO TENAMOS EL VALOR DE img.item(i,j) = 127 ENTONCES TENEMOS
            #intensidadesDegris[127] = 0, DESPUÉS LE SUMAMOS 1 
            #O SEA QUE EN LA POSICIÓN 127 TENEMOS 1
            intensidadesDegris[img.item(i,j)] = intensidadesDegris[img.item(i,j)] +1 
            #print("Valor de i,j= "+str(img.item(i,j))+" en la posición "+str(i)+" "+str(j))
            #img.item(i,j)-> NOS REGRESA UN VALOR EN UNA POCICIÓN DETERMINADA
    intensidadesDegris = np.asarray(intensidadesDegris)
    print("Posiciones en Y (intensidad) : ",end="")
    print(" "+str(intensidadesDegris))
    plt.plot(intensidadesDegris)
    plt.show()#MUESTRA LA PRIMERA FORMA DEL HISTOGRAMA
    
    
    
