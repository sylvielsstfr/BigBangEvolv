import random

from manim import *


class BigBangTimeline(Scene):
    def construct(self):
        # Étape 1 : Big Bang - point lumineux
        big_bang = Dot(point=ORIGIN, color=YELLOW, radius=0.1)
        self.play(FadeIn(big_bang))
        self.wait(0.5)

        # Étape 2 : Expansion - cercle qui grandit
        expansion = Circle(radius=0.1, color=BLUE).move_to(ORIGIN)
        self.play(GrowFromCenter(expansion), run_time=1)
        self.play(expansion.animate.scale(8), run_time=2)

        # Étape 3 : Apparition de particules aléatoires
        particles = VGroup()
        for _ in range(40):
            p = Dot(
                point=[random.uniform(-5, 5), random.uniform(-3, 3), 0],
                radius=0.05,
                color=random.choice([RED, ORANGE, GREEN, PURPLE]),
            )
            particles.add(p)

        self.play(FadeIn(particles, lag_ratio=0.02), run_time=2)
        self.wait(1)

        # Étape 4 : CMB - fond lumineux
        cmb_background = Circle(radius=7.5, color=WHITE, stroke_opacity=0.3, fill_opacity=0.1)
        cmb_background.set_fill(WHITE, opacity=0.1)
        self.play(FadeIn(cmb_background), run_time=1)
        self.wait(1)

        # Étape 5 : Transition vers l'univers structuré
        self.play(FadeOut(big_bang), FadeOut(expansion), FadeOut(particles), FadeOut(cmb_background))
        self.wait(1)

        # Fin de cette première scène
        txt = Text("Prochaine étape : formation des galaxies...", font_size=36)
        self.play(Write(txt))
        self.wait(2)


class GalaxiesFormation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Formation des premières galaxies", font_size=42, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Étape 1 : apparition progressive de galaxies
        galaxies = VGroup()
        for _ in range(20):
            galaxy = Star(fill_color=WHITE, stroke_width=0, fill_opacity=0.8, outer_radius=0.2)
            galaxy.move_to([random.uniform(-6, 6), random.uniform(-3, 3), 0])
            galaxies.add(galaxy)

        self.play(LaggedStart(*[FadeIn(g) for g in galaxies], lag_ratio=0.1), run_time=3)
        self.wait(1)

        # Étape 2 : déplacement pour montrer structure
        self.play(galaxies.animate.arrange_in_grid(rows=4, cols=5, buff=1.5).scale(1.5), run_time=3)
        self.wait(1)

        # Étape 3 : Zoom arrière pour montrer l'univers structuré
        # frame = self.camera.frame
        frame = self.camera
        # self.play(frame.animate.scale(1.5), run_time=2)
        # self.play(self.camera.auto_zoom(galaxies, margin=1.2), run_time=2)
        # self.play(galaxies.animate.scale(0.6), run_time=2)
        self.play(galaxies.animate.arrange_in_grid(rows=4, cols=5, buff=1.5).scale(1.2), run_time=3)

        # Texte final
        conclusion = Text("Apparition des structures cosmiques", font_size=36, color=BLUE)
        conclusion.to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)
