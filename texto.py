import pytesseract  
import cv2
img=cv2.imread("img.jpg") #para abrir la imagen y analizar
texto=pytesseract.image_to_string(img,lang="spa") #lang es para selecionar el idioma 
#de la transcripcion de imagen a texto,tesseract viene por defecto con ingles
print(texto) #es para leer por la terminal lo que pudo traducir

cv2.waitKey(0)
cv2.destroyAllWindows()