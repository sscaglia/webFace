# example of face detection in real-time
# using the webcam with python and openCV

import cv2
import sys
import os


def main():
  cascPath = "haarcascade_frontalface_default.xml"
  if not os.path.exists(cascPath):
    cascPath = "/snap/webface/current/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml"
  print("Config file location: ", cascPath)
  faceCascade = cv2.CascadeClassifier(cascPath)

  video_capture = cv2.VideoCapture(0)

  while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    if len(faces) > 0:
        print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

  # When everything is done, release the capture
  video_capture.release()
  cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
