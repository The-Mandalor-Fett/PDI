from re import I
from PIL import Image

def abrir(img):

    #EL NOMBRE DE LA IMAGEN SERA INTRODUCIDA EN LA VARIABLE img
    #POR ESO SE CONCATENA
    rutaArchivo=("./img/"+img) #./ ES PARA LA RUTA ACTUAL EN LA QUE ESTAMOS

    img= Image.open(rutaArchivo) #ABRE LA IMAGEN DESDE LA RUTA OBTENIDA

    img.show() #MUESTRA LA IMAGEN EN TU EXPLORADOR DEFALUT
    print(rutaArchivo)#MUESTRA LA RUTA DEL ARCHIVO
    
