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
        self.wait(0.1)


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

        vid = cv2.VideoCapture("assets/rotating.mp4")
        img = ImageMobject(vid.read()[1])

        self.next_slide()

        self.play(
            GrowFromPoint(img, 1.75 * np.array([np.cos(np.pi / 3 + np.pi / 6), np.sin(np.pi / 3 + np.pi / 6), 0])))

        vid.release()

        # self.play(*[FadeOut(j) for j in texts], FadeOut(chem))


class OrbitingOrbitals(Slide):
    def construct(self):
        vid = cv2.VideoCapture("assets/rotating.mp4")
        img = ImageMobject(vid.read()[1])

        self.start_loop()
        self.play(VideoPlayer(img, vid), run_time=2)
        self.end_loop()

        vid.release()

        translating = cv2.VideoCapture("assets/translating.mp4")

        translating_img = ImageMobject(translating.read()[1])

        self.play(FadeIn(translating_img))

        self.play(VideoPlayer(translating_img, translating))

        bonding = cv2.VideoCapture("assets/bonding.mp4")
        bonding_img = ImageMobject(bonding.read()[1])
        self.add(bonding_img)

        self.next_slide()
        self.wait(1)

        bonding.release()
        translating.release()


class Bonding(Slide):
    def construct(self):
        bonding = cv2.VideoCapture("assets/bonding.mp4")
        bonding_img = ImageMobject(bonding.read()[1])

        self.add(bonding_img)
        self.play(VideoPlayer(bonding_img, bonding))

        bonding.release()

        antibonding = cv2.VideoCapture("assets/antibonding.mp4")
        antibonding_img = ImageMobject(antibonding.read()[1])

        self.next_slide()

        self.play(FadeIn(antibonding_img))
        self.play(VideoPlayer(antibonding_img, antibonding))

        self.remove(bonding_img)

        antibonding.release()

        antibonding_static = ImageMobject("assets/antibondingstatic.png")
        self.add(antibonding_static)
        self.remove(antibonding_img)

        self.next_slide()

        antibonding_static.generate_target()
        antibonding_static.target.shift(3.5 * LEFT + 1.5 * UP)
        antibonding_static.target.scale(0.5)
        self.play(MoveToTarget(antibonding_static))

        bonding_static = ImageMobject("assets/bondingstatic.png")
        bonding_static.shift(3.5 * LEFT + 1.5 * DOWN)
        bonding_static.scale(0.5)
        self.play(FadeIn(bonding_static))

        self.next_slide()

        arrow = Arrow(start=4 * DOWN + 1 * LEFT, end=4 * UP + 1 * LEFT)
        self.play(Create(arrow))

        pi_el = Line(start=2 * DOWN + 2 * RIGHT, end=2 * DOWN + 4 * RIGHT)

        pi_star_el = Line(start=2 * UP + 2 * RIGHT, end=2 * UP + 4 * RIGHT)

        self.play(Create(pi_el), run_time=0.5)
        self.play(Create(pi_star_el), run_time=0.5)

        self.next_slide()

        pi_mo_text = MathTex(r'\pi-\text{Molecular Orbital}', font_size=16).move_to(DOWN * 3)
        pi_mo_text.next_to(pi_el, DOWN)
        self.play(Create(pi_mo_text), run_time=1)

        pi_star_mo_text = MathTex(r'\pi^\ast-\text{Molecular Orbital}', font_size=16).move_to(DOWN * 3)
        pi_star_mo_text.next_to(pi_star_el, DOWN)
        self.play(Create(pi_star_mo_text), run_time=1)

        electron1 = Arrow(start=2 * DOWN + 2.75 * RIGHT, end=0.5 * DOWN + 2.75 * RIGHT)
        electron2 = Arrow(end=2 * DOWN + 3.25 * RIGHT, start=0.5 * DOWN + 3.25 * RIGHT)

        self.next_slide()

        self.play(Create(electron1, run_time=0.25))
        self.play(Create(electron2), run_time=0.25)

        self.next_slide()

        self.play(*[FadeOut(o) for o in self.mobjects if o != arrow])


