import cv2


def read(filename):
    cap = cv2.VideoCapture(filename)

    if cap.isOpened():
        retval, image = cap.read()
        if retval:
            yield image

    cap.release()
    raise StopIteration
