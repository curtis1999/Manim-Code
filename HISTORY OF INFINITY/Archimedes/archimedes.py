from manim import *
import numpy as np

class ArchimedesCircleArea(Scene):
    def construct(self):
        # Create the circle with radius 1
        circle = Circle(radius=2, color=YELLOW, stroke_width=4)  # Display radius 2 for visibility
        circle_label = MathTex("C", color=YELLOW).next_to(circle, RIGHT)
        
        # Add origin point and radius line
        origin = Dot(ORIGIN, color=WHITE, radius=0.02)
        radius_line = Line(ORIGIN, [2, 0, 0], color=WHITE, stroke_width=3)
        radius_label = MathTex("1", color=WHITE, font_size=24).next_to(radius_line, DOWN, buff=0.1)
        
        self.play(
            Create(circle), 
            Write(circle_label),
            Create(origin),
            Create(radius_line),
            Write(radius_label)
        )
        self.wait(1)
        
        # Define pi as the ratio of circumference to radius
        pi_definition = MathTex(r"\pi = \frac{\text{circumference of semicircle}}{\text{radius}}", font_size=28)
        pi_definition.to_edge(UP).shift(DOWN*0.5)
        self.play(Write(pi_definition))
        self.wait(2)
        
        # Create number line from 0-5 before highlighting semicircle
        number_line = NumberLine(
            x_range=[0, 5, 1],
            length=8,
            include_numbers=True,
            numbers_to_include=[0, 1, 2, 3, 4, 5],
            font_size=24
        ).shift(DOWN * 2.5)
        
        self.play(Create(number_line))
        self.wait(1)
        
        # Highlight the top semicircle
        top_semicircle = Arc(radius=2, angle=PI, color=GREEN, stroke_width=6)
        self.play(Create(top_semicircle))
        self.wait(1)
        
        # Superimpose the flattened semicircle over the number line
        # Calculate the positions on the number line for 0 to π
        start_point = number_line.number_to_point(0)
        end_point = number_line.number_to_point(PI)
        
        # Create the unfurled line directly on the number line
        unfurled_line = Line(start_point, end_point, color=GREEN, stroke_width=6)
        unfurl_label = MathTex(r"\pi", color=GREEN, font_size=24).next_to(end_point, UP, buff=0.2)
        
        # Animate the unfurling onto the number line
        # Store the transformed object properly
        self.play(
            Transform(top_semicircle, unfurled_line),
            Write(unfurl_label)
        )
        
        # Add pi marker on number line
        pi_point = Dot(number_line.number_to_point(PI), color=YELLOW, radius=0.06)  # Made slightly larger
        pi_label = MathTex(r"\pi", color=YELLOW, font_size=28).next_to(pi_point, UP, buff=0.1)
        
        self.play(Create(pi_point), Write(pi_label))
        self.wait(1)  # Add a small wait to let it settle
                
        # Show the ratio
        ratio_text = MathTex(r"\pi \approx 3.14159...", font_size=24)
        ratio_text.next_to(number_line, DOWN, buff=0.5)
        self.play(Write(ratio_text))
        self.wait(2)  # Give time to read
        
        # Clean up before continuing with polygon approximation
        self.play(
            FadeOut(pi_definition),
            FadeOut(top_semicircle),  # This will fade the transformed line
            FadeOut(unfurl_label),
            FadeOut(ratio_text),
            FadeOut(pi_point),
            FadeOut(pi_label)
        )
        self.wait(1)
        
        # Function to create inscribed polygon (with squares having flat bottom)
        def create_inscribed_polygon(n_sides, radius=2, color=BLUE):
            vertices = []
            # For squares, start with bottom edge horizontal
            start_angle = -PI/2 if n_sides == 4 else 0
            for i in range(n_sides):
                angle = start_angle + 2 * PI * i / n_sides
                x = radius * np.cos(angle)
                y = radius * np.sin(angle)
                vertices.append([x, y, 0])
            return Polygon(*vertices, color=color, fill_opacity=0.3, stroke_width=3)
        # Function to create circumscribed polygon (with squares having flat bottom)
        def create_circumscribed_polygon(n_sides, radius=2, color=RED):
            # For circumscribed polygon, we need to find the distance from center to side
            apothem = radius  # radius of inscribed circle
            side_distance = apothem / np.cos(PI / n_sides)  # distance from center to vertex
            
            vertices = []
            # For squares, start with bottom edge horizontal
            start_angle = -PI/2 if n_sides == 4 else 0
            for i in range(n_sides):
                angle = start_angle + 2 * PI * i / n_sides
                x = side_distance * np.cos(angle)
                y = side_distance * np.sin(angle)
                vertices.append([x, y, 0])
            return Polygon(*vertices, color=color, fill_opacity=0.2, stroke_width=3)
        
        # Function to calculate actual areas (for radius=1 circle)
        def get_inscribed_area(n_sides):
            # Area of regular n-gon inscribed in unit circle
            return 0.5 * n_sides * np.sin(2 * PI / n_sides)
        
        def get_circumscribed_area(n_sides):
            # Area of regular n-gon circumscribed around unit circle
            return n_sides * np.tan(PI / n_sides)
        
        # Show inscribed and circumscribed squares first
        inscribed_square = create_inscribed_polygon(4, color=BLUE)
        i_square_label = MathTex(r"I_0", color=BLUE, font_size=35).next_to(inscribed_square, LEFT, buff=0.3).shift(RIGHT*0.25)
        circumscribed_square = create_circumscribed_polygon(4, color=RED)
        e_square_label = MathTex(r"E_0", color=RED, font_size=35).next_to(circumscribed_square, RIGHT, buff=0.3).shift(LEFT*0.35)
        # Calculate areas for n=4 and show on number line
        i_4 = get_inscribed_area(4)
        e_4 = get_circumscribed_area(4)
        
        # Add vertical lines on number line instead of dots
        i_4_line = Line(
            number_line.number_to_point(i_4) + UP * 0.15,
            number_line.number_to_point(i_4) + DOWN * 0.15,
            color=BLUE, stroke_width=3
        )
        e_4_line = Line(
            number_line.number_to_point(e_4) + UP * 0.15,
            number_line.number_to_point(e_4) + DOWN * 0.15,
            color=RED, stroke_width=3
        )
        i_4_line_label = MathTex(r"I_0", color=BLUE, font_size=20).next_to(i_4_line, UP, buff=0.1)
        e_4_line_label = MathTex(r"E_0", color=RED, font_size=20).next_to(e_4_line, UP, buff=0.1)
        
        self.play(
            Create(inscribed_square),
            Write(i_square_label),Create(i_4_line), Write(i_4_line_label),) 
        self.wait(2)

        self.play(
            Create(circumscribed_square),
             Write(e_square_label), 
            Create(e_4_line), Write(e_4_line_label))   
        # Show the areas relationship
        area_text = MathTex(
            r"I_0 < \pi < E_0",
            font_size=40
        ).to_edge(DOWN)
        self.play(Write(area_text))
        self.wait(2)
        
        # Transition to octagon (n=8) - show inscribed first, then circumscribed
        #self.play(FadeOut(area_text))
        
        # Store previous elements for smooth transitions
        current_inscribed = inscribed_square
        current_circumscribed = circumscribed_square
        current_i_line = i_4_line
        current_e_line = e_4_line
        current_i_line_label = i_4_line_label  
        current_e_line_label = e_4_line_label
        current_i_label = i_square_label
        current_e_label = e_square_label
        
        # Show inscribed and circumscribed octagons
        inscribed_octagon = create_inscribed_polygon(8, color=BLUE)
        circumscribed_octagon = create_circumscribed_polygon(8, color=RED)
        
        # Add polygon labels
        i_octagon_label = MathTex(r"I_1", color=BLUE, font_size=24).next_to(inscribed_octagon, LEFT, buff=0.3)
        e_octagon_label = MathTex(r"E_1", color=RED, font_size=24).next_to(circumscribed_octagon, RIGHT, buff=0.3)
        
         # Calculate areas for n=8
        i_8 = get_inscribed_area(8)
        e_8 = get_circumscribed_area(8)
        
        # New lines on number line
        i_8_line = Line(
            number_line.number_to_point(i_8) + UP * 0.15,
            number_line.number_to_point(i_8) + DOWN * 0.15,
            color=BLUE, stroke_width=3
        )
        e_8_line = Line(
            number_line.number_to_point(e_8) + UP * 0.15,
            number_line.number_to_point(e_8) + DOWN * 0.15,
            color=RED, stroke_width=3
        )
        i_8_line_label = MathTex(r"I_1", color=BLUE, font_size=20).next_to(i_8_line, DOWN, buff=0.1)
        e_8_line_label = MathTex(r"E_1", color=RED, font_size=20).next_to(e_8_line, UP, buff=0.1)
        
        self.play(
            Transform(current_inscribed, inscribed_octagon),
            Transform(current_i_label, i_octagon_label),
            Transform(current_i_line, i_8_line),
            Transform(current_i_line_label, i_8_line_label))
        self.wait(1)
        #Update area text
        area_text2 = MathTex(
            r"I_0 < I_1 < \pi < E_0",
            font_size=40
        ).to_edge(DOWN)
        self.play(Transform(area_text,area_text2))
        self.wait(2)
        self.play(
            Transform(current_circumscribed, circumscribed_octagon),
            Transform(current_e_label, e_octagon_label),
            Transform(current_e_line, e_8_line),
            Transform(current_e_line_label, e_8_line_label)
        )
        # Update area text
        area_text3 = MathTex(
            r"I_0 < I_1< \pi < E_1 < E_0",
            font_size=40
        ).to_edge(DOWN)
        self.play(Transform(area_text,area_text3))
        self.wait(2)
        
        # Show progression with increasing n
        n_values = [16, 32, 64]
        polygon_names = ["16-gon", "32-gon", "64-gon"]
        label_indices = [2, 3, 4]  # I_2/E_2, I_3/E_3, I_4/E_4
        
        for i, (n, name, label_idx) in enumerate(zip(n_values, polygon_names, label_indices)):
            # Create new polygons
            inscribed_poly = create_inscribed_polygon(n, color=BLUE)
            circumscribed_poly = create_circumscribed_polygon(n, color=RED)
            
            # Add polygon labels
            i_poly_label = MathTex(f"I_{{{label_idx}}}", color=BLUE, font_size=24).next_to(inscribed_poly, LEFT, buff=0.3)
            e_poly_label = MathTex(f"E_{{{label_idx}}}", color=RED, font_size=24).next_to(circumscribed_poly, RIGHT, buff=0.3)
            
             # Calculate areas for current n
            i_n = get_inscribed_area(n)
            e_n = get_circumscribed_area(n)
            
            # New lines on number line
            i_n_line = Line(
                number_line.number_to_point(i_n) + UP * 0.15,
                number_line.number_to_point(i_n) + DOWN * 0.15,
                color=BLUE, stroke_width=3
            )
            e_n_line = Line(
                number_line.number_to_point(e_n) + UP * 0.15,
                number_line.number_to_point(e_n) + DOWN * 0.15,
                color=RED, stroke_width=3
            )
            i_n_line_label = MathTex(f"I_{{{label_idx}}}", color=BLUE, font_size=20).next_to(i_n_line, DOWN, buff=0.1)
            e_n_line_label = MathTex(f"E_{{{label_idx}}}", color=RED, font_size=20).next_to(e_n_line, UP, buff=0.1)
            
            self.play(
                Transform(current_inscribed, inscribed_poly),
                Transform(current_i_label, i_poly_label),
                Transform(current_i_line, i_n_line),
                Transform(current_i_line_label, i_n_line_label),)
            
            # Update area text after showing inscribed polygon
            if label_idx == 2:
                area_text4 = MathTex(
                    r"I_0 < I_1 < I_2 < \pi < E_1 < E_0",
                    font_size=40
                ).to_edge(DOWN)
            elif label_idx == 3:
                area_text4 = MathTex(
                    r"I_0 < I_1 < I_2 < I_3 < \pi < E_2 < E_1 < E_0",
                    font_size=40
                ).to_edge(DOWN)
            elif label_idx == 4:
                area_text4 = MathTex(
                    r"I_0 < I_1 < I_2 < I_3 < I_4 < \pi < E_3 < E_2 < E_1 < E_0",
                    font_size=40
                ).to_edge(DOWN)
            
            self.play(Transform(area_text, area_text4))
            self.wait(1)
            
            self.play(
                Transform(current_circumscribed, circumscribed_poly),                
                Transform(current_e_label, e_poly_label),
                Transform(current_e_line, e_n_line),                
                Transform(current_e_line_label, e_n_line_label),
            )
            
            # Update area text after showing circumscribed polygon
            if label_idx == 2:
                area_text5 = MathTex(
                    r"I_0 < I_1 < I_2 < \pi < E_2 < E_1 < E_0",
                    font_size=40
                ).to_edge(DOWN)
            elif label_idx == 3:
                area_text5 = MathTex(
                    r"I_0 < I_1 < I_2 < I_3 < \pi < E_3 < E_2 < E_1 < E_0",
                    font_size=40
                ).to_edge(DOWN)
            elif label_idx == 4:
                area_text5 = MathTex(
                    r"I_0 < I_1 < I_2 < I_3 < I_4 < \pi < E_4 < E_3 < E_2 < E_1 < E_0",
                    font_size=40
                ).to_edge(DOWN)
            
            self.play(Transform(area_text, area_text5))
            self.wait(1)
        
        # Fade out polygons but keep the circle and number line
        self.play(
            FadeOut(current_inscribed),
            FadeOut(current_circumscribed),
            FadeOut(current_i_label),
            FadeOut(current_e_label),
            FadeOut(area_text)
        )
        
        final_text = MathTex(r"I_\infty = E_\infty = \pi", font_size=40)
        final_text.to_edge(DOWN)
        
        area_formula = MathTex(r"\text{Area} = \pi r^2 = \pi \cdot 1^2 = \pi", font_size=40)
        area_formula.next_to(final_text, DOWN, buff=0.3)
        
        self.play(
            circle.animate.set_stroke(width=6),
            Write(final_text),
            Write(area_formula)
        )
        self.wait(3)
        self.play(FadeOut(final_text), FadeOut(area_formula), FadeOut(circle), FadeOut(radius_line), FadeOut(radius_label), FadeOut(origin), FadeOut(circle_label), FadeOut(number_line), FadeOut(pi_point), FadeOut(pi_label), FadeOut(current_i_line), FadeOut(current_e_line), FadeOut(current_i_line_label), FadeOut(current_e_line_label))
                # Euclid's definition (historical context)
        continuity_citation = Text(
            "If initially a > E, and then diminished by at least half of itself,\n"
            "and the remainder again by at least half of itself, and so on,\n"
            "a point will be reached where the remainder is less than E.",
            font_size=24,
            line_spacing=1.2
        ).to_edge(UP, buff=1)

        self.play(Write(continuity_citation))
        self.wait(2)

        # Modern delta-epsilon definition of limits/continuity
        limit_definition = MathTex(
        r"\text{If there is given a sequence of infinitely many numbers } S_1, S_2, \ldots, \\",
        r"\text{and if for any preassigned number } E > 0 \text{ a number } S_p \text{ of the sequence} \\",
        r"\text{can be found such that it and all subsequent } S_n, (n \geq p), \text{ differ} \\",
        r"\text{from a fixed number } s \text{ by less than } E, \text{ then we say that the sequence} \\",
        r"\text{converges to the limit } s, \text{ and write } \lim S_n = s.",
        font_size=22
    ).next_to(continuity_citation, DOWN, buff=1.5)

        self.play(Write(limit_definition))
        self.wait(3)

        # Fade out both definitions
        self.play(
            FadeOut(continuity_citation),
            FadeOut(limit_definition)
        )
        
        
        #REINMANN AND CALCULUS
        
        
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
        
        self.play(Create(curve))
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
        
        self.play(Create(area_under_curve))
        self.wait(2)

        
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
        n_values = [2, 4, 8, 16, 32, 64, 128]
        colors = [RED, PURPLE, ORANGE, GREEN, BLUE]
        
        for i, (n, color) in enumerate(zip(n_values, colors)):
            # Create rectangles using left endpoint rule
            rectangles, approx_area = create_rectangles(n, method="left", color=color, opacity=0.3)
            
            if i == 0:
                # First iteration - create everything
                self.play(
                    Create(rectangles),
                )
                current_rectangles = rectangles
            else:
                # Subsequent iterations - transform existing elements
                self.play(
                    Transform(current_rectangles, rectangles),
                    run_time=1
                )
            
            self.wait(0.5)
        
        # Show that rectangles are getting closer to the exact area
        convergence_text = MathTex(r"\lim_{n \to \infty} \sum_{i=1}^{n} f(x_i) \Delta x = \int_a^b f(x) \, dx", 
                                 font_size=24)
        convergence_text.shift(RIGHT*2)
        
        self.play(Write(convergence_text))
        self.wait(2)
        
        # Clean up for final demonstration
        self.play(
            FadeOut(current_rectangles)
        )
