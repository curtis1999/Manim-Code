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

        def get_function_box(symbol_text):
            rect = Square(side_length=0.8).set_color(WHITE).set_fill(BLACK, 1)
            sign = MathTex(symbol_text, font_size=36).move_to(rect.get_center())
            in_w1 = Line(rect.get_left() + LEFT*0.3 + UP*0.2, rect.get_left() + UP*0.2)
            in_w2 = Line(rect.get_left() + LEFT*0.3 + DOWN*0.2, rect.get_left() + DOWN*0.2)
            out_w = Line(rect.get_right(), rect.get_right() + RIGHT*0.3)
            return VGroup(rect, sign, in_w1, in_w2, out_w)

        # Klein Bottle Parametric Equation
        def klein_bottle_func(u, v):
            r = 1.5
            x = (r + np.cos(u/2)*np.sin(v) - np.sin(u/2)*np.sin(2*v)) * np.cos(u)
            y = (r + np.cos(u/2)*np.sin(v) - np.sin(u/2)*np.sin(2*v)) * np.sin(u)
            z = np.sin(u/2)*np.sin(v) + np.cos(u/2)*np.sin(2*v)
            return np.array([x, y, z])

        # Hyperbolic Saddle Parametric Equation
        def hyperbolic_saddle(u, v):
            return np.array([u, v, (u**2 - v**2)*0.5])

        # ==========================================
        # SCENE 1: GEOMETRY & INFINITY
        # ==========================================
        script_1 = "In this video series we will go deep into mathematical logic to try and figure out what math is, and what it's limits are."
        with self.voiceover(text=script_1) as tracker:
            self.wait(tracker.duration)

        tri = Polygon([-1.5, -1, 0], [0.5, -1, 0], [-1.5, 1, 0], color=BLUE).shift(LEFT * 4 + UP * 1)
        pythagoras = MathTex("a^2+b^2=c^2").next_to(tri, DOWN)

        circle = Circle(radius=1.2, color=RED).shift(ORIGIN + UP * 1)
        area_circ = MathTex(r"\text{Area} = \pi r^2").next_to(circle, DOWN)

        cone = Cone(base_radius=1, height=2, direction=DOWN).rotate(PI/2, axis=RIGHT).shift(RIGHT * 4 + UP * 1)
        vol_cone = MathTex(r"\text{Volume} = \frac{1}{3}\pi r^2 h").next_to(cone, DOWN)

        script_2 = "For much of history math was essentially geometry, in the sense that everything we proved was grounded in some form of geometric intuition."
        with self.voiceover(text=script_2) as tracker:
            self.play(FadeIn(tri, pythagoras), FadeIn(circle, area_circ), FadeIn(cone, vol_cone), run_time=2)
            self.wait(max(0, tracker.duration - 2))

        script_3 = "Its not hard to imagine triangles, squares and circles, and as we start to study them, we can start to notice certain patterns, find different ways classify the shapes and we can find certain surprising relations between different shapes."
        with self.voiceover(text=script_3) as tracker:
            self.wait(tracker.duration)

        right_tri = Polygon([0, 0, 0], [2, 0, 0], [0, 2, 0], color=BLUE).move_to(ORIGIN)
        lbl_base = MathTex("1").next_to(right_tri, DOWN, buff=0.1)
        lbl_height = MathTex("1").next_to(right_tri, LEFT, buff=0.1)
        lbl_hyp = MathTex(r"\sqrt{2}").move_to(right_tri.get_center() + UR * 0.5)
        root2_expansion = MathTex(r"\sqrt{2} = 1.41421356237\dots", color=YELLOW).next_to(right_tri, DOWN, buff=1)

        script_4 = "However, infinity is hiding even within a simple triangle, as was shown by the pythagoreans that the square root of two --which is the length of the long side of any unit right angle triangle-- is incommensurable meaning that its decimal expansion is endless."
        with self.voiceover(text=script_4) as tracker:
            self.play(
                FadeOut(circle, area_circ, cone, vol_cone, pythagoras),
                ReplacementTransform(tri, right_tri), 
                run_time=1.5
            )
            self.play(FadeIn(lbl_base, lbl_height, lbl_hyp), run_time=1)
            self.play(Write(root2_expansion), run_time=2)
            self.wait(max(0, tracker.duration - 4.5))

        # ==========================================
        # SCENE 2: ABSTRACTION, PHYSICS & TOPOLOGY
        # ==========================================
        self.play(FadeOut(right_tri, lbl_base, lbl_height, lbl_hyp, root2_expansion))

        # Formulas
        calc_def = MathTex(r"e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n").move_to(LEFT * 3.5 + DOWN * 1)
        alg_def = MathTex(r"\sqrt{-1} = i").move_to(RIGHT * 3.5 + DOWN * 1)

        # Solar System Orbit
        sun = Dot(color=YELLOW, radius=0.2).move_to(LEFT * 3.5 + UP * 1.5)
        orbit = Ellipse(width=3.5, height=2, color=DARK_GREY).move_to(sun.get_center())
        planet = Dot(color=BLUE, radius=0.1)
        
        orb_tracker = ValueTracker(0)
        planet.add_updater(lambda m: m.move_to(orbit.point_from_proportion(orb_tracker.get_value() % 1)))
        
        def get_tangent():
            p1 = orbit.point_from_proportion((orb_tracker.get_value() - 0.001) % 1)
            p2 = orbit.point_from_proportion((orb_tracker.get_value() + 0.001) % 1)
            return Line(p1, p2).set_length(1.5).set_color(RED).move_to(planet.get_center())
            
        tangent = always_redraw(get_tangent)
        solar_system = VGroup(orbit, sun, planet, tangent)

        # Atom
        nucleus = Dot(color=RED, radius=0.15).move_to(RIGHT * 3.5 + UP * 1.5)
        orb1 = Ellipse(width=2.5, height=0.6, color=DARK_GREY).move_to(nucleus.get_center()).rotate(PI/4)
        orb2 = Ellipse(width=2.5, height=0.6, color=DARK_GREY).move_to(nucleus.get_center()).rotate(-PI/4)
        
        e1 = Dot(color=YELLOW, radius=0.08)
        e2 = Dot(color=YELLOW, radius=0.08)
        e1_tracker = ValueTracker(0)
        e2_tracker = ValueTracker(0.5)
        
        e1.add_updater(lambda m: m.move_to(orb1.point_from_proportion(e1_tracker.get_value() % 1)))
        e2.add_updater(lambda m: m.move_to(orb2.point_from_proportion(e2_tracker.get_value() % 1)))
        atom = VGroup(nucleus, orb1, orb2, e1, e2)

        script_5 = "Allowing more abstract ideas into mathematics broadened the scope of math, and made it more applicable in the real world. But this came at the cost of making math harder to wrap our heads around."
        with self.voiceover(text=script_5) as tracker:
            self.play(FadeIn(calc_def), FadeIn(alg_def), run_time=1)
            self.play(FadeIn(solar_system), FadeIn(atom), run_time=1)
            
            # Animate the orbits during the voiceover
            self.play(
                orb_tracker.animate.set_value(1.5),
                e1_tracker.animate.set_value(3),
                e2_tracker.animate.set_value(3.5),
                run_time=tracker.duration - 2,
                rate_func=linear
            )

        self.play(FadeOut(calc_def, alg_def, solar_system, atom))

        # 3D Topology Surfaces
        torus = Torus(major_radius=1.2, minor_radius=0.4, resolution=(30, 30)).set_style(fill_color=BLUE, fill_opacity=0.7, stroke_color=WHITE, stroke_width=0.5)
        torus.move_to(LEFT * 4.5)
        torus.rotate(PI/4, axis=RIGHT).rotate(PI/6, axis=UP)

        saddle = Surface(hyperbolic_saddle, u_range=[-1.5, 1.5], v_range=[-1.5, 1.5], resolution=(20, 20)).set_style(fill_color=TEAL, fill_opacity=0.7, stroke_color=WHITE, stroke_width=0.5)
        saddle.move_to(ORIGIN)
        saddle.rotate(PI/3, axis=RIGHT).rotate(PI/4, axis=UP)


        script_6 = "For now I will just say that in the 1800's mathematics had developed far beyond the intuitive realm of geometry."
        with self.voiceover(text=script_6) as tracker:
            self.play(FadeIn(torus), FadeIn(saddle), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        script_8 = "However, math had branched out in so many different ways, that it was hard to pin down what math was. This prompted people in the 1800's to attempt to ground mathematics in the logic."
        with self.voiceover(text=script_8) as tracker:
            # Gently rotate them to show off the 3D depth
            self.play(
                Rotate(torus, angle=PI/4, axis=UP),
                Rotate(saddle, angle=PI/4, axis=UP),
                run_time=tracker.duration,
                rate_func=linear
            )

        self.play(FadeOut(torus, saddle))

        # ==========================================
        # SCENE 3: 1+2=3 INTERPRETATION
        # ==========================================
        eq_123 = MathTex("1", "+", "2", "=", "3", font_size=50).move_to(syntax_center + UP*1)
        num_line_1 = NumberLine(x_range=[0, 9, 1], length=6, include_numbers=True, font_size=24).move_to(semantics_center + DOWN*1)

        script_9 = "To understand this, let us return to the easy stuff and consider 1+2=3. When viewed in one way, this is just an arbitrary string of five symbols."
        with self.voiceover(text=script_9) as tracker:
            self.play(FadeIn(divider), FadeIn(eq_123), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        a_1 = CurvedArrow(eq_123[0].get_top(), num_line_1.n2p(1)+UP*0.3, angle=-PI/4, color=YELLOW)
        a_2 = CurvedArrow(eq_123[2].get_top(), num_line_1.n2p(2)+UP*0.3, angle=-PI/4, color=YELLOW)
        a_3 = CurvedArrow(eq_123[4].get_top(), num_line_1.n2p(3)+UP*0.3, angle=-PI/4, color=ORANGE)

        script_10 = "It get's its meaning when interpreted in a structure like the natural number line, where the numbers get interpreted as we expect."
        with self.voiceover(text=script_10) as tracker:
            self.play(Create(num_line_1), run_time=1)
            self.play(Create(a_1), Create(a_2), Create(a_3), run_time=1.5)
            self.wait(max(0, tracker.duration - 2.5))

        plus_box = get_function_box("+").move_to(semantics_center + UP*1.5)
        a_plus = CurvedArrow(eq_123[1].get_bottom(), plus_box.get_bottom(), angle=PI/4, color=RED)
        d_in1 = DashedLine(num_line_1.n2p(1), plus_box[2].get_left(), color=GREEN)
        d_in2 = DashedLine(num_line_1.n2p(2), plus_box[3].get_left(), color=GREEN)
        d_out = DashedLine(plus_box[4].get_right(), num_line_1.n2p(3), color=ORANGE)

        script_11 = "The plus sign can be interpreted as a function --which we can see as a computer program-- which takes in two inputs and has a well-defined output."
        with self.voiceover(text=script_11) as tracker:
            self.play(FadeIn(plus_box), Create(a_plus), run_time=1)
            self.play(Create(d_in1), Create(d_in2), Create(d_out), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        script_12 = "The equality symbol just checks that the two sides of the equation map to this same element in the line, so we say that the equation holds."
        with self.voiceover(text=script_12) as tracker:
            self.play(Indicate(num_line_1.numbers[3], color=ORANGE, scale_factor=1.5))
            self.wait(max(0, tracker.duration - 1))

        # ==========================================
        # SCENE 4: EULER'S IDENTITY
        # ==========================================
        self.play(FadeOut(a_1, a_2, a_3, a_plus, plus_box, d_in1, d_in2, d_out))

        eq_euler = MathTex("e", "^{\pi", " i}", "=", "-1", font_size=50).move_to(syntax_center + UP*1)
        c_plane = ComplexPlane(x_range=[-4, 4, 1], y_range=[-3, 3, 1], x_length=7, y_length=5).move_to(semantics_center + DOWN*0.5).add_coordinates()
        
        script_13 = "Now, if we consider a more complicated equation such as Euler's identity, we see that this equation is meaningless in the natural number line, since the intended interpretations of each of the constants involved do not exist in the natural number line."
        with self.voiceover(text=script_13) as tracker:
            self.play(ReplacementTransform(eq_123, eq_euler), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_14 = "To understand this equation, we require a more complex structure known as the complex plane."
        with self.voiceover(text=script_14) as tracker:
            self.play(ReplacementTransform(num_line_1, c_plane), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        dot_e = Dot(c_plane.n2p(2.718 + 0j), color=YELLOW)
        dot_pi = Dot(c_plane.n2p(3.141 + 0j), color=YELLOW)
        dot_i = Dot(c_plane.n2p(0 + 1j), color=YELLOW)
        dot_neg1 = Dot(c_plane.n2p(-1 + 0j), color=ORANGE)

        script_15 = "However, once we have done this, we can evaluate it in the same way as 1+2=3. We just have map the constants to their representations in the structure,"
        with self.voiceover(text=script_15) as tracker:
            self.play(FadeIn(dot_e, dot_pi, dot_i, dot_neg1), run_time=1)
            ae1 = CurvedArrow(eq_euler[0].get_top(), dot_e.get_top(), angle=-PI/4, color=YELLOW)
            api = CurvedArrow(eq_euler[1].get_top(), dot_pi.get_top(), angle=-PI/4, color=YELLOW)
            ai = CurvedArrow(eq_euler[2].get_top(), dot_i.get_top(), angle=-PI/4, color=YELLOW)
            aneg1 = CurvedArrow(eq_euler[4].get_top(), dot_neg1.get_top(), angle=-PI/4, color=ORANGE)
            self.play(Create(ae1), Create(api), Create(ai), Create(aneg1), run_time=1.5)
            self.wait(max(0, tracker.duration - 2.5))

        mult_box = get_function_box(r"\times").scale(0.7).move_to(semantics_center + UP * 2.5 + LEFT * 1)
        new_exp_box = get_function_box("exp").scale(0.7).move_to(semantics_center + UP * 2.5 + RIGHT * 1.5)

        script_16 = "and then perform the complex exponentiations function, and we can observe that the left side hand side evaluates to the same point in the structure as the interpretation of the right hand side."
        with self.voiceover(text=script_16) as tracker:
            self.play(FadeIn(mult_box), FadeIn(new_exp_box), FadeOut(ae1), FadeOut(api), FadeOut(ai), run_time=1)
            
            d_pi = DashedLine(dot_pi.get_center(), mult_box[2].get_left(), color=GREEN)
            d_i = DashedLine(dot_i.get_center(), mult_box[3].get_left(), color=GREEN)
            d_out_mult = DashedLine(mult_box[4].get_right(), new_exp_box[3].get_left(), color=BLUE_B, path_arc=-PI/4)
            d_e = DashedLine(dot_e.get_center(), new_exp_box[2].get_left(), color=GREEN)
            d_final = DashedLine(new_exp_box[4].get_right(), dot_neg1.get_center(), color=ORANGE, path_arc=PI/4)
            
            self.play(Create(d_pi), Create(d_i), run_time=0.5)
            self.play(Create(d_out_mult), Create(d_e), run_time=0.5)
            self.play(Create(d_final), run_time=0.5)
            
            self.play(Indicate(dot_neg1, color=ORANGE, scale_factor=1.5))
            self.wait(max(0, tracker.duration - 2.5))

        euler_circle = Arc(radius=c_plane.x_axis.unit_size, start_angle=0, angle=PI, arc_center=c_plane.n2p(0)).set_color(TEAL)

        script_17 = "3 Blue 1 Brown made an excellent video explaining why this equality holds --you can check that video out here--."
        with self.voiceover(text=script_17) as tracker:
            self.play(
                FadeOut(aneg1, mult_box, new_exp_box, d_pi, d_i, d_out_mult, d_e, d_final),
                run_time=1
            )
            self.play(Create(euler_circle), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        # ==========================================
        # SCENE 5: LOGICIAN'S POV (FORMULAS)
        # ==========================================
        self.play(FadeOut(c_plane, euler_circle, dot_e, dot_pi, dot_i, dot_neg1, divider, eq_euler))

        eq_123_center = MathTex("1+2=3", font_size=60).move_to(LEFT * 2)
        eq_euler_center = MathTex("e^{\pi i} = -1", font_size=60).move_to(RIGHT * 2)

        script_18 = "But from the point of view of a logician, both of these formulas are the simplest possible. They are at the bottom of the complexity hierarchy."
        with self.voiceover(text=script_18) as tracker:
            self.play(FadeIn(eq_123_center), FadeIn(eq_euler_center), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        # ==========================================
        # SCENE 6: QUANTIFIERS
        # ==========================================
        self.play(FadeOut(eq_123_center, eq_euler_center))

        q_forall = MathTex(r"\forall", font_size=100, color=TEAL).move_to(LEFT * 2 + UP * 0.5)
        lbl_forall = Text("For all", font_size=36).next_to(q_forall, DOWN)
        
        q_exists = MathTex(r"\exists", font_size=100, color=ORANGE).move_to(RIGHT * 2 + UP * 0.5)
        lbl_exists = Text("Exists", font_size=36).next_to(q_exists, DOWN)

        script_19 = "Using quantifiers, which are these symbols and are read as for all, and exists,"
        with self.voiceover(text=script_19) as tracker:
            self.play(FadeIn(q_forall, shift=UP), FadeIn(q_exists, shift=UP), run_time=1)
            self.play(FadeIn(lbl_forall), FadeIn(lbl_exists), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        # ==========================================
        # SCENE 7: SUM OF ODDS (SPLIT SCREEN)
        # ==========================================
        self.play(FadeOut(q_forall, q_exists, lbl_forall, lbl_exists))

        eq_quant = MathTex(r"\forall n \left[\sum_{i=1}^n (2i-1) = n^2\right]", font_size=40).move_to(syntax_center + UP*1)
        brace_eq = MathTex("1+3+5+\dots = n^2", font_size=36).next_to(eq_quant, UP, buff=0.8)
        brace = Brace(brace_eq[0][0:7], DOWN)
        brace_lbl = brace.get_text("(n-times)")
        
        num_line_2 = NumberLine(x_range=[0, 9, 1], length=6, include_numbers=True, font_size=24).move_to(semantics_center + UP*1.5)

        script_20 = "We can create more complicated formulas using quantifiers. For example, consider this equation, which states that the sum of the first n odd numbers is equal to n-squared. Meaning that 1 plus 3 plus 5 plus dot dot dot n-times, then it is equal to n squared."
        with self.voiceover(text=script_20) as tracker:
            self.play(FadeIn(divider), FadeIn(eq_quant), FadeIn(num_line_2), run_time=1)
            self.play(FadeIn(brace_eq), GrowFromCenter(brace), FadeIn(brace_lbl), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        script_21 = "This is some random pattern which one notices if one looks for patterns in the natural numbers for long enough. We can convince ourselves that it is true by going through each possible value of n."
        with self.voiceover(text=script_21) as tracker:
            self.wait(tracker.duration)

        evals = VGroup(
            MathTex(r"1 = 1^2", font_size=36),
            MathTex(r"1+3 = 2^2", font_size=36),
            MathTex(r"1+3+5 = 3^2", font_size=36)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(eq_quant, DOWN, buff=1.0)

        grid_start = semantics_center + DOWN * 1.5 + LEFT * 0.5
        s = 0.5 
        
        sq_1 = Square(side_length=s, color=YELLOW, fill_opacity=0.7).move_to(grid_start)
        
        script_22 = "Since one is equal to 1 squared."
        with self.voiceover(text=script_22) as tracker:
            self.play(FadeIn(evals[0]), FadeIn(sq_1, scale=0.5), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        sq_2_1 = Square(side_length=s, color=BLUE, fill_opacity=0.7).move_to(grid_start + RIGHT*s)
        sq_2_2 = Square(side_length=s, color=BLUE, fill_opacity=0.7).move_to(grid_start + UP*s)
        sq_2_3 = Square(side_length=s, color=BLUE, fill_opacity=0.7).move_to(grid_start + RIGHT*s + UP*s)
        group_n2 = VGroup(sq_2_1, sq_2_2, sq_2_3)

        script_23 = "1 plus 3 is equal to 2 squared,"
        with self.voiceover(text=script_23) as tracker:
            self.play(FadeIn(evals[1]), FadeIn(group_n2, shift=DL*0.2), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        group_n3 = VGroup()
        for pos in [(2,0), (2,1), (2,2), (1,2), (0,2)]:
            sq = Square(side_length=s, color=RED, fill_opacity=0.7).move_to(grid_start + RIGHT*pos[0]*s + UP*pos[1]*s)
            group_n3.add(sq)

        script_24 = "1 plus 3 plus 5 is equal to 3 squared etc."
        with self.voiceover(text=script_24) as tracker:
            self.play(FadeIn(evals[2]), FadeIn(group_n3, shift=DL*0.2), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        eq_qt = MathTex(r"\sum_{i=1}^{3\uparrow\uparrow3} (2i-1) = (3\uparrow\uparrow3)^2", font_size=32).next_to(evals, DOWN, buff=0.8)
        q_mark = Text("?", color=RED, font_size=32).next_to(eq_qt, RIGHT)

        script_25 = "It seems to always hold, but how do we know that there is not some weird number, just beyond our grasp which breaks this pattern?"
        with self.voiceover(text=script_25) as tracker:
            self.play(FadeIn(eq_qt), FadeIn(q_mark), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        # ==========================================
        # SCENE 8: INDUCTION TEXT
        # ==========================================
        script_26 = "Well, to evaluate a formula such as this one, we use the principle of mathematical induction."
        with self.voiceover(text=script_26) as tracker:
            self.play(FadeOut(evals, eq_qt, q_mark), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        base_case = MathTex(r"\text{BASE CASE: } 1^2 = 1", font_size=32, color=GREEN).next_to(eq_quant, DOWN, buff=1).align_to(eq_quant, LEFT)
        
        script_27 = "Meaning that we check if it holds for n equals 1,"
        with self.voiceover(text=script_27) as tracker:
            self.play(FadeIn(base_case, shift=LEFT), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        ind_step = MathTex(
            r"\text{INDUCTIVE STEP:}",
            r"\text{Assuming } 1+3+\dots+(2k-1) = k^2", 
            r"\text{then } 1+3+\dots+(2k+1) = (k+1)^2", 
            font_size=28, color=YELLOW
        ).arrange(DOWN, aligned_edge=LEFT).next_to(base_case, DOWN, buff=0.6).align_to(base_case, LEFT)

        script_28 = "and check that if it holds for k, then it holds for k plus 1."
        with self.voiceover(text=script_28) as tracker:
            self.play(FadeIn(ind_step, lag_ratio=0.2), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        # ==========================================
        # SCENE 9: 3D DOMINOES
        # ==========================================
        self.play(
            FadeOut(divider, num_line_2, sq_1, group_n2, group_n3, base_case, ind_step, eq_quant, brace_eq, brace, brace_lbl)
        )

        self.move_camera(phi=65 * DEGREES, theta=-110 * DEGREES, run_time=1.5)

        dominoes = VGroup()
        for t in np.linspace(0, 4, 35):
            x = 3 * t - 4 
            y = 1.5 * np.sin(1.2 * t) 
            
            dom = Prism(dimensions=[0.2, 0.8, 1.5])
            dom.set_color(DARK_GREY).set_opacity(1)
            
            dx = 3
            dy = 1.5 * 1.2 * np.cos(1.2 * t)
            angle = np.arctan2(dy, dx)
            
            dom.rotate(angle, axis=OUT)
            dom.move_to([x, y, 0.75])
            dominoes.add(dom)

        script_29 = "This can be seen using dominoes."
        with self.voiceover(text=script_29) as tracker:
            self.play(FadeIn(dominoes, lag_ratio=0.05), run_time=2)
            self.wait(max(0, tracker.duration - 2))

        script_30 = "I will now say, if we know that we will push the first domino over,"
        with self.voiceover(text=script_30) as tracker:
            # Add an arrow pointing into the first domino
            push_arrow = Arrow3D(
                start=dominoes[0].get_center() + LEFT*1.5 + UP*0.5, 
                end=dominoes[0].get_center() + LEFT*0.2, 
                color=RED,
                thickness=0.03
            )
            self.play(Create(push_arrow), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_31 = "and we know that given any domino,"
        with self.voiceover(text=script_31) as tracker:
            self.wait(tracker.duration)

        mid_idx = 10
        highlight_dom = dominoes[mid_idx]
        next_dom = dominoes[mid_idx + 1]

        script_32 = "if it falls over, then the next domino is guaranteed to fall as well,"
        with self.voiceover(text=script_32) as tracker:
            self.play(highlight_dom.animate.set_color(YELLOW), run_time=0.5)
            
            fall_arrow = Arrow3D(
                start=highlight_dom.get_center() + UP*1.2, 
                end=next_dom.get_center() + UP*0.8, 
                color=ORANGE,
                thickness=0.03
            )
            self.play(Create(fall_arrow), run_time=1)
            self.wait(max(0, tracker.duration - 1.5))

        script_33 = "then we can conclude that every domino will eventually fall, even if there are infinitely many."
        with self.voiceover(text=script_33) as tracker:
            self.play(FadeOut(fall_arrow), FadeOut(push_arrow))
            # Highlight ALL dominoes to show they all eventually fall
            cascade = [dominoes[i].animate.set_color(YELLOW) for i in range(len(dominoes))]
            self.play(AnimationGroup(*cascade, lag_ratio=0.1), run_time=3)
            self.wait(max(0, tracker.duration - 3))