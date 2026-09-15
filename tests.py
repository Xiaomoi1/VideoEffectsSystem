import unittest

from effects import Effect, BlurEffect, ZoomEffect, RotateEffect, SpeedEffect, CropEffect
from editors import VideoEditor

#a fake video used only for testing we dont need to load or render a real video when testing the logic of VideoEditor and the Effect classes

class FakeVideo:
    def __init__(self):
        self.applied_effects = []

class FakeEffect(Effect):
    def __init__(self, name):
        self.name = name

    def apply(self, video):
        video.applied_effects.append(self.name)
        return video

class TestEffects(unittest.TestCase):
#testing the inheritance
    def test_effects_inherit_from_effect(self):
        self.assertTrue(issubclass(BlurEffect, Effect))
        self.assertTrue(issubclass(ZoomEffect, Effect))
        self.assertTrue(issubclass(RotateEffect, Effect))
        self.assertTrue(issubclass(SpeedEffect, Effect))
        self.assertTrue(issubclass(CropEffect, Effect))

#test of the VideoEditor.add.effects()
    def test_editor_stores_effect(self):
        video = FakeVideo()
        editor = VideoEditor(video)

        effect = FakeEffect("Test Effect")
        editor.add_effect(effect)

        self.assertEqual(len(editor.effects), 1)
        self.assertIs(editor.effects[0], effect)

#testing polymorphism
    def test_editor_applies_effects_polymorphically(self):
        video = FakeVideo()
        editor = VideoEditor(video)

        editor.add_effect(FakeEffect("Blur"))
        editor.add_effect(FakeEffect("Zoom"))
        editor.add_effect(FakeEffect("Rotate"))

        editor.apply_effects()

        self.assertEqual(
            video.applied_effects,
            ["Blur", "Zoom", "Rotate"]
        )
#testing SpeedEffect, checking if it stores the number 
    def test_speed_effect_stores_factor(self):
        effect = SpeedEffect(2)

        self.assertEqual(effect.factor, 2)

#testing CropEffect, same thing

    def test_crop_effect_stores_coordinates(self):
        effect = CropEffect(10, 20, 100, 200)

        self.assertEqual(effect.x1, 10)
        self.assertEqual(effect.y1, 20)
        self.assertEqual(effect.x2, 100)
        self.assertEqual(effect.y2, 200)
#python -m unittest tests.py -v has been run in the terminal