import threading
from queue import Queue

import cv2


class VideoCapture(object):

    def __init__(self, filename):
        self.cap = cv2.VideoCapture(filename)
        self.queue = Queue()
        self.thread = threading.Thread(target=self._read)
        self.thread.start()

    def _read(self):
        while self.cap.isOpened():
            retval, image = self.cap.read()
            if retval:
                self.queue.put(image)
            else:
                break

        self.queue.put(None)
        self.cap.release()

    def __iter__(self):
        return self

    def __next__(self):
        item = self.queue.get()
        if item is not None:
            return item
        else:
            raise StopIteration


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
