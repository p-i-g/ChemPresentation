from chanim import *
import cv2


class VideoPlayer(Animation):
    def __init__(self, obj, video, **kwargs):
        super(VideoPlayer, self).__init__(obj, **kwargs)

        self.video = video
        self.total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)

    def interpolate_mobject(self, alpha: float) -> None:
        self.video.set(cv2.CAP_PROP_POS_FRAMES, round(alpha * self.total_frames))
        ret, img = self.video.read()
        if ret:
            np.copyto(self.mobject.pixel_array, cv2.cvtColor(img, cv2.COLOR_BGR2BGRA))
