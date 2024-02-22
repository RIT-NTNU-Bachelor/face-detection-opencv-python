# OpenCV Library 
import cv2
import matplotlib.pyplot as plt

from detect_face_from_image import detect_face_from_image

def run_program():
    print("Options:\n")
    print(" - [1] Detect face from a given image\n")
    print(" - [2] Detect image from camera feed\n")
    user_input = input("Please choose a option (1/2):")

    # Validate user input
    if int(user_input) < 1 or int(user_input) > 2:
        print("Incorrect usage of program.\n")
        print(" - python3 main.py <OPTION> \n")
        exit(1)


    if user_input.strip() == "1":
        # Detect the face from the image
        img = detect_face_from_image()

        # Displaying the image with pyplot 
        plt.figure()
        plt.imshow(img)
        plt.axis('off')
        plt.show()


# Running the script
if __name__ == "__main__":
    run_program()

