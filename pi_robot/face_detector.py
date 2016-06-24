import cv2
import sys
import time
from pi_robot.location import Location
from pi_robot.distance import Distance

class FaceDetector(object):
        def __init__(self, width, height, fps, center_offset, casc_path):
            self.width = width
            self.height = height
            self.fps = fps
            self.center_offset = center_offset
            self.face_cascade = cv2.CascadeClassifier(casc_path)
            self.location = Location.NONE
            self.distance = Distance.NONE

        def init(self):
            self.video_capture = cv2.VideoCapture(0)
            self.video_capture.set(3, self.width)
            self.video_capture.set(4, self.height)
            self.video_capture.set(5, self.fps)

        def clear(self):
            # When everything is done, release the capture
            self.video_capture.release()
            cv2.destroyAllWindows()

        def detect(self):
            self.start_time = time.time()

            # Skip frames
            exec_time = time.time() - self.start_time
            while exec_time > 0:
                self.video_capture.grab()
                exec_time -= 1

            ret, frame = self.video_capture.read()
            start_time = time.time()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(20,20),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )

            # Draw a rectangle around the faces
            has_faces = False
            for (x, y, w, h) in faces:
                has_faces = True
                if h/self.height > 0.45:
                    self.distance = Distance.NEAR
                else:
                    self.distance = Distance.FAR

                loc_center = (x + (w / 2)) / (self.width / 2)
                if loc_center < 1 - self.center_offset :
                    self.location = Location.LEFT
                elif loc_center > 1 + self.center_offset :
                    self.location = Location.RIGHT
                else:
                    self.location = Location.CENTER

            if not has_faces:
                self.location = Location.NONE
                self.distance = Distance.NONE


