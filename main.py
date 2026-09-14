from video import Video
from effects import ZoomEffect, RotateEffect, SpeedEffect, CropEffect
from editors import VideoEditor
#the effects are supposed to be put manually by modifying this specific file (for now, will be changed)

#the part where you put your video part
video = Video("test.mp4")

#the place you put your effects at
editor = VideoEditor(video)
editor.add_effect(CropEffect(90, 160, 990, 1760))
editor.apply_effects()
#name your creation
editor.export("cropped.mp4")
video.close()

print("Success")