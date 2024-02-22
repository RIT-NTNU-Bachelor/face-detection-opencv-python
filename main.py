# OpenCV Library 
import cv2

# Path to the image with 
imagePath = "images/4_faces.jpg"

# Read the image
img = cv2.imread(imagePath)

# Printing the image
print(f"The image size is - ({img.shape})")