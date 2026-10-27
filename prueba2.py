import cv2
capture=cv2.VideoCapture('video.mp4') #guardamos el video 
while True: #aplicamos el while para leer por fragmentos el video
    isTrue, frame=capture.read() #se pasa a fragmentos 
    cv2.imshow('HH',frame) #Mostramos el video
    if cv2.waitKey(20) & 0XFF==ord('d'): #ponemos 20 milisegundo para cada fragmentos
        #presionamos la letra D para salir del bucle 
        break
   
capture.release() #Liberamos el archivo de video
cv2.destroyAllWindows()
