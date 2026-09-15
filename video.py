from moviepy import VideoFileClip

#represents a video in this program and provides access to the information and MoviePy clip needed for editing
class Video:
    def __init__(self, filepath):
        self.filepath = filepath
        self.clip = VideoFileClip(filepath)

#needed to free us from the bracket in: 'place.holderclass()' kind of thing
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