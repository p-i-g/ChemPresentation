import cv2
from chanim import *
# or: from manimlib import *
from manim_slides.slide import Slide
import numpy as np
from utils import VideoPlayer


class Introduction(Slide):
    def construct(self):
        # Introduction
        title = Text('OLEDs')
        self.play(Create(title))
        self.next_slide()

        expanded_title = Text('Organic Light Emitting Diodes')
        self.play(Transform(title, expanded_title))

        self.next_slide()
        self.play(FadeOut(expanded_title))


class InorganicVSOrganic(Slide):
    def construct(self):
        crystal = ImageMobject('assets/crystal.png')
        crystal.move_to((-3.5, 0, 0))
        self.play(FadeIn(crystal))

        self.next_slide()

        cross = Cross(stroke_width=12, scale_factor=1.75).move_to(crystal)
        self.play(Create(cross))

        self.next_slide()

        alq3 = ChemWithName(r'''H-[:30,0.62]-[:90]=_[:30](-[:89.1,1.042]N=^[:149.6,1.042](%
                            -[:89.8,0.62]H)-[:210,1.042](-[:150.2,0.62]H)=^[:270.4,1.042](%
                            -[:210.7,0.62]H)-[:330.9,1.042])-[:330](=_[:270](-[:330,0.62]H)-[:210](%
                            -[:270,0.62]H)=_[:150])-[:30]O-[:330]Al(-[:270]O-[:330]-[:270]%
                            -[:209.1,1.042]N=^[:269.6,1.042](-[:209.8,0.62]H)-[:330,1.042](%
                            -[:270.2,0.62]H)=^[:30.4,1.042](-[:330.7,0.62]H)-[:90.9,1.042](-[:30](%
                            -[:330,0.62]H)=^[:90](-[:30,0.62]H)-[:150](-[:90,0.62]H)=^[:210])=_[:150])%
                            -[:30]O-[:90]-[:30]-[:329.1,1.042]N=^[:29.6,1.042](-[:329.8,0.62]H)%
                            -[:90,1.042](-[:30.2,0.62]H)=^[:150.4,1.042](-[:90.7,0.62]H)-[:210.9,1.042]%
                            (=_[:270])-[:150](-[:90,0.62]H)=^[:210](-[:150,0.62]H)-[:270](=^[:330])%
                            -[:210,0.62]H''', 'Aluminium tris(quinolin-8-olate)')

        alq3.scale(0.4).move_to((3.5, 0, 0))

        self.play(alq3.creation_anim())

        self.next_slide()
        self.play(FadeOut(crystal), FadeOut(cross), FadeOut(alq3))


class Benzene(Slide):
    def construct(self):
        chem = ChemWithName(r'*6(-=-=-=)', 'Benzene')

        self.play(chem.creation_anim(), run_time=1)

        self.next_slide()

        texts = []

        for j in range(6):
            sp2 = MathTex("sp^2", font_size=20, color='red')
            sp2.move_to(1.75 * np.array([np.cos(j * np.pi / 3 + np.pi / 6), np.sin(j * np.pi / 3 + np.pi / 6), 0]))
            self.play(Create(sp2), run_time=0.3)
            texts.append(sp2)

        vid = cv2.VideoCapture("assets/test.mp4")
        img = ImageMobject(vid.read()[1])

        self.next_slide()

        self.play(GrowFromPoint(img, 1.75 * np.array([np.cos(np.pi / 3 + np.pi / 6), np.sin(np.pi / 3 + np.pi / 6), 0])))
        vid.release()

        # self.play(*[FadeOut(j) for j in texts], FadeOut(chem))


class OrbitingOrbitals(Slide):
    def construct(self):
        vid = cv2.VideoCapture("assets/test.mp4")
        img = ImageMobject(vid.read()[1])

        self.start_loop()
        self.play(VideoPlayer(img, vid), run_time=2)
        self.end_loop()

        self.start_loop()
        self.play(VideoPlayer(img, vid), run_time=2)
        self.end_loop()

        vid.release()


"""https://onlinelibrary.wiley.com/doi/10.1002/pi.1974"""
