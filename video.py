from moviepy import VideoFileClip
class Video:
    def __init__(self, filepath):
        self.filepath = filepath
        self.clip = VideoFileClip(filepath)

    @property
    def title(self):
        return self.filepath.split("\\")[-1]

    @property
    def duration(self):
        return self.clip.duration

    @property
    def size(self):
        return self.clip.size

    def close(self):
        self.clip.close()