class BenzeneOrbitals(Slide):
    def construct(self):
        arrow = Arrow(start=4 * DOWN + 1 * LEFT, end=4 * UP + 1 * LEFT)
        self.add(arrow)

        arrow.generate_target()
        arrow.target.shift(RIGHT)

        self.play(MoveToTarget(arrow))

        benzene = [ImageMobject(f'assets/benzene{j + 1}.png').scale(0.5) for j in range(6)]

        benzene[0].move_to(3.5 * LEFT + 3 * DOWN)
        benzene[1].move_to(3.5 * LEFT + 3 * UP)
        benzene[2].move_to(5.25 * LEFT + 1 * DOWN)
        benzene[3].move_to(1.75 * LEFT + 1 * DOWN)
        benzene[4].move_to(5.25 * LEFT + 1 * UP)
        benzene[5].move_to(1.75 * LEFT + 1 * UP)

        lines = [Line(start=LEFT, end=RIGHT) for _ in range(6)]

        lines[0].move_to(3.5 * RIGHT + 3 * DOWN)
        lines[1].move_to(3.5 * RIGHT + 3 * UP)
        lines[2].move_to(1.75 * RIGHT + 1 * DOWN)
        lines[3].move_to(5.25 * RIGHT + 1 * DOWN)
        lines[4].move_to(1.75 * RIGHT + 1 * UP)
        lines[5].move_to(5.25 * RIGHT + 1 * UP)

        order = [0, 2, 3, 4, 5, 1]
        for j in order:
            self.play(FadeIn(benzene[j]), Create(lines[j]))

        boundary = DashedLine(start=ORIGIN, end=7 * RIGHT)
        pi = MathTex(r'\pi')
        pi_star = MathTex(r'\pi^\ast')
        pi_star.next_to(boundary, UP).align_to(boundary, RIGHT)
        pi.next_to(boundary, DOWN).align_to(pi_star, LEFT)

        self.next_slide()

        self.play(Create(boundary))
        self.play(Create(pi), Create(pi_star))

        electrons = [[Arrow(start=0.25 * LEFT, end=UP + 0.25 * LEFT),
                      Arrow(end=0.25 * RIGHT, start=UP + 0.25 * RIGHT)] for _ in range(3)]

        electrons[0][0].shift(3.5 * RIGHT + 3 * DOWN)
        electrons[0][1].shift(3.5 * RIGHT + 3 * DOWN)
        electrons[1][0].shift(5.25 * RIGHT + 1 * DOWN)
        electrons[1][1].shift(5.25 * RIGHT + 1 * DOWN)
        electrons[2][0].shift(1.75 * RIGHT + 1 * DOWN)
        electrons[2][1].shift(1.75 * RIGHT + 1 * DOWN)

        self.next_slide()

        self.play(*[Create(j) for sublist in electrons for j in sublist], run_time=0.5)

        self.next_slide()

        self.play(*[FadeOut(j) for j in self.mobjects if j != arrow])


