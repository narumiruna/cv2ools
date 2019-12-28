import threading
from queue import Queue

import cv2

from .logging import get_logger

logger = get_logger(__name__)


class Controller(object):
    pause_key = ord('p')
    quit_key = ord('q')

    def __init__(self):
        self.quit = True

    def control(self, delay):
        key = cv2.waitKey(delay)

        if key == self.pause_key:
            self.wait()
        elif key == self.quit_key:
            self.quit = False

    def wait(self):
        while True:
            key = cv2.waitKey(1)
            if key == self.pause_key:
                break
            elif key == self.quit_key:
                self.quit = False
                break


class Displayer(object):

    def __init__(self, stream, winname=None):
        self.stream = stream
        self.winname = winname or str()

        self._delay = None
        self.controller = Controller()

    def display(self):
        controller = Controller()

        for image in self.stream:
            cv2.imshow(self.winname, image)

            controller.control(self.delay)

            if not controller.quit:
                self.stream.stop = True
                break

    @property
    def delay(self):
        if self._delay is None:
            self._delay = int(1000 / self.stream.fps)
        return self._delay


class VideoStream(object):

    def __init__(self, filename):
        self.cap = cv2.VideoCapture(filename)
        self.queue = Queue()
        self.thread = threading.Thread(target=self._read)
        self.thread.start()

        self._fps = None
        self.stop = False

    def _read(self):
        while self.cap.isOpened():
            retval, image = self.cap.read()
            if self.stop:
                logger.info('Stop reading stream')
                break
            elif retval:
                self.queue.put(image)
            else:
                break

        self.queue.put(None)
        self.cap.release()

    def __iter__(self):
        return self

    def __next__(self):
        item = self.queue.get()
        if item is None:
            raise StopIteration
        return item

    @property
    def fps(self):
        if self._fps is None:
            self._fps = self.cap.get(cv2.CAP_PROP_FPS)
        return self._fps


class VideoWriter(cv2.VideoWriter):

    def __init__(self, filename, api_preference=cv2.CAP_FFMPEG, fourcc='mp4v', fps=60, frame_size=(1024, 768)):
        if isinstance(fourcc, str):
            fourcc = cv2.VideoWriter_fourcc(*fourcc)
        super(VideoWriter, self).__init__(filename=filename,
                                          apiPreference=api_preference,
                                          fourcc=fourcc,
                                          fps=fps,
                                          frameSize=frame_size)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.release()

    def __repr__(self):
        return self.__class__.__name__ + '()'
