# OpenCV Library 
import cv2

from detect_face import detect_face

# Uses OpenCV's built-in function for detecting a face.
# image_path => path of the image.
# Returns the image with green boxes around
def detect_face_from_image(image_path="./images/4_faces.jpg"):
    # Read the image
    img = cv2.imread(image_path)

    # Printing the image
    print(f"Original Image dimension: ({img.shape})")
    
    # Detecting the face
    face = detect_face(img)

    # Drawing the squares from the given box
    for (x, y, w, h) in face:
        # Notify the user that a face has been detected
        print("Processing face...")

        # Using OpenCV function to create the rectangle at the given potion
        color = (0, 255, 0) # Green
        thickness = 6
        cv2.rectangle(img, (x,y), (x+w,y+h), color, thickness) 


    # Turning the color of the image back to normal and returning the image
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)