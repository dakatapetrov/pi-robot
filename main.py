import cv2
import sys
import time

from pi_robot.face_detector import FaceDetector
from pi_robot.movement_service import MovementService
from pi_robot.distance import Distance
from pi_robot.location import Location

cascPath = sys.argv[3]
width = float(sys.argv[1])
height = float(sys.argv[2])

fd = FaceDetector(width, height, 1, 0.2, cascPath)
fd.init()

ms = MovementService()

while True:
    fd.detect()
    distance = fd.distance
    location = fd.location

    if distance == Distance.NEAR:
        ms.stop()
        continue

    if location == Location.CENTER:
        ms.move_front()
    elif location == Location.RIGHT:
        ms.move_right()
    else:
        ms.move_left()


fd.clear()
