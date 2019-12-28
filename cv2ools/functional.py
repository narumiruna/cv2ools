import cv2

from .core import Displayer
from .core import VideoStream
from .core import VideoWriter
from .logging import get_logger

logger = get_logger(__name__)


def read_video(filename):
    stream = VideoStream(filename)
    for img in stream:
        yield img


def display_video(filename):
    stream = VideoStream(filename)
    displayer = Displayer(stream)
    displayer.display()


def write_video(images, filename, **kwargs):
    with VideoWriter(filename, **kwargs) as writer:
        for image in images:
            writer.write(image)


def read_images(paths):
    for path in paths:
        img = cv2.imread(path)
        if img is not None:
            yield img
        else:
            continue