class RandomBars(Slide):
    LINE_COUNT = 60

    def construct(self):
        arrow = Arrow(start=4 * DOWN, end=4 * UP)
        self.add(arrow)
        arrow.generate_target()
        arrow.target.shift(4.5 * LEFT)
        self.play(MoveToTarget(arrow))

        lines = np.linspace(1., 3., self.LINE_COUNT)

        humo_lines = np.random.permutation(lines)
        lumo_lines = np.random.permutation(lines)

        self.play(LaggedStart(*[GrowFromCenter(
            Line(start=4 * LEFT + humo_lines[j] * DOWN,
                 end=4 * RIGHT + humo_lines[j] * DOWN, stroke_color=BLUE)) for j in range(self.LINE_COUNT)],
                              lag_ratio=0.9),
                  LaggedStart(*[GrowFromCenter(
                      Line(start=4 * LEFT + lumo_lines[j] * UP,
                           end=4 * RIGHT + lumo_lines[j] * UP, stroke_color=LIGHT_GRAY)) for j in
                      range(self.LINE_COUNT)],
                              lag_ratio=0.9),
                  run_time=3)

        self.wait(0.1)

        self.next_slide()

        lumo_text = Text('Lowest Occupied Molecular Orbital (LUMO)', font_size=24, color=BLACK).shift(2 * UP)
        humo_text = Text('Highest Occupied Molecular Orbital (HOMO)', font_size=24, color=BLACK).shift(2 * DOWN)

        self.play(Create(lumo_text), Create(humo_text))
        self.wait(1)

        self.next_slide()

        band_gap_arrow = DoubleArrow(start=1 * DOWN + 2 * RIGHT, end=1 * UP + 2 * RIGHT, buff=0, tip_length=0.2)
        band_gap_text = Text('Band Gap', font_size=24).next_to(band_gap_arrow, RIGHT)

        self.play(GrowFromCenter(band_gap_arrow), run_time=1)
        self.play(Create(band_gap_text), run_time=1)

        self.next_slide()

        self.play(FadeOut(lumo_text, humo_text, band_gap_text, band_gap_arrow, arrow))


class FlyingElectrons(Slide):
    def construct(self):
        lumo_rect = Rectangle(fill_color=LIGHT_GRAY, stroke_opacity=0, fill_opacity=1, width=8, height=2).shift(2 * UP)
        humo_rect = Rectangle(fill_color=BLUE, stroke_opacity=0, fill_opacity=1, width=8, height=2).shift(2 * DOWN)

        self.add(lumo_rect)
        self.add(humo_rect)

        lumo_rect.target = Rectangle(fill_color=LIGHT_GRAY, stroke_opacity=0, fill_opacity=1, width=16, height=2).shift(
            2 * UP)
        humo_rect.target = Rectangle(fill_color=BLUE, stroke_opacity=0, fill_opacity=1, width=16, height=2).shift(
            2 * DOWN)

        self.play(MoveToTarget(lumo_rect), MoveToTarget(humo_rect))

        electron = VGroup(
            Circle(radius=0.75, fill_color=BLUE, fill_opacity=1, stroke_color=DARK_BLUE, stroke_opacity=1),
            Text('-', font_size=36, color=DARK_BLUE)
        ).shift(2 * DOWN)

        electron.z_index = 1

        hole = VGroup(
            Circle(radius=0.75, fill_color=RED_B, fill_opacity=1, stroke_color=RED_E, stroke_opacity=1),
            Text('+', font_size=36, color=RED_E)
        ).shift(2 * DOWN)

        self.next_slide()

        self.play(Create(electron))
        self.add(hole)

        electron.generate_target()
        electron.target.shift(4 * UP)

        self.play(MoveToTarget(electron))

        self.next_slide()

        e_field_arrow = Arrow(start=4 * LEFT, end=4 * RIGHT)
        self.play(Create(e_field_arrow))

        electron.generate_target()
        electron.target.shift(8 * LEFT)
        hole.generate_target()
        hole.target.shift(8 * RIGHT)

        self.play(MoveToTarget(electron), MoveToTarget(hole), run_time=5, rate_func=rate_functions.ease_in_quad)


