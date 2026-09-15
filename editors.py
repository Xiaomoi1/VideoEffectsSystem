#VideoEditor coordinates the editing process, it stores the selected effects and applies them to the current video.
class VideoEditor:
    def __init__(self, video):
        self.video = video
        self.effects = []

    def add_effect(self, effect):
        self.effects.append(effect)

    def apply_effects(self):
        for effect in self.effects:
            self.video = effect.apply(self.video)

    def trim(self, start, end):
        self.video.clip = self.video.clip.subclipped(start, end)

    def export(self, filepath):
        self.video.clip.write_videofile(filepath)