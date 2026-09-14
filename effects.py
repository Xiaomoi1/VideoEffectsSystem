class Effect:
    def apply(self, video):
        raise NotImplementedError

class BlurEffect(Effect):
    def apply(self, video):
        print(f"Applying blur effect to '{video.title}'")

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