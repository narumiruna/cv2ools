import threading
from queue import Queue

import cv2


class VideoStream(object):

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
        if item is None:
            raise StopIteration
        return item