class Injection(Slide):
    def construct(self):
        lumo_rect = Rectangle(fill_color=LIGHT_GRAY, stroke_opacity=0, fill_opacity=1, width=16, height=2).shift(
            2 * UP)
        homo_rect = Rectangle(fill_color=BLUE, stroke_opacity=0, fill_opacity=1, width=16, height=2).shift(
            2 * DOWN)

        lumo_rect.target = Rectangle(fill_color=LIGHT_GRAY, stroke_opacity=0, fill_opacity=1, width=8, height=2).shift(
            2 * UP)
        homo_rect.target = Rectangle(fill_color=BLUE, stroke_opacity=0, fill_opacity=1, width=8, height=2).shift(
            2 * DOWN)
        self.add(lumo_rect)
        self.add(homo_rect)
        self.wait(1)
        self.next_slide()
        self.play(MoveToTarget(lumo_rect), MoveToTarget(homo_rect))

        self.next_slide()

        hil = Rectangle(width=3, height=6, fill_color=TEAL, fill_opacity=1, stroke_opacity=0).shift(5.5 * LEFT)
        eil = Rectangle(width=3, height=6, fill_color=PURPLE, fill_opacity=1, stroke_opacity=0).shift(5.5 * RIGHT)

        hil = VGroup(
            hil,
            Paragraph('Hole', 'Injection', 'Layer', alignment='center', font_size=24).align_to(hil.center(), ORIGIN)
        ).shift(5.5 * LEFT)

        eil = VGroup(
            eil,
            Paragraph('Electron', 'Injection', 'Layer', alignment='center', font_size=24).align_to(eil.center(), ORIGIN)
        ).shift(5.5 * RIGHT)

        self.play(Create(hil), Create(eil))

        electron = VGroup(
            Circle(radius=0.75, fill_color=BLUE, fill_opacity=1, stroke_color=DARK_BLUE, stroke_opacity=1),
            Text('-', font_size=36, color=DARK_BLUE)
        ).shift(2 * DOWN + 3 * LEFT)

        hole = VGroup(
            Circle(radius=0.75, fill_color=RED_B, fill_opacity=1, stroke_color=RED_E, stroke_opacity=1),
            Text('+', font_size=36, color=RED_E)
        ).shift(2 * DOWN + 3 * LEFT)

        self.next_slide()

        electron.z_index = 1
        self.play(Create(electron))
        self.add(hole)

        electron.generate_target()
        electron.target.shift(2.5 * LEFT)
        self.play(MoveToTarget(electron), rate_func=rate_functions.ease_in_out_circ)
        self.play(FadeOut(electron))

        electron2 = VGroup(
            Circle(radius=0.75, fill_color=BLUE, fill_opacity=1, stroke_color=DARK_BLUE, stroke_opacity=1),
            Text('-', font_size=36, color=DARK_BLUE)
        ).shift(2 * UP + 5.5 * RIGHT)

        electron2.generate_target()
        electron2.target.shift(2.5 * LEFT)

        self.next_slide()

        self.play(Create(electron2))
        self.play(MoveToTarget(electron2), rate_func=rate_functions.ease_in_out_circ)

        electron2.generate_target()
        electron2.target.shift(3 * LEFT)

        hole.generate_target()
        hole.target.shift(3 * RIGHT)

        self.next_slide()

        self.play(MoveToTarget(electron2), MoveToTarget(hole), run_time=3)

        tracker = ValueTracker(0)

        plane = NumberPlane(x_range=(0, 1), y_range=(-1, 1), x_length=8, y_length=0.1,
                            background_line_style={
                                'stroke_opacity': 0
                            },
                            faded_line_style={
                                'stroke_opacity': 0
                            }).shift(RIGHT * 3.5)

        photon = always_redraw(
            lambda: plane.plot(
                lambda x: np.sin(100 * x), x_range=(tracker.get_value(), tracker.get_value() + 0.1, 0.1 / 100), color=PURE_GREEN
            )
        )

        electron2.generate_target()
        electron2.target.shift(2 * DOWN)

        self.next_slide()

        self.play(MoveToTarget(electron2), rate_func=rate_functions.linear)

        self.add(photon)
        electron2.generate_target()
        electron2.target.shift(2 * DOWN)

        self.play(MoveToTarget(electron2), tracker.animate.set_value(1), rate_func=rate_functions.linear)

        self.remove(hole)
        self.next_slide()
        self.play(FadeOut(electron2))


