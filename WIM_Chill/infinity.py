from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class Infinity(VoiceoverScene):
    def construct(self):
        # The RecorderService will prompt you in the terminal to record your own voice 
        # or press Enter to skip and use estimated text-length timings.
        self.set_speech_service(RecorderService(transcription_model=None))

        # --- PART 1: ZENO'S PARADOX ---
        with self.voiceover(text="The history of the role of infinity in math is very interesting, and will have its own video soon.") as tracker:
            self.wait(tracker.duration)
            
        with self.voiceover(text="For now just note, that due to various paradoxes, infinity was only accepted theoretically. Meaning that the sentence for all y, there exists an x such that x is greater than y. was accepted") as tracker: 
            sent1 = MathTex(r"\forall y\exists x (x>y)", color=GREEN)
            self.play(Write(sent1))

        with self.voiceover(text="But it was not accepted that there exists an x for all y, such that x is greater than y, since such an x would be a truly infinite set.") as tracker:
            sent2 = MathTex(r"\exists x \forall y (x>y)", color=RED).next_to(sent1, DOWN, buff=0.5)
            self.play(Write(sent2))
            self.wait(0.5)

        # --- PART 3: GEORG CANTOR ---
        with self.voiceover(text="It took this man right here, Georg Cantor to develop a theory of infinity.") as tracker:
            self.play(*[FadeOut(m) for m in self.mobjects])
            
            # Replaced with your ImageMobject
            cantor_img = ImageMobject("Cantor.jpg")
            # Added a slight height boundary to ensure the image scales nicely on screen
            cantor_img.height = min(cantor_img.height, 6) 
            
            self.play(FadeIn(cantor_img))
            self.wait(tracker.duration * 0.5)
            self.play(FadeOut(cantor_img))

        # --- PART 4: COMPARING SIZES (0-10) ---
        with self.voiceover(text="The first obstacle we encounter is the seeming paradox we encounter when trying to compare the sizes of infinite sets. For example, if we compare the size of the natural numbers with the set of square numbers...") as tracker:
            nl = NumberLine(
                x_range=[0, 10, 1],
                length=10,
                include_numbers=True,
                font_size=24
            ).shift(DOWN * 2)
            self.play(Create(nl))

        with self.voiceover(text="on the one hand, the set of natural numbers seems way larger, since most numbers are not perfect squares.") as tracker:
            # Highlight square numbers 1, 4, 9 in yellow
            squares_highlight = VGroup(
                SurroundingRectangle(nl.numbers[1], color=YELLOW),
                SurroundingRectangle(nl.numbers[4], color=YELLOW),
                SurroundingRectangle(nl.numbers[9], color=YELLOW)
            )
            self.play(Create(squares_highlight))
            
            # Initial circles for < 10
            nat_circle = Circle(radius=1.25, color=BLUE).shift(UP * 1.5 + LEFT * 2)
            sq_circle = Circle(radius=0.5, color=YELLOW).shift(UP * 1.5 + RIGHT * 2)
            nat_label = MathTex(r"\text{Naturals}_{<10}", font_size=32).next_to(nat_circle, UP)
            sq_label = MathTex(r"\text{Squares}_{<10}", font_size=32).next_to(sq_circle, UP)
            
            self.play(Create(nat_circle), Create(sq_circle), Write(nat_label), Write(sq_label))
            
        with self.voiceover(text="And in fact the difference in size increases with larger numbers. The squares make up 10 percent of numbers less than 100.") as tracker:
            sq_circle_100 = Circle(radius=0.125, color=YELLOW).move_to(sq_circle.get_center())
            sq_label_100 = MathTex(r"\text{Squares}_{<100}", font_size=32).move_to(sq_label.get_center())
            nat_label_100 = MathTex(r"\text{Naturals}_{<100}", font_size=32).move_to(nat_label.get_center())
            self.play(
                Transform(sq_circle, sq_circle_100),
                Transform(sq_label, sq_label_100),
                Transform(nat_label, nat_label_100)
            )
            
        with self.voiceover(text="1 per cent of numbers less than 10K") as tracker:
            sq_circle_10k = Circle(radius=0.0125, color=YELLOW).move_to(sq_circle.get_center())
            sq_label_10k = MathTex(r"\text{Squares}_{<10k}", font_size=32).move_to(sq_label.get_center())
            nat_label_10k = MathTex(r"\text{Naturals}_{<10k}", font_size=32).move_to(nat_label.get_center())
            self.play(
                Transform(sq_circle, sq_circle_10k),
                Transform(sq_label, sq_label_10k),
                Transform(nat_label, nat_label_10k)
            )
            
        with self.voiceover(text="and 0.1 percent of numbers less than a million and so on.") as tracker:
            sq_circle_1m = Circle(radius=0.00125, color=YELLOW).move_to(sq_circle.get_center())
            sq_label_1m = MathTex(r"\text{Squares}_{<1M}", font_size=32).move_to(sq_label.get_center())
            nat_label_1m = MathTex(r"\text{Naturals}_{<1M}", font_size=32).move_to(nat_label.get_center())
            self.play(
                Transform(sq_circle, sq_circle_1m),
                Transform(sq_label, sq_label_1m),
                Transform(nat_label, nat_label_1m)
            )

        # --- PART 5: BIJECTION ---
        self.play(FadeOut(nl), FadeOut(squares_highlight))

        # Create zoomed-in number line for naturals only
        naturals_line_zoom = NumberLine(
            x_range=[1, 7, 1],
            length=8,
            include_numbers=True,
            numbers_to_include=list(range(1, 8)),
            font_size=20
        ).shift(DOWN * 1.5)

        naturals_label_zoom = Text("Naturals", font_size=22).next_to(naturals_line_zoom, LEFT, buff=0.3)
        squares_label_zoom = Text("Squares", font_size=22).next_to(naturals_label_zoom, DOWN, buff=2)
        function_text = Text("f(n) = n²", font_size=24).next_to(naturals_label_zoom, DOWN, buff=1)
        
        with self.voiceover(text="But on the other hand, every natural number has exactly one square. So, at infinity, we have to admit that the two sets have the same size.") as tracker:
            # Transform circles back to equal size for infinity
            sq_circle_inf = Circle(radius=1.25, color=YELLOW).move_to(sq_circle.get_center())
            sq_label_inf = Text("All Squares", font_size=28).next_to(sq_circle_inf.get_top(), UP, buff=0.5)
            nat_label_inf = Text("All Naturals", font_size=28).move_to(nat_label.get_center())
            
            self.play(
                Create(naturals_line_zoom),
                Write(naturals_label_zoom), 
                Write(squares_label_zoom)
            )
            self.wait(0.1)
            self.play(Write(function_text))
            
            # Animate the bijection with arrows pointing down
            natural_dots = []
            arrows = []
            formula_texts = []
            colors = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE, PINK, TEAL, MAROON, GOLD]

            for i in range(1, 8):
                square_val = i * i
                nat_dot = Dot(naturals_line_zoom.number_to_point(i), color=colors[i-1], radius=0.08)
                nat_dot_label = Text(str(i), font_size=18, color=colors[i-1]).next_to(nat_dot, UP, buff=0.1)
                
                arrow_start = nat_dot.get_center()
                arrow_end = arrow_start + DOWN * 2
                arrow = Arrow(arrow_start, arrow_end, color=colors[i-1], stroke_width=3, max_tip_length_to_length_ratio=0.15)
                
                formula_t = Text(f"{i}²", font_size=20, color=colors[i-1]).move_to(arrow_end + DOWN * 0.3)
                result_t = Text(str(square_val), font_size=20, color=colors[i-1]).move_to(arrow_end + DOWN * 0.3)
                
                self.play(Create(nat_dot), Write(nat_dot_label), run_time=0.1)
                self.play(Create(arrow), run_time=0.1)
                self.play(Write(formula_t), run_time=0.1)
                self.play(Transform(formula_t, result_t), run_time=0.15)
                
                natural_dots.append((nat_dot, nat_dot_label))
                arrows.append(arrow)
                formula_texts.append(formula_t)            
                
            self.play(
                Transform(sq_circle, sq_circle_inf),
                Transform(sq_label, sq_label_inf),
                Transform(nat_label, nat_label_inf),
                run_time=1.5
            )

        with self.voiceover(text="Now, to most of you, this just means that sets are either finite or infinite, and once they are infinite, their size cannot be increased or compared.") as tracker:
            self.wait(tracker.duration * 0.8)

        # Fade out zoomed bijection logic, keeping the upper circles
        all_final_objects = [ 
            naturals_line_zoom, naturals_label_zoom, squares_label_zoom, function_text 
        ] + [dot for dot, lbl in natural_dots] + [lbl for dot, lbl in natural_dots] + arrows + formula_texts
        
        self.play(*[FadeOut(obj) for obj in all_final_objects])

        # --- PART 6: DEDEKIND & SET SIZES ---
        with self.voiceover(text="But to Cantor, the defining characteristic of size, was whether the two sets could be put into correspondence with each other. So, to Cantor, these two do literally have the same size") as tracker:
            self.wait(tracker.duration * 0.8)

        with self.voiceover(text="and Cantor's friend Dedekind defined a set to be infinite if and only if it could be put into 1 to 1 correspondence with a proper subset of itself.") as tracker:
            def_text = MathTex(
                r"\text{Def: } X \text{ is infinite } \iff \exists f:X\rightarrow X", 
                r"\,(f \text{ is 1-1 and ran}(f)\subsetneq X)", 
                font_size=36
            ).shift(DOWN * 1.5)
            self.play(Write(def_text))

        with self.voiceover(text="So, the existence of this 1-1 mapping just shows that the natural numbers are infinite.") as tracker:
            self.wait(tracker.duration * 0.5)
            self.play(FadeOut(def_text))

        # --- PART 7: RATIONALS & ALGEBRAICS ---
        with self.voiceover(text="Cantor then showed how to put the rational numbers") as tracker:
            # Format row 1 uniformly: circles radius 0.8, labels top-left[cite: 1]
            n_circ_q = Circle(radius=0.8, color=BLUE).move_to(LEFT * 2 + UP * 2.0)
            q_circ = Circle(radius=0.8, color=BLUE).move_to(RIGHT * 2 + UP * 2.0)
            
            n_label_q = MathTex(r"\mathbb{N}", font_size=40).next_to(n_circ_q, UP, buff=-0.1).shift(LEFT*0.6)
            q_label = MathTex(r"\mathbb{Q}", font_size=40).next_to(q_circ, UP, buff=-0.1).shift(LEFT*0.6)
            
            self.play(
                Transform(nat_circle, n_circ_q),
                Transform(sq_circle, q_circ),
                Transform(nat_label, n_label_q),
                Transform(sq_label, q_label)
            )
            
            q_arrows = VGroup(
                Arrow(nat_circle.get_right() + UP*0.5, sq_circle.get_left() + UP*0.5, buff=0.1, stroke_width=3, max_tip_length_to_length_ratio=0.15),
                Arrow(nat_circle.get_right(), sq_circle.get_left(), buff=0.1, stroke_width=3, max_tip_length_to_length_ratio=0.15),
                Arrow(nat_circle.get_right() + DOWN*0.5, sq_circle.get_left() + DOWN*0.5, buff=0.1, stroke_width=3, max_tip_length_to_length_ratio=0.15)
            )
            self.play(Create(q_arrows))

        with self.voiceover(text="and even the algebraic numbers (which include certain irrational numbers like the square root of two) into 1-1 correspondence with the natural numbers.") as tracker:
            # Middle pair for Algebraics[cite: 1]
            n_circ_a = Circle(radius=0.8, color=BLUE).move_to(LEFT * 2 + DOWN * 0.5)
            a_circ = Circle(radius=0.8, color=BLUE).move_to(RIGHT * 2 + DOWN * 0.5)
            n_label_a = MathTex(r"\mathbb{N}", font_size=40).next_to(n_circ_a, UP, buff=-0.1).shift(LEFT*0.6)
            a_label = MathTex(r"\mathbb{A}", font_size=40).next_to(a_circ, UP, buff=-0.1).shift(LEFT*0.6)
            
            a_arrows = VGroup(
                Arrow(n_circ_a.get_right() + UP*0.5, a_circ.get_left() + UP*0.5, buff=0.1, stroke_width=3, max_tip_length_to_length_ratio=0.15),
                Arrow(n_circ_a.get_right(), a_circ.get_left(), buff=0.1, stroke_width=3, max_tip_length_to_length_ratio=0.15),
                Arrow(n_circ_a.get_right() + DOWN*0.5, a_circ.get_left() + DOWN*0.5, buff=0.1, stroke_width=3, max_tip_length_to_length_ratio=0.15)
            )
            self.play(Create(n_circ_a), Create(a_circ), Write(n_label_a), Write(a_label))
            self.play(Create(a_arrows))

        # --- PART 8: REALS & OUTRO ---
        with self.voiceover(text="Some would say that set theory was born when Cantor showed that this pattern breaks once we hit the Real numbers.  Meaning that there is no way to put the naturals and reals into 1-1 correspondence.  And therefore the set of real numbers are a larger infinite set") as tracker:
            # Bottom pair for Reals with funneled arrows[cite: 1]
            n_circ_r = Circle(radius=0.8, color=BLUE).move_to(LEFT * 2 + DOWN * 3.0)
            r_circ = Circle(radius=0.8, color=BLUE).move_to(RIGHT * 2 + DOWN * 3.0)
            n_label_r = MathTex(r"\mathbb{N}", font_size=40).next_to(n_circ_r, UP, buff=-0.1).shift(LEFT*0.6)
            r_label = MathTex(r"\mathbb{R}", font_size=40).next_to(r_circ, UP, buff=-0.1).shift(LEFT*0.6)

            funnel_top = ArcBetweenPoints(n_circ_r.get_right() + UP*0.5, r_circ.get_left() + LEFT*0.3, angle=-PI/4, color=WHITE)
            funnel_bot = ArcBetweenPoints(n_circ_r.get_right() + DOWN*0.5, r_circ.get_left() + LEFT*0.3, angle=PI/4, color=WHITE)
            funnel_arrow = Arrow(r_circ.get_left() + LEFT*0.5, r_circ.get_left(), buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.3)
            
            self.play(Create(n_circ_r), Create(r_circ), Write(n_label_r), Write(r_label))
            self.play(Create(funnel_top), Create(funnel_bot), Create(funnel_arrow))

        with self.voiceover(text="We sketch this proof now.") as tracker:
            self.wait(tracker.duration * 0.8)
            self.play(*[FadeOut(m) for m in self.mobjects])