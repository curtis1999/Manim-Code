from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class TransfiniteUniverse(VoiceoverScene):
    def construct(self):
        # Setup voiceover service
        self.set_speech_service(RecorderService(transcription_model=None))

        # --- PART 1: POWER SET ITERATIONS WITH AXIOMS ---
        ax_infinity = MathTex(r"\text{Infinity: } \exists x (\emptyset \in x \land \forall y \in x (y \cup \{y\} \in x))").scale(0.7).to_edge(UP)
        ax_powerset = MathTex(r"\text{Power Set: } \forall x \exists y \forall z (\forall w\in z (w \in z \rightarrow w\in y))").scale(0.7).next_to(ax_infinity, DOWN, buff=0.2)
        
        pow_1 = MathTex(r"|\omega| < |\mathcal{P}(\omega)|", font_size=48).shift(DOWN*1)

        with self.voiceover(text="Meaning that if we accept the axiom of infinity, which essentially just states that omega exists,") as tracker:
            self.play(Write(ax_infinity))
            
        with self.voiceover(text="then by the power set axiom,") as tracker:
            self.play(Write(ax_powerset))
            
        with self.voiceover(text="the power set of omega exists and is larger than omega.") as tracker:
            self.play(Write(pow_1))

        with self.voiceover(text="But then we can take the power set of the power set of omega, resulting in a new larger infinity.") as tracker:
            pow_2 = MathTex(r"< |\mathcal{P}(\mathcal{P}(\omega))|", font_size=48).next_to(pow_1, RIGHT)
            self.play(pow_1.animate.shift(LEFT*2))
            pow_2.next_to(pow_1, RIGHT)
            self.play(Write(pow_2))
            
            pow_3 = MathTex(r"< |\mathcal{P}(\mathcal{P}(\mathcal{P}(\omega)))|", font_size=48).next_to(pow_2, RIGHT)
            self.play(VGroup(pow_1, pow_2).animate.shift(LEFT*3))
            pow_3.next_to(pow_2, RIGHT)
            self.play(Write(pow_3))
            
            dots = MathTex(r"< \dots", font_size=48).next_to(pow_3, RIGHT)
            self.play(Write(dots))

        # --- PART 2: RETURNING TO THE UNIVERSE & AXIOMS ---
        with self.voiceover(text="And we can repeat this as many times as we like.") as tracker:
            self.play(*[FadeOut(m) for m in self.mobjects])
            
        with self.voiceover(text="So, returning the Universe of sets which we had, let's simplify by representing the ordinals using numbers.") as tracker:
            # Original hierarchy with empty sets
            v0_orig = MathTex(r"\emptyset").move_to(DOWN * 3)
            v1_orig = MathTex(r"\{\emptyset\}").move_to(DOWN * 2)
            v2_orig = MathTex(r"\{\emptyset, \{\emptyset\}\}").move_to(DOWN * 1)
            v3_orig = MathTex(r"\{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}, \{\{\emptyset\}\}\}").scale(0.85).move_to(ORIGIN)
            v4_orig = MathTex(r"\{\dots, \{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}\}, \dots\}").scale(0.85).move_to(UP * 1)
            v5_orig = MathTex(r"\{\dots, \{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}, \{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}\}\}, \dots\}").scale(0.65).move_to(UP * 2)
            v_dots_top = MathTex(r"\vdots").move_to(UP * 2.8)
            
            left_line = Line(v0_orig.get_center() + DOWN*0.5, v_dots_top.get_center() + LEFT*4.5 + UP*0.5, color=GREEN)
            right_line = Line(v0_orig.get_center() + DOWN*0.5, v_dots_top.get_center() + RIGHT*4.5 + UP*0.5, color=GREEN)
            
            # Dashed line and label for V_omega
            v_omega_dashed = DashedLine(left_line.get_end(), right_line.get_end(), color=GREEN)
            v_omega_label = MathTex(r"V_\omega", color=GREEN).next_to(v_omega_dashed, LEFT, buff=0.2)
            
            self.play(
                FadeIn(v0_orig), FadeIn(v1_orig), FadeIn(v2_orig), 
                FadeIn(v3_orig), FadeIn(v4_orig), FadeIn(v5_orig), 
                FadeIn(v_dots_top), Create(left_line), Create(right_line), 
                Create(v_omega_dashed), FadeIn(v_omega_label), run_time=tracker.duration * 0.4
            )
            
            # Number representations
            v0_num = MathTex(r"0").move_to(v0_orig)
            v1_num = MathTex(r"\{0\}").move_to(v1_orig)
            v2_num = MathTex(r"\{0, 1\}").move_to(v2_orig)
            v3_num = MathTex(r"\dots\{0, 1, 2\}\dots").move_to(v3_orig)
            v4_num = MathTex(r"\dots\{0, 1, 2, 3\}\dots").move_to(v4_orig)
            v5_num = MathTex(r"\dots\{0, 1, 2, 3, 4 \}\dots").move_to(v5_orig)
            
            self.play(
                Transform(v0_orig, v0_num), Transform(v1_orig, v1_num),
                Transform(v2_orig, v2_num), Transform(v3_orig, v3_num),
                Transform(v4_orig, v4_num), Transform(v5_orig, v5_num),
                run_time=tracker.duration * 0.6
            )
            
            hierarchy_group = VGroup(
                v0_orig, v1_orig, v2_orig, v3_orig, v4_orig, v5_orig, 
                v_dots_top, left_line, right_line, v_omega_dashed, v_omega_label
            )

        with self.voiceover(text="Recall that each level of the hierarchy is obtained by taking the power set of the previous level.  So, now that we are equipped with the axiom of infinity, we may take the power set more than omega many times") as tracker:
            # --- ZFC Axioms on the left ---
            ax_texts = [
                r"\text{Existence: } \exists x \forall y (y \notin x)",
                r"\text{Extensionality: } \forall x \forall y (x=y \leftrightarrow \forall z (z\in x\leftrightarrow z \in y))",
                r"\text{Pairing: } \forall x \forall y \exists z (x\in z\land y\in z)",
                r"\text{Union: } \forall x \exists y \forall z (z\in y \leftrightarrow \exists w \in x (z\in w))",
                r"\text{Power Set: } \forall x \exists y \forall z (\forall w\in z (w \in z \rightarrow w\in y))",
                r"\text{Replacement: } \forall x \in a \exists! y \varphi(x, y) \rightarrow \exists z \forall x \in a \exists y \in z \varphi(x, y)",
                r"\text{Separation: } \forall x \exists y \forall z (z \in y \leftrightarrow z \in x \land \varphi(z))",
                r"\text{Foundation: } \forall x (x \neq \emptyset \rightarrow \exists y \in x (x \cap y = \emptyset))",
                r"\text{Choice: } \forall X (\emptyset \notin X \rightarrow \exists f: X \rightarrow \cup X \land \forall Y \in X(f(Y)\in Y))",
                r"\text{Infinity: } \exists x (\emptyset \in x \land \forall y \in x (y \cup \{y\} \in x))"
            ]
            ax_group = VGroup(*[MathTex(formula).scale(0.45) for formula in ax_texts])
            ax_group.arrange(UP, aligned_edge=LEFT, buff=0.25).to_edge(LEFT)
            
            self.play(
                hierarchy_group.animate.scale(0.6).to_edge(RIGHT).shift(DOWN * 0.5),
                FadeIn(ax_group)
            )
            

        with self.voiceover(text="This means that we are now performing so-called transfinite recursion. Again, many mathematicians, namely those with constructivist intuitions about mathematics, don't believe in such constructions, but let's just see how far this idea can go, because it does lead to interesting places.") as tracker:
            self.wait(tracker.duration)

        with self.voiceover(text="So we take the power set of V omega to obtain V_omega+1.  Since V omega has omega many elements, V omega +1 has 2^omega many elements. So this slice of the hierarchy has continuum many sets in it.") as tracker:
            l_start = left_line.get_start()
            l_dir = left_line.get_vector()
            r_start = right_line.get_start()
            r_dir = right_line.get_vector()

            # Extending upward without a horizontal cap, just the side lines
            new_left_line = Line(l_start, l_start + l_dir * 1.25, color=GREEN)
            new_right_line = Line(r_start, r_start + r_dir * 1.25, color=GREEN)
                        
            # New dashed line and label for V_omega+1
            v_omega_plus_1_dashed = DashedLine(new_left_line.get_end(), new_right_line.get_end(), color=YELLOW)
            v_omega_plus_1_label = MathTex(r"V_{\omega+1}", font_size=28, color=YELLOW).next_to(v_omega_plus_1_dashed, LEFT, buff=0.2)
                        
            center_pt = (new_left_line.get_end() + new_right_line.get_end()) / 2
            center_highlight = MathTex(r"\dots\{0, 1, 2, \dots, \omega\}\dots", font_size=32, color=WHITE).move_to(center_pt + DOWN*0.2)
                        
            self.play(
                Transform(left_line, new_left_line), 
                Transform(right_line, new_right_line),
                Create(v_omega_plus_1_dashed),
                Write(v_omega_plus_1_label),
                Write(center_highlight)
            )
            
            continuum_brace = Brace(v_omega_plus_1_dashed, UP, color=YELLOW)
            continuum_label = continuum_brace.get_tex(r"2^{\aleph_0} = \mathfrak{c}").set_color(YELLOW).scale(0.8)
            self.play(Create(continuum_brace), Write(continuum_label))
            

        with self.voiceover(text="Now if we look at the ordinal at this level, which is just omega+1, it is just the set of all natural numbers with omega at the top. So, unlike omega itself, omega plus 1 has a largest element, namely omega") as tracker:
            # Change continuum brace/label to \omega+1 and arrow pointing to the set
            omega1_label = MathTex(r"\omega+1", color=YELLOW, font_size=32).move_to(continuum_label)
            arrow = Arrow(omega1_label.get_bottom(), center_highlight.get_top(), buff=0.1, color=YELLOW)
            
            self.play(
                FadeOut(continuum_brace),
                Transform(continuum_label, omega1_label),
                Create(arrow),
                center_highlight.animate.set_color(YELLOW)
            )
            self.wait(tracker.duration * 0.8)

        # --- PART 4: CARDINALS VS ORDINALS ---
        with self.voiceover(text="Now have to quickly mention the difference between cardinals and ordinals. When I have been saying size so far, I have been referring to the cardinality, which is the answer to how many elements.") as tracker:
            # We explicitly DO NOT fade out here so the V-hierarchy stays.
            self.wait(tracker.duration)
            
        with self.voiceover(text="The ordinal numbers is the answer to how many and in what order. This is another key difference between finite and infinite sets.") as tracker:
            self.wait(tracker.duration* 0.9)
            self.play(*[FadeOut(m) for m in self.mobjects])

        with self.voiceover(text="If we want to determine how many elements a finite set has, we can simply count them.") as tracker:
            fin_circle = Circle(radius=1.8, color=BLUE)
            
            # 5 dots in a pentagon-like layout
            dot_positions = [UP*0.8, RIGHT*0.8 + UP*0.2, RIGHT*0.5 + DOWN*0.8, LEFT*0.5 + DOWN*0.8, LEFT*0.8 + UP*0.2]
            fin_dots = [Dot(pos) for pos in dot_positions]
            
            # Display dots first
            self.play(Create(fin_circle), *[FadeIn(d) for d in fin_dots])
            self.wait(2)
            # Then number them
            dot_labels = [Text(str(i+1), font_size=24).next_to(fin_dots[i], UP, buff=0.1) for i in range(5)]
            for i in range(5):
                self.play(Write(dot_labels[i]), run_time=0.3)
            
            big_5 = Text("5", font_size=48, color=YELLOW).next_to(fin_circle, UP)
            self.play(Write(big_5))

        with self.voiceover(text="We note that this imposes some arbitrary order of the elements, but that this order does not affect the final result.") as tracker:
            arrows = VGroup()
            for i in range(4):
                arrow_obj = Arrow(fin_dots[i].get_center(), fin_dots[i+1].get_center(), buff=0.15, color=YELLOW, max_tip_length_to_length_ratio=0.15)
                arrows.add(arrow_obj)
            
            for arrow_obj in arrows:
                self.play(Create(arrow_obj), run_time=0.3)

        with self.voiceover(text="For infinite sets, the order we count does in some sense affect the final result.") as tracker:
            inf_label = MathTex(r"\infty", font_size=48, color=YELLOW).move_to(big_5)
            self.play(
                FadeOut(VGroup(*fin_dots, *dot_labels, arrows, big_5)), 
                Write(inf_label)
            )

        with self.voiceover(text="For example, we could consider counting the natural numbers where we first count all of the even numbers, and then all of the odd numbers.") as tracker:
            self.play(FadeOut(fin_circle), FadeOut(inf_label))
            evens_odds = MathTex(r"0 < 2 < 4 < \dots < 1 < 3 < 5 < \dots", font_size=36).shift(UP*1.5)
            self.play(Write(evens_odds))

        with self.voiceover(text="This would result in something which we can represent as follows. This structure has a different order type than the set of natural numbers in its normal ordering.") as tracker:
            # Custom function for Achilles-run circles
            def get_omega_visual():
                vg = VGroup()
                current_x = 0
                for i in range(16):
                    r = 0.15 * (0.85**i)
                    c = Circle(radius=r, color=WHITE, stroke_width=2).move_to(RIGHT * current_x)
                    vg.add(c)
                    current_x += r + 0.15 * (0.85**(i+1)) + 0.03
                vg.move_to(ORIGIN)
                return vg

            w1 = get_omega_visual()
            w2 = get_omega_visual().next_to(w1, RIGHT, buff=0.05)
            w_w_visual = VGroup(w1, w2).move_to(DOWN*0.5)
            
            w_w_brace = Brace(w_w_visual, DOWN, color=YELLOW)
            w_w_label = w_w_brace.get_tex(r"\omega+\omega")
            
            self.play(Create(w_w_visual), Create(w_w_brace), Write(w_w_label))

        with self.voiceover(text="Of course the number of total elements used is the same, but the order in which they appear is different. Using this idea we can start to count past infinity.") as tracker:
            self.wait(tracker.duration)

        
        
        # Start the ordinal list horizontally
        ordinals = VGroup()
        def add_to_list(tex_str):
            mobj = MathTex(tex_str, font_size=32)
            if len(ordinals) == 0:
                mobj.to_edge(LEFT).shift(UP*1.5)
            else:
                mobj.next_to(ordinals[-1], RIGHT, buff=0.2)
            ordinals.add(mobj)
            return mobj

        # Helper to generate \omega + n (picks up immediately with big circle, distance halved to 0.015)
        def get_omega_plus_n_visual(n):
            w = get_omega_visual()
            vg = VGroup(*w)
            last_obj = w[-1]
            for i in range(n):
                c = Circle(radius=0.15, color=WHITE, stroke_width=2).next_to(last_obj, RIGHT, buff=0.015)
                vg.add(c)
                last_obj = c
            vg.move_to(DOWN*0.5)
            return vg

        with self.voiceover(text="So again, we start with omega, which is just another way of saying the natural numbers in their usual ordering.") as tracker:
            
            o1 = add_to_list(r"0, 1, 2, \dots,")
            o2 = add_to_list(r"\omega,")
            
            
            cur_visual = get_omega_visual().move_to(DOWN*0.5)
            cur_brace = Brace(cur_visual, DOWN, color=YELLOW)
            cur_label = cur_brace.get_tex(r"\omega")
            
            self.play(
                FadeOut(evens_odds), FadeOut(w_w_brace), FadeOut(w_w_label), FadeOut(w_w_visual),
                Write(o1), Write(o2),
                o2.animate.set_color(YELLOW),
                Create(cur_visual), 
                Create(cur_brace), 
                Write(cur_label)
            )

        with self.voiceover(text="Then we can define omega+1 using the same Russian doll successor function as before. So omega+1 represents the ordering of omega with a single greatest element.") as tracker:
            o3 = add_to_list(r"\omega+1,")
            self.play(Write(o3))
            
            next_visual = get_omega_plus_n_visual(1)
            next_brace = Brace(next_visual, DOWN, color=YELLOW)
            next_label = next_brace.get_tex(r"\omega+1")
            
            self.play(
                o2.animate.set_color(WHITE), o3.animate.set_color(YELLOW),
                Transform(cur_visual, next_visual), Transform(cur_brace, next_brace), Transform(cur_label, next_label)
            )

        with self.voiceover(text="Then we can define omega plus 2, in the same way, and we see that it represents the order type of omega with two greatest elements.") as tracker:
            o4 = add_to_list(r"\omega+2, \dots,")
            self.play(Write(o4))
            
            next_visual_2 = get_omega_plus_n_visual(2)
            next_brace_2 = Brace(next_visual_2, DOWN, color=YELLOW)
            next_label_2 = next_brace_2.get_tex(r"\omega+2")
            
            self.play(
                o3.animate.set_color(WHITE), o4.animate.set_color(YELLOW),
                Transform(cur_visual, next_visual_2), Transform(cur_brace, next_brace_2), Transform(cur_label, next_label_2)
            )

        with self.voiceover(text="and then we can repeat this omega many times, to obtain omega+omega, like we saw earlier.") as tracker:
            o5 = add_to_list(r"\omega+\omega, \dots,")
            self.play(Write(o5))
            
            next_visual_w = VGroup(get_omega_visual(), get_omega_visual().next_to(get_omega_visual(), RIGHT, buff=0.25)).move_to(DOWN*0.5)
            next_brace_w = Brace(next_visual_w, DOWN, color=YELLOW)
            next_label_w = next_brace_w.get_tex(r"\omega+\omega")
            
            self.play(
                o4.animate.set_color(WHITE), o5.animate.set_color(YELLOW),
                Transform(cur_visual, next_visual_w), Transform(cur_brace, next_brace_w), Transform(cur_label, next_label_w)
            )

        with self.voiceover(text="We can continue using this successor function, passing through omega times omega or omega squared, which is similar to the rational numbers.") as tracker:
            o6 = add_to_list(r"\omega^2, \dots,")
            self.play(Write(o6))
            
            # \omega^2 visual: four blocks of omega circles with dots between 3rd and 4th
            w_block1 = get_omega_visual()
            w_block2 = get_omega_visual().next_to(w_block1, RIGHT, buff=0.2)
            w_block3 = get_omega_visual().next_to(w_block2, RIGHT, buff=0.2)
            sq_dots = MathTex(r"\dots").next_to(w_block3, RIGHT, buff=0.1)
            w_block4 = get_omega_visual().next_to(sq_dots, RIGHT, buff=0.1)
            
            next_visual_sq = VGroup(w_block1, w_block2, w_block3, sq_dots, w_block4)
            next_visual_sq.scale(0.85).move_to(DOWN*0.5) 
            
            next_brace_sq = Brace(next_visual_sq, DOWN, color=YELLOW)
            next_label_sq = next_brace_sq.get_tex(r"\omega^2")
            
            self.play(
                o5.animate.set_color(WHITE), o6.animate.set_color(YELLOW),
                Transform(cur_visual, next_visual_sq), Transform(cur_brace, next_brace_sq), Transform(cur_label, next_label_sq)
            )
            self.play(o6.animate.set_color(WHITE))

        with self.voiceover(text="Eventually through omega to the omega, and to even larger ordinals such as epsilon naught, which is the fixed point of the operation sending omega to the omega.") as tracker:
            self.play(FadeOut(cur_visual), FadeOut(cur_brace), FadeOut(cur_label))
            o7 = add_to_list(r"\omega^\omega, \dots,")
            o8 = add_to_list(r"\epsilon_0, \dots,")
            self.play(Write(o7))
            self.play(Write(o8))

        with self.voiceover(text="Meaning that epsilon naught is the least solution to the equation epsilon equals omega to the epsilon.") as tracker:
            fix_point_eq = MathTex(r"\epsilon_0 = \text{min}(\{\epsilon: \omega^{\epsilon} = \epsilon\})", font_size=42, color=YELLOW).shift(DOWN*1.5)
            self.play(Write(fix_point_eq))

        with self.voiceover(text="But each of these ordinals are countable, meaning that they can be put into 1 to 1 correspondence with omega. So, we see these as different ways of re-ordering omega.") as tracker:
            # Change: The brace now correctly covers only the elements from \omega up to \epsilon_0 (indices 1 onwards)
            countable_brace = Brace(VGroup(*ordinals[1:]), DOWN, color=BLUE)
            countable_text = countable_brace.get_text("Countable Orderings").set_color(BLUE)
            self.play(Create(countable_brace), Write(countable_text))

        with self.voiceover(text="But now we can consider the set of all possible orderings of omega, i.e. the set of all countable ordinals. If this set is a countable ordinal, then it would be a member of itself. But this contradicts the axiom of Foundation.") as tracker:
            # Replaces equation with the set representation
            self.play(FadeOut(fix_point_eq))
            set_of_countable = MathTex(r"\{0, 1, \dots, \omega, \dots, \omega^2, \dots, \epsilon_0, \dots\}", font_size=38)
            set_of_countable.shift(DOWN * 1.5)
            self.play(Write(set_of_countable))

        with self.voiceover(text="So, the set of all countable ordinals is uncountable. Meaning that there are more ways or re-ordering omega, then there are elements in omega. We will call this set, as Cantor did, omega 1.") as tracker:
            self.play(FadeOut(countable_brace), FadeOut(countable_text))
            
            # Change: Scales in place around its left edge so it doesn't jump up
            self.play(ordinals.animate.scale(0.8, about_point=ordinals[0].get_left()))
            
            o9 = MathTex(r"\omega_1, \dots,", font_size=32*0.8, color=WHITE).next_to(ordinals[-1], RIGHT, buff=0.2)
            ordinals.add(o9)
            
            set_brace = Brace(set_of_countable, UP, color=RED)
            arrow_to_w1 = Arrow(set_brace.get_top(), o9.get_bottom() + LEFT * 0.15, buff=0.1, color=RED)
            
            self.play(Write(o9))
            self.play(Create(set_brace), Create(arrow_to_w1))

        with self.voiceover(text="Now we can repeat the same process with omega_1.  So, we can define omega_1 plus 1, using the same successor function, and then consider all possible orderings of this new larger base set omega_1.   Then we can continue applying this successor function, passing through all possible orderings of the new base set omega 1.  Then we can think of omega_2 as the set containing each of the orderings of omega_1, and we know that this set has large cardinality than omega_1") as tracker:
            o10 = MathTex(r"\omega_2, \dots", font_size=32*0.8, color=WHITE).next_to(ordinals[-1], RIGHT, buff=0.2)
            ordinals.add(o10)
            self.play(Write(o10))

        with self.voiceover(text="So, if we just care about the cardinality, meanings how many elements there are, we see that all of these sets have the same size, since they are just different orderrings of omega.  We will call this size aleph_0.") as tracker:
            aleph_0_group = VGroup(*ordinals[1:8])
            brace_0 = Brace(aleph_0_group, UP, color=GREEN)
            label_0 = brace_0.get_tex(r"\aleph_0").set_color(GREEN)
            self.play(Create(brace_0), Write(label_0))
        
        with self.voiceover(text = "And similarly these sets have the same size, whcih we call aleph_1.  And these guys have size aleph_2 ") as tracker:
            aleph_1_group = VGroup(*ordinals[8:9]) 
            brace_1 = Brace(aleph_1_group, UP, color=RED)
            label_1 = brace_1.get_tex(r"\aleph_1").set_color(RED)
            self.play(Create(brace_1), Write(label_1))
            
            self.wait(0.5)
            aleph_2_group = VGroup(*ordinals[9:10])
            brace_2 = Brace(aleph_2_group, UP, color=BLUE)
            label_2 = brace_2.get_tex(r"\aleph_2").set_color(BLUE)
            self.play(Create(brace_2), Write(label_2))
            self.wait(tracker.duration * 0.5)

        self.play(*[FadeOut(m) for m in self.mobjects])