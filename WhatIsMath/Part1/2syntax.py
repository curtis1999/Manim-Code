from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
import networkx as nx
import numpy as np
import random
# ==========================================
# SCENE 2: SYNTAX VS SEMANTICS
# ==========================================
class SyntaxVsSemantics(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        SYNTAX_COLOR = WHITE 
        SEMANTICS_HIGHLIGHT = YELLOW 

        # --- SCENE SETUP ---
        divider = Line(UP * 4, DOWN * 4, stroke_width=2).set_color(SYNTAX_COLOR)
        self.add(divider)

        syntax_center = LEFT * 3.5
        semantics_center = RIGHT * 3.5

        title_syntax = Text("Syntax", font_size=40, weight=BOLD).set_color(WHITE).move_to(syntax_center + UP * 3.3)
        title_semantics = Text("Semantics", font_size=40, weight=BOLD).set_color(WHITE).move_to(semantics_center + UP * 3.3)
        
        # Start by showing ONLY titles and divider
        self.add(title_syntax, title_semantics)

        # --- PRE-BUILD SYNTAX ELEMENTS ---
        syntax_title = MathTex(r"\Sigma \vdash \varphi", font_size=50).set_color(SYNTAX_COLOR).next_to(title_syntax, DOWN, buff=0.4)
        alphabet_tex = MathTex(r"\mathbb{A}: \{ \neg, \land, \lor, \to, \forall, \exists, =, x, y, z, P, Q... \}", font_size=24).next_to(syntax_title, DOWN, buff=0.5)
        
        axioms_group = VGroup(
            MathTex(r"\text{A1: } \varphi \to (\psi \to \varphi)", font_size=22),
            MathTex(r"\text{A2: } (\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))", font_size=22),
            MathTex(r"\text{A3: } (\neg \varphi \to \neg \psi) \to ((\neg \varphi \to \psi) \to \varphi)", font_size=22),
            MathTex(r"\text{A4: } \forall x \varphi \to \varphi(_{t}^{x})", font_size=22),
            MathTex(r"\text{A5: } \forall x (\varphi \to \psi) \to (\forall x \varphi \to \forall x \psi)", font_size=22),
            MathTex(r"\text{A6: } \varphi \to \forall x \varphi", font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).set_color(SYNTAX_COLOR)
        
        mp_tex = MathTex(r"\frac{\varphi, \varphi \to \psi}{\psi}", font_size=36).set_color(SYNTAX_COLOR)
        rules_group = VGroup(axioms_group, mp_tex).arrange(RIGHT, buff=0.5).next_to(alphabet_tex, DOWN, buff=0.5).shift(LEFT * 0.2) 
        proof_tree = self.get_simple_proof_tree().scale(0.5).next_to(rules_group, DOWN, buff=0.4)

        left_side_objects = VGroup(syntax_title, alphabet_tex, rules_group, proof_tree)

        # --- PRE-BUILD SEMANTICS ELEMENTS ---
        semantics_title = MathTex(r"\Sigma \models \varphi", font_size=50).set_color(BLUE).next_to(title_semantics, DOWN, buff=0.4)
        num_line = NumberLine(x_range=[-3, 3, 1], length=4, include_numbers=True, font_size=24).move_to(semantics_center + UP * 1.2).set_color(BLUE_B)
        dag = self.get_dag_graph().scale(0.5).move_to(semantics_center + DOWN * 0.5 + LEFT * 1.5)
        tree_graph = self.get_tree_graph().scale(0.5).move_to(semantics_center + DOWN * 0.5 + RIGHT * 1.5)
        farey = self.get_farey_graph(radius=1.2, depth=2).move_to(semantics_center + DOWN * 2.5 + RIGHT * 1.5)
        manifold_2d = ParametricFunction(
            lambda t: np.array([1.2 * np.sin(2 * t), 1.2 * np.sin(t), 0]), 
            t_range=[0, TAU], color=GREEN_D
        ).set_stroke(width=3).move_to(semantics_center + DOWN * 2.5 + LEFT * 1.5)
        
        right_side_objects = VGroup(semantics_title, num_line, dag, tree_graph, manifold_2d, farey)

        # --- ANIMATIONS & VOICEOVER ---
        
        script_1 = (
            "In this video we cover two different ways of looking at math. "
            "On the one side, we have the mechanical world of syntax, and on the "
            "other we have the intuitive world of semantics."
        )
        with self.voiceover(text=script_1) as tracker:
            # Display everything at once as you begin speaking
            self.play(
                FadeIn(left_side_objects, lag_ratio=0.05),
                FadeIn(right_side_objects, lag_ratio=0.05),
                run_time=tracker.duration
            )

        script_2 = (
            "Each side has its own definition of truth. In the world of syntax, "
            "a statement is true if and only if we have a formal proof of it. "
            "This relation means that there is a proof of phi assuming all of Sigma."
        )
        with self.voiceover(text=script_2) as tracker:
            # Highlight early in the sentence
            self.play(syntax_title.animate.set_color(SEMANTICS_HIGHLIGHT), run_time=1)
            # Wait while you finish the sentence
            self.wait(max(0, tracker.duration - 2))
            # Fade out the highlight right as the sentence ends
            self.play(syntax_title.animate.set_color(SYNTAX_COLOR), run_time=1)

        script_3 = (
            "In the semantical side, truth is given by Tarski's definition of truth. "
            "Namely that something is true if and only if it is true in all models. "
            "We denote by this relation, that in all possible worlds where Sigma is "
            "satisfied, phi is also satisfied."
        )
        with self.voiceover(text=script_3) as tracker:
            # Highlight early in the sentence
            self.play(semantics_title.animate.set_color(SEMANTICS_HIGHLIGHT), run_time=1)
            # Wait while you finish the sentence
            self.wait(max(0, tracker.duration - 2))
            # Fade out the highlight back to its original blue
            self.play(semantics_title.animate.set_color(BLUE), run_time=1)

        self.wait(1)

    # --- Helper Functions ---
    def get_simple_proof_tree(self):
        phi = MathTex(r"\varphi", font_size=40)
        l1_left = MathTex(r"\psi", font_size=30).move_to(phi.get_center() + UP*1 + LEFT*0.8)
        l1_right = MathTex(r"\psi \to \varphi", font_size=30).move_to(phi.get_center() + UP*1 + RIGHT*0.8)
        line1L = Line(phi.get_top(), l1_left.get_bottom(), buff=0.1)
        line1R = Line(phi.get_top(), l1_right.get_bottom(), buff=0.1)
        l2_1 = MathTex(r"A_1", font_size=24).move_to(l1_left.get_center() + UP*0.8 + LEFT*0.4)
        l2_2 = MathTex(r"A_2", font_size=24).move_to(l1_left.get_center() + UP*0.8 + RIGHT*0.4)
        line2L = Line(l1_left.get_top(), l2_1.get_bottom(), buff=0.1)
        line2R = Line(l1_left.get_top(), l2_2.get_bottom(), buff=0.1)
        l2_3 = MathTex(r"\dots", font_size=24).move_to(l1_right.get_center() + UP*0.8)
        line2C = Line(l1_right.get_top(), l2_3.get_bottom(), buff=0.1)
        return VGroup(phi, l1_left, l1_right, line1L, line1R, l2_1, l2_2, l2_3, line2L, line2R, line2C)

    def get_dag_graph(self):
        nx_graph = nx.DiGraph()
        nx_graph.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])
        return Graph(list(nx_graph.nodes), list(nx_graph.edges), layout="spring", labels=True, vertex_config={"radius": 0.15, "color": BLUE_A}, edge_config={"color": GREY, "stroke_width": 2})

    def get_tree_graph(self):
        nx_tree = nx.balanced_tree(r=2, h=3)
        return Graph(list(nx_tree.nodes), list(nx_tree.edges), layout="kamada_kawai", vertex_config={"radius": 0.08, "color": GREEN_B}, edge_config={"color": GREEN_E, "stroke_width": 1})

    def get_farey_graph(self, radius=2, depth=3):
        farey_group = VGroup()
        farey_group.add(Circle(radius=radius, color=WHITE, stroke_opacity=0.5))
        def add_arcs(a, b, level):
            if level == 0: return
            mid = (a + b) / 2
            p1 = np.array([radius * np.cos(a), radius * np.sin(a), 0])
            p2 = np.array([radius * np.cos(b), radius * np.sin(b), 0])
            arc = ArcBetweenPoints(p1, p2, angle=-PI/2) 
            arc.set_stroke(color=RED_A, width=2 * (level/depth), opacity=0.8)
            farey_group.add(arc)
            add_arcs(a, mid, level - 1)
            add_arcs(mid, b, level - 1)
        sectors = [0, PI/2, PI, 3*PI/2, 2*PI]
        for i in range(len(sectors)-1):
            add_arcs(sectors[i], sectors[i+1], depth)
        return farey_group
    
