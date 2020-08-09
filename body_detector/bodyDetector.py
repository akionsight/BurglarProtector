import os
import cv2  # Video Capture, Person Recognition
import sirenPlayer


def detect_faces_from_webcam(webcam_index=0, window_title='Faces In Video', cascade='haarcascade_frontalface_default.xml',box_colour=(0, 255, 0), line_thickness=2):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascade)

    cap = cv2.VideoCapture(webcam_index, cv2.CAP_DSHOW)
    while True:
        _, frame = cap.read()
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY, 1)
        bodies = face_cascade.detectMultiScale(grey,1.05, 6)
        for (x, y, w, h) in bodies:
            cv2.rectangle(frame, (x,y), (x+w, y+h), box_colour, line_thickness)
            sirenPlayer.playSiren()

        cv2.imshow(window_title, frame)
        k = cv2.waitKey(1)
        if k == 27:
            break




detect_faces_from_webcam(1, window_title='frame',box_colour=(0, 0, 255), line_thickness=5, cascade='haarcascade_fullbody.xml')
