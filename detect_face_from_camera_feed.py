# OpenCV Library 
import cv2

def detect_bounding_box(vid):
    # Loading the classifier from a pretrained dataset
    face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.2, 3, minSize=(50, 50))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)

    return faces



def detect_face_from_camera_feed():
    # Start capturing the video
    video_capture = cv2.VideoCapture(0)
    print("Starting capturing the video feed..")

    while True:
        result, video_frame = video_capture.read()  # read frames from the video

        if result is False:
            print("Not able to read from camera")
            break  # terminate the loop if the frame is not read successfully

        faces = detect_bounding_box(
            video_frame
        )  # apply the function we created to the video frame

        for (x, y, w, h) in faces:
            cv2.rectangle(video_frame, (x, y), (x + w, y + h), (0, 255, 0), 4)

        cv2.imshow(
            "Face Detection - OpenCV", video_frame
        )  # display the processed frame in a window named "My Face Detection Project"

        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Exiting...")
            break

    video_capture.release()
    cv2.destroyAllWindows()