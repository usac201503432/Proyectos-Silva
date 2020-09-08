# USAGE
# python equalize.py --image ../images/beach.png

# Import the necessary packages
import numpy as np
import argparse
import cv2

# Construct the argument parser and parse the arguments

# Load the image and convert it to grayscale
image = cv2.imread("beach.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization to stretch the constrast
# of our image
eq = cv2.equalizeHist(image)

# Show our images -- notice how the constrast of the second
# image has been stretched
cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
cv2.waitKey(0)