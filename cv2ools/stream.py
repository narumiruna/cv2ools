import cv2


class VideoStream(object):
    def __init__(self, filename):
        self.cap = cv2.VideoCapture(filename)

    def __iter__(self):
        return self

    def __next__(self):
        if self.cap.isOpened():
            retval, image = self.cap.read()
            if retval:
                return image

        self.cap.release()
        raise StopIteration
