from manim import *
import numpy as np

# Fonction brute non normalisée
def a_raw(t):
    return 1e-5 * (t**0.5 + 0.01 * t**(2/3) + 1e-4 * np.exp(0.09 * t))

# Normalisation pour que a(13.8 Gyr) = 1
a_today = a_raw(13.8)
def a_of_t(t):
    return a_raw(t) / a_today

def z_of_a(a):
    return 1/a - 1

def T_of_a(a):
    return 2.725 / a  # Température approximée en Kelvin

class ScaleFactorTimeline(Scene):
    def construct(self):
        # Axes primaires
        ax = Axes(
            x_range=[0, 14, 2],
            y_range=[0, 1.2, 0.2],
            x_length=10,
            y_length=5,
            axis_config={"include_tip": False},
        )
        labels = ax.get_axis_labels(x_label="Temps (Gyr)", y_label="a(t)")

        # Axe secondaire pour le redshift z = 1/a - 1
        z_labels = VGroup()
        for a_tick in np.arange(0.2, 1.1, 0.2):
            z = z_of_a(a_tick)
            z_text = MathTex(f"z={z:.0f}", font_size=24)
            y_pos = ax.c2p(0, a_tick)[1]
            z_text.move_to(ax.c2p(-0.8, a_tick))
            z_labels.add(z_text)

        # Axe secondaire pour la température
        T_labels = VGroup()
        for a_tick in np.arange(0.2, 1.1, 0.2):
            T = T_of_a(a_tick)
            T_text = MathTex(f"T={T:.0f}K", font_size=24)
            T_text.move_to(ax.c2p(14.8, a_tick))
            T_labels.add(T_text)

        # Courbe a(t)
        graph = ax.plot(a_of_t, color=BLUE)

        self.play(Create(ax), Write(labels))
        self.play(Create(graph), run_time=3)
        self.play(*[Write(lbl) for lbl in z_labels])
        self.play(*[Write(lbl) for lbl in T_labels])

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

        # Curseur temporel animé
        time_marker = ValueTracker(0.0)
        moving_dot = always_redraw(lambda: Dot(ax.c2p(time_marker.get_value(), a_of_t(time_marker.get_value())), color=RED))
        self.add(moving_dot)
        self.play(time_marker.animate.set_value(13.8), run_time=8, rate_func=linear)

        # Zoom progressif sur différentes phases
        self.wait(0.5)
        self.play(
            ax.animate.scale(1.5).move_to(ORIGIN),
            graph.animate.scale(1.5).move_to(ORIGIN),
            *[d.animate.scale(1.5).move_to(ax.c2p(t_val, a_of_t(t_val))) for (t_val, _), d in zip(events, dots)],
            *[l.animate.scale(1.5).next_to(d, UP) for d, l in zip(dots, labels)],
            run_time=2
        )

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
