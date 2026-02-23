from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class GodelIncompleteness(VoiceoverScene):
    def construct(self):
        # 1. Voiceover Setup
        self.set_speech_service(RecorderService(transcription_model=None))

        # --- PART 1: INTRO & NUMBER LINE ---
        
        text_1 = (
            "Now we will explain Godel's famous incompleteness theorem, which tells us "
            "that any theory capable of interpreting the theory of arithmetic is incomplete. "
            "Meaning that there are sentences which it cannot prove nor disprove. "
            "Alternatively, this means that most interesting theories have many models. "
            "I.e. we cannot pin down a single model for the theory."
        )

        with self.voiceover(text=text_1) as tracker:
            title = Text("Gödel's First Incompleteness Theorem", font_size=48).to_edge(UP)
            self.play(Write(title))
            self.wait(2)

        # Create Number Line
        number_line = NumberLine(
            x_range=[1, 8, 1],
            length=11,
            include_numbers=True,
            numbers_to_include=range(1, 9),
            font_size=24
        ).next_to(title, DOWN, buff=0.5)
        
        dots = MathTex("\dots").next_to(number_line, RIGHT)
        full_line_group = VGroup(number_line, dots)

        text_2 = (
            "The first key to understanding this proof is what is known as Godel numbering, "
            "whereby we can code every formula with a natural number."
        )

        with self.voiceover(text=text_2) as tracker:
            self.play(FadeIn(full_line_group))

        # --- PART 2: FUNDAMENTAL THEOREM & SMALL TREES ---

        text_3 = (
            "This relies on the Fundamental theorem of arithmetic, which states that every "
            "number has a unique prime factor decomposition."
        )

        # Theorem Box
        theorem_text = Tex(
            "\\textbf{Fundamental Theorem of Arithmetic:}\\\\",
            "Every integer $n > 1$ has a unique prime factor decomposition\\\\",
        ).scale(0.65)
        
        theorem_box = SurroundingRectangle(theorem_text, color=BLUE, fill_opacity=0.1, fill_color=BLACK)
        theorem_group = VGroup(theorem_box, theorem_text)

        with self.voiceover(text=text_3) as tracker:
            self.play(Create(theorem_box), Write(theorem_text), run_time = tracker.duration/2)

        text_4 = "Essentially this means that we can view each number as a tree, where the leaves are prime numbers."

        # HELPER: Build simple factor trees
        def get_factor_tree(num, top_point, scale=0.4):
            grp = VGroup()
            font_sz = 36 * scale
            start = top_point + DOWN * 0.4
            
            # Trees for specific numbers
            if num == 4:
                # 4 -> 2, 2
                l = Line(start, start + DL*0.5, color=YELLOW, stroke_width=2)
                r = Line(start, start + DR*0.5, color=YELLOW, stroke_width=2)
                n1 = MathTex("2", font_size=font_sz).next_to(l.get_end(), DOWN, buff=0.1)
                n2 = MathTex("2", font_size=font_sz).next_to(r.get_end(), DOWN, buff=0.1)
                grp.add(l, r, n1, n2)
            
            elif num == 6:
                # 6 -> 3, 2
                l = Line(start, start + DL*0.5, color=YELLOW, stroke_width=2)
                r = Line(start, start + DR*0.5, color=YELLOW, stroke_width=2)
                n1 = MathTex("3", font_size=font_sz).next_to(l.get_end(), DOWN, buff=0.1)
                n2 = MathTex("2", font_size=font_sz).next_to(r.get_end(), DOWN, buff=0.1)
                grp.add(l, r, n1, n2)
            
            elif num == 8:
                # 8 -> 2, 4 -> 2, (2,2)
                l = Line(start, start + DL*0.5, color=YELLOW, stroke_width=2)
                n_2 = MathTex("2", font_size=font_sz).next_to(l.get_end(), DOWN, buff=0.1)
                
                r = Line(start, start + DR*0.5, color=YELLOW, stroke_width=2)
                n_4 = MathTex("4", font_size=font_sz).next_to(r.get_end(), DOWN, buff=0.1)
                
                start_4 = n_4.get_bottom()
                l4 = Line(start_4, start_4 + DL*0.3, color=YELLOW, stroke_width=2)
                r4 = Line(start_4, start_4 + DR*0.3, color=YELLOW, stroke_width=2)
                n_4_1 = MathTex("2", font_size=font_sz).next_to(l4.get_end(), DOWN, buff=0.1)
                n_4_2 = MathTex("2", font_size=font_sz).next_to(r4.get_end(), DOWN, buff=0.1)
                
                grp.add(l, r, n_2, n_4, l4, r4, n_4_1, n_4_2)
            return grp

        # Generate trees one by one
        # We only animate 4, 6, 8. Primes stay empty (as they are just roots).
        trees_group = VGroup()
        
        with self.voiceover(text=text_4) as tracker:
            self.wait()
            # We iterate 1-8. If composite, we build and play. 
            for i in range(1, 9):
                if i in [4, 6, 8]:
                    pos = number_line.number_to_point(i)
                    t = get_factor_tree(i, pos)
                    trees_group.add(t)
                    self.play(FadeIn(t), run_time=0.5)
                # For primes (1,2,3,5,7), we do nothing/wait briefly if desired
                # or just continue loop immediately.

        # --- PART 3: THE BIG TREE (1792) ---

        text_5 = (
            "With this in mind, we see that large numbers carry a lot of hidden information. "
            "They are not just points, but they can be seen as complicated trees."
        )

        # 1792 Tree Construction
        tree_start = number_line.get_center() + DOWN * 0.5
        scale_factor = 0.7 
        
        def make_node(val, pos, scale=1.0):
            return MathTex(str(val), font_size=36*scale).move_to(pos)

        # Level 0
        root = make_node(1792, tree_start, scale=scale_factor)
        
        # Level 1
        p_16 = tree_start + DL * 1.5 + LEFT * 0.5
        p_112 = tree_start + DR * 1.5 + RIGHT * 0.5
        n_16 = make_node(16, p_16, scale=scale_factor)
        n_112 = make_node(112, p_112, scale=scale_factor)
        l_root_16 = Line(root.get_bottom(), n_16.get_top(), color=YELLOW)
        l_root_112 = Line(root.get_bottom(), n_112.get_top(), color=YELLOW)

        # Level 2
        p_4a = p_16 + DL * 0.8
        p_4b = p_16 + DR * 0.8
        n_4a = make_node(4, p_4a, scale=scale_factor)
        n_4b = make_node(4, p_4b, scale=scale_factor)
        l_16_4a = Line(n_16.get_bottom(), n_4a.get_top(), color=YELLOW)
        l_16_4b = Line(n_16.get_bottom(), n_4b.get_top(), color=YELLOW)

        p_8 = p_112 + DL * 0.8
        p_14 = p_112 + DR * 0.8
        n_8 = make_node(8, p_8, scale=scale_factor)
        n_14 = make_node(14, p_14, scale=scale_factor)
        l_112_8 = Line(n_112.get_bottom(), n_8.get_top(), color=YELLOW)
        l_112_14 = Line(n_112.get_bottom(), n_14.get_top(), color=YELLOW)

        # Level 3
        p_2a = p_4a + DL * 0.6
        p_2b = p_4a + DR * 0.6
        p_2c = p_4b + DL * 0.6
        p_2d = p_4b + DR * 0.6
        n_2a = make_node(2, p_2a, scale=scale_factor)
        n_2b = make_node(2, p_2b, scale=scale_factor)
        n_2c = make_node(2, p_2c, scale=scale_factor)
        n_2d = make_node(2, p_2d, scale=scale_factor)
        l_4a_2s = VGroup(Line(n_4a.get_bottom(), n_2a.get_top(), color=YELLOW),
                         Line(n_4a.get_bottom(), n_2b.get_top(), color=YELLOW))
        l_4b_2s = VGroup(Line(n_4b.get_bottom(), n_2c.get_top(), color=YELLOW),
                         Line(n_4b.get_bottom(), n_2d.get_top(), color=YELLOW))

        p_8_2 = p_8 + DL * 0.6
        p_8_4 = p_8 + DR * 0.6
        n_8_2 = make_node(2, p_8_2, scale=scale_factor)
        n_8_4 = make_node(4, p_8_4, scale=scale_factor)
        l_8_split = VGroup(Line(n_8.get_bottom(), n_8_2.get_top(), color=YELLOW),
                           Line(n_8.get_bottom(), n_8_4.get_top(), color=YELLOW))

        p_14_2 = p_14 + DL * 0.6
        p_14_7 = p_14 + DR * 0.6
        n_14_2 = make_node(2, p_14_2, scale=scale_factor)
        n_14_7 = make_node(7, p_14_7, scale=scale_factor)
        l_14_split = VGroup(Line(n_14.get_bottom(), n_14_2.get_top(), color=YELLOW),
                            Line(n_14.get_bottom(), n_14_7.get_top(), color=YELLOW))

        # Level 4 (The split of the 4 in the 8 branch)
        p_8_4_2a = p_8_4 + DL * 0.5
        p_8_4_2b = p_8_4 + DR * 0.5
        n_8_4_2a = make_node(2, p_8_4_2a, scale=scale_factor)
        n_8_4_2b = make_node(2, p_8_4_2b, scale=scale_factor)
        l_8_4_split = VGroup(Line(n_8_4.get_bottom(), n_8_4_2a.get_top(), color=YELLOW),
                             Line(n_8_4.get_bottom(), n_8_4_2b.get_top(), color=YELLOW))

        # Grouping by levels for animation
        level_0 = root
        level_1 = VGroup(l_root_16, l_root_112, n_16, n_112)
        level_2 = VGroup(l_16_4a, l_16_4b, n_4a, n_4b, l_112_8, l_112_14, n_8, n_14)
        level_3 = VGroup(l_4a_2s, l_4b_2s, n_2a, n_2b, n_2c, n_2d, l_8_split, n_8_2, n_8_4, l_14_split, n_14_2, n_14_7)
        level_4 = VGroup(l_8_4_split, n_8_4_2a, n_8_4_2b)

        big_tree_full = VGroup(level_0, level_1, level_2, level_3, level_4)

        with self.voiceover(text=text_5) as tracker:
            # Clear previous stuff
            self.play(FadeOut(theorem_group), FadeOut(trees_group))
            
            # Animate 1792 level by level
            self.play(FadeIn(level_0, shift=UP))
            self.wait(0.25)
            self.play(FadeIn(level_1, shift=UP))
            self.wait(0.25)
            self.play(FadeIn(level_2, shift=UP))
            self.wait(0.25)
            self.play(FadeIn(level_3, shift=UP))
            self.wait(0.25)
            self.play(FadeIn(level_4, shift=UP))
            self.wait
        
        self.play(FadeOut(big_tree_full))

        # --- PART 4: ENCODING ---

        text_6 = "Next, we can encode every symbol in our vocabulary by an odd number."

        symbols = [
            ("\\neg", "1"),
            ("\\rightarrow", "3"),
            ("\\exists", "5"),
            ("=", "7"),
            ("(", "9"),
            (")", "11"),
            ("+", "13"),
            ("\\cdot", "15"),
            ("x", "17"),
            ("y", "19")
        ]
        
        rows = []
        for sym, num in symbols:
            row = VGroup(
                MathTex("f(", sym, ")"),
                MathTex("\\mapsto", color=YELLOW),
                MathTex(num)
            ).arrange(RIGHT, buff=0.3)
            rows.append(row)
        
        ellipses = MathTex("\\vdots").scale(1.5)
        rows.append(ellipses)
        
        table_group = VGroup(*rows).next_to(number_line, DOWN, buff=0.25).align(LEFT)
        table_group.scale(0.6)

        with self.voiceover(text=text_6) as tracker:
            self.play(Write(table_group))

        # --- PART 5: FORMULA AND GODEL NUMBERING ---

        text_7 = "Then for each formula, for clarity let us use: exists y, y plus y equals x."
        
        formula_str = "\\varphi:=\\exists y (y + y = x)"
        formula = MathTex(formula_str).next_to(number_line, DOWN, buff=0.5)

        with self.voiceover(text=text_7) as tracker:
            self.play(Write(formula), run_time = tracker.duration/2)

        text_8 = "We can define its Godel number as..."
        
        godel_formal = MathTex(
            "\\langle s \\rangle = \\prod_{i < n} p_i^{s(i)+1}"
        ).scale(1.0).next_to(formula, DOWN, buff=0.5)

        with self.voiceover(text=text_8) as tracker:
            self.play(Write(godel_formal))

        text_9 = "Then fill in for the specific values of the specific formula."

        godel_specific = MathTex(
            "G(\\varphi) = 2^{f(\\exists)} \\cdot 3^{f(y)} \\cdot 5^{f( ( )} \\cdot 7^{f(y)} \\cdot 11^{f(+)} \\cdot 13^{f(y)} \\cdot 17^{f(=)}\\cdot 19^{f(x)} \\cdot 23^{f())}"
        ).scale(0.6).next_to(godel_formal, DOWN, buff=0.5)
        
        godel_numbers = MathTex(
            "= 2^{5} \\cdot 3^{19} \\cdot 5^{9} \\cdot 7^{19} \\cdot 11^{13} \\cdot 13^{19}\\cdot 17^{7}\\cdot 19^{17}\\cdot 23^{11}"
        ).scale(0.8).next_to(godel_specific, DOWN, buff=0.2)

        with self.voiceover(text=text_9) as tracker:
            self.play(TransformFromCopy(godel_formal, godel_specific))
            self.wait(1)
            self.play(Write(godel_numbers))

        text_10 = "Then display the number. It is huge, so in scientific notation, and show that it is a point in the number line."

        huge_num = MathTex("\\approx 1.45 \\times 10^{65}").scale(1.2).next_to(godel_numbers, DOWN, buff=0.5)
        
        # Position slightly to the right of the ellipses (dots)
        # dots is part of full_line_group
        far_point = Dot(point=dots.get_right() + RIGHT * 0.1, color=RED)
        arrow = Arrow(start=huge_num.get_top(), end=far_point.get_bottom(), color=RED)

        with self.voiceover(text=text_10) as tracker:
            self.play(Write(huge_num))
            self.play(
                FadeIn(far_point),
                GrowArrow(arrow)
            )

        self.wait(3)