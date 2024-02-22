import cv2

def detect_face(img, scale=1.1, neighbors=10, size=50):
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
        gray_image, scaleFactor=scale, minNeighbors=neighbors, minSize=(size,size)
    )

    return face