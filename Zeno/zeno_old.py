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
            x_range=[0, 1, 0.1],
            length=10,
            color=WHITE,
            include_numbers=True,
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
        
        # Initialize an empty list to store fraction terms
        fraction_terms = []

        # Animate the first 3 steps of the paradox
        for i in range(5):
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
            
            # Animate the segment first
            self.play(
                Create(segment),
                run_time=1.5
            )
            
            # Then show/update the fraction sum
            if i == 0:
                # Add the new fraction term to our list
                current_frac = MathTex(
                f"\\frac{{1}}{{{2**(i+1)}}}",
                font_size=48,
                color = colors[i % len(colors)]
                )
                current_frac.shift(UP, RIGHT*(i-2))
                # First iteration: write the fraction
                self.play(
                    Write(current_frac),
                    run_time=0.8
                )
            else:
                # Add the new fraction term to our list
                current_frac = MathTex(
                f"+ \ \\frac{{1}}{{{2**(i+1)}}}",
                font_size=48,
                color = colors[i % len(colors)]
                )
                current_frac.shift(UP, RIGHT*(i-2))
                # Subsequent iterations: transform from previous to new
                self.play(
                    Write(current_frac),
                    run_time=0.8
                )
            
            # Create a dot at the midpoint
            midpoint_dot = Dot(
                number_line.number_to_point(midpoint),
                color=colors[i % len(colors)],
                radius=0.05
            )
            self.play(Create(midpoint_dot), run_time=0.5)
            
            segments.append(segment)
            dots.append(midpoint_dot)
            
            # Update for next iteration
            current_pos = midpoint
            self.wait(0.5)
        
        # Store current position for zoom calculations
        zoom_start_pos = current_pos
        
        # Create a rectangle to highlight the zoom region
        zoom_region_start = number_line.number_to_point(0.95)
        zoom_region_end = number_line.number_to_point(1.0)
        zoom_highlight = Rectangle(
            width=abs(zoom_region_end[0] - zoom_region_start[0]),
            height=0.25,
            color=YELLOW,
            stroke_width=3,
            fill_opacity=0.1
        )
        zoom_highlight.move_to((zoom_region_start + zoom_region_end) / 2)
        
        self.play(Create(zoom_highlight))
        
        # Zoom in by scaling the camera
        # Calculate zoom factor to make the 0.85-1.0 section fill the screen
        zoom_factor = 6.67  # This will make the 0.15 unit section fill the original line length
        zoom_center = number_line.number_to_point(0.985)  # Center of the 0.85-1.0 section
        
        # Group all existing objects for zooming
        everything = Group(
            number_line, start_point, target_point, start_label, target_label,
            zoom_highlight, *segments, *dots
        )
        everything.shift(DOWN)
        
        # Calculate the translation needed to center the zoom region
        current_center = zoom_center
        target_center = np.array([0, -0.5, 0])  # Center horizontally, but keep at number line's y-position
        translation = target_center - current_center * zoom_factor
        
        # Animate the zoom and translation
        self.play(
            everything.animate.scale(zoom_factor).shift(translation),
            run_time=1
        )
        self.wait(0.25)
        
        # Remove the highlight rectangle after zoom
        self.play(FadeOut(zoom_highlight))
        
        # Continue the paradox in the zoomed view for 2 more steps
        current_zoom_pos = zoom_start_pos
        target_zoom_pos = 1.0
        
        for i in range(3):
            # Calculate the midpoint in the zoomed section
            midpoint = (current_zoom_pos + target_zoom_pos) / 2
            
            # Create the segment from current position to midpoint
            segment_start = number_line.number_to_point(current_zoom_pos)
            segment_end = number_line.number_to_point(midpoint)
            
            segment = Line(
                segment_start, 
                segment_end, 
                color=colors[(i + 3) % len(colors)],
                stroke_width=8
            )
            
            # Animate the segment
            self.play(
                Create(segment),
                run_time=0.75
            )
            
            # Create a dot at the midpoint
            midpoint_dot = Dot(
                number_line.number_to_point(midpoint),
                color=colors[(i + 3) % len(colors)],
                radius=0.05
            )
            self.play(Create(midpoint_dot), run_time=0.4)
            
            segments.append(segment)
            dots.append(midpoint_dot)
            
            # Update for next iteration
            current_zoom_pos = midpoint
            
            self.wait(0.4)
        
        self.wait(1)
        
        # Fade out everything for a clean ending
        all_objects = [
            title, number_line, start_point, target_point,
            start_label, target_label
        ] + segments + dots
        
        self.play(*[FadeOut(obj) for obj in all_objects])