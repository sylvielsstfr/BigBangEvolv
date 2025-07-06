from manim import *
import numpy as np




# Fonction brute non normalisée
def a_raw(t):
    return 1e-5 * (t**0.5 + 0.01 * t**(2/3) + 1e-4 * np.exp(0.09 * t))

# Normalisation pour que a(13.8 Gyr) = 1
a_today = a_raw(13.8)
def a_of_t(t):
    return a_raw(t) / a_today 




class ScaleFactorTimeline(Scene):
    def construct(self):
        # Axes
        ax = Axes(
            x_range=[0, 14, 2],
            y_range=[0, 1.2, 0.2],
            x_length=10,
            y_length=5,
            axis_config={"include_tip": False},
        )
        labels = ax.get_axis_labels(x_label="Temps (Gyr)", y_label="a(t)")

        # Courbe a(t)
        #graph = ax.plot(a_of_t, color=BLUE)
        graph = ax.plot(lambda t: 0.1 * t, color=BLUE)

        self.play(Create(ax), Write(labels))
        self.play(Create(graph), run_time=3)

        # Événements clés avec temps approximatifs (en Gyr)
        events = [
            (1e-10, "Planck"),
            (1e-6, "Particules"),
            (0.00038, "CMB"),
            (0.2, "Réionisation"),
            (1.0, "Galaxies"),
            (4.5, "Voie Lactée"),
            (9.0, "Réaccélération"),
            (13.8, "Aujourd'hui")
        ]

        dots = []
        labels = []
        for t_val, name in events:
            y_val = a_of_t(t_val)
            dot = Dot(ax.c2p(t_val, y_val), color=YELLOW)
            text = Text(name, font_size=24).next_to(dot, UP)
            dots.append(dot)
            labels.append(text)
            self.play(FadeIn(dot), Write(text), run_time=0.5)

        # Zoom-out pour voir l’inflation en début
        self.wait(0.5)
        self.play(
            ax.animate.scale(0.5).to_edge(LEFT),
            graph.animate.scale(0.5).to_edge(LEFT),
            *[d.animate.scale(0.5).to_edge(LEFT) for d in dots],
            *[l.animate.scale(0.5).to_edge(LEFT) for l in labels],
            run_time=2
        )

        # Annotation spéciale pour inflation (exponentielle)
        infl_text = Text("Inflation", font_size=28, color=RED).to_edge(RIGHT)
        self.play(Write(infl_text))
        self.wait(1)

        # Outro
        conclusion = Text("Expansion accélérée aujourd'hui", font_size=30, color=GREEN)
        conclusion.to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)



