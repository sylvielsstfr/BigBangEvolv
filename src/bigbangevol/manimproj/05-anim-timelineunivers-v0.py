from manim import *


class TimelineUnivers(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Titre
        titre = Text("Histoire de l'univers", font_size=48, color=WHITE)
        titre.to_edge(UP)
        self.play(Write(titre))

        # Axe horizontal (timeline)
        ligne = Line(LEFT * 6, RIGHT * 6, color=GRAY)
        self.play(Create(ligne))

        # Dates et événements
        evenements = [
            ("0 s", "Big Bang"),
            ("10⁻³⁶ s", "Inflation"),
            ("10⁻⁶ s", "Particules"),
            ("3 min", "Nucléosynthèse"),
            ("380 000 ans", "CMB"),
            ("400 M années", "Galaxies"),
            ("9 Ga", "Soleil"),
            ("13,8 Ga", "Aujourd’hui"),
        ]

        points = []
        for i, (date, label) in enumerate(evenements):
            pos = interpolate(LEFT * 5.5, RIGHT * 5.5, i / (len(evenements) - 1))
            pt = Dot(point=pos, color=WHITE)
            txt_date = Text(date, font_size=24, color=YELLOW).next_to(pt, DOWN)
            txt_label = Text(label, font_size=26, color=BLUE).next_to(pt, UP)
            self.play(FadeIn(pt), Write(txt_date), Write(txt_label), run_time=0.8)
            points.append(pt)

        self.wait(2)

        # Animation finale : surbrillance de la timeline
        surbrillance = SurroundingRectangle(ligne, color=BLUE, buff=0.1)
        self.play(Create(surbrillance))
        self.wait(2)
