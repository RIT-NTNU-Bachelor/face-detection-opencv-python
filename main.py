# OpenCV Library 
import cv2

# Path to the image with 
image_path = "images/4_faces.jpg"

# Read the image
img = cv2.imread(image_path)

# Printing the image
print(f"Original Image dimension: ({img.shape})")


# Turing the image into a grayscale image
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Printing the gray scale image
print(f"Gray-Scale Image dimension: ({gray_image.shape})")

# Loading the classifier from a pretrained dataset
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Performing the face detection
# - Using the method detectMultiScale() to detect faces
# - Using the grayscale image 
# - scaleFactor is for scaling down the input image
#   - Makes it easier to detect faces 
#   - Reducing size by 10%
# - minNeighbors is for setting the number of neighboring rectangles next to a object to make it valid
#   - Changing this number will reduce the amount of false positives
# - minSize is the minimum size of the object to be detected
face = face_classifier.detectMultiScale(
    gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40,40)
)

