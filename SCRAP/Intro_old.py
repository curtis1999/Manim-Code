from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
import networkx as nx

class SyntaxVsSemanticsFinal(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))
        SYNTAX_COLOR = WHITE 
        SEMANTICS_HIGHLIGHT = YELLOW 

        # --- SCENE SETUP ---
        divider = Line(UP * 4, DOWN * 4, stroke_width=2).set_color(SYNTAX_COLOR)
        
        syntax_center = LEFT * 3.5
        semantics_center = RIGHT * 3.5

        title_syntax = Text("Syntax", font_size=40, weight=BOLD).set_color(WHITE).move_to(syntax_center + UP * 3.3)
        title_semantics = Text("Semantics", font_size=40, weight=BOLD).set_color(WHITE).move_to(semantics_center + UP * 3.3)
        
        # Build Syntax Elements
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

        syntax_contents = VGroup(syntax_title, alphabet_tex, rules_group, proof_tree)

        # Build Semantics Elements
        semantics_title = MathTex(r"\Sigma \models \varphi", font_size=50).set_color(BLUE).next_to(title_semantics, DOWN, buff=0.4)
        num_line = NumberLine(x_range=[-3, 3, 1], length=4, include_numbers=True, font_size=24).move_to(semantics_center + UP * 1.2).set_color(BLUE_B)
        dag = self.get_dag_graph().scale(0.5).move_to(semantics_center + DOWN * 0.5 + LEFT * 1.5)
        tree_graph = self.get_tree_graph().scale(0.5).move_to(semantics_center + DOWN * 0.5 + RIGHT * 1.5)
        farey = self.get_farey_graph(radius=1.2, depth=2).move_to(semantics_center + DOWN * 2.5 + RIGHT * 1.5)
        manifold_2d = ParametricFunction(
            lambda t: np.array([1.2 * np.sin(2 * t), 1.2 * np.sin(t), 0]), 
            t_range=[0, TAU], color=GREEN_D
        ).set_stroke(width=3).move_to(semantics_center + DOWN * 2.5 + LEFT * 1.5)
        
        semantics_contents = VGroup(semantics_title, num_line, dag, tree_graph, manifold_2d, farey)

        # 1. DISPLAY EVERYTHING RIGHT FROM THE START
        self.add(divider, title_syntax, title_semantics, syntax_contents, semantics_contents)

        # Pre-build Interpretation Elements (1+1=2 scene)
        formula_1p1 = MathTex("1", "+", "1", "=", "2", font_size=60).move_to(syntax_center + UP * 0.5)
        num_line_interp = NumberLine(x_range=[-3, 3, 1], length=5, include_numbers=True).move_to(semantics_center + DOWN * 1)
        
        # Build the Plus Box
        plus_box_rect = Square(side_length=0.8).set_color(WHITE)
        plus_sign = MathTex("+", font_size=36).move_to(plus_box_rect.get_center())
        in_wire_1 = Line(plus_box_rect.get_left() + LEFT*0.3 + UP*0.2, plus_box_rect.get_left() + UP*0.2)
        in_wire_2 = Line(plus_box_rect.get_left() + LEFT*0.3 + DOWN*0.2, plus_box_rect.get_left() + DOWN*0.2)
        out_wire = Line(plus_box_rect.get_right(), plus_box_rect.get_right() + RIGHT*0.3)
        plus_box = VGroup(plus_box_rect, plus_sign, in_wire_1, in_wire_2, out_wire).move_to(semantics_center + UP * 1.5)

        # Pre-build Logic Types List
        prop_logic = Text("Propositional Logic (0th order)", font_size=24).next_to(title_syntax, DOWN, buff=0.8)
        fol_logic = Text("First Order Logic (FOL)", font_size=24).next_to(prop_logic, DOWN, buff=0.6)
        sol_logic = Text("Higher Order Logics (SOL)", font_size=24).next_to(fol_logic, DOWN, buff=0.6)

        # --- ANIMATIONS ---
        
        # Intro
        with self.voiceover(text="We can look at math from two different points of view. Syntactically and Semantically.") as tracker:
            self.wait(tracker.duration)

        with self.voiceover(text="The world of syntax is a formal and mechanical world where truth is given by proofs in a formal calculus.") as tracker:
            self.wait(tracker.duration)

        # Highlight Axioms
        with self.voiceover(text="Which is just a specific set of axioms") as tracker:
            self.play(axioms_group.animate.set_color(SEMANTICS_HIGHLIGHT), run_time=0.5)
            self.wait(max(0, tracker.duration - 0.5))

        # Highlight Proof Tree
        with self.voiceover(text="written in a formal language, which can be combined according to certain rules of inference to generate proofs.") as tracker:
            self.play(axioms_group.animate.set_color(SYNTAX_COLOR), run_time=0.5)
            self.play(proof_tree.animate.set_color(SEMANTICS_HIGHLIGHT), run_time=0.5)
            self.wait(max(0, tracker.duration - 1))
            self.play(proof_tree.animate.set_color(SYNTAX_COLOR), run_time=0.5)

        # Semantics
        with self.voiceover(text="The semantics is the intuitive world in which the symbols of our logical language get interpreted into. Similar to how English words are just words which describe things that actually exist in the world. If viewed platonically, we can see mathematical formulas as describing properties of pre-existing structures which enhabit a perfect world of forms.") as tracker:
            self.wait(tracker.duration)

        with self.voiceover(text="This platonistic view of math is not shared by everyone. Some hold a formalist view of math, in which they essentially just ignore the semantic side of math. Others hold a constructivist view of math, where we have to be able to construct or at least define a mathematical object before we can say that it exists.") as tracker:
            self.wait(tracker.duration)

        with self.voiceover(text="But the branch of mathematics which deals with the relation between the syntax and the semantics --known as Model Theory-- makes the most sense when viewed from the platonic world.") as tracker:
            self.wait(tracker.duration)

        # --- NEW INTERPRETATION SECTION (1+1=2) ---
        
        # Clear the old contents to make room for the 1+1=2 map
        self.play(FadeOut(syntax_contents), FadeOut(semantics_contents), run_time=1)

        with self.voiceover(text="In model theory, mathematical formulas aquire meaning when they get interpreted into a structure.") as tracker:
            self.wait(tracker.duration)

        with self.voiceover(text="So 1 plus 1 equals 2,") as tracker:
            self.play(FadeIn(formula_1p1))
            self.wait(max(0, tracker.duration - 1))

        with self.voiceover(text="gets its meaning only when we interpret each of the symbols involved into the number line.") as tracker:
            self.play(FadeIn(num_line_interp))
            self.wait(max(0, tracker.duration - 1))

        # Arrows mapping the syntax to semantics
        # 2 -> Number Line
        arrow_2 = CurvedArrow(formula_1p1[4].get_top(), num_line_interp.n2p(2) + UP*0.3, angle=-PI/4, color=YELLOW)
        with self.voiceover(text="First draw an arrow from 2 to the number 2 on the number line,") as tracker:
            self.play(Create(arrow_2), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        # + -> Plus Box
        arrow_plus = CurvedArrow(formula_1p1[1].get_bottom(), plus_box.get_bottom(), angle=PI/6, color=RED)
        with self.voiceover(text="then draw an arrow from plus into a square box with two input lines, and one output line, with plus inside.") as tracker:
            self.play(FadeIn(plus_box), Create(arrow_plus), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        # 1's -> Input Wires
        arrow_1_a = CurvedArrow(formula_1p1[0].get_top(), in_wire_1.get_left(), angle=-PI/3, color=GREEN)
        arrow_1_b = CurvedArrow(formula_1p1[2].get_top(), in_wire_2.get_left(), angle=-PI/4, color=GREEN)
        with self.voiceover(text="Then draw arrows from the 1's in the formula to the input wires,") as tracker:
            self.play(Create(arrow_1_a), Create(arrow_1_b), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        # Output -> Number Line
        arrow_out = CurvedArrow(out_wire.get_right(), num_line_interp.n2p(2) + UP*0.3, angle=-PI/3, color=ORANGE)
        with self.voiceover(text="and then draw an arrow from the output wire to the point 2 on the number line.") as tracker:
            self.play(Create(arrow_out), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        with self.voiceover(text="We will make this precise in the next two videos.") as tracker:
            self.wait(tracker.duration)

        # --- TRANSITION TO LOGIC TYPES ---
        
        # Clear the 1+1=2 visuals, keep titles and divider
        self.play(
            FadeOut(formula_1p1), FadeOut(num_line_interp), FadeOut(plus_box), 
            FadeOut(arrow_2), FadeOut(arrow_plus), FadeOut(arrow_1_a), FadeOut(arrow_1_b), FadeOut(arrow_out)
        )

        with self.voiceover(text="There are different languages within which we can define our logic:") as tracker:
            self.wait(tracker.duration)

        with self.voiceover(text="Propositional or 0th order logic,") as tracker:
            self.play(FadeIn(prop_logic))
            self.wait(max(0, tracker.duration - 1))

        with self.voiceover(text="FOL") as tracker:
            self.play(FadeIn(fol_logic))
            self.wait(max(0, tracker.duration - 1))

        with self.voiceover(text="and finally Higher OL's.") as tracker:
            self.play(FadeIn(sol_logic))
            self.wait(max(0, tracker.duration - 1))

        with self.voiceover(text="Of these FOL is used to build or define mathematics. This is because FOL is strong enough to describe most mathematical structures well enough, and not so strong that we can no longer define a complete and sound calculus for it.") as tracker:
            self.play(fol_logic.animate.set_color(SEMANTICS_HIGHLIGHT).scale(1.1))
            self.wait(max(0, tracker.duration - 1))

        # NEW LOGIC STRENGTHS SECTION
        with self.voiceover(text="So propositional logic is too weak for our purposes, and SOL is so strong that we lost control over it. We will see what this means later in the video.") as tracker:
            self.wait(tracker.duration)

        # Outro
        with self.voiceover(text="But, we will start simple by understanding the basic of propositional logic.") as tracker:
            self.wait(max(0, tracker.duration - 1))
            self.play(FadeOut(*self.mobjects), run_time=1.5)

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