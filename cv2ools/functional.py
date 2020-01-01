import os
import urllib

import cv2

from .core import Displayer
from .core import VideoFileStream
from .core import VideoStream
from .core import VideoWriter
from .utils import get_logger

logger = get_logger(__name__)


def _is_url(s: str) -> bool:
    try:
        result = urllib.parse.urlparse(s)
        return all([result.scheme, result.netloc, result.path])
    except Exception as e:
        logger.debug(e)
        return False


def _is_file(s):
    return os.path.exists(s)


def read_video(filename):
    stream = VideoStream(filename)
    for img in stream:
        yield img


def display_video(filename):
    if _is_file(filename):
        stream = VideoFileStream(filename)
    elif _is_url(filename):
        stream = VideoStream(filename)
    else:
        raise ValueError('filename is invalid')

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
