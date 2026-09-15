import numpy as np
from PIL import Image, ImageFilter
class Effect:
    def apply(self, video):
        raise NotImplementedError

#base class for all video effects, every effect provides its own version of apply(), which allows the VideoEditor to work with different
#effects through the same interface
class BlurEffect(Effect):
    def apply(self, video):
        def blur_frame(frame):
            frame = frame.astype(np.uint8)
            image = Image.fromarray(frame)
            return np.array(image.filter(ImageFilter.GaussianBlur(5)))

        video.clip = video.clip.image_transform(blur_frame)
        return video

class ZoomEffect(Effect):
    def apply(self, video):
        video.clip = video.clip.resized(1.5)
        return video

class RotateEffect(Effect):
    def apply(self, video):
        video.clip = video.clip.rotated(90)
        return video

class SpeedEffect(Effect):
    def __init__(self, factor):
        self.factor = factor

    def apply(self, video):
        video.clip = video.clip.with_speed_scaled(self.factor)
        return video

class CropEffect(Effect):
    def __init__(self, x1, y1, x2, y2):
#the coordinates describe the rectangle that will remain (x1, y1) is the top-left corner and (x2, y2) is the  bottom-right corner of the cropped area
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def apply(self, video):
        video.clip = video.clip.cropped(
            x1=self.x1,
            y1=self.y1,
            x2=self.x2,
            y2=self.y2
        )
        return video