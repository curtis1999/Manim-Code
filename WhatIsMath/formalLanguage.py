from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class LogicSymbols(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        COLOR_CONST = YELLOW
        COLOR_FUNC = GREEN
        COLOR_REL = BLUE
        COLOR_VAR = PURPLE
        COLOR_QUANT = ORANGE
        COLOR_CONN = PINK

        title_main = Text("The basics of Mathematical Logic", font_size=40, weight=BOLD).to_edge(UP, buff=0.3)
        self.add(title_main)

        # 1. Symbols
        sym_constants = Tex(r"Constants: $c_0, c_1, \dots \ (e.g., \ 0, 1, e, \pi)$", font_size=30, color=COLOR_CONST)
        sym_functions = Tex(r"Functions: $F_0, F_1, \dots \ (e.g., \ +, \times)$", font_size=30, color=COLOR_FUNC)
        sym_relations = Tex(r"Relations: $R_0, R_1, \dots \ (e.g., \ <, \in)$", font_size=30, color=COLOR_REL)
        sym_variables = Tex(r"Variables: $v_0, v_1, v_2, \dots$", font_size=30, color=COLOR_VAR)
        sym_quantifiers = Tex(r"Quantifiers: $\forall, \exists$", font_size=30, color=COLOR_QUANT)
        sym_brackets = Tex(r"Brackets: $(, )$", font_size=30, color=COLOR_CONN)
        
        # Connectives separated so we can highlight individual symbols by index
        sym_connectives = Tex(
            "Connectives: ", 
            r"$\neg$", ", ", 
            r"$\land$", ", ", 
            r"$\lor$", ", ", 
            r"$\to$", 
            font_size=30, color=COLOR_CONN
        )

        symbols_list = VGroup(
            sym_constants, sym_functions, sym_relations, 
            sym_variables, sym_quantifiers, sym_brackets, sym_connectives
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(LEFT * 3.5 + UP * 0.2)

        non_logical_group = VGroup(sym_constants, sym_functions, sym_relations)
        logical_group = VGroup(sym_variables, sym_quantifiers, sym_brackets, sym_connectives)

        # 2. Truth Tables
        # 5 Column Table (Initial)
        table_5col = MathTable(
            [["T", "T", "T", "T", "T"], 
             ["T", "F", "F", "T", "F"], 
             ["F", "T", "F", "T", "T"], 
             ["F", "F", "F", "F", "T"]],
            col_labels=[MathTex("A"), MathTex("B"), MathTex(r"A \land B"), MathTex(r"A \lor B"), MathTex(r"A \to B")],
            include_outer_lines=True
        ).scale(0.3).move_to(RIGHT * 3.5 + UP * 0.5)

        # 6 Column Table (Equivalence)
        table_6col = MathTable(
            [["T", "T", "T", "T", "T", "T"], 
             ["T", "F", "F", "T", "F", "F"], 
             ["F", "T", "F", "T", "T", "T"], 
             ["F", "F", "F", "F", "T", "T"]],
            col_labels=[MathTex("A"), MathTex("B"), MathTex(r"A \land B"), MathTex(r"A \lor B"), MathTex(r"A \to B"), MathTex(r"\neg A \lor B")],
            include_outer_lines=True
        ).scale(0.3).move_to(table_5col.get_center())

        # --- ANIMATIONS ---
        
        script_1a = "First we fix our formal language L. It was Frege in the 1800's who realized that the act of doing mathematics simply involves the manipulations of the following sets of symbols:"
        with self.voiceover(text=script_1a) as tracker:
            self.wait(tracker.duration)

        script_1b = "Constant symbols, which represent special elements of a given structure like 0, 1, e, pi or the root of some tree."
        with self.voiceover(text=script_1b) as tracker:
            self.play(FadeIn(sym_constants, shift=RIGHT * 0.5), run_time=1)
            self.wait(max(0, tracker.duration - 1))
            
        script_1c = "Function symbols, such as successor, addition, multiplication."
        with self.voiceover(text=script_1c) as tracker:
            self.play(FadeIn(sym_functions, shift=RIGHT * 0.5), run_time=0.5)
            self.wait(max(0, tracker.duration - 0.5))
            
        script_1d = "Relation symbols, such as less than or in."
        with self.voiceover(text=script_1d) as tracker:
            self.play(FadeIn(sym_relations, shift=RIGHT * 0.5), run_time=0.5)
            self.wait(max(0, tracker.duration - 0.5))
            
        script_1e = "Variables, quantifiers, and brackets."
        with self.voiceover(text=script_1e) as tracker:
            self.play(FadeIn(sym_variables, shift=RIGHT * 0.5), FadeIn(sym_quantifiers, shift=RIGHT * 0.5), FadeIn(sym_brackets, shift=RIGHT * 0.5), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        # Precision highlights for Connectives
        with self.voiceover(text="The boolean connectives,") as tracker:
            self.play(FadeIn(sym_connectives, shift=RIGHT * 0.5), run_time=0.5)
            self.wait(max(0, tracker.duration - 0.5))
            
        with self.voiceover(text="of negation,") as tracker:
            self.play(sym_connectives[1].animate.set_color(YELLOW), run_time=0.3)
            self.wait(max(0, tracker.duration - 0.3))
            
        with self.voiceover(text="conjunctions,") as tracker:
            self.play(sym_connectives[3].animate.set_color(YELLOW), run_time=0.3)
            self.wait(max(0, tracker.duration - 0.3))
            
        with self.voiceover(text="disjunction") as tracker:
            self.play(sym_connectives[5].animate.set_color(YELLOW), run_time=0.3)
            self.wait(max(0, tracker.duration - 0.3))
            
        with self.voiceover(text="and implication.") as tracker:
            self.play(sym_connectives[7].animate.set_color(YELLOW), run_time=0.3)
            self.wait(max(0, tracker.duration - 0.3))

        # Reset connective colors before moving on
        self.play(sym_connectives.animate.set_color(COLOR_CONN), run_time=0.5)

        script_2 = "The Boolean connectives can be represented by truth tables or logic gates."
        with self.voiceover(text=script_2) as tracker:
            self.play(FadeIn(table_5col), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_3 = "Note that in classical logic, a implies b is equivalent to not a or b."
        with self.voiceover(text=script_3) as tracker:
            self.play(ReplacementTransform(table_5col, table_6col), run_time=1)
            self.wait(max(0, tracker.duration - 1))
            
        script_3b = "This is not the case in intuitionistic logic for example. But for this video we will stick to classical logic, and soon I will make a video on non-classical logics and they give rise to different mathematical universes."
        with self.voiceover(text=script_3b) as tracker:
            self.wait(tracker.duration)

        script_4 = "We can divide these symbols into two groups, the logical and non-logical symbols. The logical symbols are common to all first order theories, and so proofs only involving the logical symbols apply to all possible first-order structures. The non-logical symbols are specific to a given theory,"
        
        title_logical = Text("Logical Symbols", font_size=32).move_to(UP * 2.5 + LEFT * 3.5).set_color(WHITE)
        title_non_logical = Text("Non-Logical Symbols", font_size=32).move_to(UP * 2.5 + RIGHT * 3.5).set_color(WHITE)

        with self.voiceover(text=script_4) as tracker:
            self.play(FadeOut(table_6col), run_time=1)
            self.play(
                Write(title_logical), Write(title_non_logical),
                logical_group.animate.arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(title_logical, DOWN, buff=0.5),
                non_logical_group.animate.arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(title_non_logical, DOWN, buff=0.5),
                run_time=2
            )
            self.wait(max(0, tracker.duration - 3))

        script_5 = "for example if we are working with the theory of arithmetic, we only need the constant 0, the successor function, and the addition function."
        
        # Build Expanded Arithmetic Visual
        num_line = NumberLine(x_range=[0, 11, 1], length=7.5, include_numbers=True, font_size=24).move_to(DOWN * 2.5 + RIGHT * 2.5)
        
        # Successor arcs for the whole line
        successor_arcs = VGroup(*[CurvedArrow(num_line.n2p(i), num_line.n2p(i+1), angle=-PI/2, color=COLOR_FUNC) for i in range(10)])
        label_S = Tex("S", color=COLOR_FUNC, font_size=24).next_to(successor_arcs[0], UP, buff=0.1)
        
        # Addition operation visualizing 2 and 8 mapping to 10
        j_point = num_line.n2p(5) + UP * 1.5 # Junction point perfectly between 2 and 8
        dash_2 = DashedLine(num_line.n2p(2) + UP * 0.1, j_point, color=YELLOW)
        dash_8 = DashedLine(num_line.n2p(8) + UP * 0.1, j_point, color=YELLOW)
        arrow_10 = Arrow(j_point, num_line.n2p(10) + UP * 0.1, color=YELLOW, buff=0.1)
        plus_label = MathTex("+", color=YELLOW, font_size=30).move_to(j_point + UP * 0.25)
        
        addition_group = VGroup(dash_2, dash_8, arrow_10, plus_label)
        arithmetic_group = VGroup(num_line, successor_arcs, label_S, addition_group)

        with self.voiceover(text=script_5) as tracker:
            self.play(FadeIn(arithmetic_group), run_time=2)
            self.wait(max(0, tracker.duration - 2))

        script_6 = "Whereas, if we work with the theory of graphs, we only need a single binary relation E, where aEb means that there is an edge between a and b."
        
        # Build Graph
        graph_nodes = ["a", "b", "c", "d", "e", "f"]
        graph_edges = [("a", "b"), ("b", "c"), ("c", "a"), ("c", "d"), ("d", "e"), ("e", "f"), ("f", "d")]
        graph_pos = {"a": [-1, 0.5, 0], "b": [-1.5, -0.5, 0], "c": [-0.5, -0.5, 0], "d": [0.5, -0.5, 0],  "e": [1.5, -0.5, 0], "f": [1, 0.5, 0]}
        
        theory_graph = Graph(
            graph_nodes, graph_edges, layout=graph_pos, labels=True, 
            vertex_config={"radius": 0.2, "color": COLOR_REL}, 
            edge_config={"color": WHITE, "stroke_width": 2}
        ).scale(1.3).move_to(DOWN * 2.5 + RIGHT * 3.5)

        edges_text = Tex(r"$\{aEb, bEc, cEa, cEd, dEe, eEf, fEd\}$", font_size=30).next_to(theory_graph, UP, buff=0.4)

        with self.voiceover(text=script_6) as tracker:
            self.play(FadeOut(arithmetic_group), run_time=1)
            self.play(Create(theory_graph), FadeIn(edges_text), run_time=1.5)
            self.wait(max(0, tracker.duration - 2.5))

        self.wait(2)