from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

# ==========================================
# SCENE 4: HILBERT CALCULUS & PROOFS AS PROGRAMS
# ==========================================
class HilbertCalculus(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # ------------------------------------------
        # 1. THE CALCULUS (AXIOMS & MP)
        # ------------------------------------------
        title = Text("Hilbert Calculus", font_size=48, weight=BOLD).to_edge(UP)
        
        axioms_group = VGroup(
            MathTex(r"\mathbf{A1:} \quad \varphi \to (\psi \to \varphi)"),
            MathTex(r"\mathbf{A2:} \quad ((\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi)))"),
            MathTex(r"\mathbf{A3:} \quad ((\neg \varphi \to \neg \psi) \to ((\neg \varphi \to \psi) \to \varphi))")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).scale(0.8).shift(LEFT * 2)

        mp_title = Text("Modus Ponens (MP)", font_size=24, color=YELLOW)
        mp_rule = MathTex(r"\frac{\varphi \quad \varphi \to \psi}{\psi}", font_size=60)
        mp_group = VGroup(mp_title, mp_rule).arrange(DOWN, buff=0.3).next_to(axioms_group, RIGHT, buff=1.5)

        # ------------------------------------------
        # ANIMATIONS: PART 1
        # ------------------------------------------
        script_1 = "The syntax of classical propositional logic is given by a calculus. There are many calculi which turn out to be equivalent, but each has a set of axioms, which are just some logically valid formulas..."
        with self.voiceover(text=script_1) as tracker:
            self.play(Write(title), run_time=1)
            self.play(FadeIn(axioms_group, lag_ratio=0.2), run_time=2)
            self.wait(max(0, tracker.duration - 3))

        script_2 = "...and rules of inference, which allow us to derive new formulas from a set of premises while preserving truth."
        with self.voiceover(text=script_2) as tracker:
            self.wait(tracker.duration)

        script_3 = "The most concise calculus is the Hilbert style calculus, which has the following 3 axioms, and the only rule of inference is Modus Ponens, which says that if you have phi and you have phi implies psi, then you can conclude psi."
        with self.voiceover(text=script_3) as tracker:
            self.play(FadeIn(mp_group, shift=LEFT), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_4 = "These axioms seem random at first, and you may notice that conjunction and disjunction do not appear, but one can prove that they are both necessary and sufficient for propositional logic."
        with self.voiceover(text=script_4) as tracker:
            arrows = VGroup(*[axioms_group[0][0][3], axioms_group[0][0][6], mp_rule[0][3]])
            self.play(arrows.animate.set_color(TEAL), run_time=1)
            self.play(arrows.animate.set_color(WHITE), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        self.play(FadeOut(axioms_group), FadeOut(mp_group), FadeOut(title))

        # ------------------------------------------
        # 2. THE PROOF TREE
        # ------------------------------------------
        tree_group = self.get_proof_tree().scale(0.85).move_to(DOWN * 0.5)
        
        script_5 = "Once we have our calculus, we can start to construct proofs. We can visualize proofs as trees, where the leaves are axioms, and we combine nodes using our rule of inference."
        with self.voiceover(text=script_5) as tracker:
            self.play(FadeIn(tree_group[0], shift=DOWN), FadeIn(tree_group[1], shift=DOWN), run_time=1)
            self.play(Create(tree_group[5][0]), Create(tree_group[5][1]), run_time=0.5)
            self.play(FadeIn(tree_group[2], shift=DOWN), run_time=0.5)
            self.play(FadeIn(tree_group[3], shift=DOWN), run_time=0.5)
            self.play(Create(tree_group[5][2]), Create(tree_group[5][3]), run_time=0.5)
            self.play(FadeIn(tree_group[4], shift=DOWN), run_time=1)
            self.wait(max(0, tracker.duration - 4))

        self.play(FadeOut(tree_group))

        # ------------------------------------------
        # 3. PROOFS AS PROGRAMS
        # ------------------------------------------
        prog_box = Rectangle(width=4, height=2.5, color=BLUE, fill_opacity=0.1)
        prog_text = MathTex(r"\varphi \to \psi", font_size=48).move_to(prog_box.get_center())
        main_program = VGroup(prog_box, prog_text)

        in_arrow = Arrow(LEFT * 5, prog_box.get_left(), color=WHITE)
        in_label = MathTex(r"\varphi", font_size=48).next_to(in_arrow, UP)
        out_arrow = Arrow(prog_box.get_right(), RIGHT * 5, color=WHITE)
        out_label = MathTex(r"\psi", font_size=48).next_to(out_arrow, UP)

        script_6 = "Proofs can also be seen as computer programs. Where the axioms can be used as inputs, and modus ponens is seen as running a given program."
        with self.voiceover(text=script_6) as tracker:
            self.play(Create(prog_box), Write(prog_text), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        script_7 = "Since phi implies psi can be interpreted as a computer program which if given phi as input, can output psi."
        with self.voiceover(text=script_7) as tracker:
            self.play(GrowArrow(in_arrow), FadeIn(in_label, shift=RIGHT), run_time=1)
            self.play(prog_box.animate.set_fill(BLUE, opacity=0.4), run_time=0.5)
            self.play(prog_box.animate.set_fill(BLUE, opacity=0.1), run_time=0.5)
            self.play(GrowArrow(out_arrow), FadeIn(out_label, shift=RIGHT), run_time=1)
            self.wait(max(0, tracker.duration - 3))

        small_box = Rectangle(width=1.5, height=1, color=TEAL, fill_opacity=0.8)
        small_text = MathTex(r"\varphi", font_size=36).move_to(small_box.get_center())
        small_program = VGroup(small_box, small_text).move_to(LEFT * 5 + UP * 2)

        script_8 = "So, an application of Modus Ponens is akin to running a computer program. The complexity, and therefore power, comes from the fact that the input formula phi, can be seen as a program itself."
        with self.voiceover(text=script_8) as tracker:
            self.play(FadeIn(small_program, shift=DOWN), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_9 = "So we can pass programs as input to other programs. I will cover this in more detail in a later video, but for now just know that the world of syntax deals with formal proofs, and proofs can be carried out by computers."
        with self.voiceover(text=script_9) as tracker:
            self.play(FadeOut(in_label), small_program.animate.next_to(in_arrow, UP), run_time=1)
            self.play(small_program.animate.move_to(prog_box.get_center()), run_time=1)
            self.play(Indicate(out_label, color=YELLOW), run_time=1)
            self.wait(max(0, tracker.duration - 3))

        self.play(FadeOut(Group(main_program, small_program, in_arrow, out_arrow, out_label)))

        # ------------------------------------------
        # 4. SOUNDNESS & COMPLETENESS (NEW)
        # ------------------------------------------
        
        # 4a. Re-introduce smaller Calculus
        axioms_group_small = VGroup(
            MathTex(r"\mathbf{A1:} \ \varphi \to (\psi \to \varphi)"),
            MathTex(r"\mathbf{A2:} \ (\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))"),
            MathTex(r"\mathbf{A3:} \ (\neg \varphi \to \neg \psi) \to ((\neg \varphi \to \psi) \to \varphi)")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).scale(0.55)
        
        mp_rule_small = MathTex(r"\text{MP: } \frac{\varphi \quad \varphi \to \psi}{\psi}", font_size=36)
        calc_group = VGroup(axioms_group_small, mp_rule_small).arrange(RIGHT, buff=1).to_edge(UP).shift(DOWN * 0.2)
        
        script_10 = "There are two main questions we can ask about our calculus."
        with self.voiceover(text=script_10) as tracker:
            self.play(FadeIn(calc_group, shift=DOWN), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_11 = "The first is whether we can trust it. Meaning if we prove something in our calculus, how do we know that it is really true?"
        with self.voiceover(text=script_11) as tracker:
            self.wait(tracker.duration)

        # Build A1 Truth Table step-by-step
        a1_table = self.get_a1_table().move_to(DOWN * 1.5)
        
        script_12 = "In propositional logic this is easy to check, since each of the axioms is logically valid..."
        with self.voiceover(text=script_12) as tracker:
            # Show base columns
            self.play(FadeIn(VGroup(a1_table.get_columns()[0], a1_table.get_columns()[1])), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_13 = "...again this means that each row in their truth table evaluates to 1."
        with self.voiceover(text=script_13) as tracker:
            # Step by step evaluate A1
            self.play(FadeIn(a1_table.get_columns()[2][0]), run_time=0.3)
            self.play(Write(a1_table.get_columns()[2][1:]), run_time=0.6)
            
            self.play(FadeIn(a1_table.get_columns()[3][0]), run_time=0.3)
            self.play(Write(a1_table.get_columns()[3][1:]), run_time=0.6)
            
            box = SurroundingRectangle(a1_table.get_columns()[3][1:], color=GREEN, buff=0.1)
            self.play(Create(box), run_time=0.5)
            self.wait(max(0, tracker.duration - 2.3))

        script_14 = "And clearly Modus Ponens preserves truth. So whatever we prove will be logically valid. This means that our calculus is sound."
        with self.voiceover(text=script_14) as tracker:
            soundness_text = Text("Soundness", font_size=40, color=GREEN).next_to(a1_table, LEFT, buff=1)
            self.play(FadeIn(soundness_text, shift=RIGHT), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        # Clear board for Completeness
        self.play(FadeOut(a1_table), FadeOut(box), FadeOut(soundness_text))

        script_15 = "The second question is whether this list is sufficient to prove all valid statements?"
        with self.voiceover(text=script_15) as tracker:
            self.wait(tracker.duration)

        # 4-Variable valid formula and table
        complex_formula = MathTex(r"\Phi = (p \land (q \to r)) \to (s \lor \neg s)", font_size=40, color=YELLOW).next_to(calc_group, DOWN, buff=0.5)
        table_16_row = self.get_16_row_table().next_to(complex_formula, DOWN, buff=0.3)

        script_16 = "So, if we come across some arbitrary formula phi, and we check the truth table, and see that all rows evaluate to 1, can we guarantee that there is a proof of phi?"
        with self.voiceover(text=script_16) as tracker:
            self.play(Write(complex_formula), run_time=1)
            # Show inputs
            self.play(FadeIn(VGroup(*[table_16_row.get_columns()[i] for i in range(4)])), run_time=1)
            # Show output 1s
            self.play(FadeIn(table_16_row.get_columns()[4][0]), run_time=0.3)
            self.play(Write(table_16_row.get_columns()[4][1:]), run_time=1)
            
            box_16 = SurroundingRectangle(table_16_row.get_columns()[4][1:], color=GREEN, buff=0.05)
            self.play(Create(box_16), run_time=0.5)
            self.wait(max(0, tracker.duration - 3.8))

        script_17 = "Perhaps there is some valid statement out there which no matter how hard we try, we cannot prove. Perhaps we need to add more axioms? This is the question of completeness."
        with self.voiceover(text=script_17) as tracker:
            completeness_text = Text("Completeness", font_size=40, color=YELLOW).next_to(table_16_row, LEFT, buff=0.8)
            self.play(FadeIn(completeness_text, shift=RIGHT), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_18 = "It turns out that this set of axioms is complete and we will see a stronger version of this in the fourth video."
        with self.voiceover(text=script_18) as tracker:
            self.wait(tracker.duration)

        script_19 = "So, this simple calculus can only prove logically valid statements, and it can prove all logically valid statements."
        with self.voiceover(text=script_19) as tracker:
            self.play(Circumscribe(soundness_text, color=GREEN, time_width=0.5), run_time=1.5)
            self.play(Circumscribe(completeness_text, color=YELLOW, time_width=0.5), run_time=1.5)
            self.wait(max(0, tracker.duration - 3))

        self.play(FadeOut(Group(calc_group, complex_formula, table_16_row, box_16, completeness_text)))
        self.wait(1)

    # ---------------------------------------------------
    # Helper Functions 
    # ---------------------------------------------------
    def get_proof_tree(self):
        n1_tex = MathTex(
            r"((\varphi \to ((\varphi \to \varphi) \to \varphi)) \to", 
            r"((\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi)))", 
            r"\quad [A2]", font_size=28
        ).arrange(DOWN, aligned_edge=LEFT)
        n1 = VGroup(n1_tex).move_to(LEFT * 3.5 + UP * 3)

        n2 = MathTex(r"(\varphi \to ((\varphi \to \varphi) \to \varphi)) \quad [A1]", font_size=28).move_to(RIGHT * 3.5 + UP * 3)
        n3 = MathTex(r"((\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi)) \quad [MP]", font_size=32).move_to(LEFT * 2 + UP * 0.5)
        n4 = MathTex(r"(\varphi \to (\varphi \to \varphi)) \quad [A1]", font_size=32).move_to(RIGHT * 3.5 + UP * 0.5)
        n5 = MathTex(r"\vdash \varphi \to \varphi \quad [MP]", font_size=40, color=YELLOW).move_to(DOWN * 2)

        e1 = Line(n1.get_bottom(), n3.get_top(), buff=0.1)
        e2 = Line(n2.get_bottom(), n3.get_top(), buff=0.1)
        e3 = Line(n3.get_bottom(), n5.get_top(), buff=0.1)
        e4 = Line(n4.get_bottom(), n5.get_top(), buff=0.1)
        edges = VGroup(e1, e2, e3, e4).set_color(GREY)

        return VGroup(n1, n2, n3, n4, n5, edges)

    def get_a1_table(self):
        # Axiom 1: phi -> (psi -> phi)
        content = [
            ["0", "0", "1", "1"],
            ["0", "1", "0", "1"],
            ["1", "0", "1", "1"],
            ["1", "1", "1", "1"]
        ]
        return MathTable(
            content,
            col_labels=[MathTex(r"\varphi"), MathTex(r"\psi"), MathTex(r"\psi \to \varphi"), MathTex(r"\varphi \to (\psi \to \varphi)")],
            include_outer_lines=True
        ).scale(0.35)

    def get_16_row_table(self):
        # Dynamically generate 16 rows of binary inputs, all mapping to output '1'
        content = []
        for i in range(16):
            b = f"{i:04b}" # Creates padded binary string like '0000', '0001', etc.
            content.append([b[0], b[1], b[2], b[3], "1"])
            
        return MathTable(
            content,
            col_labels=[MathTex("p"), MathTex("q"), MathTex("r"), MathTex("s"), MathTex(r"\Phi")],
            include_outer_lines=True
        ).scale(0.22) # Scaled down nicely so 16 rows perfectly fit the lower half of the screen