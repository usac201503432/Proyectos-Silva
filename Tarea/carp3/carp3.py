import cv2

#Cargamos la imagen que ya tiene que estar en la misma
#carpeta donde esta el programa de python, esta imagen
#ira a la variable imagen
imagen = cv2.imread('trex.png')

#Mostramos la imagen original en una venta
cv2.imshow('Imagen original', imagen)

#reescribimos la imagen originalmente en formato
#.PNG a .JPG  
cv2.imwrite('nueva.jpg', imagen)

#el atributo waitkey(0) es para que la ventana no se
#cierre y se mantenga abierta la ventana hasta que 
#detengamos el programa
cv2.waitKey(0)
cv2.destroyAllWindows()