# OpenCV Library 
import cv2

from detect_face import detect_face

def detect_face_from_camera_feed():
    # Start capturing the video
    video_capture = cv2.VideoCapture(0)
    print("Starting capturing the video feed..")

    while True:
        result, video_frame = video_capture.read()  # read frames from the video

        if result is False:
            print("Not able to read from camera")
            break  # terminate the loop if the frame is not read successfully

        # Detecting the face that is in the video
        faces = detect_face(video_frame, scale=1.2, size=50, neighbors=10)

        # Draw a box around each face
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
