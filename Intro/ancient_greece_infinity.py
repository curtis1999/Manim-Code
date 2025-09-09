from manim import *
import random

class AncientGreeceInfinity(Scene):
    def construct(self):
        # Title screen
        title = Text("History of Infinity", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # Create full number line from 0-1200 with every 10th number labeled
        full_number_line = NumberLine(
            x_range=[0, 1200, 1],
            length=120,  # Total length for the full range (0.1 units per number)
            color=WHITE,
            include_numbers=False,  # We'll add custom numbers
            label_direction=DOWN,
            font_size=24
        )
        
        # Create ALL number labels for every 10th number (0, 10, 20, ..., 1200)
        all_numbers = VGroup()
        for i in range(0, 1201, 10):  # Every 10th number
            number_label = MathTex(str(i), font_size=24)
            number_label.next_to(full_number_line.n2p(i), DOWN, buff=0.2)
            all_numbers.add(number_label)
        
        # Position the number line centered on 50 (so we see 0-100 initially)
        # Move the number line left so that 50 is at the center of the screen
        initial_offset = -full_number_line.n2p(75)[0]
        full_number_line.shift(RIGHT * initial_offset)
        all_numbers.shift(RIGHT * initial_offset)
        
        # Create the complete number line with all labels
        self.play(Create(full_number_line), Write(all_numbers))
        self.wait(1)
        
        # Single accelerating pan to the right with fade out
        # We'll pan towards 900 but fade out around 700-800 to create the infinite illusion
        target_position = 900  # Where we're panning towards
        fade_start_position = 600  # When to start fading (at around 600 on the number line)
        
        pan_distance = full_number_line.n2p(target_position)[0] - full_number_line.n2p(50)[0]
        
        # Calculate when to start fading (as a fraction of the total animation)
        fade_start_fraction = (fade_start_position - 50) / (target_position - 50)
        
        # Create the pan animation with accelerating movement
        pan_animation = AnimationGroup(
            full_number_line.animate.shift(LEFT * pan_distance),
            all_numbers.animate.shift(LEFT * pan_distance),
        )
        
        # Create fade out animation that starts partway through
        fade_animation = AnimationGroup(
            FadeOut(full_number_line),
            FadeOut(all_numbers),
        )
        
        # Play the pan with quadratic acceleration
        self.play(
            pan_animation,
            run_time=8,
            rate_func=lambda t: t**2  # Quadratic acceleration
        )
        
        # Start fade out during the last portion of the pan
        # We'll use a separate fade animation that starts when we're around 700
        self.play(
            full_number_line.animate.shift(LEFT * pan_distance * 0.3),  # Continue panning a bit more
            all_numbers.animate.shift(LEFT * pan_distance * 0.3),
            FadeOut(full_number_line, run_time=3),
            FadeOut(all_numbers, run_time=3),
            run_time=3,
        )
        
        self.wait(1)
        
        # Show the potential infinity formula in green
        potential_infinity = MathTex(
            r"\forall x \,\exists y \,: x < y",
            color=GREEN,
            font_size=48
        )
        potential_infinity.shift(UP * 1.5)
        
        # Add explanation for potential infinity
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
        self.wait(1)
        self.play(Write(potential_explanation))
        self.wait(1)
        self.play(Write(title_potential_infinity))
        self.wait(2)
        
        # Show the actual infinity formula in red (below the green one)
        actual_infinity = MathTex(
            r"\exists y \,\forall x \,: x < y",
            color=RED,
            font_size=48
        )
        actual_infinity.move_to(DOWN * 1.5)
        
        # Add explanation for actual infinity
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
        self.wait(1)
        self.play(Write(actual_explanation))
        self.wait(1)
        self.play(Write(actual_title))
        self.wait(2)
        
        # Add a line to separate the concepts
        separator = Line(LEFT * 6, RIGHT * 6, color=WHITE)
        separator.move_to(ORIGIN)
        
        self.play(Create(separator))
        self.wait(1)
                
        # Fade out everything
        self.play(
            FadeOut(potential_infinity),
            FadeOut(potential_explanation),
            FadeOut(title_potential_infinity),
            FadeOut(actual_infinity),
            FadeOut(actual_explanation),
            FadeOut(actual_title),
            FadeOut(separator),
        )
        self.wait(1)