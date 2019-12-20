import cv2

from .logging import get_logger

logger = get_logger(__name__)


def read(filename):
    cap = cv2.VideoCapture(filename)

    while cap.isOpened():
        retval, image = cap.read()
        if retval:
            yield image
        else:
            break

    cap.release()
    logger.info('video capture: %s released', filename)
