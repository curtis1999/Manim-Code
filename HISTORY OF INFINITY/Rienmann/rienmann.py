from manim import *
import numpy as np

class RiemannSumArea(Scene):
    def construct(self):
        # Title
        title = Text("Calculus Method for Area Under Curves", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create axes
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 3, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": WHITE, "stroke_width": 2},
            tips=False
        )
        axes.center().shift(DOWN * 0.5)
        
        # Add axis labels
        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=RIGHT, buff=0.1)
        y_label = axes.get_y_axis_label("y", edge=UP, direction=UP, buff=0.1)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)
        
        # Define the function f(x) = x^2/2 + 0.5
        def func(x):
            return x**2 / 2 + 0.5
        
        # Create the curve
        curve = axes.plot(func, x_range=[0.5, 3.5], color=BLUE, stroke_width=4)
        curve_label = MathTex(r"f(x) = \frac{x^2}{2} + 0.5", color=BLUE, font_size=28)
        curve_label.next_to(axes, UP, buff=0.5).shift(RIGHT * 2)
        
        self.play(Create(curve), Write(curve_label))
        self.wait(1)
        
        # Define integration bounds
        a, b = 1, 3
        
        # Add vertical lines at bounds
        left_line = axes.get_vertical_line(axes.c2p(a, func(a)), color=GREEN, stroke_width=3)
        right_line = axes.get_vertical_line(axes.c2p(b, func(b)), color=GREEN, stroke_width=3)
        
        # Add labels for bounds
        a_label = MathTex("a", color=GREEN, font_size=24).next_to(axes.c2p(a, 0), DOWN, buff=0.1)
        b_label = MathTex("b", color=GREEN, font_size=24).next_to(axes.c2p(b, 0), DOWN, buff=0.1)
        
        self.play(
            Create(left_line), Create(right_line),
            Write(a_label), Write(b_label)
        )
        self.wait(1)
        
        # Highlight the area under the curve
        area_under_curve = axes.get_area(curve, x_range=[a, b], color=YELLOW, opacity=0.3)
        area_text = Text("Area = ?", font_size=24, color=YELLOW)
        area_text.next_to(axes.c2p(2, 1.5), RIGHT, buff=0.3)
        
        self.play(Create(area_under_curve), Write(area_text))
        self.wait(2)
        
        # Create number line for area estimation
        number_line = NumberLine(
            x_range=[2, 6, 0.5],
            length=8,
            include_numbers=True,
            numbers_to_include=[2, 3, 4, 5, 6],
            font_size=20
        ).shift(DOWN * 3)
        
        line_title = Text("Area Estimation", font_size=20).next_to(number_line, DOWN, buff=0.2)
        
        self.play(Create(number_line), Write(line_title))
        self.wait(1)
        
        # Calculate exact area for reference (integral of x^2/2 + 0.5 from 1 to 3)
        exact_area = (3**3/6 + 0.5*3) - (1**3/6 + 0.5*1)  # ≈ 4.333
        exact_point = Dot(number_line.number_to_point(exact_area), color=YELLOW, radius=0.06)
        exact_label = MathTex(r"\text{Exact}", color=YELLOW, font_size=18).next_to(exact_point, UP, buff=0.1)
        
        self.play(Create(exact_point), Write(exact_label))
        self.wait(1)
        
        # Function to create rectangles for Riemann sum
        def create_rectangles(n, method="left", color=RED, opacity=0.4):
            rectangles = VGroup()
            dx = (b - a) / n
            total_area = 0
            
            for i in range(n):
                x_left = a + i * dx
                x_right = a + (i + 1) * dx
                x_mid = (x_left + x_right) / 2
                
                if method == "left":
                    height = func(x_left)
                elif method == "right":
                    height = func(x_right)
                elif method == "midpoint":
                    height = func(x_mid)
                
                # Create rectangle
                rect = Rectangle(
                    width=axes.x_axis.unit_size * dx,
                    height=axes.y_axis.unit_size * height,
                    color=color,
                    fill_opacity=opacity,
                    stroke_width=2
                )
                
                # Position rectangle
                rect.align_to(axes.c2p(x_left, 0), DOWN + LEFT)
                rectangles.add(rect)
                
                total_area += height * dx
            
            return rectangles, total_area
        
        # Store current rectangles and points for transitions
        current_rectangles = VGroup()
        current_point = Dot()
        current_label = MathTex("")
        
        # Show progression with different numbers of rectangles
        n_values = [2, 4, 8, 16, 32]
        colors = [RED, PURPLE, ORANGE, GREEN, BLUE]
        
        for i, (n, color) in enumerate(zip(n_values, colors)):
            # Create rectangles using left endpoint rule
            rectangles, approx_area = create_rectangles(n, method="left", color=color, opacity=0.3)
            
            # Create point on number line
            area_point = Dot(number_line.number_to_point(approx_area), color=color, radius=0.05)
            area_label = MathTex(f"n={n}", color=color, font_size=16).next_to(area_point, DOWN, buff=0.1)
            
            # Show method description
            method_text = Text(f"Left Riemann Sum with n = {n} rectangles", font_size=20)
            method_text.to_edge(DOWN).shift(UP * 0.8)
            
            if i == 0:
                # First iteration - create everything
                self.play(
                    Create(rectangles),
                    Create(area_point),
                    Write(area_label),
                    Write(method_text)
                )
                current_rectangles = rectangles
                current_point = area_point
                current_label = area_label
                current_method_text = method_text
            else:
                # Subsequent iterations - transform existing elements
                self.play(
                    Transform(current_rectangles, rectangles),
                    Transform(current_point, area_point),
                    Transform(current_label, area_label),
                    Transform(current_method_text, method_text),
                    run_time=1.5
                )
            
            self.wait(1.5)
        
        # Show that rectangles are getting closer to the exact area
        convergence_text = MathTex(r"\lim_{n \to \infty} \sum_{i=1}^{n} f(x_i) \Delta x = \int_a^b f(x) \, dx", 
                                 font_size=24)
        convergence_text.next_to(area_text, DOWN, buff=0.5)
        
        self.play(Write(convergence_text))
        self.wait(2)
        
        # Clean up for final demonstration
        self.play(
            FadeOut(current_rectangles),
            FadeOut(current_method_text),
            FadeOut(area_text)
        )
        
        # Show comparison of different methods with n=8
        n = 8
        
        # Left Riemann sum
        left_rects, left_area = create_rectangles(n, method="left", color=RED, opacity=0.2)
        left_point = Dot(number_line.number_to_point(left_area), color=RED, radius=0.05)
        left_label = MathTex("L", color=RED, font_size=16).next_to(left_point, DOWN, buff=0.1)
        
        # Right Riemann sum  
        right_rects, right_area = create_rectangles(n, method="right", color=BLUE, opacity=0.2)
        right_point = Dot(number_line.number_to_point(right_area), color=BLUE, radius=0.05)
        right_label = MathTex("R", color=BLUE, font_size=16).next_to(right_point, UP, buff=0.1)
        
        # Midpoint rule
        mid_rects, mid_area = create_rectangles(n, method="midpoint", color=GREEN, opacity=0.2)
        mid_point = Dot(number_line.number_to_point(mid_area), color=GREEN, radius=0.05)
        mid_label = MathTex("M", color=GREEN, font_size=16).next_to(mid_point, DOWN, buff=0.1)
        
        # Show left rectangles first
        comparison_text = Text("Left Riemann Sum", font_size=20, color=RED).to_edge(DOWN).shift(UP * 0.8)
        self.play(
            Create(left_rects),
            Create(left_point),
            Write(left_label),
            Write(comparison_text)
        )
        self.wait(1.5)
        
        # Add right rectangles
        right_comparison_text = Text("Left (Red) vs Right (Blue) Riemann Sums", font_size=18).to_edge(DOWN).shift(UP * 0.8)
        self.play(
            Create(right_rects),
            Create(right_point),
            Write(right_label),
            Transform(comparison_text, right_comparison_text)
        )
        self.wait(1.5)
        
        # Add midpoint rectangles
        final_comparison_text = Text("Left (Red), Right (Blue), Midpoint (Green)", font_size=18).to_edge(DOWN).shift(UP * 0.8)
        self.play(
            Create(mid_rects),
            Create(mid_point),
            Write(mid_label),
            Transform(comparison_text, final_comparison_text)
        )
        self.wait(2)
        
        # Show inequality relationship
        inequality_text = MathTex(r"L_n \leq \int_a^b f(x) \, dx \leq R_n", font_size=24)
        inequality_text.next_to(convergence_text, DOWN, buff=0.3)
        self.play(Write(inequality_text))
        self.wait(1)
        
        # Final emphasis on convergence
        final_text = MathTex(r"\lim_{n \to \infty} L_n = \lim_{n \to \infty} R_n = \int_a^b f(x) \, dx", 
                           font_size=20)
        final_text.next_to(inequality_text, DOWN, buff=0.3)
        
        self.play(
            Write(final_text),
            curve.animate.set_stroke(width=6)
        )
        self.wait(3)
        
        # Show final result
        result_text = MathTex(r"\int_1^3 \left(\frac{x^2}{2} + 0.5\right) dx = \frac{13}{3} \approx 4.33", 
                            font_size=24, color=YELLOW)
        result_text.next_to(final_text, DOWN, buff=0.5)
        
        self.play(Write(result_text))
        self.wait(3)