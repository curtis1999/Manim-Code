from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
import random

# ==========================================
# SCENE 3: PROPOSITIONAL LOGIC & TRUTH TABLES
# ==========================================
class PropositionalLogic(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # ------------------------------------------
        # 1. ATOMS, VARIABLES & CONNECTIVES
        # ------------------------------------------
        title = Text("Propositional Logic (0th Order Logic)", font_size=40, weight=BOLD).to_edge(UP)
        
        # Variables: p, q, r, s ...
        vars_tex = MathTex("p", ",", "q", ",", "r", ",", "s", ",", r"\dots", font_size=48)
        vars_tex.move_to(UP * 2)

        # ------------------------------------------
        # 2. BOOLEAN CONNECTIVES & 5/6 COL TABLES
        # ------------------------------------------
        table_5col = MathTable(
            [["0", "0", "0", "0", "1"], 
             ["0", "1", "0", "1", "1"], 
             ["1", "0", "0", "1", "0"], 
             ["1", "1", "1", "1", "1"]],
            col_labels=[MathTex("A"), MathTex("B"), MathTex(r"A \land B"), MathTex(r"A \lor B"), MathTex(r"A \to B")],
            include_outer_lines=True
        ).scale(0.35).move_to(DOWN * 1.5)

        table_6col = MathTable(
            [["0", "0", "0", "0", "1", "1"], 
             ["0", "1", "0", "1", "1", "1"], 
             ["1", "0", "0", "1", "0", "0"], 
             ["1", "1", "1", "1", "1", "1"]],
            col_labels=[MathTex("A"), MathTex("B"), MathTex(r"A \land B"), MathTex(r"A \lor B"), MathTex(r"A \to B"), MathTex(r"\neg A \lor B")],
            include_outer_lines=True
        ).scale(0.35).move_to(table_5col.get_center())

        # ------------------------------------------
        # ANIMATIONS: PART 1
        # ------------------------------------------
        script_1 = "To understand the relation between these two worlds, let's first consider the simple world of classical propositional logic, also known as 0th order logic."
        with self.voiceover(text=script_1) as tracker:
            self.play(Write(title), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_2 = "Here we have a set of propositional variables, which can either be true or false."
        with self.voiceover(text=script_2) as tracker:
            self.play(FadeIn(vars_tex, shift=RIGHT), run_time=1)
            
            # Generate random 0s and 1s with NO arrows
            assignments = VGroup()
            for i in [0, 2, 4, 6]:  # Indices of p, q, r, s in the MathTex
                val = str(random.choice([0, 1]))
                num = MathTex(val, font_size=36, color=YELLOW).next_to(vars_tex[i], UP, buff=0.3)
                assignments.add(num)
            
            self.play(FadeIn(assignments, shift=DOWN), run_time=1)
            self.wait(max(0, tracker.duration - 2))
            self.play(FadeOut(assignments), run_time=0.5)

        script_3 = "These serve as the atoms of our logic, which we can combine using the Boolean connectives of conjunction, disjunction, implication and negation to form proposition formulas."
        with self.voiceover(text=script_3) as tracker:
            connectives_list = MathTex(r"\{ \land, \lor, \to, \neg \}", font_size=48).next_to(vars_tex, DOWN, buff=0.5)
            self.play(FadeIn(connectives_list, shift=DOWN), run_time=1)
            
            complex_formula = MathTex(r"\varphi = (p \land \neg q) \to (r \lor s)", font_size=48).set_color(TEAL).next_to(connectives_list, DOWN, buff=0.5)
            self.play(Write(complex_formula), run_time=1.5)
            
            self.wait(max(0, tracker.duration - 2.5))
            self.play(FadeOut(complex_formula), FadeOut(connectives_list), run_time=1)

        script_4 = "The connectives are governed by truth tables, where conjunction, disjunction, and negation are as we would expect."
        with self.voiceover(text=script_4) as tracker:
            self.play(FadeIn(table_5col), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_5 = "In classical logic, implication is equivalent to 'not p or q', meaning that p implies q is true either if p is false, or q is true."
        with self.voiceover(text=script_5) as tracker:
            self.play(ReplacementTransform(table_5col, table_6col), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        script_6 = "Note that there are non-classical logics which interpret these symbols differently, especially implication and negation. We will cover this in the bonus video at the end, for now we stick to classical logic."
        with self.voiceover(text=script_6) as tracker:
            self.wait(tracker.duration)

        # Clear the board for the 8-row table section
        self.play(FadeOut(vars_tex), FadeOut(table_6col), FadeOut(title))

        # ------------------------------------------
        # 3. THE STEP-BY-STEP 8-ROW TRUTH TABLES
        # ------------------------------------------
        
        # Big formula at top
        big_formula_v = MathTex(r"\varphi = (p \to (q \to r)) \to ((p \land q) \to r)").to_edge(UP).set_color(GREEN)
        table_detailed = self.get_detailed_valid_table().move_to(DOWN * 0.5)

        status_text = Text("", font_size=36, weight=BOLD).to_edge(RIGHT).shift(LEFT * 1)

        script_7 = "So, given an arbitrary propositional formula, like this one, we can easily evaluate it using a truth table."
        with self.voiceover(text=script_7) as tracker:
            self.play(Write(big_formula_v), run_time=1.5)
            
            # Show ONLY the base columns (p, q, r)
            base_cols = VGroup(*[table_detailed.get_columns()[i] for i in range(3)])
            self.play(FadeIn(base_cols), run_time=1)
            self.wait(max(0, tracker.duration - 2.5))

        script_8 = "Meaning that we list every possible combination of 0 and 1 for the propositional variables involved, and then compute the output using the rules of the connectives."
        with self.voiceover(text=script_8) as tracker:
            # Build up the table step-by-step
            for i in range(3, 8):
                # Fade in Header
                self.play(FadeIn(table_detailed.get_columns()[i][0]), run_time=0.3)
                # Fill in Values
                self.play(Write(table_detailed.get_columns()[i][1:]), run_time=0.6)
            
            self.wait(max(0, tracker.duration - 4.5))

        script_9 = "If all rows evaluate to 1, as is the case with this formula, then we say that the formula is logically valid."
        with self.voiceover(text=script_9) as tracker:
            box = SurroundingRectangle(table_detailed.get_columns()[7][1:], color=GREEN, buff=0.1)
            status_text.become(Text("Logically Valid", font_size=36, color=GREEN).to_edge(RIGHT).shift(LEFT * 0.5))
            self.play(Create(box), FadeIn(status_text, shift=LEFT), run_time=1)
            self.wait(max(0, tracker.duration - 1))


        # --- TRANSITION TO UNSATISFIABLE ---
        big_formula_u = MathTex(r"\psi_{unsat} = (p \land \neg p) \land (q \lor r)").to_edge(UP).set_color(RED)
        table_u = self.get_8_row_table(r"\psi_{unsat}", ["0"] * 8).move_to(DOWN * 0.5)

        script_10 = "If all rows evaluate to 0, then we say that the formula is unsatisfiable."
        with self.voiceover(text=script_10) as tracker:
            # Fade out the extra intermediate columns and the box
            cols_to_fade = VGroup(*[table_detailed.get_columns()[i] for i in range(3, 8)])
            self.play(
                ReplacementTransform(big_formula_v, big_formula_u),
                FadeOut(box), FadeOut(status_text), FadeOut(cols_to_fade),
                run_time=1
            )
            
            # Morph the first 3 columns directly into the new table structure 
            # and show the new final formula header
            self.play(
                ReplacementTransform(table_detailed.get_columns()[0], table_u.get_columns()[0]),
                ReplacementTransform(table_detailed.get_columns()[1], table_u.get_columns()[1]),
                ReplacementTransform(table_detailed.get_columns()[2], table_u.get_columns()[2]),
                FadeIn(table_u.get_columns()[3][0]),
                run_time=1
            )
            
            # Write the new '0's
            col_values_u = table_u.get_columns()[3][1:]
            status_text.become(Text("Unsatisfiable", font_size=36, color=RED).to_edge(RIGHT).shift(LEFT * 0.5))
            self.play(Write(col_values_u), FadeIn(status_text, shift=LEFT), run_time=0.8)
            self.wait(max(0, tracker.duration - 2.8))


        # --- TRANSITION TO SATISFIABLE ---
        big_formula_s = MathTex(r"\psi_{sat} = (p \lor q) \to r").to_edge(UP).set_color(YELLOW)
        results_sat = ["1", "1", "0", "1", "0", "1", "0", "1"]
        table_s = self.get_8_row_table(r"\psi_{sat}", results_sat).move_to(DOWN * 0.5)

        script_11 = "And if at least one row is true, then we say that it is satisfiable."
        with self.voiceover(text=script_11) as tracker:
            # Fade out previous results
            self.play(
                ReplacementTransform(big_formula_u, big_formula_s),
                FadeOut(status_text), FadeOut(col_values_u), FadeOut(table_u.get_columns()[3][0]),
                run_time=0.8
            )
            # Match new structure
            self.play(
                ReplacementTransform(table_u.get_columns()[0], table_s.get_columns()[0]),
                ReplacementTransform(table_u.get_columns()[1], table_s.get_columns()[1]),
                ReplacementTransform(table_u.get_columns()[2], table_s.get_columns()[2]),
                FadeIn(table_s.get_columns()[3][0]),
                run_time=0.8
            )
            
            col_values_s = table_s.get_columns()[3][1:]
            status_text.become(Text("Satisfiable", font_size=36, color=YELLOW).to_edge(RIGHT).shift(LEFT * 0.5))
            self.play(Write(col_values_s), FadeIn(status_text, shift=LEFT), run_time=0.8)
            self.wait(max(0, tracker.duration - 2.4))

        script_12 = "We see that each row in the truth table represents a specific interpretation of the propositional variables. So each row can be seen as a possible world or interpretation."
        with self.voiceover(text=script_12) as tracker:
            # Explicitly bound the box from cell (5,1) to cell (5,4)
            # (Note: Row index 5 is the 4th row of actual data below the header)
            row_entries = VGroup(
                table_s.get_entries((5, 1)), table_s.get_entries((5, 2)), 
                table_s.get_entries((5, 3)), table_s.get_entries((5, 4))
            )
            row_box = SurroundingRectangle(row_entries, color=BLUE, buff=0.15) 
            self.play(Create(row_box), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        self.wait(2)

    # --- Helper Functions ---
    def get_detailed_valid_table(self):
        # 8 columns computing: p, q, r, (q->r), p->(q->r), (p^q), (p^q)->r, phi
        content = [
            ["0", "0", "0", "1", "1", "0", "1", "1"],
            ["0", "0", "1", "1", "1", "0", "1", "1"],
            ["0", "1", "0", "0", "1", "0", "1", "1"],
            ["0", "1", "1", "1", "1", "0", "1", "1"],
            ["1", "0", "0", "1", "1", "0", "1", "1"],
            ["1", "0", "1", "1", "1", "0", "1", "1"],
            ["1", "1", "0", "0", "0", "1", "0", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"]
        ]
        col_labels = [
            MathTex("p"), MathTex("q"), MathTex("r"),
            MathTex(r"q \to r"),
            MathTex(r"p \to (q \to r)"),
            MathTex(r"p \land q"),
            MathTex(r"(p \land q) \to r"),
            MathTex(r"\varphi")
        ]
        return MathTable(content, col_labels=col_labels, include_outer_lines=True).scale(0.32)

    def get_8_row_table(self, formula_tex, results):
        content = [
            ["0", "0", "0", results[0]],
            ["0", "0", "1", results[1]],
            ["0", "1", "0", results[2]],
            ["0", "1", "1", results[3]],
            ["1", "0", "0", results[4]],
            ["1", "0", "1", results[5]],
            ["1", "1", "0", results[6]],
            ["1", "1", "1", results[7]]
        ]
        return MathTable(
            content,
            col_labels=[MathTex("p"), MathTex("q"), MathTex("r"), MathTex(formula_tex)],
            include_outer_lines=True
        ).scale(0.35)