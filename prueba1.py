import cv2 #esta parte del codigo es para ver una img por pantalla con open cv
img=cv2.imread('Foto.jpg') #el termino imread es para leer la imagen 
#se crea una variable para guardar la iamgen
cv2.imshow('Computer Scince',img) #el termino imshow es para mostrar 
cv2.waitKey(0)