class Layers(Slide):
    def construct(self):
        lumo_rect = Rectangle(fill_color=LIGHT_GRAY, stroke_opacity=0, fill_opacity=1, width=8, height=2).shift(
            2 * UP)
        homo_rect = Rectangle(fill_color=BLUE, stroke_opacity=0, fill_opacity=1, width=8, height=2).shift(
            2 * DOWN)

        hil = Rectangle(width=3, height=6, fill_color=TEAL, fill_opacity=1, stroke_opacity=0).shift(5.5 * LEFT)
        eil = Rectangle(width=3, height=6, fill_color=PURPLE, fill_opacity=1, stroke_opacity=0).shift(5.5 * RIGHT)

        hil = VGroup(
            hil,
            Paragraph('Hole', 'Injection', 'Layer', alignment='center', font_size=24).align_to(hil.center(), ORIGIN)
        ).shift(5.5 * LEFT)

        eil = VGroup(
            eil,
            Paragraph('Electron', 'Injection', 'Layer', alignment='center', font_size=24).align_to(eil.center(), ORIGIN)
        ).shift(5.5 * RIGHT)

        self.add(lumo_rect, homo_rect, hil, eil)

        semicon = VGroup(lumo_rect, homo_rect)

        el = Rectangle(width=3, height=6, fill_color=GREEN, fill_opacity=1, stroke_opacity=0)

        self.play(Transform(semicon, el))
        self.play(Create(Paragraph('Emissive', 'Layer', alignment='center', font_size=24)), run_time=1)

        htl = VGroup(
            Rectangle(width=2.5, height=6, fill_color=PINK, fill_opacity=1, stroke_opacity=0),
            Paragraph('Hole', 'Transport', 'Layer', alignment='center', font_size=24)
        ).shift(2.75 * LEFT)

        etl = VGroup(
            Rectangle(width=2.5, height=6, fill_color=DARK_BROWN, fill_opacity=1, stroke_opacity=0),
            Paragraph('Electron', 'Transport', 'Layer', alignment='center', font_size=24)
        ).shift(2.75 * RIGHT)

        self.play(Create(htl), Create(etl))

        self.next_slide()
        self.play(*[FadeOut(m) for m in self.mobjects])


class Summary(Slide):
    def construct(self):

        text = Tex(r'''\begin{flushleft}\textbf{Advantages}
                                \begin{itemize}
                                    \item Layers can be made very thin
                                    \begin{itemize}
                                        \item Thinner
                                        \item Flexible
                                    \end{itemize}

                                    \item Can be made to pixel size
                                    \begin{itemize}
                                        \item Pixels can be individually turned off
                                        \item Higher contrast
                                        \item More energy efficient
                                    \end{itemize}
                                \end{itemize}

                                \textbf{Disadvantages}
                                \begin{itemize}
                                    \item Lower maximum brightness
                                    \item Lower quantum efficiency
                                    \item Less durable
                                    \item Shorter lifespan
                                \end{itemize}\end{flushleft}''', font_size=24)
        self.play(Create(text))
        self.wait(1)
        self.next_slide()
        self.play(FadeOut(text))
        refs = Tex(r'''\begin{flushleft}(1) Boudrioua, A.; Chakaroun, M.; Fischer, A. In \textit{Organic Lasers}, Boudrioua, A., Chakaroun, M., Fischer, A., Eds.; Elsevier: 2017, pp 1–47.\\
(2) Boudrioua, A.; Chakaroun, M.; Fischer, A. In \textit{Organic Lasers}, Boudrioua, A., Chakaroun, M., Fischer, A., Eds.; Elsevier: 2017, pp 49–93.\\
(3) Huang, Y.; Hsiang, E.-L.; Deng, M.-Y.; Wu, S.-T. \textit{Light: Science \& Applications} \textbf{2020}, 9, 105.\end{flushleft}''', font_size=24)
        self.play(Create(refs))
        self.wait(1)


"""https://onlinelibrary.wiley.com/doi/10.1002/pi.1974"""
