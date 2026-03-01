from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class StructureAndSatisfaction(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # --- SCENE DEFINITIONS & STYLING ---
        COLOR_DOMAIN = RED_B
        COLOR_SYMBOLS = YELLOW
        COLOR_MAP = ORANGE
        COLOR_TRUE = GREEN

        # 1. Main Title & Structure Definition
        title_main = Text("Structure, Denotation and Satisfaction", font_size=40, weight=BOLD)
        title_main.to_edge(UP, buff=0.3)

        # Breaking the definition into parts so we can highlight indices
        m_def = MathTex(
            r"\mathbb{M} = (",                                                                        # 0
            r"M",                                                                                     # 1 (Domain)
            r", ",                                                                                    # 2
            r"c_0^\mathbb{M}, \dots, c_k^\mathbb{M}, F_0^\mathbb{M}, \dots, F_n^\mathbb{M}, R_0^\mathbb{M}, \dots, R_m^\mathbb{M}", # 3 (Symbols)
            r")",                                                                                     # 4
            font_size=36
        ).next_to(title_main, DOWN, buff=0.5)

        # Domain Arrow
        domain_arrow = Arrow(m_def[1].get_bottom() + DOWN * 0.8, m_def[1].get_bottom(), color=COLOR_DOMAIN, buff=0.1)
        domain_label = Text("Domain", font_size=24, color=COLOR_DOMAIN).next_to(domain_arrow, DOWN, buff=0.1)
        domain_group = VGroup(domain_arrow, domain_label)

        # Example Formula (Quantifier ranges)
        ex_formula = MathTex(r"\forall x \exists y (x < y)", font_size=36).move_to(LEFT * 3 + DOWN * 1.5)
        ex_formula_graph = MathTex(r"\forall x \exists y (x E y)", font_size=36).move_to(LEFT * 3 + DOWN * 1.5)

        # 2. Interpretation Function Definitions
        interp_map = MathTex(r"s \mapsto s^\mathbb{M}", font_size=36, color=COLOR_MAP).move_to(LEFT * 4 + UP * 0.5)
        
        def_c = MathTex(r"c^\mathbb{M} \in M \text{ for every constant } c \in L", font_size=28)
        def_f = MathTex(r"F^\mathbb{M} : M^n \to M \text{ for each } n\text{-ary function } F \in L", font_size=28)
        def_r = MathTex(r"R^\mathbb{M} \subseteq M^n \text{ for each } n\text{-ary relation } R \in L", font_size=28)
        interp_defs = VGroup(def_c, def_f, def_r).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(interp_map, DOWN, buff=0.5).align_to(interp_map, LEFT)

        # Maps examples on the right
        map_plus = MathTex(r"+ \mapsto \{(1,1,2), (1,2,3), (2,1,3), (1,3,4)\dots\}", font_size=28).move_to(RIGHT * 2.5 + DOWN * 0.5)
        map_less = MathTex(r"< \mapsto \{(0,1), (0,2), (1,2), (2,3), (1,3)\dots\}", font_size=28).next_to(map_plus, DOWN, buff=0.5).align_to(map_plus, LEFT)


        # --- ANIMATIONS: PART 1 (STRUCTURE & MAPS) ---

        script_1 = "A mathematical structure M is defined algebraically as follows."
        with self.voiceover(text=script_1) as tracker:
            self.play(Write(title_main), FadeIn(m_def), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        script_2 = "There is a set M, called the domain of the structure."
        with self.voiceover(text=script_2) as tracker:
            self.play(m_def[1].animate.set_color(COLOR_DOMAIN), FadeIn(domain_group, shift=UP*0.3), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_3 = "So, again for the theory of arithmetic, this would just be the set of natural numbers. For a graph this would be the set of vertices, etc. This is the domain over which the quantifiers range."
        with self.voiceover(text=script_3) as tracker:
            self.wait(tracker.duration)

        script_4a = "So in arithmetic, when we say for all x there exists a y such that x is less than y,"
        with self.voiceover(text=script_4a) as tracker:
            self.play(FadeIn(ex_formula, shift=RIGHT*0.3), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_4b = "the quantifiers range over the natural numbers and this says that for all numbers, there is a bigger number,"
        with self.voiceover(text=script_4b) as tracker:
            self.wait(tracker.duration)

        script_4c = "whereas in the theory of graphs, the quantifiers range over the set of vertices in the graph, if we change the less than relation to the graph edge relation, this expresses that all vertices have an outgoing edge."
        with self.voiceover(text=script_4c) as tracker:
            self.play(ReplacementTransform(ex_formula, ex_formula_graph), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_5 = "Then we have a set of constant symbols, function symbols and relation symbols specific to this theory."
        with self.voiceover(text=script_5) as tracker:
            self.play(
                FadeOut(domain_group), FadeOut(ex_formula_graph),
                m_def[1].animate.set_color(WHITE),
                m_def[3].animate.set_color(COLOR_SYMBOLS),
                run_time=1.5
            )
            self.wait(max(0, tracker.duration - 1.5))

        script_6a = "The bridge between the syntax and the semantics is given by an interpretation function, which is a special map, sending each symbol to its interpretation,"
        with self.voiceover(text=script_6a) as tracker:
            self.play(m_def[3].animate.set_color(WHITE))
            self.play(FadeIn(interp_map, shift=RIGHT*0.3), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_6b = "such that constant symbols are mapped to elements in the domain,"
        with self.voiceover(text=script_6b) as tracker:
            self.play(FadeIn(interp_defs[0]), run_time=0.5)
            self.wait(max(0, tracker.duration - 0.5))

        script_6c = "function symbols are mapped to functions in the structure,"
        with self.voiceover(text=script_6c) as tracker:
            self.play(FadeIn(interp_defs[1]), run_time=0.5)
            self.wait(max(0, tracker.duration - 0.5))

        script_6d = "and relation symbols to subsets of the domain."
        with self.voiceover(text=script_6d) as tracker:
            self.play(FadeIn(interp_defs[2]), run_time=0.5)
            self.wait(max(0, tracker.duration - 0.5))

        script_7a = "Where functions can be seen as tuples, where inputs are mapped uniquely to an output. For example, the addition function will map to the set of all possible triples a, b, c, where a plus b equals c."
        with self.voiceover(text=script_7a) as tracker:
            self.play(FadeIn(map_plus, shift=LEFT*0.3), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_7b = "Similarly, relation symbols will be mapped to all tuples satisfying the axioms imposed on the relation symbol. For example the less than relation in the theory of arithmetic, will map to all pairs a, b such that a is less than b."
        with self.voiceover(text=script_7b) as tracker:
            self.play(FadeIn(map_less, shift=LEFT*0.3), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_8 = "This is a bit of a contrived map, but this is our bridge between the mechanical world of syntax, where the symbols have no inherent meaning, and the intuitive world of semantics where mathematical structures exist."
        with self.voiceover(text=script_8) as tracker:
            self.wait(tracker.duration)


        # --- ANIMATIONS: PART 2 (FREE VARIABLES & SATISFACTION) ---

        # Definitions for Part 2
        form_free = MathTex(r"\exists x(x+x=y)", font_size=40).move_to(RIGHT * 3 + UP * 1)
        form_set = MathTex(r"E = \{y : \exists x(x+x=y)\}", font_size=36, color=YELLOW).next_to(form_free, DOWN, buff=0.8)
        
        struct_pair = MathTex(r"(\mathbb{M}, \Phi)", font_size=40).move_to(LEFT * 4 + UP * 1)
        struct_expand = MathTex(r"\mathbb{M} = (M, c_0^\mathbb{M}, \dots)", font_size=24, color=GRAY).next_to(struct_pair, UP, buff=0.2)

        sat_title = Tex("Satisfaction Relation:", font_size=32, color=COLOR_TRUE).move_to(LEFT * 3 + DOWN * 0.5)
        sat_1 = MathTex(r"\mathbb{M} \models t_1 \doteq t_2 \text{ iff } t_1^\mathbb{M} = t_2^\mathbb{M}", font_size=28)
        sat_2 = MathTex(r"\mathbb{M} \models R t_1 \dots t_n \text{ iff } (t_1^\mathbb{M}, \dots, t_n^\mathbb{M}) \in R^\mathbb{M}", font_size=28)
        sat_3 = MathTex(r"\mathbb{M} \models \neg \varphi \text{ iff } \mathbb{M} \not\models \varphi", font_size=28)
        sat_4 = MathTex(r"\mathbb{M} \models (\varphi \land \psi) \text{ iff } \mathbb{M} \models \varphi \text{ and } \mathbb{M} \models \psi", font_size=28)
        sat_5 = MathTex(r"\mathbb{M} \models \forall x \varphi \text{ iff } \mathbb{M} \models \varphi[a/x] \text{ for each } a \in M", font_size=28)
        
        sat_group = VGroup(sat_1, sat_2, sat_3, sat_4, sat_5).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(sat_title, DOWN, buff=0.3).align_to(sat_title, LEFT)

        script_9a = "Finally, we need a variable assignment, which will map the set of free variables to specific elements in the domain. To motivate this, we show how formulas with free variables, serve a completely different purpose to formulas without free variables."
        with self.voiceover(text=script_9a) as tracker:
            self.play(
                FadeOut(title_main), FadeOut(m_def), FadeOut(interp_defs), 
                FadeOut(map_plus), FadeOut(map_less),
                interp_map.animate.to_corner(UL).scale(0.8),
                run_time=1.5
            )
            self.wait(max(0, tracker.duration - 1.5))

        script_9b = "Where a free variable is one which is not bounded by a quantifier. For example, there exists an x such that x plus x equals y. Here x is bounded by the existential quantifier and so it is not free, but y is free."
        with self.voiceover(text=script_9b) as tracker:
            self.play(FadeIn(form_free, shift=LEFT*0.3), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_10 = "Formulas without free variables, such as 1 plus 1 equals 2, or for all x there exists y where x is greater than y are known as sentences, and they make a claims about the structure in question, which are either true or false in the structure. Formulas with free variables, such as x is less than y, or there exists an x such that x plus x equals y, are sometimes true and sometimes false, depending on what x and y refer to. Formulas with free variables are used for definitions."
        with self.voiceover(text=script_10) as tracker:
            self.wait(tracker.duration)

        script_11 = "For example, in the structure of the natural numbers, this formula defines the set of even numbers, since it is true if and only if we instantiate y by an even number. So, we can define E equals the set of y such that there exists an x such that x plus x equals y."
        with self.voiceover(text=script_11) as tracker:
            self.play(FadeIn(form_set, shift=UP*0.3), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_12 = "So, a mathematical structure is defined as the pair M, Phi, where M is as before, and Phi is a map from the free variables in the formulas to elements in the domain."
        with self.voiceover(text=script_12) as tracker:
            self.play(FadeOut(form_free), FadeOut(form_set), run_time=1)
            self.play(Write(struct_pair), FadeIn(struct_expand, shift=DOWN*0.2), run_time=1.5)
            self.wait(max(0, tracker.duration - 2.5))

        script_13 = "Now we can define the satisfaction relation, which is the definition of truth in the semantical world."
        with self.voiceover(text=script_13) as tracker:
            self.play(FadeIn(sat_title), run_time=1)
            self.play(FadeIn(sat_group, lag_ratio=0.1), run_time=2)
            self.wait(max(0, tracker.duration - 3))

        # --- ANIMATIONS: PART 3 (EVALUATING EXAMPLES) ---
        
        # Example 1: 1+2=3
        ex_eq = MathTex("1", "+", "2", "=", "3", font_size=40).move_to(RIGHT * 3.5 + UP * 2.5)
        num_line = NumberLine(x_range=[0, 4, 1], length=4, include_numbers=True, font_size=24).move_to(RIGHT * 3.5 + UP * 0.5)
        
        # Arrows for evaluation mapping
        arrow_3 = CurvedArrow(ex_eq[4].get_bottom(), num_line.n2p(3) + UP*0.2, angle=-PI/4, color=YELLOW)
        
        j_point = num_line.n2p(1.5) + UP * 0.8 # Junction for addition
        dash_1 = DashedLine(ex_eq[0].get_bottom(), j_point, color=GREEN)
        dash_2 = DashedLine(ex_eq[2].get_bottom(), j_point, color=GREEN)
        arrow_add = Arrow(j_point, num_line.n2p(3) + UP*0.2, color=GREEN, buff=0.1)
        add_eval_group = VGroup(dash_1, dash_2, arrow_add)

        script_14a = "So, when we say 1 plus 2 equals 3, we check whether the terms 1 plus 2 and 3 evaluate to the same element in the structure."
        with self.voiceover(text=script_14a) as tracker:
            self.play(FadeIn(ex_eq), FadeIn(num_line), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_14b = "On the right hand side, we simply map 3 to its interpretation, which is just the number 3."
        with self.voiceover(text=script_14b) as tracker:
            self.play(Create(arrow_3), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_14c = "On the left we have a function term, so we map the components to their interpretations, and then evaluate the result of the function."
        with self.voiceover(text=script_14c) as tracker:
            self.play(Create(add_eval_group), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        # Example 2: 2+3 < 4 * 3
        ex_ineq = MathTex("2+3", "<", "4 \cdot 3", font_size=40).move_to(RIGHT * 3.5 + UP * 2.5)
        eval_ineq = MathTex("5", "<", "12", font_size=40, color=YELLOW).next_to(ex_ineq, DOWN, buff=0.5)
        
        rel_set = MathTex(r"<^\mathbb{M} = \{(0,1), \dots, \mathbf{(5, 12)}, \dots\}", font_size=28).next_to(eval_ineq, DOWN, buff=0.5)
        rel_set[0][16:22].set_color(GREEN) # Highlight (5,12) in the set

        script_15 = "Similar for other atomic formulas, such as 2 plus 3 is less than 4 times 3. We evaluate the terms on each side, and check whether the result exists in the subset of pairs of numbers in the relation."
        with self.voiceover(text=script_15) as tracker:
            self.play(
                FadeOut(ex_eq), FadeOut(num_line), FadeOut(arrow_3), FadeOut(add_eval_group),
                run_time=1
            )
            self.play(FadeIn(ex_ineq), run_time=0.5)
            self.play(TransformFromCopy(ex_ineq, eval_ineq), run_time=1)
            self.play(FadeIn(rel_set, shift=UP*0.2), run_time=1)
            self.wait(max(0, tracker.duration - 3.5))

        script_16 = "Then, for boolean combinations, the definition of truth is given recursively as we would expect. So phi and psi is true in a structure if and only if both phi and psi individually are true in the structure."
        with self.voiceover(text=script_16) as tracker:
            self.play(sat_4.animate.set_color(YELLOW), run_time=0.5)
            self.wait(1)
            self.play(sat_4.animate.set_color(WHITE), run_time=0.5)
            self.wait(max(0, tracker.duration - 2))

        # Example 3: Quantifiers
        ex_quant = MathTex(r"\forall x \ (x+1)^2 = x^2+2x+1", font_size=36, color=BLUE_B).move_to(RIGHT * 3.5 + DOWN * 2)

        script_17 = "For the quantifiers, an expression for all x phi x evaluates to true, if no matter which value we choose for x, it turns out to be true. For example, for all x, x plus 1 squared equals x squared plus 2x plus 1 is true of all natural numbers, and so will be true in N."
        with self.voiceover(text=script_17) as tracker:
            self.play(FadeIn(ex_quant, shift=UP*0.3), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        self.wait(2)