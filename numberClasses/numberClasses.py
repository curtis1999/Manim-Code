from manim import *

class NumberSetsVisualization(Scene):
    def construct(self):
        # Part 1: Concentric circles representing number sets
        self.show_concentric_circles()
        
        # Transition to number line
        self.wait(2)
        self.fade_everything()
        
        # Part 2: Number line with interval demonstrations
        self.show_number_line()
        
    def show_concentric_circles(self):
        # Create concentric circles on the left side
        circles_center = LEFT * 3
        
        # Natural numbers (innermost circle)
        natural_circle = Circle(radius=0.8, color=BLUE).move_to(circles_center)
        natural_label = Text("ℕ", font_size=24, color=BLUE).move_to(circles_center)
        
        # Rational numbers (middle circle)
        rational_circle = Circle(radius=1.4, color=GREEN).move_to(circles_center)
        rational_label = Text("ℚ", font_size=24, color=GREEN).move_to(circles_center + UP * 1.1)
        
        # Real numbers (outermost circle)
        real_circle = Circle(radius=2.0, color=RED).move_to(circles_center)
        real_label = Text("ℝ", font_size=24, color=RED).move_to(circles_center + UP * 1.7)
        
        # Definitions on the right side
        definitions_start = RIGHT * 2 + UP * 2
        
        natural_def = VGroup(
            Text("Natural Numbers (ℕ): 1, 2, 3, 4,...", font_size=20, color=BLUE).align_to(definitions_start, LEFT),
        ).arrange(DOWN, aligned_edge=LEFT)
        
        rational_def = VGroup(
            Text("Rational Numbers (ℚ): eg 1/2, 7/8, 17/35,.. ", font_size=20, color=GREEN).align_to(definitions_start, LEFT),
            Text(r"\{\frac{a}{b}: a,b \in \mathbb{N} b \ne 0\}", font_size=16, color=WHITE).align_to(definitions_start, LEFT),
        ).arrange(DOWN, aligned_edge=LEFT)
        
        real_def = VGroup(
            Text("Real Numbers (ℝ):", font_size=20, color=RED).align_to(definitions_start, LEFT),
            Text("All numbers that fit on the number line", font_size=16, color=WHITE).align_to(definitions_start, LEFT),
            Text("Including √2, π, e, etc.", font_size=16, color=WHITE).align_to(definitions_start, LEFT)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        # Position the definitions
        natural_def.move_to(definitions_start)
        rational_def.next_to(natural_def, DOWN * 1.5, aligned_edge=LEFT)
        real_def.next_to(rational_def, DOWN * 1.5, aligned_edge=LEFT)
        
        # Animation sequence
        
        self.play(Create(natural_circle))
        self.play(Write(natural_label))
        self.play(Write(natural_def))
        
        self.play(Create(rational_circle))
        self.play(Write(rational_label))
        self.play(Write(rational_def))
        
        self.wait(1)
        
        self.play(Create(real_circle))
        self.play(Write(real_label))
        self.play(Write(real_def))
        self.wait(2)
        
        # Store objects for later fading
        self.circles_group = VGroup(
            natural_circle, rational_circle, real_circle,
            natural_label, rational_label, real_label,
            natural_def, rational_def, real_def
        )
    
    def fade_everything(self):
        self.play(FadeOut(self.circles_group))
        self.wait(1)
    
    def show_number_line(self):
        # Create number line from 0 to 10
        number_line = NumberLine(
            x_range=[0, 10, 1],
            length=12,
            color=WHITE,
            include_numbers=True,
            numbers_with_elongated_ticks=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        )
        
        self.play(Create(number_line))
        self.wait(1)
        
        # Highlight first interval [0,1]
        interval_1 = Rectangle(
            width=1.2, height=0.5, 
            color=YELLOW, fill_opacity=0.3
        ).move_to(number_line.number_to_point(0.5))
        
        interval_label_1 = Text("[0,1]", font_size=20, color=YELLOW).next_to(interval_1, UP)
        
        self.play(Create(interval_1), Write(interval_label_1))
        self.wait(1)
        
        # Show fractions in first interval
        fractions_1 = []
        fraction_labels_1 = []
        
        fractions_data_1 = [
            (1/2, "1/2"),
            (1/4, "1/3"),
            (1/8, "1/4"),
        ]
        
        for frac_val, frac_text in fractions_data_1:
            point = number_line.number_to_point(frac_val)
            dot = Dot(point, color=YELLOW, radius=0.05)
            label = Text(frac_text, font_size=12, color=YELLOW).next_to(dot, UP, buff=0.1)
            fractions_1.append(dot)
            fraction_labels_1.append(label)
        
        self.play(*[Create(dot) for dot in fractions_1])
        self.play(*[Write(label) for label in fraction_labels_1])
        self.wait(2)
        
        # Fade out first interval
        self.play(
            FadeOut(interval_1), FadeOut(interval_label_1),
            *[FadeOut(dot) for dot in fractions_1],
            *[FadeOut(label) for label in fraction_labels_1]
        )
        
        # Highlight second interval [1,2]
        interval_2 = Rectangle(
            width=1.2, height=0.5,
            color=GREEN, fill_opacity=0.3
        ).move_to(number_line.number_to_point(1.5))
        
        interval_label_2 = Text("[1,2]", font_size=20, color=GREEN).next_to(interval_2, UP)
        
        self.play(Create(interval_2), Write(interval_label_2))
        self.wait(1)
        
        # Show fractions in second interval
        fractions_2 = []
        fraction_labels_2 = []
        
        fractions_data_2 = [
            (3/2, "3/2"),
            (5/4, "5/4"),
            (9/8, "9/8"),
        ]
        
        for frac_val, frac_text in fractions_data_2:
            if 1 <= frac_val <= 2:  # Only show fractions in the interval
                point = number_line.number_to_point(frac_val)
                dot = Dot(point, color=GREEN, radius=0.05)
                label = Text(frac_text, font_size=12, color=GREEN).next_to(dot, UP, buff=0.1)
                fractions_2.append(dot)
                fraction_labels_2.append(label)
        
        self.play(*[Create(dot) for dot in fractions_2])
        self.play(*[Write(label) for label in fraction_labels_2])
        self.wait(2)
        
        # Transition to Cantor's argument
        self.play(FadeOut(VGroup(number_line, interval_2, interval_label_2, *fractions_2, *fraction_labels_2)))
        self.wait(1)
        
        # Part 3: Cantor's bijection argument
        self.show_cantor_bijection()
    
    def show_cantor_bijection(self):
        
        # Create grid of fractions
        grid_origin = LEFT * 4 + UP * 1
        cell_size = 0.8
        
        # Grid dimensions
        rows, cols = 6, 6
        
        # Create the grid structure
        grid_lines = VGroup()
        
        # Horizontal lines
        for i in range(rows + 1):
            line = Line(
                grid_origin + RIGHT * 0 + DOWN * i * cell_size,
                grid_origin + RIGHT * cols * cell_size + DOWN * i * cell_size,
                color=GRAY, stroke_width=1
            )
            grid_lines.add(line)
        
        # Vertical lines  
        for j in range(cols + 1):
            line = Line(
                grid_origin + RIGHT * j * cell_size + DOWN * 0,
                grid_origin + RIGHT * j * cell_size + DOWN * rows * cell_size,
                color=GRAY, stroke_width=1
            )
            grid_lines.add(line)
        
        # Create fraction labels and positions
        fractions = VGroup()
        fraction_positions = {}
        
        for i in range(1, rows + 1):  # numerator (1 to 6)
            for j in range(1, cols + 1):  # denominator (1 to 6)
                pos = grid_origin + RIGHT * (j - 0.5) * cell_size + DOWN * (i - 0.5) * cell_size
                
                # Create fraction text
                if i == j:  # Highlight diagonal (integers)
                    frac_text = Text(f"{i}/{j}", font_size=16, color=YELLOW)
                elif gcd(i, j) == 1:  # Reduced fractions
                    frac_text = Text(f"{i}/{j}", font_size=16, color=WHITE)
                else:  # Non-reduced fractions
                    frac_text = Text(f"{i}/{j}", font_size=16, color=GRAY)
                
                frac_text.move_to(pos)
                fractions.add(frac_text)
                fraction_positions[(i, j)] = (pos, frac_text)
        
        # Row and column headers
        headers = VGroup()
        
        # Column headers (denominators)
        for j in range(1, cols + 1):
            header_pos = grid_origin + RIGHT * (j - 0.5) * cell_size + UP * 0.3
            header = Text(str(j), font_size=14, color=BLUE).move_to(header_pos)
            headers.add(header)
        
        # Row headers (numerators)  
        for i in range(1, rows + 1):
            header_pos = grid_origin + LEFT * 0.3 + DOWN * (i - 0.5) * cell_size
            header = Text(str(i), font_size=14, color=RED).move_to(header_pos)
            headers.add(header)
        
        # Labels for axes
        num_label = Text("Numerator", font_size=16, color=RED).next_to(grid_origin + LEFT * 0.5 + DOWN * 2.5 * cell_size, LEFT)
        den_label = Text("Denominator", font_size=16, color=BLUE).next_to(grid_origin + RIGHT * 2.5 * cell_size + UP * 0.5, UP)
        
        # Draw the grid
        self.play(Create(grid_lines))
        self.play(Write(headers))
        self.play(Write(num_label), Write(den_label))
        self.play(Write(fractions))
        self.wait(2)
        
        # Show the zig-zag path
        self.show_zigzag_path(fraction_positions, grid_origin, cell_size, rows, cols)
        
    def show_zigzag_path(self, fraction_positions, grid_origin, cell_size, rows, cols):
        # Create the zigzag enumeration path
        path_order = []
        
        # Generate diagonal traversal order
        for d in range(2, rows + cols + 1):  # diagonal sum
            diagonal = []
            for i in range(1, min(d, rows + 1)):
                j = d - i
                if 1 <= j <= cols:
                    diagonal.append((i, j))
            
            # Alternate direction for each diagonal
            if d % 2 == 0:
                diagonal.reverse()
            
            path_order.extend(diagonal)
        
        # Limit to first 20 positions for clarity
        path_order = path_order[:20]
        
        # Create path visualization
        path_lines = VGroup()
        enumeration_text = VGroup()
        
        natural_counter = 1
        prev_pos = None
        
        for i, (num, den) in enumerate(path_order):
            pos, frac_text = fraction_positions[(num, den)]
            
            # Only count reduced fractions (skip duplicates)
            #if gcd(num, den) == 1:
            # Highlight the current fraction
            highlight = Circle(radius=0.3, color=YELLOW, fill_opacity=0.3).move_to(pos)
            self.play(Create(highlight), run_time=0.3)
            
            # Add enumeration text
            enum_pos = RIGHT * 3 + UP * (2 - natural_counter * 0.3)
            enum_text = Text(f"{natural_counter} ↔ {num}/{den}", font_size=16).move_to(enum_pos)
            enumeration_text.add(enum_text)
            self.play(Write(enum_text), run_time=0.3)
            
            # Draw path line from previous position
            if prev_pos is not None:
                path_line = Line(prev_pos, pos, color=GREEN, stroke_width=3)
                path_lines.add(path_line)
                self.play(Create(path_line), run_time=0.2)
            
            prev_pos = pos
            natural_counter += 1
            
            self.play(FadeOut(highlight), run_time=0.2)
            #else:
                # Show crossed out non-reduced fractions
                #cross = VGroup(
                #    Line(pos + UP * 0.2 + LEFT * 0.2, pos + DOWN * 0.2 + RIGHT * 0.2, color=RED),
                #    Line(pos + UP * 0.2 + RIGHT * 0.2, pos + DOWN * 0.2 + LEFT * 0.2, color=RED)
                #)
                #self.play(Create(cross), run_time=0.1)
        
        self.wait(2)
        

# Helper function for GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a