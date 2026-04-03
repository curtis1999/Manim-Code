from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

# ==========================================
# SCENE 6: FIRST ORDER LOGIC & STRUCTURES
#CONTAINS THE DEFINITION OF INTERPRETATION AND EXAMPLE OF NATURALS.  GOOD TRANSITION TO GRAPH EXAMPLE
# ==========================================
class FirstOrderLogic(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # ------------------------------------------
        # 1. LANGUAGE AND SYMBOLS
        # ------------------------------------------
        title = Text("First Order Logic", font_size=48, weight=BOLD).to_edge(UP)
        
        # Base Logical Symbols
        l_log = MathTex(
            r"\mathbb{L} = \{", 
            r"\neg, \land, \lor, \to, ", 
            r"\forall, \exists, x_0, x_1, \dots", 
            r"\}"
        ).move_to(UP * 1.8)

        script_1 = "First order logic is an expansion of propositional logic, where we add variables and quantifiers to our set of logical symbols."
        with self.voiceover(text=script_1) as tracker:
            self.play(Write(title))
            self.play(Write(l_log), run_time=1)
            self.play(l_log[2].animate.set_color(YELLOW), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        # General Theory
        l_gen = MathTex(
            r"\mathbb{L} = \{", 
            r"\neg, \dots, \forall, x_i, ", 
            r"c_0, \dots, c_k", r", ", 
            r"F_0, \dots, F_n", r", ", 
            r"R_0, \dots, R_m", 
            r"\}"
        ).move_to(UP * 1.8)
        l_gen[1].set_color(YELLOW) 

        script_2 = "We also add certain constant, function and relation symbols, which are specific to a given theory."
        with self.voiceover(text=script_2) as tracker:
            self.play(ReplacementTransform(l_log, l_gen), run_time=1.5)
            self.play(l_gen[1].animate.set_color(WHITE), run_time=0.5)
            self.wait(max(0, tracker.duration - 2))

        # Arithmetic Theory
        l_arith = MathTex(
            r"\mathbb{L} = \{", 
            r"\neg, \dots, \forall, x_i, ", 
            r"0", r", ", 
            r"S, +, \cdot", r", ", 
            r"<", 
            r"\}"
        ).move_to(UP * 1.8)

        script_3 = "For example, if we want to study the natural numbers, we add the constant 0, the successor function S, which just maps n to n plus 1, the addition and multiplication function, and the less than relation."
        with self.voiceover(text=script_3) as tracker:
            self.play(ReplacementTransform(l_gen, l_arith), run_time=1)
            # Highlight non-logical arithmetic symbols
            self.play(l_arith[2].animate.set_color(YELLOW), l_arith[4].animate.set_color(YELLOW), l_arith[6].animate.set_color(YELLOW), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        # Graph Theory
        l_graph = MathTex(
            r"\mathbb{L} = \{", 
            r"\neg, \dots, \forall, x_i, ", 
            r"E", 
            r"\}"
        ).move_to(UP * 1.8)

        script_4 = "But if we want to study graphs, all we would need is a single binary relation E expressing an edge between nodes."
        with self.voiceover(text=script_4) as tracker:
            self.play(ReplacementTransform(l_arith, l_graph), run_time=1)
            # Highlight non-logical graph symbol
            self.play(l_graph[2].animate.set_color(YELLOW), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        # Back to General
        l_gen_final = MathTex(
            r"\mathbb{L} = \{", 
            r"\neg, \dots, \forall, x_i", r", ", 
            r"c_0, \dots, c_k", r", ", 
            r"F_0, \dots, F_n", r", ", 
            r"R_0, \dots, R_m", 
            r"\}"
        ).move_to(UP * 1.8)

        script_5a = "These symbols which are specific to a given theory are called the non-logical symbols,"
        with self.voiceover(text=script_5a) as tracker:
            self.play(ReplacementTransform(l_graph, l_gen_final), run_time=1)
            self.play(l_gen_final[3].animate.set_color(YELLOW), l_gen_final[5].animate.set_color(YELLOW), l_gen_final[7].animate.set_color(YELLOW), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        script_5b = "and these are the logical symbols."
        with self.voiceover(text=script_5b) as tracker:
            self.play(
                l_gen_final[3].animate.set_color(DARK_GREY), l_gen_final[5].animate.set_color(DARK_GREY), l_gen_final[7].animate.set_color(DARK_GREY),
                l_gen_final[1].animate.set_color(YELLOW), run_time=1
            )
            self.wait(max(0, tracker.duration - 1))

        script_6 = "If we restrict ourselves to the logical symbols, then we are in the domain of pure logic, and whatever we prove applies to all first order structures."
        with self.voiceover(text=script_6) as tracker:
            self.play(
                l_gen_final[1].animate.set_color(WHITE), 
                l_gen_final[3].animate.set_color(WHITE), l_gen_final[5].animate.set_color(WHITE), l_gen_final[7].animate.set_color(WHITE), 
                run_time=1
            )
            self.wait(max(0, tracker.duration - 1))

        # ------------------------------------------
        # 2. SYNTAX & AXIOMS (Language Stays at Top)
        # ------------------------------------------
        # Make axioms larger (0.55) and shift left
        axioms_all = VGroup(
            MathTex(r"\mathbf{A1:} \ \varphi \to (\psi \to \varphi)"),
            MathTex(r"\mathbf{A2:} \ (\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))"),
            MathTex(r"\mathbf{A3:} \ (\neg \varphi \to \neg \psi) \to ((\neg \varphi \to \psi) \to \varphi)"),
            MathTex(r"\mathbf{A4:} \ \forall x \varphi \to \varphi(_{t}^{x}) \quad \text{(if } t \text{ is freely substitutable)}"),
            MathTex(r"\mathbf{A5:} \ \forall x (\varphi \to \psi) \to (\forall x \varphi \to \forall x \psi)"),
            MathTex(r"\mathbf{A6:} \ \varphi \to \forall x \varphi \quad \text{(if } x \text{ is not free in } \varphi\text{)}")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).scale(0.55).to_edge(LEFT, buff=0.5).shift(DOWN * 0.5)

        script_7 = "The syntax of first order logic is given by the so-called logical axioms."
        with self.voiceover(text=script_7) as tracker:
            self.play(FadeIn(axioms_all, lag_ratio=0.1), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        script_8 = "We note that we have just added three axioms to the axioms of propositional logic..."
        with self.voiceover(text=script_8) as tracker:
            brace = Brace(axioms_all[0:3], direction=LEFT, color=BLUE)
            brace_text = brace.get_text("Propositional", "Axioms").scale(0.6).set_color(BLUE)
            
            self.play(GrowFromCenter(brace), FadeIn(brace_text), run_time=1)
            self.play(axioms_all[3:6].animate.set_color(YELLOW), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        script_9 = "which determine how the forall quantifiers work. Note that since exists x P x, where P is some arbitrary property like being even, is equivalent to not forall x not P x. If there is an even number, then we know that not all numbers are odd, so this is why we technically only need to add the forall quantifier to the language."
        with self.voiceover(text=script_9) as tracker:
            self.wait(tracker.duration)

        script_10 = "One can show that this set of axioms is once again sound and complete, but this time for first order logic, and we will see this proof in the fourth video."
        with self.voiceover(text=script_10) as tracker:
            self.wait(tracker.duration)

        # Equality Axioms
        eq_axioms = VGroup(
            MathTex(r"\mathbf{E1:} \ \forall x (x \doteq x)"),
            MathTex(r"\mathbf{E2:} \ \forall x \forall y (x \doteq y \to y \doteq x)"),
            MathTex(r"\mathbf{E3:} \ \forall x \forall y \forall z ((x \doteq y \land y \doteq z) \to x \doteq z)"),
            MathTex(r"\mathbf{E4:} \ \forall x_1 \dots x_n \forall y_1 \dots y_n ((x_1 \doteq y_1 \land \dots \land x_n \doteq y_n) \to Fx_1\dots x_n \doteq Fy_1\dots y_n)"),
            MathTex(r"\mathbf{E5:} \ \forall x_1 \dots x_n \forall y_1 \dots y_n ((x_1 \doteq y_1 \land \dots \land x_n \doteq y_n \land Rx_1\dots x_n) \to Ry_1\dots y_n)")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).scale(0.55).next_to(axioms_all, RIGHT, buff=0.5, aligned_edge=UP)

        script_11 = "Often the equality relation is taken to be a logical symbol. In this case, we need to add the following five axioms to our list of logical axioms which define the behaviour of the equality symbol."
        with self.voiceover(text=script_11) as tracker:
            # Language and A1-A6 stay on screen!
            self.play(FadeIn(eq_axioms, lag_ratio=0.1), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        script_12 = "These axioms are hard to argue against, everything is equal to itself, if a is equal to b then b is also equal to a, and so on."
        with self.voiceover(text=script_12) as tracker:
            self.wait(tracker.duration)

        # Clear board for Semantics (Language is transformed smoothly)
        self.play(FadeOut(axioms_all), FadeOut(eq_axioms), FadeOut(brace), FadeOut(brace_text), FadeOut(title))

        # ------------------------------------------
        # 3. SEMANTICS (STRUCTURES)
        # ------------------------------------------
        l_tex = MathTex(
            r"\mathcal{L} = \{", 
            r"c_0, \dots, c_k", r", ", 
            r"F_0, \dots, F_n", r", ", 
            r"R_0, \dots, R_m", 
            r"\}", font_size=40
        ).move_to(UP * 1.5)

        # Separated elements for perfect kerning and targeting
        m_tex = MathTex(
            r"\mathcal{M}", r" = (", 
            r"M", r", ", 
            r"c_0^\mathcal{M}, \dots, c_k^\mathcal{M}", r", ", 
            r"F_0^\mathcal{M}, \dots, F_n^\mathcal{M}", r", ", 
            r"R_0^\mathcal{M}, \dots, R_m^\mathcal{M}", 
            r")", font_size=40
        ).move_to(DOWN * 0.5)

        script_13 = "Now we are ready to move to the semantics of FOL. Again we fix our language, which again means we pick a set of constant, function and relations symbols..."
        with self.voiceover(text=script_13) as tracker:
            self.play(ReplacementTransform(l_gen_final, l_tex), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        script_14a = "and we can define a structure,"
        with self.voiceover(text=script_14a) as tracker:
            self.play(Write(m_tex), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        script_14b = "which is represented by this fancy M, and is equal to this tuple of elements."
        with self.voiceover(text=script_14b) as tracker:
            self.play(m_tex[0].animate.set_color(YELLOW), run_time=0.5)
            self.play(m_tex[0].animate.set_color(WHITE), run_time=0.5)
            self.wait(max(0, tracker.duration - 1))

        script_15 = "This is the domain or universe of the structure..."
        with self.voiceover(text=script_15) as tracker:
            # Domain Arrow: Small, aligned exactly at the base
            domain_arrow = Arrow(
                m_tex[2].get_bottom() + DOWN * 0.6, 
                m_tex[2].get_bottom() + DOWN * 0.1, 
                color=WHITE, stroke_width=3, tip_length=0.15
            )
            domain_label = Text("Domain", font_size=24).next_to(domain_arrow, DOWN, buff=0.1)
            self.play(GrowArrow(domain_arrow), FadeIn(domain_label), run_time=1)
            self.wait(max(0, tracker.duration - 1))
            self.play(FadeOut(domain_arrow), FadeOut(domain_label), run_time=0.5)

        script_16 = "and these are the 'interpretations' of the symbols in the language."
        with self.voiceover(text=script_16) as tracker:
            s_arrows = VGroup(
                Arrow(l_tex[1].get_bottom(), m_tex[4].get_top(), color=TEAL, buff=0.1),
                Arrow(l_tex[3].get_bottom(), m_tex[6].get_top(), color=TEAL, buff=0.1),
                Arrow(l_tex[5].get_bottom(), m_tex[8].get_top(), color=TEAL, buff=0.1)
            )
            s_label = MathTex("s", color=TEAL, font_size=36).next_to(s_arrows[1], RIGHT, buff=0.1)
            self.play(GrowArrow(s_arrows[0]), GrowArrow(s_arrows[1]), GrowArrow(s_arrows[2]), FadeIn(s_label), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_17 = "Constants are interpreted as specific elements in the structure..."
        with self.voiceover(text=script_17) as tracker:
            self.play(l_tex[1].animate.set_color(YELLOW), m_tex[4].animate.set_color(YELLOW), run_time=0.5)
            self.wait(max(0, tracker.duration - 0.5))

        script_18 = "and functions and relations are interpreted as subsets of tuples of elements of the structures."
        with self.voiceover(text=script_18) as tracker:
            self.play(
                l_tex[1].animate.set_color(WHITE), m_tex[4].animate.set_color(WHITE),
                l_tex[3].animate.set_color(ORANGE), m_tex[6].animate.set_color(ORANGE),
                l_tex[5].animate.set_color(PINK), m_tex[8].animate.set_color(PINK),
                run_time=1
            )
            self.wait(max(0, tracker.duration - 1))
            self.play(
                l_tex[3].animate.set_color(WHITE), m_tex[6].animate.set_color(WHITE),
                l_tex[5].animate.set_color(WHITE), m_tex[8].animate.set_color(WHITE),
                run_time=0.5
            )

        self.play(FadeOut(s_arrows), FadeOut(s_label))

        # ------------------------------------------
        # 4. ARITHMETIC EXAMPLE
        # ------------------------------------------
        l_arith_sem = MathTex(
            r"\mathcal{L} = \{", 
            r"0", r", ", 
            r"S, +, \cdot", r", ", 
            r"<", 
            r"\}", font_size=40
        ).move_to(UP * 1.5)

        n_tex = MathTex(
            r"\mathcal{N}", r" = (", 
            r"\mathbb{N}", r", ", 
            r"0^\mathcal{N}", r", ", 
            r"S^\mathcal{N}", r", ", 
            r"+^\mathcal{N}", r", \cdot^\mathcal{N}", r", ", 
            r"<^\mathcal{N}", 
            r")", font_size=40
        ).move_to(DOWN * 0.5)

        script_19 = "This is a bit abstract, so lets consider the example of the standard structure of arithmetic, which is essentially just a number line."
        with self.voiceover(text=script_19) as tracker:
            self.wait(tracker.duration)

        script_20 = "Again we work within the language of arithmetic."
        with self.voiceover(text=script_20) as tracker:
            self.play(ReplacementTransform(l_tex, l_arith_sem), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_21 = "So, the universe is the set of natural numbers."
        with self.voiceover(text=script_21) as tracker:
            self.play(ReplacementTransform(m_tex, n_tex), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        num_line = NumberLine(x_range=[0, 6, 1], length=8, include_numbers=True, font_size=24).move_to(DOWN * 2.2)

        script_22 = "We can visualize this structure as a the number line, and as we would expect, the interpretation of 0 is just the first element in the number line."
        with self.voiceover(text=script_22) as tracker:
            self.play(Create(num_line), run_time=1)
            zero_arrow = Arrow(n_tex[4].get_bottom(), num_line.number_to_point(0), color=YELLOW)
            self.play(GrowArrow(zero_arrow), n_tex[4].animate.set_color(YELLOW), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        script_23 = "The interpretations of the relations and functions are harder to visualize. But formally we interpret the less than symbol as the set of all pairs of natural numbers (x,y) such that x is less than y."
        with self.voiceover(text=script_23) as tracker:
            self.play(FadeOut(zero_arrow), n_tex[4].animate.set_color(WHITE), run_time=0.5)
            
            less_set = MathTex(r"<^\mathcal{N} = \{(0,1), (0,2), (1,2), (0,3), \dots \}", font_size=32, color=PINK).next_to(num_line, DOWN, buff=0.5)
            rel_arrow = Arrow(n_tex[11].get_bottom(), less_set.get_top(), color=PINK)
            
            self.play(n_tex[11].animate.set_color(PINK), GrowArrow(rel_arrow), Write(less_set), run_time=1.5)
            self.wait(max(0, tracker.duration - 2))

        script_24 = "The successor function will map to the set of all pairs of numbers such that the second is one greater than the first."
        with self.voiceover(text=script_24) as tracker:
            self.play(FadeOut(rel_arrow), FadeOut(less_set), n_tex[11].animate.set_color(WHITE), run_time=0.5)

            succ_set = MathTex(r"S^\mathcal{N} = \{(0,1), (1,2), (2,3) \dots \}", font_size=32, color=TEAL).next_to(num_line, DOWN, buff=0.5)
            succ_arrow = Arrow(n_tex[6].get_bottom(), succ_set.get_top(), color=TEAL)
            
            self.play(n_tex[6].animate.set_color(TEAL), GrowArrow(succ_arrow), Write(succ_set), run_time=1.5)
            self.wait(max(0, tracker.duration - 2))

        script_25 = "Similarly for the addition function, it maps to the set of all triples (x,y,z) such that x plus y equals z."
        with self.voiceover(text=script_25) as tracker:
            self.play(FadeOut(succ_arrow), FadeOut(succ_set), n_tex[6].animate.set_color(WHITE), run_time=0.5)
            
            add_set = MathTex(r"+^\mathcal{N} = \{(0,0,0), (0,1,1), (1,0,1), (1,1,2), \dots \}", font_size=32, color=ORANGE).next_to(num_line, DOWN, buff=0.5)
            func_arrow = Arrow(n_tex[8].get_bottom(), add_set.get_top(), color=ORANGE)
            
            self.play(n_tex[8].animate.set_color(ORANGE), GrowArrow(func_arrow), Write(add_set), run_time=1.5)
            self.wait(max(0, tracker.duration - 2))

        script_26 = "So in general the interpretation function s is the bridge between syntax and semantics, where s is a function which maps symbols in a formal language, either to elements, or subsets of tuples of elements of the domain of the structure."
        with self.voiceover(text=script_26) as tracker:
            self.wait(tracker.duration)

        # ------------------------------------------
        # 5. GRAPH THEORY EXAMPLE
        # ------------------------------------------
        self.play(FadeOut(func_arrow), FadeOut(add_set), FadeOut(num_line), n_tex[8].animate.set_color(WHITE), run_time=1)

        l_graph_sem = MathTex(r"\mathcal{L} = \{", r"E", r"\}", font_size=40).move_to(UP * 1.5)
        g_tex = MathTex(r"\mathcal{G} = (", r"X", r", ", r"E^\mathcal{G}", r")", font_size=40).move_to(DOWN * 0.5)

        script_27 = "This is a strange and abstract idea, to get a better understanding, let us move to perhaps the simplest theory, the theory of graphs."
        with self.voiceover(text=script_27) as tracker:
            self.wait(tracker.duration)

        script_28 = "The language has a single binary relation E, and models are arbitrary sets of points, which may or may not be connected by an arrow."
        with self.voiceover(text=script_28) as tracker:
            self.play(ReplacementTransform(l_arith_sem, l_graph_sem), ReplacementTransform(n_tex, g_tex), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        # Create a Directed Graph
        vertices = ["a", "b", "c", "d", "e"]
        edges = [("a", "b"), ("a", "c"), ("b", "c"), ("c", "d"), ("d", "e")]
        di_graph = DiGraph(
            vertices, edges, 
            layout="circular", labels=True, 
            vertex_config={"radius": 0.2, "color": BLUE},
            edge_config={"color": WHITE, "stroke_width": 2, "tip_length": 0.2}
        ).scale(0.8).move_to(DOWN * 2.5)

        script_29 = "Where given nodes a and b, a E b if and only if there is an arrow from a to b."
        with self.voiceover(text=script_29) as tracker:
            self.play(Create(di_graph), run_time=1.5)
            self.play(Indicate(di_graph.edges[("a", "b")], color=YELLOW, scale_factor=1.5), run_time=1)
            self.wait(max(0, tracker.duration - 2.5))

        self.wait(2)