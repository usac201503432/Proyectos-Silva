import argparse
import cv2

image = cv2.imread("coins.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Image", image)

#TreshInverido para la imagen
(T, threshInv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
print(T)
cv2.imshow("Threshold", threshInv)
cv2.waitKey(0)