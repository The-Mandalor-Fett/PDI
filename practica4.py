from PIL import Image
import cv2
import numpy as np
from matplotlib import collections, pyplot as plt
from scipy import stats as st
import statistics as stats
from collections import Counter
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
    ancho = img.shape[0] #OBTIENE EL ancho DE LA IMAGEN
    largo = img.shape[1] #OBTIENE EL largo DE LA IMAGEN
    #print(img1.size)
    ancho1 = img1.size[0] #OBTIENE EL ancho CON PIL
    largo1 = img1.size[1] #OBTIENE EL largo CON PIL
    #print("Ancho y largo")
    #print(ancho1,largo1)
    datoDepixel = []
    intensidadesDegris=[]
    total = ancho*largo
    for i in range(256):
        intensidadesDegris.append(0) #RELLENA LOS 256 TIPOS DE INTENSIDAD DE GRIS CON 0

    datoDepixel = list((img1.getdata()))#OBTIENE LOS NIVELES DE GRIS DE LOS PIXELES
    #print(datoDepixel)
    for i in range(ancho):
        for j in range(largo):
            #LA intensidadDegris NOS VA A AYUDAR PARA OBTENER LOS VALORES DE GRIS EN CIERTA POSICIÓN
            #EL VALOR OBTENIDO LO COLOCA  EN LA POSICIÓN img.item(i,j) Y LE SUMA 1
            #POR EJEMPLO TENAMOS EL VALOR DE img.item(i,j) = 127 ENTONCES TENEMOS
            #intensidadesDegris[127] = 0, DESPUÉS LE SUMAMOS 1
            #O SEA QUE EN LA POSICIÓN 127 TENEMOS 1
            valor = img.item(i,j)
            intensidadesDegris[img.item(i,j)] = intensidadesDegris[img.item(i,j)] +1
            #print("Valor de i,j= "+str(img.item(i,j))+" en la posición "+str(i)+" "+str(j))
            #img.item(i,j)-> NOS REGRESA UN VALOR EN UNA POCICIÓN DETERMINADA

    #datosDepixel = list(img1.getdata())#OBTIENE LOS VALORES DE CADA pixel EN GRIS DE LA IMAGEN

    intensidadesDegris = np.array(intensidadesDegris)#OBTENEMOS LOS VALORES COMO array PARA EL HISTOGRAMA
    #Y ENCONTRAR, media, moda, etc. DEL HISTOGRAMA
    #print("Posiciones en Y (intensidad) : ")
    #print(" "+str(intensidadesDegris))
    media = int(np.mean(intensidadesDegris)) #CALCULA LA media DEL HISTOGRAMA
    moda = (stats.mode(datoDepixel)) #CALCULA LA DEL moda HISTOGRAMA CON statistics, SI ENCUENTRA DOS MODAS
    #RETORNA LA PRIMERA ENCONTRADA
    moda2 = ((st.mode(datoDepixel))) #CALCULA LA DEL moda HISTOGRAMA CON scipy, SI HAY DOS MODAS
    #RETORNA LA MÁS PEQUEÑA
    mediana = int(np.median(intensidadesDegris)) #CALCULA LA mediana DEL HISTOGRAMA
    desvEst = int(np.std(intensidadesDegris)) #CALCULA LA  desviación estandar DEL HISTOGRAMA
    varianza = int(np.var(intensidadesDegris)) #CALCULA LA varianza DEL HISTOGRAMA
    moda3 = Counter(datoDepixel)

    print("La media es: "+str(media))
    print("La moda con statistics es: "+str(moda))
    print("La moda con scipy es: "+str(moda2))
    print("La moda con collections y flatten es: "+str(moda3))
    print("La mediana es: "+str(mediana))
    print("La varianza es: "+str(varianza))
    print("La desviación estandar es: "+str(desvEst))
    cv2.imshow("Imagen para histograma",img)
    plt.plot(intensidadesDegris)
    plt.show()#MUESTRA LA PRIMERA FORMA DEL HISTOGRAMA

    imghisto = cv2.calcHist([img],[0],None,[256],[0,255])#SEGUNDA FORMA DE CALCULAR EL HISTOGRAMA
    fig, ax=plt.subplots(2,2)#DIVIDE LAVENTANA EN QUE MUESTRA LA GRÁFICA EN 4 PARTES
    ax[0,0].imshow(img,cmap="gray")#EN EL LUGAR 0,0 MUESTRA LA IMAGEN, EN GRIS Y CON UN TÍTULO
    ax[0,0].set_title("Jinx")
    ax[0,0].axis("off")#MUESTRA EL PLANO CARTESIANO DE LA IMAGEN

    ax[0,1].plot(imghisto,color="blue")
    ax[0,1].set_title("Jinx")


    ax[1,0].axis("off")
    ax[1,1].axis("off")
    #CALCULA LO ANTERIOR PERO CON LA SEGUNDA FORMA DEL HISTOGRAMA
    print("La media es: "+str(int(np.mean(imghisto))))
    print("La moda con scipy es: "+str(moda2))
    print("La mediana es: "+str(int(np.median(imghisto))))
    print("La varianza es: "+str(int(np.var(imghisto))))
    print("La desviación estandar es: "+str(int(np.std(imghisto))))
    plt.show()#MUESTRA LA SEGUNDA FORMA DE LA CREAR EL HISTOGRAMA
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Método binarizació/umbralización
def umbral(img):
    rutaArchivo=("./img/"+img)
    imgUmbral = cv2.imread(rutaArchivo,0)#ABRE LA IMAGEN CON OPENCV
    #EL CERO ES PARA IMAGENES A ESCALA DE GRISES, 1  PARA A COLOR
    cv2.imshow("Imagen original (en grises)",imgUmbral)
    umbral=int(input("Por favor introduce el umbral: "))#PIDE AL USUARIO EL VALOR DEL umbral
    mascara=np.uint8((umbral < imgUmbral)*255)#CALCULA EL umbral BINARIO CON LA FORMULA
    # PARA TODO umbral < valorDeGRisEn(x,y) ASIGNALE EL VALOR MÁXMO 255
    # SÍ NO ES ASÍ ENCONTES ES 0
    #umbral < imgUmbral NOS RETORNA VERDADERO O FALSO, O SEA UN UNO O CERO
    #DEPENDIENDO DE EL VALOR DE umbral Y EL VALOR DEL pixel
    #ESO SE MULTIPLICA POR 255, DANDO 0 O 255 DEPENDIENDO DEL CASO
    #uint8 SIGNIFICA UNSIGNED INTEGER O SEA ENTERO SIN SIGNO, SIEMPRE ES POSITIVO
    #Y ES DE 8 BITS, POR LO QUE VA DE 0 A 255, ESO NOS DARÁ LA máscara PARA OBTENER LA IMAGEN 

    #Segunda forma de obtener el umbralado binario
    ret,thresh1= cv2.threshold(imgUmbral,umbral,255,cv2.THRESH_BINARY)#OBTIENE EL umbralado MEDIANTE LA FUNCIÓN threshold DE OPENCV
    cv2.imshow("Imagen binarizada",mascara)
    cv2.imshow("Imagen binarizada 2",thresh1)
    cv2.imwrite("./img/binarizado.jpg",mascara)#GUARDA LA IMAGEN
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def log(img):
    rutaArchivo=("./img/"+img)
    img = cv2.imread(rutaArchivo,0)#ABRE LA IMAGEN CON OPENCV
    #CALCULAMOS LA CONSTANTE c = 255/(log(1 + max(f(x,y)))) con NumPy
    constante = int(input("Por favor introduce la constante: "))
    #CALCULA EL logaritmo DE LA FORMA log(1+x)
    logaritmo = constante * (np.log1p(img))

    #NORMALIZAMOS POR SI TENEMOS VALORES MUY PEQUEÑOS
    maximoDelLogaritmo = np.amax(logaritmo) #REGRESA EL VALOR MÁXIMO DEL ARREGLO

    #CONVIERTE LOS VALORES A ENTEROS DE 8 BITS MÁXIMO
    imgLog = np.uint8(logaritmo/maximoDelLogaritmo * 255)

    
    #cv2.imshow("Imagen original",img)
    #cv2.imshow("LOG",imgLog)
    #print(constante)

    cv2.waitKey(0)
    cv2.destroyAllWindows()