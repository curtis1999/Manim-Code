from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class ContinuumAndBeyond(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # --- Block 1 ---
        with self.voiceover(text="Before seeing how far this idea can go, let us address a natural question.") as tracker:
            pass
        
        # --- Block 2 ---
        with self.voiceover(text="Where in this hierarchy does the continuum fit?") as tracker:
            cardinals_hierarchy = MathTex(
                r"\aleph_0", ",", 
                r"\aleph_1", ",", 
                r"\aleph_2", r", \dots, ", 
                r"\aleph_n", r", \dots", 
                color=YELLOW
            ).to_edge(UP).shift(DOWN)
            
            continuum_c = MathTex(r"\mathfrak{c}", color=BLUE).next_to(cardinals_hierarchy, UP, buff=0.5)
            
            self.play(FadeIn(cardinals_hierarchy))
            self.play(FadeIn(continuum_c))
            
            # Slide it left and right to indicate uncertainty
            self.play(continuum_c.animate.shift(RIGHT * 2), run_time=tracker.duration * 0.3)
            self.play(continuum_c.animate.shift(LEFT * 4), run_time=tracker.duration * 0.3)
            self.play(continuum_c.animate.next_to(cardinals_hierarchy, UP, buff=0.5), run_time=tracker.duration * 0.3)

        # --- Block 3 ---
        with self.voiceover(text="The Continuum Hypothesis, which Cantor believed but was unable to prove and we will soon see why, states that size of the continuum is the next infinity after omega.") as tracker:
            aleph_1_pos = cardinals_hierarchy[2].get_top()
            arrow_ch = Arrow(start=continuum_c.get_bottom(), end=aleph_1_pos, color=BLUE)
            self.play(Create(arrow_ch))

        # --- Block 4 ---
        with self.voiceover(text="If the CH is false, then there are sets of intermediate size, greater than the size of the natural numbers, but smaller than the set of real numbers.") as tracker:
            aleph_n_pos = cardinals_hierarchy[6].get_top()
            arrow_not_ch = Arrow(start=continuum_c.get_bottom(), end=aleph_n_pos, color=RED)
            self.play(ReplacementTransform(arrow_ch, arrow_not_ch))

        # --- Block 5 ---
        with self.voiceover(text="And the Generalized continuum hypothesis, asserts that the power set of any cardinal is the next cardinal.") as tracker:
            self.play(FadeOut(continuum_c), FadeOut(arrow_not_ch))
            
            gch_eq = MathTex(r"|\mathcal{P}(\aleph_n)| = \aleph_{n+1}").next_to(cardinals_hierarchy, DOWN, buff=0.5)
            self.play(Write(gch_eq))

        # --- Block 6 ---
        with self.voiceover(text="We will do a whole video on the CH soon, as it is the first statement which was formally shown to be independent from the axioms of ZFC.") as tracker:
            pass

        # --- Block 7 ---
        with self.voiceover(text="Meaning that if we feed the ZFC axioms into our theorem prover, it will never spit out a proof of CH nor its negation.") as tracker:
            pass

        # --- Block 8 ---
        with self.voiceover(text="For now, let us just assume for simplicity that the GCH holds, and let us see how far this infinite hierarchy can go.") as tracker:
            self.play(FadeOut(gch_eq))

        # --- Block 9 ---
        with self.voiceover(text="Now we can surely continue performing this procedure all the way to aleph omega.") as tracker:
            aleph_omega = MathTex(r", \aleph_\omega", color=YELLOW).next_to(cardinals_hierarchy, RIGHT)
            self.play(Write(aleph_omega))
            cardinals_hierarchy.add(aleph_omega)

        # --- Block 10 ---
        with self.voiceover(text="Recall that we were originally trying to define a Universe of sets.  I.e. some set which satisfies each of the ZFC axioms.  Now, if we cut off the universe at aleph omega, we would obtain a model of a lot of ZFC, but the axiom of Replacement would fail.") as tracker:
            # Constructing the right-hand side V_aleph_omega hierarchy
            v_hierarchy = VGroup()
            v_line_left = Line(DOWN*2, UP*2, color=GREEN).shift(RIGHT*2.5)
            v_line_right = Line(DOWN*2, UP*2, color=GREEN).shift(RIGHT*6.5)
            
            v_dots = MathTex(r"\vdots").next_to(v_line_left, UP, buff=0.2).shift(RIGHT*2)
            
            v_omega_dashed = DashedLine(v_line_left.point_from_proportion(0.3), v_line_right.point_from_proportion(0.3), color=GREEN)
            v_omega_label = MathTex(r"V_\omega", color=GREEN).next_to(v_omega_dashed, LEFT, buff=0.2)
            
            v_omega_plus_dashed = DashedLine(v_line_left.point_from_proportion(0.6), v_line_right.point_from_proportion(0.6), color=GREEN)
            v_omega_plus_label = MathTex(r"V_{\omega+1}", color=GREEN).next_to(v_omega_plus_dashed, LEFT, buff=0.2)
            
            v_aleph_omega_label = MathTex(r"V_{\aleph_\omega}", color=GREEN).next_to(v_dots, LEFT, buff=0.2).shift(DOWN*0.5)
            
            v_hierarchy.add(v_line_left, v_line_right, v_dots, v_omega_dashed, v_omega_label, v_omega_plus_dashed, v_omega_plus_label, v_aleph_omega_label)
            
            self.play(Create(v_hierarchy))

        # --- Block 11 ---
        with self.voiceover(text="Since we can define a function which maps natural numbers n to aleph_n.") as tracker:
            func_def = MathTex(r"f(n) = \aleph_n").to_edge(LEFT).shift(UP*1)
            self.play(Write(func_def))

        # --- Block 12 ---
        with self.voiceover(text="By the axiom of replacement the range of this function should be a set.") as tracker:
            range_set = MathTex(r"\{", r"\aleph_0, \aleph_1, \dots, \aleph_n, \dots", r"\}").next_to(func_def, DOWN, buff=0.5).align_to(func_def, LEFT)
            self.play(Write(range_set))

        # --- Block 13 ---
        with self.voiceover(text="And by the axiom of union, so should its union.") as tracker:
            union_set = MathTex(r"\bigcup", r"\{", r"\aleph_0, \aleph_1, \dots, \aleph_n, \dots", r"\}").move_to(range_set.get_center())
            self.play(ReplacementTransform(range_set, union_set))

        # --- Block 14 ---
        with self.voiceover(text="But the union of the range of this function is V_omega itself, and equals aleph omega.") as tracker:
            equals_aleph_omega = MathTex(r"= \aleph_\omega").next_to(union_set, RIGHT)
            self.play(Write(equals_aleph_omega))

        # --- Block 15 ---
        with self.voiceover(text="But V_omega cannot contain aleph_omega.") as tracker:
            pass

        # --- Block 16 ---
        with self.voiceover(text="So, we don't yet have a model of set theory.") as tracker:
            pass

        # --- Block 17 ---
        with self.voiceover(text="We have to continue further. But the cat is already out of the bag, we have already accepted the existence of transfinite numbers, so we can continue beyond V_omega just as we did before.") as tracker:
            pass

        # --- Block 18 ---
        with self.voiceover(text="We can define aleph omega plus one, and eventually aleph omega one and so on.") as tracker:
            pass

        # --- Block 19 ---
        with self.voiceover(text="Now if we look at the generalization of this function here, which sends an ordinal alpha to aleph_alpha, we see that this is an increasing continuous function on the ordinals, and so by the fixed point theorem, there is a fixed point which we will call kappa.") as tracker:
            func_alpha = MathTex(r"f(\alpha) = \aleph_\alpha").move_to(func_def.get_center())
            self.play(ReplacementTransform(func_def, func_alpha))

        # --- Block 20 ---
        with self.voiceover(text="So kappa equals aleph kappa.") as tracker:
            kappa_eq = MathTex(r"\kappa = \aleph_\kappa").next_to(func_alpha, DOWN, buff=0.5).align_to(func_alpha, LEFT)
            self.play(ReplacementTransform(union_set, kappa_eq), FadeOut(equals_aleph_omega))

        # --- Block 21 ---
        with self.voiceover(text="If kappa is also a so-called regular cardinal then V_kappa is a model of ZFC.") as tracker:
            v_kappa_label = MathTex(r"V_\kappa", color=GREEN).next_to(v_dots, UP, buff=0.5)
            
            # Updating the hierarchy labels on the right
            self.play(
                FadeOut(v_omega_plus_dashed), FadeOut(v_omega_plus_label),
                Write(v_kappa_label)
            )
            
            # Rendering ZFC axioms on the left
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
            ax_group = VGroup(*[MathTex(formula).scale(0.35) for formula in ax_texts])
            ax_group.arrange(UP, aligned_edge=LEFT, buff=0.15).to_edge(LEFT).shift(DOWN*1)
            
            self.play(FadeOut(func_alpha), FadeOut(kappa_eq), FadeIn(ax_group))

        # --- Block 22 ---
        with self.voiceover(text="Meaning that it is a Universe of sets.") as tracker:
            pass

        # --- Block 23 ---
        with self.voiceover(text="However, by Godel's completeness theorem, this means that ZFC is consistent.") as tracker:
            pass

        # --- Block 24 ---
        with self.voiceover(text="But then this implies that we cannot prove the existence of such a cardinal kappa, since if we could then we would have a proof of the consistency of ZFC, which contradicts Godel's second incompleteness theorem.") as tracker:
            pass
            
        self.wait(2)