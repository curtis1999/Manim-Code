from manim import *
import numpy as np

class ZenosParadox(Scene):
    def construct(self):
        # Title
        title = Text("The Dichotomy", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # Create number line
        number_line = NumberLine(
            x_range=[0, 1, 1],
            length=10,
            color=WHITE,
            #include_numbers=True,
            label_direction=DOWN,
            font_size=24
        )
        number_line.shift(DOWN * 0.5)
        
        self.play(Create(number_line))
        self.wait(0.5)
        
        # Starting point and target
        start_point = Dot(number_line.number_to_point(0), color=GREEN, radius=0.1)
        target_point = Dot(number_line.number_to_point(1), color=RED, radius=0.1)
        
        start_label = Text("Start", font_size=24, color=GREEN).next_to(start_point, UP)
        target_label = Text("Finish Line", font_size=24, color=RED).next_to(target_point, UP)
        
        self.play(
            Create(start_point),
            Create(target_point),
            Write(start_label),
            Write(target_label)
        )
        self.wait()
        
        # Initialize variables for the animation
        current_pos = 0
        target_pos = 1
        colors = [YELLOW, ORANGE, PINK, PURPLE, BLUE, TEAL, MAROON]
        
        # Store all segments and dots for later reference
        segments = []
        dots = []
        
        # Group to hold all fraction terms for uniform positioning
        fraction_group = VGroup()
        
        # Pre-calculate the final position for the fraction group
        # We'll create temporary fractions to measure the final width
        temp_fractions = []
        for j in range(5):
            if j == 0:
                temp_frac = MathTex(f"\\frac{{1}}{{{2**(j+1)}}}", font_size=48)
            else:
                temp_frac = MathTex(f"+ \\frac{{1}}{{{2**(j+1)}}}", font_size=48)
            temp_fractions.append(temp_frac)
        
        temp_group = VGroup(*temp_fractions)
        temp_group.arrange(RIGHT, buff=0.3)
        temp_group.move_to(UP * 2)
        final_position = temp_group.get_center()
        
        # Animate the first 7 steps of the paradox
        for i in range(7):
            # Calculate the midpoint
            midpoint = (current_pos + target_pos) / 2
            
            # Create the segment from current position to midpoint
            segment_start = number_line.number_to_point(current_pos)
            segment_end = number_line.number_to_point(midpoint)
            
            segment = Line(
                segment_start, 
                segment_end, 
                color=colors[i % len(colors)],
                stroke_width=8
            )
            
            # Create a dot at the midpoint
            midpoint_dot = Dot(
                number_line.number_to_point(midpoint),
                color=colors[i % len(colors)],
                radius=0.05
            )
            
            # Animate the segment and dot
            self.play(
                Create(segment),
                Create(midpoint_dot),
                run_time=0.8
            )
            self.wait(1/(i+1))
            
            # Create the fraction term
            if i == 0:
                current_frac = MathTex(
                    f"\\frac{{1}}{{{2**(i+1)}}}",
                    font_size=48,
                    color=colors[i % len(colors)]
                )
            else:
                current_frac = MathTex(
                    f"+ \\frac{{1}}{{{2**(i+1)}}}",
                    font_size=48,
                    color=colors[i % len(colors)]
                )
            
            # Add to the group and arrange uniformly at final position
            fraction_group.add(current_frac)
            fraction_group.arrange(RIGHT, buff=0.3)
            fraction_group.move_to(final_position)
            
            # Animate only the new fraction appearing
            self.play(
                Write(current_frac),
                run_time=0.6               
            )
            
            segments.append(segment)
            dots.append(midpoint_dot)
            
            # Update for next iteration
            current_pos = midpoint
            self.wait(0.5)

        self.clear()

        series_expr = MathTex(
            r"\sum_{i=1}^{\infty} \frac{1}{2^i}",
            font_size=48,
            color=YELLOW
        )
        series_expr.shift(LEFT*5)
        series_nums = Text(
            "= 1/2 + 1/4 + 1/8 + 1/16 + 1/32 + ... = 1",
            font_size=46,
            color = YELLOW
        ).next_to(series_expr)
        self.play(
            Write(series_expr)
        )
        self.wait()
        self.play(
            Write(series_nums),
            run_time=5
        )
        self.wait(3)
        