import cv2


# Cargamos la imagen en la variabe imagen en el formato original
# Luego al correr el programa la mostraremos y la ventana se llamara imagen original
imagen = cv2.imread('trex.png')
cv2.imshow("Imagen originala", imagen)

# Arreglo de imagenes numpy
# found at (0, 0)
(b, g, r) = imagen[0, 0]
print("Pixel at (0, 0) - Red: %d, Green: %d, Blue: %d" % (r, g, b))

# Cambiamos los valores de los pixeles que queremos alterar
# make it red
imagen[0, 0] = (0, 0, 255)
(b, g, r) = imagen[0, 0]
print("Pixel at (0, 0) - Red: %d, Green: %d, Blue: %d" % (r, g, b))

#Se corta la esquina de la imagen original y la mostramos en una ventana
#que se llamara corner
corner = imagen[0:100, 0:100]
cv2.imshow("Corner", corner)

# Le cambiamos los colores de la esquina, en nuestro caso sera verde
imagen[0:100, 0:100] = (0, 255, 0)

# En una nueva ventana se se mostrara la imagen con el cuadro de color verde
# en la esquina que recortamos y pintamos de color verde
cv2.imshow("Updated", imagen)
cv2.waitKey(0)


#Pueden jugar con los numeritos donde hay 0 o donde esta el 255 y cambiaran 
#los colores, recordar poder cambiar los comentarios y variables y de ser posible
#los colores, la imagen tiene que estar guardada en la misma carpeta donde
#esta el programa de python corriendo.