from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
import numpy as np

class MathematicalLogicDeepDive(VoiceoverScene, ThreeDScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # ==========================================
        # SETUP: HELPERS & POSITIONS
        # ==========================================
        syntax_center = LEFT * 3.5
        semantics_center = RIGHT * 3.5
        divider = Line(UP * 4, DOWN * 4, stroke_width=2).set_color(WHITE)

        # ==========================================
        # SCENE 1: PRE-EXISTING PLATONIC SOLIDS
        # ==========================================
        # We define them immediately so they are "pre-existing" like stars in a galaxy
        tetrahedron = Tetrahedron().scale(0.8).move_to(UL * 3).rotate(PI/4, axis=UP).rotate(PI/6, axis=RIGHT)
        cube = Cube().scale(0.8).move_to(UR * 3.5).rotate(PI/3, axis=UP).rotate(PI/4, axis=RIGHT)
        octahedron = Octahedron().scale(0.8).move_to(DL * 3.5).rotate(PI/5, axis=UP).rotate(PI/3, axis=RIGHT)
        icosahedron = Icosahedron().scale(0.8).move_to(DR * 3).rotate(PI/4, axis=UP).rotate(PI/7, axis=RIGHT)
        dodecahedron = Dodecahedron().scale(0.8).move_to(UP * 0.5 + RIGHT * 0.5).rotate(PI/2.5, axis=UP).rotate(PI/5, axis=RIGHT)
        
        solids = VGroup(tetrahedron, cube, octahedron, icosahedron, dodecahedron)
        solids.set_color_by_gradient(BLUE, TEAL, PURPLE)
        
        # Add them directly to the scene without fading in
        self.add(solids)

        script_1 = "In this video series, we will go deep into mathematical logic to figure out what math is and what its limits are."
        with self.voiceover(text=script_1) as tracker:
            # Slowly rotate them in the background
            self.play(
                Rotate(solids, angle=PI/8, axis=UP),
                run_time=tracker.duration, rate_func=linear
            )

        script_2 = "For much of history, math was essentially geometry, in the sense that everything we proved was grounded in geometric intuition."
        with self.voiceover(text=script_2) as tracker:
            self.play(
                Rotate(solids, angle=PI/8, axis=UP),
                run_time=tracker.duration, rate_func=linear
            )

        f_tet = MathTex("V = \\frac{a^3}{6\\sqrt{2}}").next_to(tetrahedron, DOWN)
        f_cub = MathTex("V = a^3").next_to(cube, DOWN)
        f_oct = MathTex("V = \\frac{\\sqrt{2}}{3}a^3").next_to(octahedron, DOWN)
        f_ico = MathTex("V = \\frac{5(3+\\sqrt{5})}{12}a^3").next_to(icosahedron, DOWN)
        f_dod = MathTex("V = \\frac{15+7\\sqrt{5}}{4}a^3").next_to(dodecahedron, DOWN)
        formulas = VGroup(f_tet, f_cub, f_oct, f_ico, f_dod)

        script_3 = "It is not hard to imagine triangles, squares, and circles, and as we study them, we discover hidden properties within these shapes."
        with self.voiceover(text=script_3) as tracker:
            self.play(FadeIn(formulas, lag_ratio=0.2), run_time=2)
            self.wait(max(0, tracker.duration - 2))

        # ==========================================
        # SCENE 2: UNIT RIGHT TRIANGLE & SQRT 2
        # ==========================================
        right_tri = Polygon([0, 0, 0], [2, 0, 0], [0, 2, 0], color=BLUE).move_to(UP * 1)
        lbl_base = MathTex("1").next_to(right_tri, DOWN, buff=0.1)
        lbl_height = MathTex("1").next_to(right_tri, LEFT, buff=0.1)
        lbl_hyp = MathTex(r"\sqrt{2}").move_to(right_tri.get_center() + UR * 0.5)
        tri_group = VGroup(right_tri, lbl_base, lbl_height, lbl_hyp)

        script_4 = "The world of geometry feels natural and intuitive — yet complexity hides even within a simple unit right triangle."
        with self.voiceover(text=script_4) as tracker:
            self.play(FadeOut(solids, formulas), run_time=1)
            self.play(FadeIn(tri_group), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        # Endless decimal expansion logic
        digits_str = "1.414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641572735013846230912297024924836055850737212644121497099935831"
        chunk_size = 28
        digit_chunks = [digits_str[i:i+chunk_size] for i in range(0, len(digits_str), chunk_size)]
        
        decimal_group = VGroup(*[Text(chunk, font_size=24, color=YELLOW) for chunk in digit_chunks])
        decimal_group.arrange(DOWN, aligned_edge=LEFT, buff=0.1).next_to(right_tri, DOWN, buff=0.5)

        script_5 = "The length of its longest side is the square root of two, which is irrational, meaning its decimal expansion is infinite and non-repeating."
        with self.voiceover(text=script_5) as tracker:
            total_chars = sum(len(c) for c in digit_chunks)
            time_per_char = (tracker.duration) / total_chars
            
            for chunk in decimal_group:
                self.play(AddTextLetterByLetter(chunk), run_time=len(chunk.text) * time_per_char, rate_func=linear)

        # ==========================================
        # SCENE 3: CALCULUS & ALGEBRA CIRCLES
        # ==========================================
        self.play(FadeOut(tri_group, decimal_group))

        # Calculus Section (Left)
        calc_circle = Circle(radius=2.5, color=TEAL, fill_opacity=0.1).move_to(LEFT * 3.5 + DOWN * 0.5)
        calc_title = Text("Calculus", font_size=32).next_to(calc_circle, UP)
        
        calc_formulas = VGroup(
            MathTex(r"e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n"),
            MathTex(r"\int_a^b f(x) dx"),
            MathTex(r"\frac{d}{dx} f(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}"),
            MathTex(r"\sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n")
        ).arrange(DOWN, buff=0.3).scale(0.6).move_to(calc_circle.get_center())

        # Algebra Section (Right)
        alg_circle = Circle(radius=2.5, color=PURPLE, fill_opacity=0.1).move_to(RIGHT * 3.5 + DOWN * 0.5)
        alg_title = Text("Algebra", font_size=32).next_to(alg_circle, UP)

        alg_formulas = VGroup(
            MathTex(r"i = \sqrt{-1}"),
            MathTex(r"e^{\pi i} + 1 = 0"),
            MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"),
            MathTex(r"p(z) = a_n z^n + \dots + a_0 = a_n(z-r_1)\dots(z-r_n)")
        ).arrange(DOWN, buff=0.4).scale(0.6).move_to(alg_circle.get_center())

        script_6 = "As math developed, it became further abstracted from our intuitions. With the development of calculus, the concept of points at infinity became commonplace."
        with self.voiceover(text=script_6) as tracker:
            self.play(Create(calc_circle), FadeIn(calc_title), FadeIn(calc_formulas), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        # Solar System Orbit (Above Calculus)
        sun = Dot(color=YELLOW, radius=0.15).move_to(LEFT * 3.5 + UP * 3)
        orbit = Ellipse(width=2.5, height=1, color=DARK_GREY).move_to(sun.get_center())
        planet = Dot(color=BLUE, radius=0.08)
        
        orb_tracker = ValueTracker(0)
        planet.add_updater(lambda m: m.move_to(orbit.point_from_proportion(orb_tracker.get_value() % 1)))
        
        def get_tangent():
            p1 = orbit.point_from_proportion((orb_tracker.get_value() - 0.001) % 1)
            p2 = orbit.point_from_proportion((orb_tracker.get_value() + 0.001) % 1)
            return Line(p1, p2).set_length(1.0).set_color(RED).move_to(planet.get_center())
            
        tangent = always_redraw(get_tangent)
        solar_system = VGroup(orbit, sun, planet, tangent)

        script_7 = "We cannot directly picture an infinite process, yet this framework proved useful for describing the physical world."
        with self.voiceover(text=script_7) as tracker:
            self.play(FadeIn(solar_system), run_time=1)
            self.play(orb_tracker.animate.set_value(1.5), run_time=tracker.duration - 1, rate_func=linear)

        script_8 = "In algebra, negative numbers and eventually imaginary numbers became accepted tools."
        with self.voiceover(text=script_8) as tracker:
            self.play(Create(alg_circle), FadeIn(alg_title), FadeIn(alg_formulas), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        # Atom (Above Algebra)
        nucleus = Dot(color=RED, radius=0.15).move_to(RIGHT * 3.5 + UP * 3)
        orb1 = Ellipse(width=2.0, height=0.5, color=DARK_GREY).move_to(nucleus.get_center()).rotate(PI/4)
        orb2 = Ellipse(width=2.0, height=0.5, color=DARK_GREY).move_to(nucleus.get_center()).rotate(-PI/4)
        
        e1 = Dot(color=YELLOW, radius=0.08)
        e2 = Dot(color=YELLOW, radius=0.08)
        e1_tracker = ValueTracker(0)
        e2_tracker = ValueTracker(0.5)
        
        e1.add_updater(lambda m: m.move_to(orb1.point_from_proportion(e1_tracker.get_value() % 1)))
        e2.add_updater(lambda m: m.move_to(orb2.point_from_proportion(e2_tracker.get_value() % 1)))
        atom = VGroup(nucleus, orb1, orb2, e1, e2)

        script_9 = "All of this broadened the scope of math and made it more powerful — but also harder to grasp intuitively."
        with self.voiceover(text=script_9) as tracker:
            self.play(FadeIn(atom), run_time=1)
            self.play(
                e1_tracker.animate.set_value(3),
                e2_tracker.animate.set_value(3.5),
                orb_tracker.animate.set_value(orb_tracker.get_value() + 1.5), # keep planet moving
                run_time=tracker.duration - 1,
                rate_func=linear
            )

        # ==========================================
        # SCENE 4: 3D TOPOLOGY (MOBIUS STRIP REPLACES KLEIN)
        # ==========================================
        self.play(FadeOut(calc_circle, calc_title, calc_formulas, alg_circle, alg_title, alg_formulas, solar_system, atom))

        def mobius_func(u, v):
            r = 1.5
            x = (r + v * np.cos(u / 2)) * np.cos(u)
            y = (r + v * np.cos(u / 2)) * np.sin(u)
            z = v * np.sin(u / 2)
            return np.array([x, y, z])

        def hyperbolic_saddle(u, v):
            return np.array([u, v, (u**2 - v**2)*0.5])

        torus = Torus(major_radius=1.2, minor_radius=0.4, resolution=(30, 30)).set_style(fill_color=BLUE, fill_opacity=0.7, stroke_color=WHITE, stroke_width=0.5)
        torus.move_to(LEFT * 4.5)
        torus.rotate(PI/4, axis=RIGHT).rotate(PI/6, axis=UP)

        saddle = Surface(hyperbolic_saddle, u_range=[-1.5, 1.5], v_range=[-1.5, 1.5], resolution=(20, 20)).set_style(fill_color=TEAL, fill_opacity=0.7, stroke_color=WHITE, stroke_width=0.5)
        saddle.move_to(ORIGIN)
        saddle.rotate(PI/3, axis=RIGHT).rotate(PI/4, axis=UP)

        mobius = Surface(mobius_func, u_range=[0, 2*PI], v_range=[-0.5, 0.5], resolution=(40, 15)).set_style(fill_color=PURPLE, fill_opacity=0.7, stroke_color=WHITE, stroke_width=0.5)
        mobius.move_to(RIGHT * 4.5)
        mobius.rotate(PI/2, axis=RIGHT).rotate(PI/4, axis=UP)

        script_10 = "And since math had branched into so many different areas, it became difficult to say what math actually was. Analysis looked quite different from group theory, which looked very different to number theory."
        with self.voiceover(text=script_10) as tracker:
            self.play(FadeIn(torus), FadeIn(saddle), FadeIn(mobius), run_time=1.5)
            self.play(
                Rotate(torus, angle=PI/4, axis=UP),
                Rotate(saddle, angle=PI/4, axis=UP),
                Rotate(mobius, angle=PI/4, axis=UP),
                run_time=tracker.duration - 1.5, rate_func=linear
            )

        self.play(FadeOut(torus, saddle, mobius))

        # ==========================================
        # SCENE 5: SYNTAX VS SEMANTICS
        # ==========================================
        script_11 = "In the 19th and early 20th century, mathematicians attempted to ground math in logic."
        with self.voiceover(text=script_11) as tracker:
            self.wait(tracker.duration)

        # Logic Symbols mapped to speech
        f_title = Text("Syntax (Logic)", font_size=40).move_to(syntax_center + UP * 3)
        
        sym_funcs = Text("Functions: f, g, +", font_size=28).move_to(syntax_center + UP * 1.5)
        sym_rels = Text("Relations: <, =", font_size=28).next_to(sym_funcs, DOWN, buff=0.3)
        sym_consts = Text("Constants: 0, 1, e", font_size=28).next_to(sym_rels, DOWN, buff=0.3)
        sym_vars = Text("Variables: x, y, z", font_size=28).next_to(sym_consts, DOWN, buff=0.3)
        sym_quants = Text("Quantifiers: ∀, ∃", font_size=28).next_to(sym_vars, DOWN, buff=0.3)
        sym_bools = Text("Connectives: ∧, ∨, →, ¬", font_size=28).next_to(sym_quants, DOWN, buff=0.3)

        self.play(FadeIn(f_title))

        script_12 = "Frege observed that the act of doing mathematics involved the manipulations of the same basic symbols: functions,"
        with self.voiceover(text=script_12) as tracker:
            self.play(FadeIn(sym_funcs), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_13 = "relations,"
        with self.voiceover(text=script_13) as tracker:
            self.play(FadeIn(sym_rels), run_time=tracker.duration)

        script_14 = "constants,"
        with self.voiceover(text=script_14) as tracker:
            self.play(FadeIn(sym_consts), run_time=tracker.duration)

        script_15 = "variables,"
        with self.voiceover(text=script_15) as tracker:
            self.play(FadeIn(sym_vars), run_time=tracker.duration)

        script_16 = "quantifiers,"
        with self.voiceover(text=script_16) as tracker:
            self.play(FadeIn(sym_quants), run_time=tracker.duration)

        script_17 = "and the boolean connectives of conjunction, disjunction, implication, and negation."
        with self.voiceover(text=script_17) as tracker:
            self.play(FadeIn(sym_bools), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_18 = "This aligns with the syntactic, or formalist, view that math is a game played with meaningless symbols according to fixed rules."
        with self.voiceover(text=script_18) as tracker:
            self.wait(tracker.duration)

        script_19 = "The opposing view is semantic: that there exist pre-existing mathematical structures in some platonic world of forms,"
        with self.voiceover(text=script_19) as tracker:
            self.play(Create(divider), run_time=1)
            
            s_title = Text("Semantics (Structures)", font_size=40).move_to(semantics_center + UP * 3)
            self.play(FadeIn(s_title), run_time=0.5)

            # Move pre-existing solids to the right side
            solids.scale(0.6).arrange_in_grid(rows=2, cols=3, buff=1.0).move_to(semantics_center + DOWN * 0.5)
            self.play(FadeIn(solids), run_time=1)
            self.wait(max(0, tracker.duration - 2.5))

        script_20 = "which our formulas attempt to describe and categorize."
        with self.voiceover(text=script_20) as tracker:
            self.play(Rotate(solids, angle=PI/6, axis=UP), run_time=tracker.duration)