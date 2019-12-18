import cv2


class VideoWriter(cv2.VideoWriter):
    def __init__(self,
                 filename,
                 api_preference=cv2.CAP_FFMPEG,
                 fourcc='mp4v',
                 fps=60,
                 frame_size=(1024, 768)):
        if isinstance(fourcc, str):
            fourcc = cv2.VideoWriter_fourcc(*fourcc)
        super(VideoWriter, self).__init__(filename=filename,
                                          apiPreference=api_preference,
                                          fourcc=fourcc,
                                          fps=fps,
                                          frameSize=frame_size)

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.release()