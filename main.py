from chanim import *
# or: from manimlib import *
from manim_slides.slide import Slide
from scipy.special import sph_harm
from manim_meshes.models.manim_models.opengl_mesh import FastManimMesh
from manim_meshes.models.data_models.mesh import Mesh
from trimesh import load_mesh


class Introduction(Slide):
    def construct(self):
        # Introduction
        title = Text('OLEDs')
        self.play(Create(title))
        self.next_slide()

        expanded_title = Text('Organic Light Emitting Diodes')
        self.play(Transform(title, expanded_title))


class Test(Slide):
    def construct(self):
        tmesh = load_mesh('test.obj', file_type='obj')
        print("test")

        mesh = FastManimMesh(mesh=Mesh(tmesh.vertices, tmesh.faces))
        print("test")
        self.add(mesh)


class Benzene(Slide):
    def construct(self):
        chem = ChemWithName(r'*6(-=-=-=)', "Caffeine")
        chem.scale(0.1)

        self.play(chem.creation_anim())

        self.wait()
        # template = TexTemplate()
        # template.add_to_preamble(r'\usepackage{chemfig}')
        # chem = Tex(r"\chemfig{*6((=O)-N(-CH_3)-*5(-N=-N(-CH_3)-=)--(=O)-N(-H_3C)-)}", tex_template=template)
        #
        # self.play(Create(chem))
        # self.wait()


class SphericalHarmonicSurface:
    def __init__(self, l, m):
        self.l = l
        self.m = m