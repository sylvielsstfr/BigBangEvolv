import random

from manim import *


class BigBangScene(Scene):
    def construct(self):
        big_bang = Dot(radius=0.1, color=YELLOW)
        self.play(FadeIn(big_bang))
        self.wait(1)

        # Expansion rapide
        expanding_circle = Circle(radius=3, color=BLUE).scale(0)
        self.play(GrowFromCenter(expanding_circle))
        self.wait(1)

        # Ajout de particules
        particles = VGroup(*[Dot(color=RED) for _ in range(10)])
        for p in particles:
            p.move_to([random.uniform(-3, 3), random.uniform(-3, 3), 0])
        self.play(FadeIn(particles))
        self.wait(2)
