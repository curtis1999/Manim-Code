from manim import *

class SquaresBijection(Scene):
    def construct(self):
        # Set initial camera to show content
        self.camera.frame_height = 8
        self.camera.frame_width = 14
        
        # Phase 1: Show first 100 natural numbers on a single line
        naturals_line_100 = NumberLine(
            x_range=[0, 100, 1],
            length=10,
            include_numbers=[0,10,20,30,40,50,60,70,80,90,100],
            numbers_to_include=list(range(0, 101, 10)),  # Show every 10th number + 100
            font_size=16
        )
        naturals_line_100.shift(UP * 2)
        
        # Create the line
        self.play(
            Create(naturals_line_100),
        )
        self.wait(1)
        
        # Now highlight the perfect squares
        perfect_squares = [i*i for i in range(1, 11)]  # 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
        square_dots = []
        square_labels = []
        
        # Animate highlighting each square
        for square in perfect_squares:
            # Create dot for the square
            square_dot = Dot(
                naturals_line_100.number_to_point(square),
                color=YELLOW,
                radius=0.06
            )
            
            # Label for the square
            square_label = Text(str(square), font_size=14, color=YELLOW)
            square_label.next_to(square_dot, DOWN, buff=0.15)
            
            self.play(
                Create(square_dot),
                Write(square_label),
                run_time=0.2
            )
            
            square_dots.append(square_dot)
            square_labels.append(square_label)
            
            self.wait(0.1)
        
        self.wait(1)
        
        squares = Circle(color=YELLOW, radius=0.3, fill_opacity=0.5).next_to(naturals_line_100, DOWN, buff=2).shift(LEFT*2)
        naturals = Circle(color=WHITE, radius=0.9, fill_opacity=0.5).next_to(squares, RIGHT, buff=1)
        
        squares_label = MathTex(r"\text{Squares }_{\le 100}", font_size=22).next_to(squares,UP,buff=0.3)
        naturals_label = MathTex(r"\text{Naturals }_{\le 100}", font_size=22).next_to(naturals,UP,buff=0.3)
        
        self.play(
            Create(squares),
            Create(naturals),
            Write(squares_label),
            Write(naturals_label)
        )
        self.wait(2)
        self.play(FadeOut( naturals_line_100,
            square_dots[0], square_labels[0],square_dots[1], square_labels[1],square_dots[2], square_labels[2],
            square_dots[3], square_labels[3],square_dots[4], square_labels[4],square_dots[5], square_labels[5],
            square_dots[6], square_labels[6],square_dots[7], square_labels[7], square_dots[8], square_labels[8],
            square_dots[9], square_labels[9]))
        
        squares_2 = Circle(color=YELLOW, radius=0.15, fill_opacity=0.5).next_to(naturals_line_100, DOWN, buff=2).shift(LEFT*2)
        naturals_2 = Circle(color=WHITE, radius=1.5, fill_opacity=0.5).next_to(squares_2, RIGHT, buff=1)
        
        squares_label_2 = MathTex(r"\text{Squares }_{\le 10000}", font_size=22).next_to(squares_2,UP,buff=0.3)
        naturals_label_2 = MathTex(r"\text{Naturals }_{\le 10000}", font_size=22).next_to(naturals_2,UP,buff=0.3)
        
        self.play(Transform(squares, squares_2), Transform(naturals, naturals_2),
                  Transform(squares_label, squares_label_2), Transform(naturals_label, naturals_label_2))
        
        self.wait(1)
        
        squares_3 = Circle(color=YELLOW, radius=0.015, fill_opacity=0.5).next_to(naturals_line_100, DOWN, buff=2).shift(LEFT*2)
        naturals_3 = Circle(color=BLUE, radius=2, fill_opacity=0.5).next_to(squares_3, RIGHT, buff=1)
        
        squares_label_3 = MathTex(r"\text{Squares }_{\le 1000000}", font_size=22).next_to(squares_3,UP,buff=0.3)
        naturals_label_3 = MathTex(r"\text{Naturals }_{\le 1000000}", font_size=22).next_to(naturals_3,UP,buff=0.3)
        
        self.play(Transform(squares, squares_3), Transform(naturals, naturals_3),
                  Transform(squares_label, squares_label_3), Transform(naturals_label, naturals_label_3))
        
        self.wait(1)
        
        # Phase 3: Transition to bijection demonstration
        # Fade out the 100-number setup
        fade_objects = [
            squares, naturals, squares_label, naturals_label
        ]
        self.play(*[FadeOut(obj) for obj in fade_objects])
        self.wait(1)
        
        # Create zoomed-in number line for naturals only
        naturals_line_zoom = NumberLine(
            x_range=[1, 10, 1],
            length=8,
            include_numbers=True,
            numbers_to_include=list(range(1, 11)),
            font_size=20
        )
        naturals_line_zoom.shift(UP * 0.8)

        # Label for naturals
        naturals_label_zoom = Text("Naturals", font_size=22)
        naturals_label_zoom.next_to(naturals_line_zoom, LEFT, buff=0.3)

        #Label for squares
        squares_label_zoom = Text("Squares", font_size=22)
        squares_label_zoom.next_to(naturals_label_zoom, DOWN, buff=2)
        
        # Function notation
        function_text = Text("f(n) = n²", font_size=24).next_to(naturals_label_zoom,DOWN, buff=1)

        self.play(
            Create(naturals_line_zoom),
            Write(naturals_label_zoom), 
            Write(squares_label_zoom)
        )
        self.wait(0.5)

        self.play(Write(function_text))
        self.wait(1)

        # Animate the bijection with arrows pointing down
        natural_dots = []
        arrows = []
        formula_texts = []

        # Colors for different mappings
        colors = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE, PINK, TEAL, MAROON, GOLD]

        for i in range(1, 11):
            square_val = i * i
            
            # Create dot for current natural number
            nat_dot = Dot(
                naturals_line_zoom.number_to_point(i),
                color=colors[i-1],
                radius=0.08
            )
            
            # Label for the natural number
            nat_label = Text(str(i), font_size=18, color=colors[i-1])
            nat_label.next_to(nat_dot, UP, buff=0.1)
            
            # Arrow pointing straight down
            arrow_start = nat_dot.get_center()
            arrow_end = arrow_start + DOWN * 2
            arrow = Arrow(
                arrow_start,
                arrow_end,
                color=colors[i-1],
                stroke_width=3,
                max_tip_length_to_length_ratio=0.15
            )
            
            # Formula text (e.g., "3²")
            formula_text = Text(f"{i}²", font_size=20, color=colors[i-1])
            formula_text.move_to(arrow_end + DOWN * 0.3)
            
            # Result text (e.g., "9")
            result_text = Text(str(square_val), font_size=20, color=colors[i-1])
            result_text.move_to(arrow_end + DOWN * 0.3)
            
            # Animate this mapping
            self.play(
                Create(nat_dot),
                Write(nat_label),
                run_time=0.2
            )
            
            self.play(
                Create(arrow),
                run_time=0.3
            )
            
            # Show formula first
            self.play(
                Write(formula_text),
                run_time=0.2
            )
            
            # Transition from formula to result
            self.play(
                Transform(formula_text, result_text),
                run_time=0.5
            )
            
            natural_dots.append((nat_dot, nat_label))
            arrows.append(arrow)
            formula_texts.append(formula_text)  # This now contains the transformed result
            
            self.wait(0.2)

        self.wait(2)
        
        
        # Final fade out
        all_final_objects = [ naturals_line_zoom,
            naturals_label_zoom, function_text, 
        ] + [dot for dot, label in natural_dots] + [label for dot, label in natural_dots] + arrows + formula_texts
        
        self.play(*[FadeOut(obj) for obj in all_final_objects])
        self.wait(1)