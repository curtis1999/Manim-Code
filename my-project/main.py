from manim import *

class SquaresBijection(Scene):
    def construct(self):
        # Set camera to show more content
        self.camera.frame_height = 10
        self.camera.frame_width = 14
        
        # Title
        title = Text("1-1 Correspondence: ℕ ↔ Perfect Squares", font_size=28)
        title.shift(UP * 3)
        
        # Create number lines
        naturals_line = NumberLine(
            x_range=[0, 10, 1],
            length=6,
            include_numbers=True,
            numbers_to_include=list(range(1, 10)),
            font_size=20
        )
        naturals_line.shift(UP * 0.8)
        
        squares_line = NumberLine(
            x_range=[0, 50, 5],
            length=6,
            include_numbers=True,
            numbers_to_include=[1, 4, 9, 16, 25, 36, 49],
            font_size=20
        )
        squares_line.shift(DOWN * 0.8)
        
        # Labels
        naturals_label = Text("Natural Numbers ℕ", font_size=22)
        naturals_label.next_to(naturals_line, LEFT, buff=0.3)
        
        squares_label = Text("Perfect Squares", font_size=22)
        squares_label.next_to(squares_line, LEFT, buff=0.3)
        
        # Function notation
        function_text = Text("f(n) = n²", font_size=24)
        function_text.shift(UP * 2 + RIGHT * 2.5)
        
        # Animate initial setup
        self.play(Write(title))
        self.wait(0.5)
        
        self.play(
            Create(naturals_line),
            Write(naturals_label)
        )
        self.wait(0.5)
        
        self.play(
            Create(squares_line),
            Write(squares_label)
        )
        self.wait(0.5)
        
        self.play(Write(function_text))
        self.wait(1)
        
        # Create dots for the correspondence
        natural_dots = []
        square_dots = []
        arrows = []
        
        # Colors for different mappings
        colors = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE, PINK]
        
        # Animate the bijection one by one
        for i in range(1, 8):
            # Natural number dot
            nat_dot = Dot(
                naturals_line.number_to_point(i),
                color=colors[i-1],
                radius=0.08
            )
            
            # Square dot
            square_val = i * i
            square_dot = Dot(
                squares_line.number_to_point(square_val),
                color=colors[i-1],
                radius=0.08
            )
            
            # Arrow connecting them
            arrow = Arrow(
                nat_dot.get_center(),
                square_dot.get_center(),
                color=colors[i-1],
                stroke_width=3,
                max_tip_length_to_length_ratio=0.1
            )
            
            # Labels showing the mapping
            nat_label = Text(str(i), font_size=20, color=colors[i-1])
            nat_label.next_to(nat_dot, UP, buff=0.1)
            
            square_label = Text(str(square_val), font_size=20, color=colors[i-1])
            square_label.next_to(square_dot, DOWN, buff=0.1)
            
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
            
            self.play(
                Create(square_dot),
                Write(square_label),
                run_time=0.3
            )
            
            natural_dots.append((nat_dot, nat_label))
            square_dots.append((square_dot, square_label))
            arrows.append(arrow)
            
            self.wait(0.2)
        
        self.wait(2)
        
        # Add explanation text
        explanation1 = Text(
            "Every natural number maps to exactly one perfect square",
            font_size=20
        )
        explanation1.shift(DOWN * 2.5)
        
        self.play(Write(explanation1))
        self.wait(2)
        
       
        
        # Fade out everything
        all_objects = [
            title, naturals_line, squares_line, naturals_label, squares_label,
            function_text, explanation1
        ] + [dot for dot, label in natural_dots] + [label for dot, label in natural_dots] + \
          [dot for dot, label in square_dots] + [label for dot, label in square_dots] + arrows
        
        self.play(*[FadeOut(obj) for obj in all_objects])
        self.wait(1)