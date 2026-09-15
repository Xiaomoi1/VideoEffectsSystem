# Video Effects System

This project is a simplified video editing system written in Python, the main purpose of the project is to demonstrate object-oriented programming, specifically inheritance and polymorphism. The system contains a base Effect class and several different effects:
BlurEffect, ZoomEffect, CropEffect, RotateEffect and SpeedEffect, each effect inherits from Effect and implements the same apply(video)
operation in its own way. This allows the VideoEditor to work with different effects through the same interface while each effect performs a different operation.

The program also provides a graphical interface where the user can open a
video, select effects, trim the video and export the edited result.

The project uses MoviePy to perform the actual video editing operations and
Tkinter for the graphical interface.