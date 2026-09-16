from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np

# We inherit from both VoiceoverScene and ThreeDScene to allow camera movements
class MathematicalSemantics(VoiceoverScene, ThreeDScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # --- Scene 1: The Semantic Circle Returns ---
        with self.voiceover(text="Alternatively, we can think, as most mathematicians do, that these formulas are merely descriptions of certain pre-existing mathematical structures, and what math really is, is the set of all of such structures.") as tracker:
            
            semantics_circle = Circle(radius=3, color=GREEN_C, stroke_width=4)
            semantics_circle.set_fill(GREEN_E, opacity=0.1)
            semantics_label = Text("Semantics", font_size=48, color=GREEN_C).next_to(semantics_circle, UP)
            
            sem_group = VGroup(semantics_circle, semantics_label)
            
            self.play(FadeIn(sem_group), run_time=tracker.duration)

        # --- Scene 2: Wiggling the Boundary ---
        with self.voiceover(text="But what would the set consisting of all mathematical structures look like?") as tracker:
            
            # Create a "fuzzy" dynamic border like we did in part 1
            fuzzy_border = VGroup(*[
                Circle(radius=3, color=GREEN_C, stroke_width=w, stroke_opacity=o)
                for w, o in [(10, 0.4), (20, 0.2), (30, 0.1)]
            ])
            
            self.play(FadeIn(fuzzy_border), run_time=tracker.duration * 0.3)
            
            # Wiggle the perimeter to signify the unbounded nature
            self.play(
                semantics_circle.animate.apply_function(
                    lambda p: p + 0.1 * np.array([np.sin(6*p[1]), np.cos(6*p[0]), 0])
                ),
                fuzzy_border.animate.apply_function(
                    lambda p: p + 0.1 * np.array([np.sin(6*p[1]), np.cos(6*p[0]), 0])
                ),
                run_time=tracker.duration * 0.7
            )

        # --- Scene 3: The Holographic Matrix Grid ---
        with self.voiceover(text="It would have to be something very general and very large, such that we could simulate essentially whatever we want inside of it.") as tracker:
            
            self.play(FadeOut(sem_group), FadeOut(fuzzy_border), run_time=tracker.duration * 0.2)
            
            # Faint background grid
            grid = NumberPlane(
                x_range=[-15, 15, 1], y_range=[-15, 15, 1],
                background_line_style={"stroke_color": GREY, "stroke_width": 1, "stroke_opacity": 0.1},
                faded_line_ratio=1
            )
            self.play(FadeIn(grid), run_time=tracker.duration * 0.2)
            
            # Move camera to 3D perspective
            self.move_camera(phi=65 * DEGREES, theta=-45 * DEGREES, run_time=tracker.duration * 0.2)
            
            # Matrix Green Hologram Torus
            matrix_green = "#00FF41"
            hologram_torus = Torus(
                major_radius=2, minor_radius=0.75, resolution=(24, 24)
            ).set_style(stroke_color=matrix_green, stroke_width=1.5, fill_color=matrix_green, fill_opacity=0.1)
            
            # Projector "Lasers"
            source_point = np.array([-5, -5, -4])
            lasers = VGroup(*[
                Line(source_point, hologram_torus.get_center() + np.array([x, y, z]), color=matrix_green, stroke_opacity=0.4)
                for x, y, z in [(2,0,0), (-2,0,0), (0,2,0), (0,-2,0), (0,0,1), (0,0,-1), (1.5,1.5,0), (-1.5,-1.5,0)]
            ])
            
            self.play(Create(lasers), run_time=tracker.duration * 0.15)
            self.play(FadeIn(hologram_torus), run_time=tracker.duration * 0.15)
            
            # Let it rotate gently as a hologram
            self.play(Rotate(hologram_torus, angle=PI/2, axis=UP), run_time=tracker.duration * 0.1)

        # --- Scene 4: The Basic Set (Cookie Chips) ---
        with self.voiceover(text="This is where set theory comes in. A set is perhaps the most basic object we can consider.") as tracker:
            
            # Return camera to flat 2D
            self.move_camera(phi=0, theta=-90 * DEGREES, run_time=tracker.duration * 0.3)
            self.play(FadeOut(lasers), FadeOut(hologram_torus), FadeOut(grid), run_time=tracker.duration * 0.2)
            
            # Create the set and elements
            main_set = Circle(radius=2.5, color=WHITE, stroke_width=4)
            
            # "Chocolate chips"
            elements = VGroup(
                Circle(radius=0.4, color=BLUE, fill_opacity=0.5).shift(UP*1 + LEFT*0.5),
                Circle(radius=0.6, color=RED, fill_opacity=0.5).shift(DOWN*0.6 + RIGHT*0.8),
                Circle(radius=0.3, color=YELLOW, fill_opacity=0.5).shift(LEFT*1.2 + DOWN*0.8),
                Circle(radius=0.5, color=PURPLE, fill_opacity=0.5).shift(UP*0.8 + RIGHT*1.0),
                Dot(color=WHITE).shift(LEFT*0.2 + DOWN*0.1) # A generic point element
            )
            
            self.play(Create(main_set), run_time=tracker.duration * 0.2)
            self.play(FadeIn(elements, scale=0.5, lag_ratio=0.1), run_time=tracker.duration * 0.3)

        with self.voiceover(text="I challenge you to try to define a set without using a synonym of set, like collection, group, class etc.") as tracker:
            # Gently pulse the set to emphasize the conceptual difficulty
            self.play(Indicate(main_set, color=WHITE, scale_factor=1.05), run_time=tracker.duration)

        with self.voiceover(text="The axioms of ZFC are a solid attempt to define what a set is.") as tracker:
            # Shift the set to the left to make room for text
            self.play(
                VGroup(main_set, elements).animate.scale(0.8).shift(LEFT * 3),
                run_time=tracker.duration * 0.4
            )
            zfc_text = Text("ZFC Axioms", font_size=48, color=YELLOW).shift(RIGHT * 3)
            self.play(Write(zfc_text), run_time=tracker.duration * 0.6)

        # --- Scene 5: Cantor and the Ordinal Spiral ---
        with self.voiceover(text="The origins of set theory date back to Georg Cantor in the later 19th century.") as tracker:
            self.play(FadeOut(main_set), FadeOut(elements), FadeOut(zfc_text), run_time=tracker.duration * 0.2)
            
            # Load Cantor Image
            cantor_img = ImageMobject("image_082cbc.png").scale(1.2)
            self.play(FadeIn(cantor_img, shift=UP), run_time=tracker.duration * 0.8)

        with self.voiceover(text="Cantor was a mathematical platonist who envisioned an unrestricted and powerful mathematics.") as tracker:
            
            # Shift Cantor to the left and shrink
            self.play(cantor_img.animate.scale(0.6).to_edge(LEFT, buff=1), run_time=tracker.duration * 0.3)
            
            # Load Ordinal Spiral Image
            spiral_img = ImageMobject("image_08301a.png").scale(1.2).to_edge(RIGHT, buff=1)
            self.play(FadeIn(spiral_img, shift=LEFT), run_time=tracker.duration * 0.7)
            
        self.wait(2)