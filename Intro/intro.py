from manim import *
import random

class AncientGreeceInfinity(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # PART 1: THE TIMELINE INTRO
        # ---------------------------------------------------------
        
        # 1. Define the Timeline
        # Range from -600 BC to 2000 AD
        timeline = NumberLine(
            x_range=[-600, 2050, 200],
            length=12,
            include_numbers=True,
            font_size=20,
            label_direction=DOWN
        )
        timeline_label = Text("Timeline of Infinity", font_size=36, color=BLUE)
        timeline_label.to_edge(UP)

        # 2. Define the Figures (Name, Year, Filename)
        # Note: I've mapped the uploaded filenames to the figures based on the images.
        figures_data = [
            ("Pythagoras", -500, "image_894d17.jpg"),
            ("Zeno", -450, "image_894cfb.png"),
            ("Galileo", 1600, "image_894fe1.jpg"),
            ("Cantor", 1880, "image_894fc1.jpg"),
            ("Gödel", 1940, "image_894d1c.jpg"),
        ]

        figures_group = VGroup()
        
        # 3. Create Mobjects for each figure
        for i, (name, year, filename) in enumerate(figures_data):
            # Load Image
            img = ImageMobject(filename)
            img.set_height(2) 
            
            # Create a label
            label = Text(name, font_size=20, color=YELLOW)
            label.next_to(img, UP, buff=0.1)
            
            # Group image and label
            figure = Group(img, label)
            
            # Position on timeline
            timeline_point = timeline.n2p(year)
            
            # Stagger logic: 
            # Modern figures (Galileo, Cantor, Godel) are close on this scale.
            # We alternate their heights so they don't overlap.
            # Pythagoras/Zeno (indices 0, 1) -> Low
            # Galileo (2) -> High, Cantor (3) -> Low, Godel (4) -> High
            if i >= 2: # Modern era
                offset = UP * 2.5 if i % 2 == 0 else UP * 1.0
            else: # Ancient era
                offset = UP * 1.5 if i % 2 == 0 else UP * 3.0

            figure.move_to(timeline_point + offset)
            
            # Add a line connecting the image to the timeline date
            line = Line(figure.get_bottom(), timeline_point, color=WHITE, stroke_opacity=0.5)
            
            figures_group.add(VGroup(line, figure))

        # 4. Animate the Intro
        self.play(Create(timeline), Write(timeline_label))
        self.play(FadeIn(figures_group, shift=UP, lag_ratio=0.5))
        self.wait(3)
        
        # Clean up intro
        self.play(
            FadeOut(figures_group), 
            FadeOut(timeline), 
            FadeOut(timeline_label)
        )

        # ---------------------------------------------------------
        # PART 2: THE INFINITE NUMBER LINE
        # ---------------------------------------------------------

        # Create full number line from 0-1200
        full_number_line = NumberLine(
            x_range=[0, 1200, 1],
            length=120, 
            color=WHITE,
            include_numbers=False,
            label_direction=DOWN,
            font_size=24
        )
        
        # Create custom labels for every 10th number to improve performance/look
        all_numbers = VGroup()
        for i in range(0, 1201, 10): 
            number_label = MathTex(str(i), font_size=24)
            number_label.next_to(full_number_line.n2p(i), DOWN, buff=0.2)
            all_numbers.add(number_label)
        
        # Group them for easier animation
        line_group = VGroup(full_number_line, all_numbers)

        # Position 0 at the left side of the screen
        initial_offset = -full_number_line.n2p(0)[0] - 6 # Shift so 0 is at x=-6 (left edge)
        line_group.shift(RIGHT * initial_offset)
        
        self.play(Create(full_number_line), Write(all_numbers))
        
        # --- THE FADE-WHILE-MOVING TRICK ---
        
        # We want to pan far to the right
        pan_distance = 100 # How many units to move left
        
        # Define a custom rate function for the fade.
        # This function returns 0 (invisible fade) until t=0.8, 
        # then ramps to 1 (full fade) at the end.
        def delayed_fade(t):
            return 0 if t < 0.8 else (t - 0.8) * 5

        self.play(
            # Animation 1: The Movement (Accelerating)
            line_group.animate(run_time=8, rate_func=lambda t: t**2).shift(LEFT * pan_distance),
            
            # Animation 2: The Fade (Happens only at the very end of the movement)
            FadeOut(line_group, run_time=8, rate_func=delayed_fade)
        )
        
        self.wait(1)

        # ---------------------------------------------------------
        # PART 3: DEFINITIONS
        # ---------------------------------------------------------

        # Show the potential infinity formula in green
        potential_infinity = MathTex(
            r"\forall x \,\exists y \,: x < y",
            color=GREEN,
            font_size=48
        )
        potential_infinity.shift(UP * 1.5)
        
        potential_explanation = Text(
            "For all x, there exists a y such that x is less than y",
            font_size=24,
            color=GREEN
        )
        potential_explanation.next_to(potential_infinity, DOWN, buff=0.3)
        
        title_potential_infinity = Text(
            "Potential Infinity",
            font_size=40,
            color=GREEN)
        title_potential_infinity.next_to(potential_infinity, UP, buff=0.5)
        
        self.play(Write(potential_infinity))
        self.wait(0.5)
        self.play(Write(potential_explanation))
        self.play(Write(title_potential_infinity))
        self.wait(2)
        
        # Show the actual infinity formula in red
        actual_infinity = MathTex(
            r"\exists y \,\forall x \,: x < y",
            color=RED,
            font_size=48
        )
        actual_infinity.move_to(DOWN * 1.5)
        
        actual_explanation = Text(
            "There exists a y such that for all x, x is less than y",
            font_size=24,
            color=RED
        )
        actual_explanation.next_to(actual_infinity, DOWN, buff=0.3)
        
        actual_title = Text(
            "Actual Infinity",
            font_size = 40,
            color = RED
        )
        actual_title.next_to(actual_infinity,UP, buff=0.5)
        
        self.play(Write(actual_infinity))
        self.wait(0.5)
        self.play(Write(actual_explanation))
        self.play(Write(actual_title))
        self.wait(2)
        
        # Separator line
        separator = Line(LEFT * 6, RIGHT * 6, color=WHITE)
        separator.move_to(ORIGIN)
        self.play(Create(separator))
        self.wait(1)
                
        # Final cleanup
        self.play(
            FadeOut(potential_infinity),
            FadeOut(potential_explanation),
            FadeOut(title_potential_infinity),
            FadeOut(actual_infinity),
            FadeOut(actual_explanation),
            FadeOut(actual_title),
            FadeOut(separator),
        )