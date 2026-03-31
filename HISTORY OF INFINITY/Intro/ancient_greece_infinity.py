from manim import *
import random

class AncientGreeceInfinity(Scene):
    def construct(self):
        # Title screen
        Pythagoras = ImageMobject("Pythagoras.png")
        Pythagoras.set_height(5)
        Pythagoras.set_width(3)
        Pythagoras.shift(UP*2 + LEFT *6)
        Zeno = ImageMobject("Zeno.png")
        Zeno.set_height(5)
        Zeno.set_width(3)
        Zeno.shift(UP*2 + LEFT *3) 
        Galileo = ImageMobject("Galileo.png")
        Galileo.set_height(7)
        Galileo.set_width(3)
        Galileo.shift(UP*2)
        Godel = ImageMobject("KurtGodel.webp")
        Godel.set_height(4)
        Godel.set_width(3)
        Godel.shift(UP*2 + RIGHT*6)
        Cantor = ImageMobject("Georg_Cantor.jpg")
        Cantor.set_height(5)
        Cantor.set_width(3)
        Cantor.shift(UP*2 + RIGHT *3)
        self.play(FadeIn(Pythagoras),FadeIn(Cantor), FadeIn(Zeno), FadeIn(Godel), FadeIn(Galileo))
        title = Text("History of Infinity", font_size=64, color=BLUE)
        self.play(Write(title))
        self.wait(5)
        self.play(FadeOut(title), FadeOut(Pythagoras),FadeOut(Cantor), FadeOut(Zeno), FadeOut(Godel), FadeOut(Galileo))
        
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
        
        # Position the number line so that 0 is visible at the left side of the screen
        # Move the number line so that 0 is positioned at the left edge
        initial_offset = -full_number_line.n2p(75)[0]  # Show 0 at left side with some margin
        full_number_line.shift(RIGHT * initial_offset)
        all_numbers.shift(RIGHT * initial_offset)
        
        # Create the number line and immediately start panning
        # Single continuous pan animation with accelerating movement
        target_position = 900  # Where we're panning towards
        pan_distance = full_number_line.n2p(target_position)[0] - full_number_line.n2p(0)[0]
        
        # Create and show the number line, then immediately start panning
        self.play(Create(full_number_line), Write(all_numbers))
        
        # Continuous pan with quadratic acceleration and fade out at the end
        self.play(
            AnimationGroup(
                full_number_line.animate.shift(LEFT * pan_distance),
                all_numbers.animate.shift(LEFT * pan_distance),
            ),
            run_time=7,
            rate_func=lambda t: t**2  # Quadratic acceleration - starts slow, gets faster
        )
        
        # Final fade out as we approach "infinity"
        self.play(
            FadeOut(full_number_line, run_time=2),
            FadeOut(all_numbers, run_time=2),
            run_time=2,
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
        Aristotle_quote = Text( "There is no smallest among \n the small and no largest among the large; but always something still smaller and something still larger.")
        self.play(Write(Aristotle_quote))