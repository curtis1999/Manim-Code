from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class MathematicalLogicDeepDive(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # ==========================================
        # SETUP: HELPERS & POSITIONS
        # ==========================================
        divider = Line(UP * 4, DOWN * 4, stroke_width=2).set_color(WHITE)
        
        syntax_center = LEFT * 3.5
        semantics_center = RIGHT * 3.5

        def get_function_box(symbol_text):
            rect = Square(side_length=0.8).set_color(WHITE).set_fill(BLACK, 1)
            sign = MathTex(symbol_text, font_size=36).move_to(rect.get_center())
            in_w1 = Line(rect.get_left() + LEFT*0.3 + UP*0.2, rect.get_left() + UP*0.2)
            in_w2 = Line(rect.get_left() + LEFT*0.3 + DOWN*0.2, rect.get_left() + DOWN*0.2)
            out_w = Line(rect.get_right(), rect.get_right() + RIGHT*0.3)
            return VGroup(rect, sign, in_w1, in_w2, out_w)

        # ==========================================
        # SCENE 1: THE FORMULAS (FULL SCREEN, BIGGER)
        # ==========================================
        row1 = VGroup(MathTex("1+2=3"), MathTex("2^3=8"), MathTex("e^{\pi i}=-1")).arrange(RIGHT, buff=1.2)
        row2 = VGroup(MathTex("2^3 < 3^2"), MathTex("\pi > 3.14")).arrange(RIGHT, buff=2.0)
        row3 = VGroup(
            MathTex(r"\forall x \left[\sum_{i=1}^x 2i-1 = x^2\right]"), 
            MathTex(r"\exists y(x+x=y)"), 
            MathTex(r"\forall x [x>4 \to 2^x > x^2]")
        ).arrange(RIGHT, buff=1.0)
        row4 = VGroup(MathTex(r"\forall x \exists y (x < y)"), MathTex(r"\exists y \forall x (x < y)")).arrange(RIGHT, buff=2.0)
        row5 = MathTex(r"\forall \epsilon \exists N \forall m,n > N [\|a_m - a_n\| < \epsilon]")

        all_formulas_full = VGroup(row1, row2, row3, row4, row5).arrange(DOWN, buff=1.5).scale(0.85).move_to(ORIGIN)

        script_1 = "When people think of math, they often think of formulas such as 1+2=3 or e^pii=-1"
        with self.voiceover(text=script_1) as tracker:
            self.play(FadeIn(all_formulas_full, lag_ratio=0.1), run_time=2)
            self.wait(max(0, tracker.duration - 2))

        script_2 = "But from a certain point of view, these are just meaningless strings symbols. They get their meaning when they are interpreted into an appropriate structure."
        with self.voiceover(text=script_2) as tracker:
            self.wait(tracker.duration)

        # ==========================================
        # SCENE 2: 1+2=3 (SPLIT SCREEN)
        # ==========================================
        eq_123 = MathTex("1", "+", "2", "=", "3", font_size=50).move_to(syntax_center + UP*1)
        num_line = NumberLine(x_range=[0, 9, 1], length=6, include_numbers=True, font_size=24).move_to(semantics_center + DOWN*1)
        
        script_3 = "For example, starting simple, 1 plus 2 equals 3 is understood based on the number line."
        with self.voiceover(text=script_3) as tracker:
            self.play(FadeOut(all_formulas_full), FadeIn(divider), FadeIn(eq_123), run_time=1)
            self.play(Create(num_line), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        a_1 = CurvedArrow(eq_123[0].get_top(), num_line.n2p(1)+UP*0.3, angle=-PI/4, color=YELLOW)
        a_2 = CurvedArrow(eq_123[2].get_top(), num_line.n2p(2)+UP*0.3, angle=-PI/4, color=YELLOW)

        script_4 = "The numbers involved get interpreted as we would expect..."
        with self.voiceover(text=script_4) as tracker:
            self.play(Create(a_1), Create(a_2), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        plus_box = get_function_box("+").move_to(semantics_center + UP*1.5)
        a_plus = CurvedArrow(eq_123[1].get_bottom(), plus_box.get_bottom(), angle=PI/4, color=RED)
        
        d_in1 = DashedLine(num_line.n2p(1), plus_box[2].get_left(), color=GREEN)
        d_in2 = DashedLine(num_line.n2p(2), plus_box[3].get_left(), color=GREEN)
        d_out = DashedLine(plus_box[4].get_right(), num_line.n2p(3), color=ORANGE)
        a_3 = CurvedArrow(eq_123[4].get_top(), num_line.n2p(3)+UP*0.3, angle=-PI/4, color=ORANGE)

        script_5 = "then we can interpret the plus symbol as a function which takes in two inputs and has a well-defined output."
        with self.voiceover(text=script_5) as tracker:
            self.play(FadeIn(plus_box), Create(a_plus), run_time=1)
            self.play(Create(d_in1), Create(d_in2), run_time=0.8)
            self.play(Create(d_out), run_time=0.8)
            self.wait(max(0, tracker.duration - 2.6))

        script_6 = "We see that the output of this function is the same as the interpretation of the right-hand side, and so the equality holds."
        with self.voiceover(text=script_6) as tracker:
            self.play(Create(a_3), run_time=1)
            self.play(Indicate(num_line.numbers[3], color=ORANGE, scale_factor=1.5))
            self.wait(max(0, tracker.duration - 2))

        eq_xyz = MathTex("x", "+", "y", "=", "z", font_size=50).move_to(syntax_center + UP*1)
        self.play(
            FadeOut(a_1), FadeOut(a_2), FadeOut(a_3), FadeOut(a_plus),
            FadeOut(plus_box), FadeOut(d_in1), FadeOut(d_in2), FadeOut(d_out),
            ReplacementTransform(eq_123, eq_xyz), run_time=1
        )

        # ==========================================
        # SCENE 3: SET OF TRIPLES
        # ==========================================
        triples_str = [
            r"\mathbb{N}^3 = \{(0,0,0), (0,0,1), (0,1,0), (1,0,0),", 
            r"(0,1,1), (1,1,0), (1,1,1), (0,0,2),",
            r"(0,2,0), (2,0,0), (0,1,2), (0,2,1), \dots\}"
        ]
        triples_tex = VGroup(*[MathTex(s, font_size=36) for s in triples_str]).arrange(DOWN, aligned_edge=LEFT).move_to(syntax_center + DOWN*1)
        
        script_7 = "Note that the formal definition of the interpretation function is the set of triples (a,b,c) such that a+b=c. We can imagine considering the set of all sets of three natural numbers."
        with self.voiceover(text=script_7) as tracker:
            self.play(FadeIn(triples_tex), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        eq_000 = MathTex("0", "+", "0", "=", "0", font_size=50).move_to(syntax_center + UP*1)
        
        script_8 = "Then we check if the first two sum to the third."
        with self.voiceover(text=script_8) as tracker:
            self.play(ReplacementTransform(eq_xyz, eq_000), run_time=1)
            t_box = get_function_box("+").scale(0.8).move_to(semantics_center + UP*1.5)
            t_in1 = DashedLine(num_line.n2p(0), t_box[2].get_left(), color=GREEN)
            t_in2 = DashedLine(num_line.n2p(0), t_box[3].get_left(), color=GREEN)
            t_out = DashedLine(t_box[4].get_right(), num_line.n2p(0), color=ORANGE)
            self.play(FadeIn(t_box), Create(t_in1), Create(t_in2), Create(t_out), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        plus_m = MathTex(r"+^\mathcal{M} = \{(0,0,0), \dots\}", font_size=36).move_to(syntax_center + DOWN*2.8)

        script_9 = "If this happens then we include this set of triples into our addition set."
        with self.voiceover(text=script_9) as tracker:
            self.play(eq_000.animate.set_color(GREEN), triples_tex[0][0][5:12].animate.set_color(GREEN))
            self.play(FadeIn(plus_m), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        eq_001 = MathTex("0", "+", "0", "=", "1", font_size=50).move_to(syntax_center + UP*1)
        
        script_10 = "If they don't, we exclude them. So, formally the plus function is interpreted as this set of triples.  This means that the addition function is a ternary relation --meaning that it is a specific subset of the set of triples of natural numbers-- and so the fact that 1 plus 2 equals 3, reveals some hidden relation between the numbers 1, 2, and 3."
        with self.voiceover(text=script_10) as tracker:
            self.play(ReplacementTransform(eq_000, eq_001), run_time=0.5)
            self.play(eq_001.animate.set_color(RED), triples_tex[0][0][13:20].animate.set_color(RED))
            self.wait(max(0, tracker.duration - 0.5))

        # ==========================================
        # SCENE 4: 2^3 = 8
        # ==========================================
        self.play(FadeOut(triples_tex), FadeOut(plus_m), FadeOut(t_box), FadeOut(t_in1), FadeOut(t_in2), FadeOut(t_out), run_time=0.5)
        
        eq_exp = MathTex("2", "^3", "=", "8", font_size=50).move_to(syntax_center + UP*1)

        script_11 = "Similarly to how 2, 3 and 8 are related, because 2 to the power of 3 equals 8."
        with self.voiceover(text=script_11) as tracker:
            self.play(ReplacementTransform(eq_001, eq_exp), eq_exp.animate.set_color(WHITE), run_time=1)
            e_box = get_function_box("exp").scale(0.8).move_to(semantics_center + UP*1.5)
            e_in1 = DashedLine(num_line.n2p(2), e_box[2].get_left(), color=GREEN)
            e_in2 = DashedLine(num_line.n2p(3), e_box[3].get_left(), color=GREEN)
            e_out = DashedLine(e_box[4].get_right(), num_line.n2p(8), color=ORANGE)
            self.play(FadeIn(e_box), Create(e_in1), Create(e_in2), Create(e_out), run_time=1.5)
            self.play(Indicate(num_line.numbers[8], color=ORANGE, scale_factor=1.5))
            self.wait(max(0, tracker.duration - 3.5))

        # ==========================================
        # SCENE 5: EULER'S IDENTITY (WITH \mathbb{C})
        # ==========================================
        self.play(FadeOut(e_box), FadeOut(e_in1), FadeOut(e_in2), FadeOut(e_out))
        
        eq_euler = MathTex("e", "^{\pi", " i}", "=", "-1", font_size=50).move_to(syntax_center + UP*1)
        
        # Make the plane large enough to comfortably show pi > 3
        c_plane = ComplexPlane(
            x_range=[-4, 4, 1], y_range=[-3, 3, 1], x_length=7, y_length=5.25
        ).move_to(semantics_center + DOWN*0.5).add_coordinates()
        
        c_label = MathTex(r"\mathbb{C}", font_size=50).next_to(c_plane, UP, buff=0.2).shift(RIGHT*2)

        script_12 = "Now, more complicated equations, such as Euler's identity don't make sense in the natural number line, since none of the constants involved in the equation exist there."
        with self.voiceover(text=script_12) as tracker:
            self.play(ReplacementTransform(eq_exp, eq_euler), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_13 = "To understand this equation, we require a more complex structure known as the complex plane."
        with self.voiceover(text=script_13) as tracker:
            self.play(ReplacementTransform(num_line, c_plane), FadeIn(c_label), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        dot_e = Dot(c_plane.n2p(2.718 + 0j), color=YELLOW)
        dot_pi = Dot(c_plane.n2p(3.141 + 0j), color=YELLOW)
        dot_i = Dot(c_plane.n2p(0 + 1j), color=YELLOW)
        dot_neg1 = Dot(c_plane.n2p(-1 + 0j), color=ORANGE)
        
        label_e = MathTex("e").next_to(dot_e, DOWN, buff=0.1).scale(0.6)
        label_pi = MathTex("\pi").next_to(dot_pi, DOWN, buff=0.1).scale(0.6)
        label_i = MathTex("i").next_to(dot_i, LEFT, buff=0.1).scale(0.6)
        
        script_14 = "However, once we have done this, we can evaluate it in essentially the same way as 1 plus 2 equals 3. We just map the constants to their representations in the structure,"
        with self.voiceover(text=script_14) as tracker:
            self.play(FadeIn(dot_e, label_e), FadeIn(dot_pi, label_pi), FadeIn(dot_i, label_i), FadeIn(dot_neg1), run_time=1)
            
            ae1 = CurvedArrow(eq_euler[0].get_top(), dot_e.get_top(), angle=-PI/4, color=YELLOW)
            api = CurvedArrow(eq_euler[1].get_top(), dot_pi.get_top(), angle=-PI/4, color=YELLOW)
            ai = CurvedArrow(eq_euler[2].get_top(), dot_i.get_top(), angle=-PI/4, color=YELLOW)
            aneg1 = CurvedArrow(eq_euler[4].get_top(), dot_neg1.get_top(), angle=-PI/4, color=ORANGE)
            self.play(Create(ae1), Create(api), Create(ai), Create(aneg1), run_time=1.5)
            self.wait(max(0, tracker.duration - 2.5))

        mult_box = get_function_box(r"\times").scale(0.7).move_to(semantics_center + UP * 2.5 + LEFT * 1)
        new_exp_box = get_function_box("exp").scale(0.7).move_to(semantics_center + UP * 2.5 + RIGHT * 1.5)

        script_15 = "and then perform the complex exponentiation function, and we observe that the left hand side evaluates to the same point in the structure as the interpretation of the right hand side."
        with self.voiceover(text=script_15) as tracker:
            self.play(FadeIn(mult_box), FadeIn(new_exp_box), FadeOut(ae1), FadeOut(api), FadeOut(ai), run_time=1)
            
            d_pi = DashedLine(dot_pi.get_center(), mult_box[2].get_left(), color=GREEN)
            d_i = DashedLine(dot_i.get_center(), mult_box[3].get_left(), color=GREEN)
            self.play(Create(d_pi), Create(d_i), run_time=0.8)
            
            d_out_mult = DashedLine(mult_box[4].get_right(), new_exp_box[3].get_left(), color=BLUE_B, path_arc=-PI/4)
            d_e = DashedLine(dot_e.get_center(), new_exp_box[2].get_left(), color=GREEN)
            self.play(Create(d_out_mult), Create(d_e), run_time=0.8)
            
            d_final = DashedLine(new_exp_box[4].get_right(), dot_neg1.get_center(), color=ORANGE, path_arc=PI/4)
            self.play(Create(d_final), run_time=0.8)
            self.play(Indicate(dot_neg1, color=ORANGE, scale_factor=1.5))
            self.wait(max(0, tracker.duration - 3.4))

        euler_circle = Arc(radius=c_plane.x_axis.unit_size, start_angle=0, angle=PI, arc_center=c_plane.n2p(0)).set_color(TEAL)
        
        script_16 = "3 Blue 1 Brown made an excellent video explaining why this equality holds, you can check that video out here."
        with self.voiceover(text=script_16) as tracker:
            self.play(
                FadeOut(aneg1), FadeOut(mult_box), FadeOut(new_exp_box),
                FadeOut(d_pi), FadeOut(d_i), FadeOut(d_out_mult), FadeOut(d_e), FadeOut(d_final),
                run_time=1
            )
            self.play(Create(euler_circle), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        script_17 = "But the takeaway is that mathematicians often have some structure in mind, and they are trying to find the hidden relations between the elements in this structure. Some of the relations are surprising, since e, pi, i and negative 1 have very different definitions, so it's not obvious a-priori that there would be any elegant relation between them. But once we have defined the correct structure and the behaviour of complex exponentiation, we can see why this equation holds."
        with self.voiceover(text=script_17) as tracker:
            self.wait(tracker.duration)

        # ==========================================
        # SCENE 6: FULL SCREEN FORMULAS AGAIN
        # ==========================================
        self.play(
            FadeOut(c_plane), FadeOut(c_label), FadeOut(euler_circle), FadeOut(dot_e), FadeOut(dot_pi), FadeOut(dot_i), FadeOut(dot_neg1),
            FadeOut(label_e), FadeOut(label_pi), FadeOut(label_i), FadeOut(eq_euler), FadeOut(divider)
        )

        all_formulas_full2 = all_formulas_full.copy().move_to(ORIGIN)

        script_18 = "So formulas like these, just tell us the relation between particular elements in the domain.  In first order logic, we can do much more by using quantifiers."
        with self.voiceover(text=script_18) as tracker:
            self.play(FadeIn(all_formulas_full2), run_time=1)
            self.play(all_formulas_full2[0].animate.set_color(YELLOW), all_formulas_full2[1].animate.set_color(YELLOW))
            self.wait(max(0, tracker.duration - 2))

        script_19 = "They simply exert a relation between certain elements. Now, by adding quantifiers, which are these symbols,"
        with self.voiceover(text=script_19) as tracker:
            self.play(all_formulas_full2[0].animate.set_color(WHITE), all_formulas_full2[1].animate.set_color(WHITE))
            
            # Highlight all quantifiers in the grid
            q_highlights = VGroup(
                all_formulas_full2[2][0][0][0:2], all_formulas_full2[2][1][0][0:2], all_formulas_full2[2][2][0][0:2],
                all_formulas_full2[3][0][0][0:2], all_formulas_full2[3][0][0][3:5],
                all_formulas_full2[3][1][0][0:2], all_formulas_full2[3][1][0][3:5],
                all_formulas_full2[4][0][0:2], all_formulas_full2[4][0][3:5], all_formulas_full2[4][0][6:8]
            )
            self.play(q_highlights.animate.set_color(YELLOW), run_time=1)
            self.wait(max(0, tracker.duration - 1))
            
        script_19_b = "we can express properties of every element in a structure, even if that structure is infinite."
        with self.voiceover(text=script_19_b) as tracker:
            self.play(q_highlights.animate.set_color(WHITE), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        # ==========================================
        # SCENE 7: QUANTIFIERS & THE SIGMA EQUATION
        # ==========================================
        num_line_2 = NumberLine(x_range=[0, 9, 1], length=6, include_numbers=True, font_size=24).move_to(semantics_center + DOWN*1)
        eq_quant = MathTex(r"\forall x \left[\sum_{i=1}^x (2i-1) = x^2\right]", font_size=40).move_to(syntax_center + UP*1)

        script_20 = "For example, consider this formula: for all x, the sum from i equals 1 to x of 2i minus 1 equals x squared."
        with self.voiceover(text=script_20) as tracker:
            self.play(FadeOut(all_formulas_full2), FadeIn(divider), FadeIn(eq_quant), FadeIn(num_line_2), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        brace_eq = MathTex("1+3+5+... = n^2", font_size=36).next_to(eq_quant, UP, buff=0.8)
        brace = Brace(brace_eq[0][0:7], DOWN)
        brace_lbl = brace.get_text("(n-times)")

        script_21 = "Which means that if we sum the first n odd numbers, the result will be n squared."
        with self.voiceover(text=script_21) as tracker:
            self.play(FadeIn(brace_eq), GrowFromCenter(brace), FadeIn(brace_lbl), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        # Step-by-step math objects 
        eval_1 = VGroup(
            MathTex(r"\sum_{i=1}^1 (2i-1) = 1^2", font_size=36),
            MathTex(r"2(1)-1 = 1", font_size=36),
            MathTex(r"1 = 1", font_size=36)
        ).arrange(DOWN, buff=0.3).move_to(syntax_center + DOWN*1)

        eval_2 = VGroup(
            MathTex(r"\sum_{i=1}^2 (2i-1) = 2^2", font_size=36),
            MathTex(r"1 + (2(2)-1) = 4", font_size=36),
            MathTex(r"1+3 = 4", font_size=36),
            MathTex(r"4 = 4", font_size=36)
        ).arrange(DOWN, buff=0.3).move_to(syntax_center + DOWN*1)

        script_22 = "This is true in the natural number line, but to evaluate it, technically we would have to check that it holds for every single natural number."
        with self.voiceover(text=script_22) as tracker:
            # Eval 1
            self.play(FadeIn(eval_1[0]), run_time=0.8)
            self.wait(0.5)
            self.play(FadeIn(eval_1[1]), run_time=0.8)
            self.wait(0.5)
            self.play(FadeIn(eval_1[2]), run_time=0.8)
            self.play(eval_1[2].animate.set_color(GREEN), run_time=0.5)
            self.wait(0.5)
            # Clear 1, Eval 2
            self.play(FadeOut(eval_1), run_time=0.5)
            self.play(FadeIn(eval_2[0]), run_time=0.8)
            self.wait(0.5)
            self.play(FadeIn(eval_2[1]), run_time=0.8)
            self.wait(0.5)
            self.play(FadeIn(eval_2[2]), run_time=0.8)
            self.wait(0.5)
            self.play(FadeIn(eval_2[3]), run_time=0.8)
            self.play(eval_2[3].animate.set_color(GREEN), run_time=0.5)
            self.wait(max(0.1, tracker.duration - 10.5))
            self.play(FadeOut(eval_2))

        eq_qt = MathTex(r"\sum_{i=1}^{3\uparrow\uparrow3} (2i-1) = (3\uparrow\uparrow3)^2", font_size=36).move_to(syntax_center + DOWN*1)
        q_mark = Text("?", color=RED, font_size=36).next_to(eq_qt, UP)
        
        script_23 = "But how do we know that at some point just beyond our reach there is not some weird number which breaks the pattern?"
        with self.voiceover(text=script_23) as tracker:
            self.play(FadeIn(eq_qt), FadeIn(q_mark), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        self.play(FadeOut(eq_qt), FadeOut(q_mark), FadeOut(brace_eq), FadeOut(brace), FadeOut(brace_lbl), run_time=1)

        # Induction Proof Formatting
        base_header = Text("Base Case:", font_size=24, color=YELLOW)
        base_step = MathTex(r"\sum_{i=1}^1 (2i-1) = 1^2 \Rightarrow 1=1", font_size=30)
        base_group = VGroup(base_header, base_step).arrange(RIGHT, buff=0.5)

        ind_header = Text("Inductive Step:", font_size=24, color=YELLOW)
        ind_step1 = MathTex(r"\sum_{i=1}^{k+1} (2i-1) = (k+1)^2", font_size=30)
        ind_step2 = MathTex(r"\sum_{i=1}^k (2i-1) + 2(k+1)-1 = k^2+2k+1", font_size=30)
        ind_step3 = MathTex(r"k^2 + 2k + 1 = k^2+2k+1", font_size=30)
        ind_group = VGroup(ind_header, ind_step1, ind_step2, ind_step3).arrange(DOWN, aligned_edge=LEFT)

        proof_group = VGroup(base_group, ind_group).arrange(DOWN, aligned_edge=LEFT, buff=0.8).next_to(eq_quant, DOWN, buff=1.0)

        script_24 = "We prove such equations by induction. We show that it holds for the base case of 1, and then show that if it holds for some arbitrary number k, then it holds for k plus 1."
        with self.voiceover(text=script_24) as tracker:
            self.play(FadeIn(base_group), run_time=1)
            self.wait(0.5)
            self.play(FadeIn(ind_header), FadeIn(ind_step1), run_time=1)
            self.wait(0.5)
            self.play(FadeIn(ind_step2), run_time=1)
            self.wait(0.5)
            self.play(FadeIn(ind_step3), run_time=1)
            self.play(ind_step3.animate.set_color(GREEN), run_time=0.5)
            self.wait(max(0, tracker.duration - 6.0))
        
        script_25 = "Don't worry about the details here, the point is that by using quantifiers, and accepting the principle of mathematical induction, a short string of symbols can tell us something about every element in an infinite structure."
        with self.voiceover(text=script_25) as tracker:
            self.play(FadeOut(proof_group), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        # ==========================================
        # SCENE 8: ORDERS OF LOGIC (CENTERED)
        # ==========================================
        self.play(FadeOut(eq_quant), FadeOut(num_line_2), FadeOut(divider))

        log0 = Text("0th Order Logic (Propositional)", font_size=30).move_to(UP*1.5)
        log1 = Text("1st Order Logic (FOL)", font_size=30).next_to(log0, DOWN, buff=0.8)
        log2 = Text("2nd Order Logic", font_size=30).next_to(log1, DOWN, buff=0.8)
        dots = MathTex(r"\vdots").next_to(log2, DOWN, buff=0.5)
        
        script_26 = "By the way, adding quantifiers to our logic, moves us up from 0'th order logic, aka Propositional logic, into First Order Logic."
        with self.voiceover(text=script_26) as tracker:
            self.play(FadeIn(log0), FadeIn(log1), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_27 = "Propositional logic is too weak to define mathematical structures. For those who are curious, there is also second order logic and even higher-order logics, where we allow so-called higher order quantification, meaning that we can iterate over subsets of the domain."
        with self.voiceover(text=script_27) as tracker:
            # Lined up with "For those who are curious" (approx 3.5s in)
            self.wait(3.5)
            self.play(FadeIn(log2), FadeIn(dots), run_time=1)
            self.wait(max(0, tracker.duration - 4.5))

        logic_list = VGroup(log0, log1, log2, dots)
        self.play(FadeOut(logic_list))
        
        num_line_3 = NumberLine(x_range=[0, 8, 1], length=8, include_numbers=True).move_to(ORIGIN)
        fol_ex = MathTex(r"\forall x P(x)", font_size=50).move_to(UP*2)
        p_fol = MathTex(r"P(0) \land P(1) \land P(2) \land \dots", font_size=36).next_to(num_line_3, DOWN, buff=1)

        script_28 = "In FOL when we write for all x P x, we mean that every element of the structure has the property P, whatever P is. In the natural number line, this means that P of 0 holds, P of 1 holds and so on."
        with self.voiceover(text=script_28) as tracker:
            self.play(FadeIn(num_line_3), FadeIn(fol_ex), run_time=1)
            # Lined up with "In the natural number line..."
            self.wait(5)
            self.play(FadeIn(p_fol), run_time=1)
            self.wait(max(0, tracker.duration - 7))

        self.play(FadeOut(fol_ex), FadeOut(p_fol))

        sol_ex = MathTex(r"\forall X P(X)", font_size=50).move_to(UP*2)
        p_sol = MathTex(r"P(\{1,3,7\}) \land P(\{12,48,128,1080\}) \land \dots", font_size=36).next_to(num_line_3, DOWN, buff=1)

        script_29 = "In SOL we write for all big X P of big X. And this means that P holds for every subset of natural numbers."
        with self.voiceover(text=script_29) as tracker:
            self.play(FadeIn(sol_ex), run_time=1)
            self.play(FadeIn(p_sol), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        script_30 = "This allows us more expressive power, but the notion of logical validity becomes separated from our ability to prove statements. So first order logic sits in a goldilocks zone where it is strong enough to be able to define most of mathematics, and yet not so strong that we lose control over it."
        with self.voiceover(text=script_30) as tracker:
            self.play(FadeOut(sol_ex), FadeOut(p_sol), FadeOut(num_line_3), run_time=1)
            self.play(FadeIn(logic_list), run_time=1)
            # Lined up with "So FOL sits..."
            self.wait(6)
            self.play(log1.animate.set_color(GREEN))
            self.wait(max(0, tracker.duration - 8))

        # ==========================================
        # SCENE 9: ARITHMETICAL HIERARCHY
        # ==========================================
        self.play(FadeOut(logic_list))

        script_31 = "So to recap, in math we have certain formulas which express relations between specific elements in the domain,"
        with self.voiceover(text=script_31) as tracker:
            self.play(FadeIn(all_formulas_full2))
            self.play(all_formulas_full2[0].animate.set_color(YELLOW), all_formulas_full2[1].animate.set_color(YELLOW))
            self.wait(max(0, tracker.duration))

        script_32 = "and we have other formulas which can express properties about entire structures."
        with self.voiceover(text=script_32) as tracker:
            self.play(all_formulas_full2[0].animate.set_color(WHITE), all_formulas_full2[1].animate.set_color(WHITE))
            self.play(all_formulas_full2[2].animate.set_color(YELLOW), all_formulas_full2[3].animate.set_color(YELLOW), all_formulas_full2[4].animate.set_color(YELLOW))
            self.wait(max(0, tracker.duration))

        script_33 = "We can continue to generate increasingly powerful formulas, by alternating quantifiers. This is given by the so-called arithmetic hierarchy."
        with self.voiceover(text=script_33) as tracker:
            self.play(all_formulas_full2[2].animate.set_color(WHITE), all_formulas_full2[3].animate.set_color(WHITE), all_formulas_full2[4].animate.set_color(WHITE))
            self.wait(tracker.duration)

        # Hierarchy Nodes Setup
        sig0 = MathTex(r"\Sigma_0", font_size=36).move_to(DOWN*3)
        sig1 = MathTex(r"\Sigma_1", font_size=36).move_to(LEFT*2.5 + DOWN*1.5)
        pi1 = MathTex(r"\Pi_1", font_size=36).move_to(RIGHT*2.5 + DOWN*1.5)
        sig2 = MathTex(r"\Sigma_2", font_size=36).move_to(LEFT*2.5 + UP*0)
        pi2 = MathTex(r"\Pi_2", font_size=36).move_to(RIGHT*2.5 + UP*0)
        sig3 = MathTex(r"\Sigma_3", font_size=36).move_to(LEFT*2.5 + UP*1.5)
        pi3 = MathTex(r"\Pi_3", font_size=36).move_to(RIGHT*2.5 + UP*1.5)

        script_34 = "At the base, we have the so-called Sigma 0 formulas, which have no quantifiers. These are the simple equations like 1 plus 2 equals 3 and Euler's identity we saw earlier."
        with self.voiceover(text=script_34) as tracker:
            self.play(FadeOut(all_formulas_full2), FadeIn(sig0))
            f_sig0 = MathTex("1+2=3", font_size=40).move_to(UP*3.2)
            self.play(FadeIn(f_sig0))
            self.wait(max(0, tracker.duration - 2))

        script_35 = "Next we have the Sigma 1 and the Pi 1 sentences, which include the existential and the universal formulas."
        with self.voiceover(text=script_35) as tracker:
            l_0s1 = Line(sig0.get_top(), sig1.get_bottom())
            l_0p1 = Line(sig0.get_top(), pi1.get_bottom())
            lbl_s1 = MathTex(r"\exists x P(x)", font_size=20).next_to(sig1, DOWN, buff=0.1)
            lbl_p1 = MathTex(r"\forall x P(x)", font_size=20).next_to(pi1, DOWN, buff=0.1)
            self.play(FadeOut(f_sig0), FadeIn(sig1), FadeIn(pi1), Create(l_0s1), Create(l_0p1), FadeIn(lbl_s1), FadeIn(lbl_p1), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        f_s1 = MathTex(r"\exists y(x+x=y)", font_size=40).move_to(UP*3.2)
        script_36 = "Where an existential formula is just one that starts with an existential quantifier, such as exists y such that x plus x equals y."
        with self.voiceover(text=script_36) as tracker:
            self.play(FadeIn(f_s1), sig1.animate.set_color(GREEN))
            self.wait(max(0, tracker.duration))

        f_p1 = MathTex(r"\forall x[(x+1)^2=x^2+2x+1]", font_size=40).move_to(UP*3.2)
        script_37 = "And a universal formula starts with a universal quantifier"
        with self.voiceover(text=script_37) as tracker:
            self.play(ReplacementTransform(f_s1, f_p1), sig1.animate.set_color(WHITE), pi1.animate.set_color(GREEN))
            self.wait(max(0.1, tracker.duration))

        script_38 = "Moving up the hierarchy, we can obtain more sophisticated formulas, which allow us to describe more complicated structures by alternating the quantifiers."
        with self.voiceover(text=script_38) as tracker:
            l_s1s2 = Line(sig1.get_top(), sig2.get_bottom())
            l_s1p2 = Line(sig1.get_top(), pi2.get_bottom())
            l_p1p2 = Line(pi1.get_top(), pi2.get_bottom())
            l_p1s2 = Line(pi1.get_top(), sig2.get_bottom())
            
            lbl_s2 = MathTex(r"\exists x \forall y P(x,y)", font_size=20).next_to(sig2, DOWN, buff=0.1)
            lbl_p2 = MathTex(r"\forall x \exists y P(x,y)", font_size=20).next_to(pi2, DOWN, buff=0.1)
            
            self.play(
                FadeIn(sig2), FadeIn(pi2), Create(l_s1s2), Create(l_s1p2), Create(l_p1p2), Create(l_p1s2),
                FadeIn(lbl_s2), FadeIn(lbl_p2), pi1.animate.set_color(WHITE), run_time=2
            )
            self.wait(max(0, tracker.duration - 2))

        f_p2 = MathTex(r"\forall x \exists y (x < y)", font_size=40).move_to(UP*3.2)
        script_39 = "The Pi 2 formulas are those which start with a for all block and then an existential block, for example: for all x exists y such that x is less than y. Which is true of the natural numbers, as there are always larger numbers."
        with self.voiceover(text=script_39) as tracker:
            self.play(ReplacementTransform(f_p1, f_p2), pi2.animate.set_color(GREEN))
            self.wait(max(0, tracker.duration))

        f_s2 = MathTex(r"\exists y \forall x (x < y)", font_size=40).move_to(UP*3.2)
        script_40 = "But if we switch the order of the quantifiers, we obtain the Sigma 2 sentences, which go exists then for all, and we obtain exists y for all x, x is less than y, which is not true of the natural numbers. Since a witness to this existential quantifier would be an actually infinite number, as it would be greater than every natural number."
        with self.voiceover(text=script_40) as tracker:
            self.play(ReplacementTransform(f_p2, f_s2), pi2.animate.set_color(WHITE), sig2.animate.set_color(GREEN))
            self.wait(max(0, tracker.duration))

        script_41 = "We can continue in this way. We move up the hierarchy diagonally, by prepending the opposite quantifier to the one which appears first in the lower level."
        with self.voiceover(text=script_41) as tracker:
            self.play(FadeOut(f_s2), sig2.animate.set_color(WHITE))
            l_s2s3 = Line(sig2.get_top(), sig3.get_bottom())
            l_s2p3 = Line(sig2.get_top(), pi3.get_bottom())
            l_p2p3 = Line(pi2.get_top(), pi3.get_bottom())
            l_p2s3 = Line(pi2.get_top(), sig3.get_bottom())
            
            lbl_s3 = MathTex(r"\exists x \forall y \exists z P(x,y,z)", font_size=20).next_to(sig3, DOWN, buff=0.1)
            lbl_p3 = MathTex(r"\forall x \exists y \forall z P(x,y,z)", font_size=20).next_to(pi3, DOWN, buff=0.1)
            
            dots_h1 = MathTex(r"\vdots").next_to(sig3, UP)
            dots_h2 = MathTex(r"\vdots").next_to(pi3, UP)
            self.play(
                FadeIn(sig3), FadeIn(pi3), Create(l_s2s3), Create(l_s2p3), Create(l_p2p3), Create(l_p2s3), 
                FadeIn(lbl_s3), FadeIn(lbl_p3), FadeIn(dots_h1), FadeIn(dots_h2)
            )
            self.wait(max(0, tracker.duration))

        # ==========================================
        # SCENE 10: SENTENCES VS FREE VARIABLES
        # ==========================================
        hierarchy_group = VGroup(
            sig0, sig1, pi1, sig2, pi2, sig3, pi3, l_0s1, l_0p1, lbl_s1, lbl_p1,
            l_s1s2, l_s1p2, l_p1p2, l_p1s2, lbl_s2, lbl_p2, l_s2s3, l_s2p3, l_p2p3, l_p2s3, 
            lbl_s3, lbl_p3, dots_h1, dots_h2
        )
        self.play(FadeOut(hierarchy_group))

        all_formulas_full3 = all_formulas_full.copy().move_to(ORIGIN)

        script_42 = "I will quickly note that we can divide the set of formulas in two different types based on whether a formula contains so-called free variables."
        with self.voiceover(text=script_42) as tracker:
            self.play(FadeIn(all_formulas_full3))
            self.wait(tracker.duration)

        s_1 = MathTex("1+2=3")
        s_3 = MathTex(r"\forall x [(x+1)^2=x^2+2x+1]")
        sentences = VGroup(s_1, s_3).arrange(DOWN, buff=0.8).move_to(LEFT * 2)

        script_43 = "A sentence is a formula without any free variables, which include sentences without any variables at all, such as 1 plus 2 equals 3, or sentences in which all variables appear bound like this one."
        with self.voiceover(text=script_43) as tracker:
            self.play(FadeOut(all_formulas_full3), FadeIn(sentences))
            self.wait(max(0, tracker.duration))
        
        arrow_b1 = CurvedArrow(s_3[0][1:3].get_bottom(), s_3[0][4:5].get_bottom(), angle=PI/2, color=YELLOW, tip_length=0.15)
        arrow_b2 = CurvedArrow(s_3[0][1:3].get_bottom(), s_3[0][11:12].get_bottom(), angle=PI/2, color=YELLOW, tip_length=0.15)
        arrow_b3 = CurvedArrow(s_3[0][1:3].get_bottom(), s_3[0][15:16].get_bottom(), angle=PI/2, color=YELLOW, tip_length=0.15)

        script_44 = "Sentences make a claim which is either true or false when interpreted into a structure."
        with self.voiceover(text=script_44) as tracker:
            self.play(s_3.animate.set_color(YELLOW))
            self.play(Create(arrow_b1), Create(arrow_b2), Create(arrow_b3))
            self.wait(max(0, tracker.duration))

        self.play(FadeOut(sentences), FadeOut(arrow_b1), FadeOut(arrow_b2), FadeOut(arrow_b3))

        self.play(FadeIn(divider))
        
        phi_form = MathTex(r"\varphi(x)", r"\equiv \exists y (y+y=x)", font_size=40).move_to(syntax_center + UP*1)
        phi_form[0].set_color(TEAL)
        num_line_4 = NumberLine(x_range=[0, 8, 1], length=6, include_numbers=True).move_to(semantics_center)

        script_45 = "Non-sentence formulas have free variables, such as exists y such that y plus y equals x, where we see that there is no quantifier to bound the occurrence of x, so we say that x appears free. Such formulas are sometimes true and sometimes false depending on what the variables point to. They are therefore not used to make claims about the properties within a structure, instead they allow us to define certain sets."
        with self.voiceover(text=script_45) as tracker:
            self.play(FadeIn(phi_form))
            self.wait(max(0, tracker.duration))

        set_E = MathTex(r"E=\{x : ", r"\varphi(x)", r" \text{ is true in } \mathbb{N}\}").move_to(syntax_center + DOWN*1)
        set_E[1].set_color(TEAL)

        script_46 = "Since exists y y plus y equals x is true in the natural numbers if and only if the free variable x is instantiated by an even number, right since if we try with the number 3 for example, there is no natural number which can be added to itself to obtain 3. We can define the set E of all such x."
        with self.voiceover(text=script_46) as tracker:
            self.play(FadeIn(num_line_4))
            self.play(FadeIn(set_E))
            
            even_highlights = VGroup(
                num_line_4.numbers[0], num_line_4.numbers[2], num_line_4.numbers[4], 
                num_line_4.numbers[6], num_line_4.numbers[8]
            )
            self.play(even_highlights.animate.set_color(TEAL), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_47 = "So, in this arithmetic hierarchy, we either have sentences which express properties of a given structure or elements within it, or we have formulas which allow us to define certain sets."
        with self.voiceover(text=script_47) as tracker:
            self.play(FadeOut(phi_form), FadeOut(set_E), FadeOut(num_line_4), FadeOut(divider))
            self.play(FadeIn(hierarchy_group))
            self.wait(max(0, tracker.duration))

        script_48 = "As we go up in this hierarchy, we can define more complicated sets, and make more complicated claims about a structure. But what do we mean by a mathematical structure in the first place?"
        with self.voiceover(text=script_48) as tracker:
            self.wait(tracker.duration)

        self.wait(2)