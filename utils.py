from chanim import *
import cv2


class VideoPlayer(Animation):
    def __init__(self, obj, video, **kwargs):
        super(VideoPlayer, self).__init__(obj, **kwargs)

        self.video = video

    def interpolate_mobject(self, alpha: float) -> None:
        self.video.set(cv2.CAP_PROP_POS_AVI_RATIO, alpha)
        ret, img = self.video.read()
        if ret:
            print(img.shape)
            np.copyto(self.mobject.pixel_array, cv2.cvtColor(img, cv2.COLOR_BGR2BGRA))
