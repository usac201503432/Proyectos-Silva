import argparse
import cv2

image = cv2.imread("coins.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Image", image)

#Invierte la imagen
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Gaussian Thresh", thresh)
cv2.waitKey(0)