from manim import *
from manim_slides.slide import Slide

class Example(Slide):
    def construct(self):
        dot = Dot(color=BLUE)

        self.start_loop()

        self.play(Indicate(dot))

        self.end_loop()

        self.start_loop()
        self.play(Indicate(dot))
        self.end_loop()
