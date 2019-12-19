import logging

import cv2

logger = logging.getLogger(__name__)


def read(filename):
    cap = cv2.VideoCapture(filename)

    while cap.isOpened():
        retval, image = cap.read()
        if retval:
            yield image
        else:
            break

    cap.release()
    logger.info('video capture: {} released', filename)
