from manim import *

class SquaresBijection(Scene):
    def construct(self):
        # Set initial camera to show content
        self.camera.frame_height = 8
        self.camera.frame_width = 14
        
        # Phase 1: Show first 100 natural numbers on a single line
        naturals_line_100 = NumberLine(
            x_range=[0, 101, 1],
            length=10,
            include_numbers=[0,10,20,30,40,50,60,70,80,90,100],
            numbers_to_include=list(range(0, 100, 10)),  # Show every 10th number + 100
            font_size=16
        )
        naturals_line_100.shift(UP * 1)
        
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
                run_time=2
            )
            
            square_dots.append(square_dot)
            square_labels.append(square_label)
            
            self.wait(0.1)
        
        self.wait(1)
        
        # Phase 2: Show first 10000 natural numbers on a single line
        naturals_line_10000 = NumberLine(
            x_range=[0, 10001, 100],
            length=10,
            include_numbers=[0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000],
            numbers_to_include=list(range(0, 10001, 1000)),  # Show every 1000th number
            font_size=16
        )
        naturals_line_10000.shift(UP * 1)
        
        # Create the line
        self.play(
            Transform(naturals_line_100, naturals_line_10000),
        )
        self.wait(1)
        
        # Now highlight the perfect squares (only the first 100 perfect squares: 1², 2², ..., 100²)
        perfect_squares_10000 = [i*i for i in range(1, 101)]  # 1, 4, 9, ..., 10000
        square_dots = []
        square_labels = []
        
        # Animate highlighting each square (much faster with fewer squares)
        for square in perfect_squares_10000:
            # Create dot for the square
            square_dot = Dot(
                naturals_line_100.number_to_point(square),
                color=YELLOW,
                radius=0.06
            )
            
            # Only label some key squares to avoid clutter
            if square in [1, 4, 9, 25, 49, 100, 400, 900, 2500, 4900, 10000]:
                square_label = Text(str(square), font_size=12, color=YELLOW)
                square_label.next_to(square_dot, DOWN, buff=0.15)
            else:
                square_label = None
            
            if square_label:
                self.play(
                    Create(square_dot),
                    Write(square_label),
                    run_time=0.5
                )
                square_labels.append(square_label)
            else:
                self.play(
                    Create(square_dot),
                    run_time=0.3
                )
            
            square_dots.append(square_dot)
            
            self.wait(0.05)
        
        self.wait(1)
        
        # Phase 3: Transition to bijection demonstration
        # Fade out the 100-number setup
        fade_objects = [
            naturals_line_100,
        ] + square_dots + square_labels
        
        self.play(*[FadeOut(obj) for obj in fade_objects])
        self.wait(0.5)
        
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
        naturals_label_zoom = Text("Natural Numbers ℕ", font_size=22)
        naturals_label_zoom.next_to(naturals_line_zoom, LEFT, buff=0.3)

        # Function notation
        function_text = Text("f(n) = n²", font_size=24)
        function_text.shift(UP * 2 + RIGHT * 2.5)

        # Subtitle for bijection phase
        bijection_subtitle = Text("One-to-one correspondence", font_size=20)
        bijection_subtitle.shift(UP * 2.2 + LEFT * 2)

        # Animate setup
        self.play(Write(bijection_subtitle))
        self.wait(0.5)

        self.play(
            Create(naturals_line_zoom),
            Write(naturals_label_zoom)
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
                run_time=0.3
            )
            
            self.play(
                Create(arrow),
                run_time=0.4
            )
            
            # Show formula first
            self.play(
                Write(formula_text),
                run_time=0.3
            )
            
            # Transition from formula to result
            self.play(
                Transform(formula_text, result_text),
                run_time=0.4
            )
            
            natural_dots.append((nat_dot, nat_label))
            arrows.append(arrow)
            formula_texts.append(formula_text)  # This now contains the transformed result
            
            self.wait(0.2)

        self.wait(2)
        
        # Add final explanation
        final_explanation = Text(
            "Every natural number maps to exactly one square",
            font_size=20
        )
        final_explanation.shift(DOWN * 2.5)
        
        self.play(Write(final_explanation))
        self.wait(3)
        
        # Final fade out
        all_final_objects = [
            bijection_subtitle, naturals_line_zoom,
            naturals_label_zoom, function_text, final_explanation
        ] + [dot for dot, label in natural_dots] + [label for dot, label in natural_dots] + arrows + formula_texts
        
        self.play(*[FadeOut(obj) for obj in all_final_objects])
        self.wait(1)