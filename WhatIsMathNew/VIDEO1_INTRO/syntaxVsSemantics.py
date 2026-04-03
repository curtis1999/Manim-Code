from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
import numpy as np

class SyntaxVsSemantics(VoiceoverScene, ThreeDScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # ==========================================
        # SETUP: HELPERS & POSITIONS
        # ==========================================
        syntax_center = LEFT * 3.5
        semantics_center = RIGHT * 3.5
        divider = Line(UP * 4, DOWN * 4, stroke_width=2).set_color(WHITE)

        def create_tp_box(label_text="Theorem\nProver", num_inputs=3):
            label = Text(label_text, font_size=16)
            # Make the box square and taller
            rect = Rectangle(width=1.6, height=1.6, color=BLUE, fill_opacity=0.2)
            label.move_to(rect.get_center())
            
            # Circuit-like input lines on the left
            inputs = VGroup()
            spacing = 1.2 / max(1, num_inputs - 1) if num_inputs > 1 else 0
            start_y = 0.6
            for i in range(num_inputs):
                y_pos = start_y - i * spacing
                line = Line(LEFT * 0.4, ORIGIN).next_to(rect, LEFT, buff=0, aligned_edge=UP).shift(DOWN * (0.8 - y_pos))
                inputs.add(line)
            
            # Output line on the right
            output = Line(ORIGIN, RIGHT * 0.4).next_to(rect, RIGHT, buff=0)
            
            return VGroup(rect, label, inputs, output)

        # ==========================================
        # RESTORE PREVIOUS SCENE STATE
        # ==========================================
        # Syntax Side (Left)
        f_title = Text("Syntax (Logic)", font_size=40).move_to(syntax_center + UP * 3)
        sym_funcs = Text("Functions: f, g, +", font_size=28).move_to(syntax_center + UP * 1.5)
        sym_rels = Text("Relations: <, =", font_size=28).next_to(sym_funcs, DOWN, buff=0.3)
        sym_consts = Text("Constants: 0, 1, e", font_size=28).next_to(sym_rels, DOWN, buff=0.3)
        sym_vars = Text("Variables: x, y, z", font_size=28).next_to(sym_consts, DOWN, buff=0.3)
        sym_quants = Text("Quantifiers: ∀, ∃", font_size=28).next_to(sym_vars, DOWN, buff=0.3)
        sym_bools = Text("Connectives: ∧, ∨, →, ¬", font_size=28).next_to(sym_quants, DOWN, buff=0.3)
        
        syntax_group = VGroup(f_title, sym_funcs, sym_rels, sym_consts, sym_vars, sym_quants, sym_bools)

        # Semantics Side (Right)
        s_title = Text("Semantics (Structures)", font_size=40).move_to(semantics_center + UP * 3)
        
        tetrahedron = Tetrahedron().rotate(PI/4, axis=UP).rotate(PI/6, axis=RIGHT)
        cube = Cube().rotate(PI/3, axis=UP).rotate(PI/4, axis=RIGHT)
        octahedron = Octahedron().rotate(PI/5, axis=UP).rotate(PI/3, axis=RIGHT)
        icosahedron = Icosahedron().rotate(PI/4, axis=UP).rotate(PI/7, axis=RIGHT)
        dodecahedron = Dodecahedron().rotate(PI/2.5, axis=UP).rotate(PI/5, axis=RIGHT)
        
        solids = VGroup(tetrahedron, cube, octahedron, icosahedron, dodecahedron)
        solids.set_color_by_gradient(BLUE, TEAL, PURPLE)
        solids.scale(0.6).arrange_in_grid(rows=2, cols=3, buff=1.0).move_to(semantics_center + DOWN * 0.5)

        self.add(divider, syntax_group, s_title, solids)

        # ==========================================
        # SCENE 6: THE THEOREM PROVER
        # ==========================================
        # 1 & 2. Wait to display Theorem Prover, make it square, place below connectives
        tp_logic = create_tp_box("Theorem\nProver").move_to(syntax_center + DOWN * 2.5)

        script_20 = "The syntactical world is governed by a deductive calculus, which we can visualize as a theorem-proving computer."
        with self.voiceover(text=script_20) as tracker:
            self.play(Rotate(solids, angle=PI/8, axis=UP), run_time=tracker.duration * 0.5)
            self.play(FadeIn(tp_logic))
            self.wait(max(0, tracker.duration - 1))

        # Logical vs Non-Logical Split
        log_title = Text("Logical:", font_size=20, color=TEAL).move_to(syntax_center + UP * 2.0 + LEFT * 1)
        log_items = Text("Variables\nQuantifiers\nConnectives", font_size=16).next_to(log_title, DOWN, aligned_edge=LEFT)
        log_group = VGroup(log_title, log_items)

        nlog_title = Text("Non-Logical:", font_size=20, color=ORANGE).move_to(syntax_center + UP * 2.0 + RIGHT * 1)
        nlog_items = Text("Constants\nFunctions\nRelations", font_size=16).next_to(nlog_title, DOWN, aligned_edge=LEFT)
        nlog_group = VGroup(nlog_title, nlog_items)

        script_22 = "The symbols of this system divide into logical and non-logical."
        with self.voiceover(text=script_22) as tracker:
            self.play(
                ReplacementTransform(VGroup(sym_vars, sym_quants, sym_bools), log_group),
                ReplacementTransform(VGroup(sym_consts, sym_funcs, sym_rels), nlog_group),
                run_time=1.5
            )

        # 3. Axioms, pure logic, and mathematical theories branch
        script_23 = "The axioms divide in the same way. If we only feed in the so-called logical axioms --which determine the behaviour of the logical symbols-- into our theorem prover then we are in the world of pure logic."
        
        log_ax_label = Text("Logical\nAxioms", font_size=16, color=TEAL).next_to(tp_logic[2], LEFT)
        valid_formula_label = Text("Logically Valid\nFormulas", font_size=16).next_to(tp_logic[3], RIGHT)
        
        with self.voiceover(text=script_23) as tracker:
            # Shift TP just below symbols and update inputs/outputs
            self.play(tp_logic.animate.move_to(syntax_center + DOWN * 0.5))
            self.play(FadeIn(log_ax_label, shift=RIGHT))
            self.wait(max(0, tracker.duration - 2))

        script_24 = "The outputs of our theorem prover will be logically valid formulas. We can think of this like the operating system, operating in the background of mathematics."
        with self.voiceover(text=script_24) as tracker:
            self.play(FadeIn(valid_formula_label, shift=RIGHT))
            self.wait(max(0, tracker.duration - 1))

        # Branch to Group Theory and Arithmetic
        l_groups = MathTex(r"\mathcal{L}_{\text{groups}}=\{e, \cdot\}", font_size=22, color=ORANGE).move_to(syntax_center + DOWN * 0.5 + LEFT * 1.8)
        l_arith = MathTex(r"\mathcal{L}_{\text{arith}}=\{0, 1, +, \cdot, <\}", font_size=22, color=ORANGE).move_to(syntax_center + DOWN * 0.5 + RIGHT * 1.8)
        
        arrow_l = Arrow(syntax_center + DOWN * 0.5, l_groups.get_top(), buff=0.2)
        arrow_r = Arrow(syntax_center + DOWN * 0.5, l_arith.get_top(), buff=0.2)

        tp_groups = create_tp_box("Theorem\nProver", num_inputs=2).scale(0.6).next_to(l_groups, DOWN, buff=0.3)
        tp_arith = create_tp_box("Theorem\nProver", num_inputs=4).scale(0.6).next_to(l_arith, DOWN, buff=0.3)

        grp_ax_label = Text("Group\nAxioms", font_size=12).next_to(tp_groups[2], LEFT, buff=0.1)
        grp_thm_label = Text("Theorems of\nGroup Theory", font_size=12).next_to(tp_groups[3], RIGHT, buff=0.1)
        
        pa_ax_label = Text("PA\nAxioms", font_size=12).next_to(tp_arith[2], LEFT, buff=0.1)
        pa_thm_label = Text("Theorems of\nArithmetic", font_size=12).next_to(tp_arith[3], RIGHT, buff=0.1)

        script_25 = "Then, to define a mathematical theory, such as group theory, or number theory, we will fix a set of constants, functions and relations, and add axioms which determine the behaviour of these new symbols."
        with self.voiceover(text=script_25) as tracker:
            self.play(FadeOut(tp_logic, log_ax_label, valid_formula_label))
            self.play(GrowArrow(arrow_l), GrowArrow(arrow_r))
            self.play(FadeIn(l_groups), FadeIn(l_arith))
            self.play(
                FadeIn(tp_groups), FadeIn(grp_ax_label), FadeIn(grp_thm_label),
                FadeIn(tp_arith), FadeIn(pa_ax_label), FadeIn(pa_thm_label)
            )
            self.wait(max(0, tracker.duration - 4))

        # Re-merge into general Theory definition
        theory_tp = create_tp_box("Theorem\nProver", num_inputs=3).move_to(syntax_center + DOWN * 2)
        gen_ax_label = Text("Axioms", font_size=16).next_to(theory_tp[2], LEFT)
        theory_label = MathTex(r"\text{Theory}=\{T_0, T_1, \dots\}", font_size=20, color=YELLOW).next_to(theory_tp[3], RIGHT)

        script_26 = "The choice of which symbols and axioms to include lead to different theories. And a theory is just the set of everything which can be outputted by the theorem proving computer."
        with self.voiceover(text=script_26) as tracker:
            self.play(
                ReplacementTransform(VGroup(tp_groups, tp_arith, arrow_l, arrow_r, l_groups, l_arith, grp_ax_label, pa_ax_label, grp_thm_label, pa_thm_label), theory_tp),
                run_time=1.5
            )
            self.play(FadeIn(gen_ax_label), FadeIn(theory_label))
            self.wait(max(0, tracker.duration - 2))

        script_27 = "So, mathematical truth on the syntactic side is given by proofs in a deductive calculus."
        with self.voiceover(text=script_27) as tracker:
            self.play(Circumscribe(theory_tp, color=BLUE, time_width=0.5))
            self.wait(max(0, tracker.duration - 1))

        # ==========================================
        # SCENE 7: SEMANTICS & TARSKI
        # ==========================================
        # 4. Keep split screen visible during semantic transition
        script_28 = "On the semantic side, truth is given by Tarski's definition: a sentence is true if and only if it holds in every model. Let us make this precise — it may feel technical for a moment, but it leads somewhere interesting."
        with self.voiceover(text=script_28) as tracker:
            self.play(Rotate(solids, angle=PI/4, axis=UP), run_time=tracker.duration)

        # Now fade out syntax to focus on semantics
        self.play(FadeOut(divider, f_title, log_group, nlog_group, theory_tp, gen_ax_label, theory_label, s_title, solids), run_time=1.5)

        m_tex = MathTex(
            r"\mathcal{M}", r" = (", 
            r"M", r", ", 
            r"c_0^\mathcal{M}, \dots", r", ", 
            r"f_0^\mathcal{M}, \dots", r", ", 
            r"R_0^\mathcal{M}, \dots", 
            r")", font_size=44
        ).move_to(UP * 1.5)

        # 5. Line up domain label
        domain_label = Text("consisting of a domain\nor universe", font_size=20, color=YELLOW).next_to(m_tex, DOWN, buff=0.8).shift(LEFT*2)
        domain_arrow = Arrow(domain_label.get_top(), m_tex[2].get_bottom(), color=YELLOW)

        script_29 = "Formally, a structure — which we denote with the symbol M — is given by a tuple consisting of a domain, or universe, together with interpretations of the constants, functions, and relations in the language."
        with self.voiceover(text=script_29) as tracker:
            self.play(Write(m_tex), run_time=1.5)
            self.play(m_tex[2].animate.set_color(YELLOW), FadeIn(domain_label), GrowArrow(domain_arrow), run_time=1)
            self.play(
                m_tex[2].animate.set_color(WHITE), FadeOut(domain_label, domain_arrow),
                m_tex[4].animate.set_color(TEAL), # Constants
                m_tex[6].animate.set_color(ORANGE), # Functions
                m_tex[8].animate.set_color(PINK), # Relations
                run_time=1
            )
            self.play(
                m_tex[4].animate.set_color(WHITE),
                m_tex[6].animate.set_color(WHITE),
                m_tex[8].animate.set_color(WHITE),
                run_time=0.5
            )

        # 5.5 Add successor function S to \mathcal{N}
        n_tex = MathTex(
            r"\mathcal{N}", r" = (", 
            r"\mathbb{N}", r", ", 
            r"0^\mathcal{N}", r", ", r"1^\mathcal{N}", r", ", 
            r"S^\mathcal{N}", r", ", r"+^\mathcal{N}", r", ", r"\cdot^\mathcal{N}", r", ", 
            r"<^\mathcal{N}", 
            r")", font_size=44
        ).move_to(UP * 1.5)

        script_30 = "To define the natural numbers with addition and multiplication, for instance, we need at least the symbols zero, one, the successor function, addition, multiplication, and the less-than relation."
        with self.voiceover(text=script_30) as tracker:
            self.play(ReplacementTransform(m_tex, n_tex), run_time=1.5)

        num_line = NumberLine(x_range=[0, 6, 1], length=8, include_numbers=True, font_size=24).move_to(DOWN * 1)

        # 6. Arrows start from distinct places
        script_31 = "We interpret zero and one as expected."
        with self.voiceover(text=script_31) as tracker:
            self.play(Create(num_line), run_time=1)
            # Arrows distinctly below 0^N and 1^N
            a_0 = Arrow(n_tex[4].get_bottom(), num_line.number_to_point(0), color=YELLOW)
            a_1 = Arrow(n_tex[6].get_bottom(), num_line.number_to_point(1), color=YELLOW)
            self.play(GrowArrow(a_0), GrowArrow(a_1), n_tex[4].animate.set_color(YELLOW), n_tex[6].animate.set_color(YELLOW), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        # 7. Skip the "functions as computer programs" part directly to relations
        script_33 = "The interpretation of functions and relations is a bit more abstract. For example, the less-than relation is interpreted as the set of all pairs (a, b) such that a is less than b."
        with self.voiceover(text=script_33) as tracker:
            self.play(FadeOut(a_0, a_1), n_tex[4].animate.set_color(WHITE), n_tex[6].animate.set_color(WHITE))
            less_set = MathTex(r"<^\mathcal{N} = \{(0,1), (0,2), (1,2), \dots \}", font_size=32, color=PINK).move_to(DOWN * 2.5)
            rel_arrow = Arrow(n_tex[14].get_bottom(), less_set.get_top(), color=PINK)
            self.play(n_tex[14].animate.set_color(PINK), GrowArrow(rel_arrow), Write(less_set), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        script_34 = "Note that functions are just special relations where the output is uniquely determined by the inputs."
        with self.voiceover(text=script_34) as tracker:
            self.wait(tracker.duration)

        # 8. Add arrow from S to S^N
        script_35 = "So the successor function would map to the set of all pair of numbers such that the second is one greater than the first."
        with self.voiceover(text=script_35) as tracker:
            self.play(FadeOut(less_set, rel_arrow), n_tex[14].animate.set_color(WHITE))
            succ_set = MathTex(r"S^\mathcal{N} = \{(0,1), (1,2), (2,3), \dots \}", font_size=32, color=TEAL).move_to(DOWN * 2.5)
            succ_arrow = Arrow(n_tex[8].get_bottom(), succ_set.get_top(), color=TEAL)
            self.play(n_tex[8].animate.set_color(TEAL), GrowArrow(succ_arrow), FadeIn(succ_set, shift=UP), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        # 9. Expand examples for +
        script_36 = "And the addition function is formally the set of all triples (a, b, c) such that a plus b equals c."
        with self.voiceover(text=script_36) as tracker:
            self.play(FadeOut(succ_set, succ_arrow), n_tex[8].animate.set_color(WHITE))
            add_set_base = MathTex(r"+^\mathcal{N} = \{(0,0,0), (1,0,1), (0,1,1), (2,0,2), (1,1,2), (0,2,2), (2,1,3), (1,2,3), \dots\}", font_size=24, color=ORANGE).move_to(DOWN * 2.5)
            add_arrow = Arrow(n_tex[10].get_bottom(), add_set_base.get_top(), color=ORANGE)
            self.play(n_tex[10].animate.set_color(ORANGE), GrowArrow(add_arrow), Write(add_set_base), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        # ==========================================
        # SCENE 8: EVALUATING 1+2=3
        # ==========================================
        self.play(FadeOut(add_arrow, add_set_base), n_tex[10].animate.set_color(WHITE))
        
        eq_123 = MathTex("1", "+", "2", "=", "3", font_size=48).move_to(UP * 0.2)
        
        script_37 = "To evaluate a simple equation like one plus two equals three, we map the constants as expected"
        with self.voiceover(text=script_37) as tracker:
            self.play(FadeIn(eq_123), run_time=1)
            
            a1 = CurvedArrow(eq_123[0].get_bottom(), num_line.number_to_point(1) + UP*0.2, angle=PI/4, color=YELLOW)
            a2 = CurvedArrow(eq_123[2].get_bottom(), num_line.number_to_point(2) + UP*0.2, angle=PI/4, color=YELLOW)
            a3 = CurvedArrow(eq_123[4].get_bottom(), num_line.number_to_point(3) + UP*0.2, angle=PI/4, color=YELLOW)
            
            self.play(Create(a1), Create(a2), Create(a3), run_time=1.5)
            self.wait(max(0, tracker.duration - 2.5))

        script_38 = "and then check whether the resulting triple belongs to the addition relation."
        with self.voiceover(text=script_38) as tracker:
            add_set_full = MathTex(r"+^\mathcal{N} = \{(0,0,0), \dots, ", r"(1,2,3)", r", \dots\}", font_size=32).move_to(DOWN * 2.5)
            self.play(FadeIn(add_set_full), run_time=1)
            
            # Highlight (1,2,3) to show the lookup succeeds
            self.play(add_set_full[1].animate.set_color(GREEN).scale(1.2), run_time=0.5)
            self.play(Indicate(eq_123, color=GREEN), run_time=1)
            self.wait(max(0, tracker.duration - 2.5))