from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
import numpy as np

# ==========================================
# SCENE 9: INCOMPLETE THEORIES & DLOWE
# ==========================================
class IncompleteTheoriesAndDLOWE(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # ------------------------------------------
        # 1. RECREATE SCENE SETUP
        # ------------------------------------------
        divider = Line(UP * 4, DOWN * 4, stroke_width=2).set_color(WHITE)
        self.add(divider)

        syntax_center = LEFT * 3.5
        semantics_center = RIGHT * 3.5

        # Syntax Left
        phi_tex = MathTex(r"\varphi: \forall x,y,z (Exy \land Eyz \to Exz)", font_size=28, color=TEAL)
        psi_tex = MathTex(r"\psi: \forall x \neg Exx", font_size=28, color=ORANGE)
        sigma_tex = MathTex(r"\Sigma = \{\varphi, \psi\}", font_size=36, color=YELLOW)
        
        syntax_group = VGroup(sigma_tex, phi_tex, psi_tex).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(syntax_center + UP * 2.5)
        self.add(syntax_group)

        # Semantics Right (Abstract Mod Box from previous scenes)
        mod_sigma = MathTex(r"Mod(\Sigma)", font_size=36, color=YELLOW).move_to(semantics_center + UP * 3)
        valid_graphs = VGroup(
            self.get_mini_graph("line"), self.get_mini_graph("tree"), self.get_mini_graph("bool_alg"),
            self.get_mini_graph("disconnected"), self.get_mini_graph("lattice"), self.get_mini_graph("pentagon_dag")
        )
        for i, g in enumerate(valid_graphs):
            row = i // 3
            col = i % 3
            g.move_to(semantics_center + UP * 2 + DOWN * (row * 0.8) + LEFT * 1.5 + RIGHT * (col * 1.2))
        
        mod_box = SurroundingRectangle(valid_graphs, color=YELLOW, buff=0.2)
        self.add(mod_sigma, valid_graphs, mod_box)

        # ------------------------------------------
        # 2. NATURAL NUMBER LINE MODEL
        # ------------------------------------------
        script_1 = "Returning to our example of Sigma equals phi, psi, we can easily see that this set is not complete."
        with self.voiceover(text=script_1) as tracker:
            self.wait(max(0.1, tracker.duration))

        # Build Number Line
        n_line = NumberLine(x_range=[0, 6, 1], length=5, include_numbers=True, font_size=24).move_to(semantics_center + DOWN * 0.2)
        n_label = MathTex(r"\mathbb{N}", font_size=32).next_to(n_line, LEFT)
        n_arrow = Arrow(mod_box.get_bottom(), n_line.get_top(), color=WHITE, buff=0.1)

        script_2 = "We see that the natural number line is a model of Sigma where E is interpreted as the less than relation."
        with self.voiceover(text=script_2) as tracker:
            self.play(Create(n_line), FadeIn(n_label), GrowArrow(n_arrow), run_time=1.5)
            self.wait(max(0.1, tracker.duration - 1.5))

        # Transitivity arrows on the number line
        arr_1_3 = CurvedArrow(n_line.number_to_point(1), n_line.number_to_point(3), angle=-PI/3, color=TEAL)
        arr_3_5 = CurvedArrow(n_line.number_to_point(3), n_line.number_to_point(5), angle=-PI/3, color=TEAL)
        arr_1_5 = CurvedArrow(n_line.number_to_point(1), n_line.number_to_point(5), angle=PI/3, color=YELLOW)

        script_3 = "Since for all numbers x, y, z, if x is less than y and y is less than z, then x is less than z,"
        with self.voiceover(text=script_3) as tracker:
            self.play(Create(arr_1_3), run_time=0.5)
            self.play(Create(arr_3_5), run_time=0.5)
            self.play(Create(arr_1_5), run_time=1)
            self.wait(max(0.1, tracker.duration - 2))

        script_4 = "and no number is less than itself."
        with self.voiceover(text=script_4) as tracker:
            self.wait(tracker.duration)

        # ------------------------------------------
        # 3. TREE MODEL
        # ------------------------------------------
        script_5 = "However, a tree is also a model of Sigma where we interpret E based on the direct-extension relation."
        with self.voiceover(text=script_5) as tracker:
            self.play(FadeOut(arr_1_3), FadeOut(arr_3_5), FadeOut(arr_1_5), FadeOut(n_arrow), run_time=1)
            n_line_group = VGroup(n_line, n_label)
            self.play(n_line_group.animate.shift(UP * 0.8).scale(0.8), run_time=1)
            
            # Build Tree
            t_root = Dot(semantics_center + DOWN * 0.5)
            t_l = Dot(semantics_center + DOWN * 1.5 + LEFT * 1)
            t_r = Dot(semantics_center + DOWN * 1.5 + RIGHT * 1)
            t_ll = Dot(semantics_center + DOWN * 2.5 + LEFT * 1.5)
            t_lr = Dot(semantics_center + DOWN * 2.5 + LEFT * 0.5)
            t_rl = Dot(semantics_center + DOWN * 2.5 + RIGHT * 0.5)
            
            tree_edges = VGroup(
                Arrow(t_root, t_l, buff=0.1), Arrow(t_root, t_r, buff=0.1),
                Arrow(t_l, t_ll, buff=0.1), Arrow(t_l, t_lr, buff=0.1), Arrow(t_r, t_rl, buff=0.1)
            )
            tree_nodes = VGroup(t_root, t_l, t_r, t_ll, t_lr, t_rl)
            tree_group = VGroup(tree_edges, tree_nodes)
            
            self.play(FadeIn(tree_group, shift=UP), run_time=1)
            self.wait(max(0.1, tracker.duration - 3))

        script_6 = "Since if a extends b, and b extends c, then a must extend c. And no node is a direct extension of itself."
        with self.voiceover(text=script_6) as tracker:
            label_a = Text("a", font_size=20).next_to(t_root, UP, buff=0.1)
            label_b = Text("b", font_size=20).next_to(t_l, LEFT, buff=0.1)
            label_c = Text("c", font_size=20).next_to(t_ll, DOWN, buff=0.1)
            
            arr_ac = Arrow(t_root, t_ll, buff=0.1, color=YELLOW, path_arc=0.3)
            
            self.play(FadeIn(label_a), FadeIn(label_b), FadeIn(label_c), run_time=0.5)
            self.play(tree_edges[0].animate.set_color(TEAL), tree_edges[2].animate.set_color(TEAL), run_time=0.5)
            self.play(GrowArrow(arr_ac), run_time=1)
            self.wait(max(0.1, tracker.duration - 2))

        # ------------------------------------------
        # 4. TOTALITY (\chi)
        # ------------------------------------------
        chi_tex = MathTex(r"\chi: \forall x,y (Exy \lor Eyx \lor x \doteq y)", font_size=28, color=PINK)
        
        script_7 = "And clearly, we can find a sentence chi to differentiate between a tree and a number line. For example, we could add this sentence, expressing totality, meaning that all elements are related by the edge relation."
        with self.voiceover(text=script_7) as tracker:
            chi_tex.next_to(psi_tex, DOWN, buff=0.4).align_to(phi_tex, LEFT)
            self.play(Write(chi_tex), run_time=1.5)
            self.wait(max(0.1, tracker.duration - 1.5))

        script_8 = "We see that our tree is not a model of this, since two different elements at the same level are not comparable by the extension relation."
        with self.voiceover(text=script_8) as tracker:
            # Circle t_l and t_r
            incomp_circle = Ellipse(width=3, height=1, color=RED).move_to(semantics_center + DOWN * 1.5)
            self.play(Create(incomp_circle), run_time=1)
            self.wait(max(0.1, tracker.duration - 1))

        # ------------------------------------------
        # 5. NEW LINEAR ORDER MODELS
        # ------------------------------------------
        sigma_3 = MathTex(r"\Sigma = \{\varphi, \psi, \chi\}", font_size=36, color=YELLOW).move_to(syntax_center + UP * 2.5)

        script_9 = "So, we could add chi as another axiom to our set Sigma."
        with self.voiceover(text=script_9) as tracker:
            self.play(
                ReplacementTransform(sigma_tex, sigma_3),
                FadeOut(tree_group), FadeOut(label_a), FadeOut(label_b), FadeOut(label_c), FadeOut(arr_ac), FadeOut(incomp_circle),
                FadeOut(valid_graphs), FadeOut(mod_box), FadeOut(n_line_group),
                run_time=1.5
            )
            self.wait(max(0.1, tracker.duration - 1.5))

        # Build 4 Linear Orders
        lo_1 = VGroup(Dot(LEFT*1), Dot(ORIGIN), Dot(RIGHT*1))
        lo_1.add(Arrow(lo_1[0], lo_1[1], buff=0.1), Arrow(lo_1[1], lo_1[2], buff=0.1))
        
        lo_2 = NumberLine(x_range=[0, 5, 1], length=4, include_numbers=False)
        lo_2_label = MathTex(r"\mathbb{N} \to", font_size=24).next_to(lo_2, LEFT)
        
        # Ruler-style Rationals
        lo_3 = Line(LEFT*2, RIGHT*2)
        lo_3_ticks = VGroup()
        for i in range(33): # 4 units * 8 segments
            h = 0.2 if i % 8 == 0 else 0.08
            tick = Line(DOWN*h/2, UP*h/2).move_to(lo_3.get_left() + RIGHT * (i * 4/32))
            lo_3_ticks.add(tick)
        lo_3_group = VGroup(lo_3, lo_3_ticks)
        lo_3_label = MathTex(r"\mathbb{Q}", font_size=24).next_to(lo_3_group, LEFT)
        
        # Real segment (0,1)
        lo_4 = Line(LEFT*2, RIGHT*2, stroke_width=6, color=BLUE)
        c1 = Circle(radius=0.08, color=BLUE, fill_opacity=0).move_to(lo_4.get_left())
        c2 = Circle(radius=0.08, color=BLUE, fill_opacity=0).move_to(lo_4.get_right())
        lo_4_group = VGroup(lo_4, c1, c2)
        lo_4_label = MathTex(r"\mathbb{R}_{(0,1)}", font_size=24).next_to(lo_4_group, LEFT)
        
        linear_models = VGroup(
            VGroup(lo_1).move_to(semantics_center + UP * 1.5),
            VGroup(lo_2_label, lo_2).move_to(semantics_center + UP * 0.5),
            VGroup(lo_3_label, lo_3_group).move_to(semantics_center + DOWN * 0.5),
            VGroup(lo_4_label, lo_4_group).move_to(semantics_center + DOWN * 1.5)
        )
        lo_dots = MathTex(r"\vdots").move_to(semantics_center + DOWN * 2.5)
        lo_box = SurroundingRectangle(VGroup(linear_models, lo_dots), color=YELLOW, buff=0.2)

        script_10 = "So Sigma now contains phi, psi, chi, and Mod Sigma is the set of linearly ordered sets."
        with self.voiceover(text=script_10) as tracker:
            self.play(FadeIn(linear_models, shift=UP), FadeIn(lo_dots), Create(lo_box), run_time=1.5)
            self.wait(max(0.1, tracker.duration - 1.5))

        # ------------------------------------------
        # 6. DENSITY (\theta)
        # ------------------------------------------
        theta_tex = MathTex(r"\theta: \forall x,y (Exy \to \exists z (Exz \land Ezy))", font_size=28, color=GREEN)
        
        script_11 = "However, the theory of Sigma is still not complete, since for example both the natural numbers and the rational numbers satisfy these axioms under the less than relation, and we can differentiate the rational numbers from the natural numbers by this sentence theta expressing density."
        with self.voiceover(text=script_11) as tracker:
            theta_tex.next_to(chi_tex, DOWN, buff=0.4).align_to(phi_tex, LEFT)
            self.play(Write(theta_tex), run_time=2)
            self.wait(max(0.1, tracker.duration - 2))

        script_12 = "Meaning that for all x, y, if x is less than y, then there exists a z such that x is less than z and z is less than y."
        with self.voiceover(text=script_12) as tracker:
            self.wait(tracker.duration)

        script_13 = "This is not true of the natural numbers, as there is no natural number in between 0 and 1 for example."
        with self.voiceover(text=script_13) as tracker:
            # Emphasize gap in N
            gap_arrow = Arrow(UP, DOWN, color=RED).scale(0.5).next_to(lo_2.point_from_proportion(0.125), UP, buff=0.1) # Between 0 and 1
            cross = Cross(gap_arrow, stroke_color=RED)
            self.play(GrowArrow(gap_arrow), Create(cross), run_time=1)
            self.wait(max(0.1, tracker.duration - 1))

        script_14 = "However, given any fractional number, we can always find a number in between it."
        with self.voiceover(text=script_14) as tracker:
            self.play(FadeOut(gap_arrow), FadeOut(cross), run_time=0.5)
            # Emphasize density in Q
            q_dot = Dot(lo_3.point_from_proportion(0.125), color=YELLOW, radius=0.06)
            q_arrow = Arrow(UP, DOWN, color=YELLOW).scale(0.5).next_to(q_dot, UP, buff=0.1)
            self.play(FadeIn(q_dot), GrowArrow(q_arrow), run_time=1)
            self.wait(max(0.1, tracker.duration - 1.5))
            self.play(FadeOut(q_dot), FadeOut(q_arrow), run_time=0.5)

        # ------------------------------------------
        # 7. DLOWE & CANTOR
        # ------------------------------------------
        xi_tex = MathTex(r"\xi: \forall x \exists y (Eyx)", font_size=28, color=PURPLE)
        zeta_tex = MathTex(r"\zeta: \forall x \exists y (Exy)", font_size=28, color=PURPLE)
        
        sigma_dlowe = MathTex(r"\Sigma_{DLOWE} = \{\varphi, \psi, \chi, \theta, \xi, \zeta\}", font_size=32, color=YELLOW).move_to(syntax_center + UP * 2.5)

        script_15 = "If we add theta to our set of axioms Sigma, and we add two more axioms expressing that there are no endpoints, then we get the theory of DLOWE."
        with self.voiceover(text=script_15) as tracker:
            xi_tex.next_to(theta_tex, DOWN, buff=0.2).align_to(phi_tex, LEFT)
            zeta_tex.next_to(xi_tex, DOWN, buff=0.2).align_to(phi_tex, LEFT)
            self.play(Write(xi_tex), Write(zeta_tex), run_time=1)
            
            # Shrink box to Q and R
            self.play(
                ReplacementTransform(sigma_3, sigma_dlowe),
                FadeOut(linear_models[0]), FadeOut(linear_models[1]),
                linear_models[2].animate.move_to(semantics_center + UP * 0.5),
                linear_models[3].animate.move_to(semantics_center + DOWN * 0.5),
                lo_dots.animate.move_to(semantics_center + DOWN * 1.5),
                run_time=1.5
            )
            
            # Recreate box tightly
            dlowe_models = VGroup(linear_models[2], linear_models[3], lo_dots)
            self.play(lo_box.animate.surround(dlowe_models, buff=0.2), run_time=0.5)
            self.wait(max(0.1, tracker.duration - 3))

        countable_title = Text("Countable DLOWE", font_size=32, color=TEAL).next_to(lo_box, UP, buff=0.2)

        script_16 = "In 1895 Georg Cantor proved that all countable dense linear orderings without endpoints are isomorphic,"
        with self.voiceover(text=script_16) as tracker:
            self.play(Write(countable_title), run_time=1)
            # Remove R and ellipses, isolate Q
            self.play(
                FadeOut(linear_models[3]), FadeOut(lo_dots),
                linear_models[2].animate.move_to(semantics_center),
                run_time=1
            )
            self.play(lo_box.animate.surround(linear_models[2], buff=0.3), run_time=0.5)
            self.wait(max(0.1, tracker.duration - 2.5))

        script_17 = "which technically just means that there is an order preserving map between them, but essentially means that there is a unique countable set which satisfies this set of axioms, and this set is the rational numbers."
        with self.voiceover(text=script_17) as tracker:
            self.wait(tracker.duration)

        script_18 = "So, this set of axioms here, is a close approximation of the structure of the fractional number line."
        with self.voiceover(text=script_18) as tracker:
            # Highlight axioms on left
            ax_box = SurroundingRectangle(VGroup(phi_tex, psi_tex, chi_tex, theta_tex, xi_tex, zeta_tex), color=YELLOW, buff=0.1)
            self.play(Create(ax_box), run_time=1)
            self.wait(max(0.1, tracker.duration - 1))

        script_19 = "However, it is not perfect as the real number line also satisfies the DLOWE axioms."
        with self.voiceover(text=script_19) as tracker:
            self.play(FadeOut(countable_title), FadeOut(ax_box), run_time=0.5)
            # Put R and ellipses back
            self.play(linear_models[2].animate.move_to(semantics_center + UP * 0.5), run_time=0.5)
            linear_models[3].move_to(semantics_center + DOWN * 0.5)
            lo_dots.move_to(semantics_center + DOWN * 1.5)
            
            self.play(FadeIn(linear_models[3]), FadeIn(lo_dots), run_time=1)
            self.play(lo_box.animate.surround(VGroup(linear_models[2], linear_models[3], lo_dots), buff=0.2), run_time=0.5)
            self.wait(max(0.1, tracker.duration - 2.5))

        script_20 = "But this set of axioms is as good as we can hope to do: Sigma is a complete axiomatization of the theory of DLOWE."
        with self.voiceover(text=script_20) as tracker:
            self.play(Indicate(sigma_dlowe, color=GREEN, scale_factor=1.1), run_time=1.5)
            self.wait(max(0.1, tracker.duration - 1.5))

        self.wait(2)


    # ---------------------------------------------------
    # Helper Function 
    # ---------------------------------------------------
    def get_mini_graph(self, g_type):
        group = VGroup()
        if g_type == "line": 
            n1, n2, n3 = Dot(LEFT*0.5), Dot(ORIGIN), Dot(RIGHT*0.5)
            e1, e2 = Arrow(n1, n2, buff=0.05), Arrow(n2, n3, buff=0.05)
            e3 = Arrow(n1, n3, buff=0.05, path_arc=-0.6)
            group.add(n1, n2, n3, e1, e2, e3)
        elif g_type == "tree": 
            n1, n2, n3 = Dot(UP*0.3), Dot(LEFT*0.4 + DOWN*0.3), Dot(RIGHT*0.4 + DOWN*0.3)
            e1, e2 = Arrow(n1, n2, buff=0.05), Arrow(n1, n3, buff=0.05)
            group.add(n1, n2, n3, e1, e2)
        elif g_type == "bool_alg": 
            n0 = Dot(DOWN*0.5)
            n1a, n1b, n1c = Dot(LEFT*0.5), Dot(ORIGIN), Dot(RIGHT*0.5)
            n3 = Dot(UP*0.5)
            edges = [Arrow(n0,n1a,buff=0), Arrow(n0,n1b,buff=0), Arrow(n0,n1c,buff=0),
                     Arrow(n1a,n3,buff=0), Arrow(n1b,n3,buff=0), Arrow(n1c,n3,buff=0),
                     Arrow(n0,n3,buff=0.05, path_arc=0.8, stroke_opacity=0.5)]
            group.add(n0, n1a, n1b, n1c, n3, *edges)
        elif g_type == "disconnected": 
            n1, n2 = Dot(LEFT*0.4), Dot(RIGHT*0.4)
            n3, n4 = Dot(UP*0.4), Dot(DOWN*0.4)
            e1 = Arrow(n3, n4, buff=0.05)
            group.add(n1, n2, n3, n4, e1)
        elif g_type == "lattice": 
            n1, n2, n3, n4 = Dot(UP*0.4), Dot(LEFT*0.4), Dot(RIGHT*0.4), Dot(DOWN*0.4)
            e1, e2 = Arrow(n1, n2, buff=0.05), Arrow(n1, n3, buff=0.05)
            e3, e4 = Arrow(n2, n4, buff=0.05), Arrow(n3, n4, buff=0.05)
            e5 = Arrow(n1, n4, buff=0.05, path_arc=0.3)
            group.add(n1, n2, n3, n4, e1, e2, e3, e4, e5)
        elif g_type == "pentagon_dag": 
            n1, n2, n3 = Dot(UP*0.4), Dot(LEFT*0.4 + UP*0.1), Dot(RIGHT*0.4 + UP*0.1)
            n4, n5 = Dot(LEFT*0.2 + DOWN*0.4), Dot(RIGHT*0.2 + DOWN*0.4)
            edges = [Arrow(n1,n2,buff=0.05), Arrow(n1,n3,buff=0.05), Arrow(n2,n4,buff=0.05), Arrow(n3,n5,buff=0.05),
                     Arrow(n1,n4,buff=0.05), Arrow(n1,n5,buff=0.05)]
            group.add(n1, n2, n3, n4, n5, *edges)
            
        return group.scale(0.55)