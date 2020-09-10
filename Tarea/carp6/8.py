
import numpy as np
import argparse
import cv2

# Construct the argument parser and parse the arguments
image = cv2.imread('trex.png')
# Load the image and show it
# image = cv2.imread(args["image"])
cv2.imshow("Original", image)


mask = np.zeros(image.shape[:2], dtype = "uint8")
(cX, cY) = (image.shape[1] / 2, image.shape[0] / 2)
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75 , cY + 75), 255, -1)
cv2.imshow("Mask", mask)

# Apply out mask -- notice how only the center rectangular
# region of the pill is shown
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

# Now, let's make a circular mask with a radius of 100 pixels
mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.circle(mask, (cX, cY), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)