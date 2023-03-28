from chanim import *
# or: from manimlib import *
from manim_slides.slide import Slide
import numpy as np


class Introduction(Slide):
    def construct(self):
        # Introduction
        title = Text('OLEDs')
        self.play(Create(title))
        self.next_slide()

        expanded_title = Text('Organic Light Emitting Diodes')
        self.play(Transform(title, expanded_title))


class Benzene(Slide):
    def construct(self):
        chem = ChemWithName(r'*6(-=-=-=)', 'Benzene')

        self.play(chem.creation_anim(), run_time=1)

        self.next_slide()

        for j in range(6):
            sp2 = MathTex("sp^2", font_size=20, color='red')
            sp2.move_to(1.75 * np.array([np.cos(j * np.pi / 3 + np.pi / 6), np.sin(j * np.pi / 3 + np.pi / 6), 0]))
            self.play(Create(sp2), run_time=0.3)

        self.wait()


class SphericalHarmonicSurface:
    def __init__(self, l, m):
        self.l = l
        self.m = m