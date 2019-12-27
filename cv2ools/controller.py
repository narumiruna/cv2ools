import cv2


class Controller(object):

    def control(self):
        raise NotImplementedError


class Compose(object):

    def __init__(self, controllers):
        self.controllers = controllers

    def control(self):
        for controller in self.controllers:
            controller.control()


class PauseController(Controller):

    def __init__(self, pause_key='p'):
        self.pause_key = ord(pause_key)

    def control(self):
        key = cv2.waitKey(1)
        if key == self.pause_key:
            self.wait()

    def wait(self):
        while True:
            key = cv2.waitKey(1)
            if key == self.pause_key:
                break
