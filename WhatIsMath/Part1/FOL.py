from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
import networkx as nx
import numpy as np

# ==========================================
# SCENE 5: TRANSITION TO FIRST-ORDER LOGIC
# ==========================================
class TransitionToFOL(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # ------------------------------------------
        # 1. SCENE SETUP (0th Order Base)
        # ------------------------------------------
        divider = Line(UP * 4, DOWN * 4, stroke_width=2).set_color(WHITE)
        
        # Titles
        title_0th = Text("Syntax vs Semantics (0th Order)", font_size=40, weight=BOLD).to_edge(UP)
        title_1st = Text("Syntax vs Semantics (1st Order)", font_size=40, weight=BOLD, color=TEAL).to_edge(UP)

        syntax_center = LEFT * 3.5
        semantics_center = RIGHT * 3.5

        header_syntax = Text("Syntax", font_size=32, color=WHITE).move_to(syntax_center + UP * 2.8)
        header_semantics = Text("Semantics", font_size=32, color=WHITE).move_to(semantics_center + UP * 2.8)

        # Left Side: 0th Order Axioms
        axioms_0th = VGroup(
            MathTex(r"\mathbf{A1:} \ \varphi \to (\psi \to \varphi)"),
            MathTex(r"\mathbf{A2:} \ ((\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi)))"),
            MathTex(r"\mathbf{A3:} \ ((\neg \varphi \to \neg \psi) \to ((\neg \varphi \to \psi) \to \varphi))")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).scale(0.6).move_to(syntax_center + UP * 0.5)
        
        mp_rule = MathTex(r"\text{MP: } \frac{\varphi \quad \varphi \to \psi}{\psi}", font_size=36).next_to(axioms_0th, DOWN, buff=0.8)
        
        syntax_0th_group = VGroup(axioms_0th, mp_rule)

        # Right Side: Big Truth Table
        big_table = self.get_big_truth_table().move_to(semantics_center + DOWN * 0.5)

        # ------------------------------------------
        # 2. FOL ELEMENTS (Hidden Initially)
        # ------------------------------------------
        # Left Side: FOL Axioms (A4, A5, A6) - Kept white and scaled to perfectly match A1-A3
        axioms_1st = VGroup(
            MathTex(r"\mathbf{A4:} \ \forall x \varphi \to \varphi(_{t}^{x})"),
            MathTex(r"\mathbf{A5:} \ \forall x (\varphi \to \psi) \to (\forall x \varphi \to \forall x \psi)"),
            MathTex(r"\mathbf{A6:} \ \varphi \to \forall x \varphi")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).scale(0.6)

        # Right Side: Mathematical Structures
        dag = self.get_dag_graph().scale(0.5).move_to(semantics_center + UP * 0.5 + LEFT * 1.5)
        tree_graph = self.get_tree_graph().scale(0.5).move_to(semantics_center + UP * 0.5 + RIGHT * 1.5)
        farey = self.get_farey_graph(radius=1.2, depth=2).move_to(semantics_center + DOWN * 1.5 + RIGHT * 1.5)
        manifold_2d = ParametricFunction(
            lambda t: np.array([1.2 * np.sin(2 * t), 1.2 * np.sin(t), 0]), 
            t_range=[0, TAU], color=GREEN_D
        ).set_stroke(width=3).move_to(semantics_center + DOWN * 1.5 + LEFT * 1.5)
        
        structures_group = VGroup(dag, tree_graph, farey, manifold_2d)

        # ------------------------------------------
        # 3. ANIMATIONS & VOICEOVER
        # ------------------------------------------
        script_1 = "So, we have seen that the syntax of propositional logic is given by a formal calculus, and that the semantics is extremely simple."
        with self.voiceover(text=script_1) as tracker:
            self.add(divider, header_syntax, header_semantics)
            self.play(
                Write(title_0th),
                FadeIn(syntax_0th_group, shift=RIGHT),
                FadeIn(big_table, shift=LEFT),
                run_time=2
            )
            self.wait(max(0, tracker.duration - 2))

        script_2 = "Models are just given by truth tables."
        with self.voiceover(text=script_2) as tracker:
            box = SurroundingRectangle(big_table, color=BLUE, buff=0.1)
            self.play(Create(box), run_time=1)
            self.wait(max(0, tracker.duration - 1))
            self.play(FadeOut(box), run_time=0.5)

        script_3 = "Things get much more interesting when we move to first order logic, since first order logic is strong enough to define mathematical theories and their corresponding structures."
        with self.voiceover(text=script_3) as tracker:
            # 1. Change Title
            self.play(ReplacementTransform(title_0th, title_1st), run_time=1)
            
            # 2. Upgrade Syntax: Create the seamless A1-A6 list
            axioms_0th.generate_target()
            axioms_0th.target.shift(UP * 1.2)
            
            # Position A4-A6 perfectly below A3's target position
            axioms_1st.next_to(axioms_0th.target, DOWN, buff=0.4, aligned_edge=LEFT)
            
            # Push MP down to make room
            mp_rule.generate_target()
            mp_rule.target.next_to(axioms_1st, DOWN, buff=0.8)

            # Move existing elements out of the way
            self.play(
                MoveToTarget(axioms_0th),
                MoveToTarget(mp_rule),
                run_time=1
            )
            # Fade in A4-A6 into the newly created gap
            self.play(FadeIn(axioms_1st, shift=UP), run_time=1)

            # 3. Upgrade Semantics: Replace truth table with mathematical structures
            self.play(
                FadeOut(big_table, scale=0.8),
                FadeIn(structures_group, scale=1.2),
                run_time=1.5
            )
            self.wait(max(0, tracker.duration - 4.5))

        self.wait(2)

    # ---------------------------------------------------
    # Helper Functions 
    # ---------------------------------------------------
    def get_big_truth_table(self):
        content = [
            ["0", "0", "0", "1", "1", "1"],
            ["0", "0", "1", "1", "1", "1"],
            ["0", "1", "0", "0", "1", "1"],
            ["0", "1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "1", "1"],
            ["1", "0", "1", "1", "1", "1"],
            ["1", "1", "0", "0", "0", "1"],
            ["1", "1", "1", "1", "1", "1"]
        ]
        col_labels = [
            MathTex("p"), MathTex("q"), MathTex("r"),
            MathTex(r"q \to r"),
            MathTex(r"p \to (q \to r)"),
            MathTex(r"\varphi")
        ]
        return MathTable(content, col_labels=col_labels, include_outer_lines=True).scale(0.35)

    def get_dag_graph(self):
        nx_graph = nx.DiGraph()
        nx_graph.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])
        return Graph(list(nx_graph.nodes), list(nx_graph.edges), layout="spring", labels=False, vertex_config={"radius": 0.15, "color": BLUE_A}, edge_config={"color": GREY, "stroke_width": 2})

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