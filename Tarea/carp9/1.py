#Importa las librerias a utilizar
import argparse
import cv2

#Carga la imagen y coloca mascara gris
image = cv2.imread("coins.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Image", image)
cv2.imshow("Blurred", blurred)

#Threshold
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Felgrand", cv2.bitwise_and(image, image, mask=threshInv))
cv2.waitKey(0)
