import cv2
img=cv2.imread('Foto.jpg' )
def rescalando(frame,scale=0.25): #la variable scale es para reducir en tanto por ciento la img 
    #redimensionando el alto y ancho de las imagenes 
    #debido a que algunas imagenes o videos superan el ancho y alto de lo que puede 
    #leer la computadora o laptop
    width=int(frame.shape[1]*scale)  #el indice 1 representa el ancho original
    height=int(frame.shape[0]*scale) #el indice 0 representa el alto original
    dimensiones=(width,height)
    return cv2.resize(frame,dimensiones,interpolation=cv2.INTER_AREA)#el ultimo parametro
    #el que dice INTER_AREA es el algoritmo que ejecuta el redimensionamiento

redi_img2=rescalando(img) #almacenamos la imagen redimensionada
cv2.imshow('Computer Science',redi_img2)
cv2.waitKey(0)