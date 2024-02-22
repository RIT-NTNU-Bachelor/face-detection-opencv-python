# OpenCV Library 
import matplotlib.pyplot as plt
from detect_face_from_camera_feed import detect_face_from_camera_feed
from detect_face_from_image import detect_face_from_image

def run_program():
    print("Options:\n")
    print(" - [1] Detect face from a given image\n")
    print(" - [2] Detect image from camera feed\n")
    user_input = input("Please choose a option (1/2):")

    # Validate user input
    if int(user_input) < 1 or int(user_input) > 4:
        print("Incorrect usage of program.\n")
        print(" - python3 main.py <OPTION> \n")
        exit(1)

    if user_input.strip() == "1":
        # Picked the image option
        print("[INFO]: Image option picked")

        # Detect the face from the image
        img = detect_face_from_image()

        # Displaying the image with pyplot 
        plt.figure()
        plt.imshow(img)
        plt.axis('off')
        plt.show()

    elif user_input.strip() == "2":
        print("[INFO]: Camera option picked")
        detect_face_from_camera_feed()
    else:
        print(f"Option not implemented: '{user_input}'")

# Running the script
if __name__ == "__main__":
    run_program()
