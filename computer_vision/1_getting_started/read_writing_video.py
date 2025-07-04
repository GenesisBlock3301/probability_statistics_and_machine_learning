import cv2
import numpy as np
import os


def video_from_webcam():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        exit("Could not open webcam")

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def video_from_file():
    root = os.getcwd()
    video_path = os.path.join(root, 'video.mp4')
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        delay = int(1000/60)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break



if __name__ == '__main__':
    video_from_webcam()

