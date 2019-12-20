import cv2

from .core import VideoWriter
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


def write(images, filename, **kwargs):
    with VideoWriter(filename, **kwargs) as writer:
        for image in images:
            writer.write(image)
