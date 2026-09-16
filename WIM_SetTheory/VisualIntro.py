from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class PhilosophyOfMath(VoiceoverScene):
    def construct(self):
        # Initialize the text-to-speech service
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # --- Scene 1: The Initial Set ---
        with self.voiceover(text="Obviously the question of what math actually is, has been debated for much of history.") as tracker:
            math_circle = Circle(radius=2.5, color=WHITE, stroke_width=4)
            math_text = Text("MATH", font_size=72)
            math_group = VGroup(math_circle, math_text)
            
            self.play(
                Create(math_circle), 
                Write(math_text), 
                run_time=tracker.duration
            )

        # --- Scene 2: Gödel and the Fuzzy Border ---
        with self.voiceover(text="And due to Godel's incompleteness theorems, there is no objective answer.") as tracker:
            # Create a "fuzzy" border effect by stacking multiple thick, transparent circles
            fuzzy_border = VGroup(*[
                Circle(radius=2.5, color=WHITE, stroke_width=w, stroke_opacity=o)
                for w, o in [(10, 0.4), (20, 0.2), (30, 0.1)]
            ])
            
            self.play(
                FadeIn(fuzzy_border),
                # Apply a subtle wiggle to the core circle
                math_circle.animate.apply_function(
                    lambda p: p + 0.05 * np.array([np.sin(5*p[1]), np.cos(5*p[0]), 0])
                ),
                run_time=tracker.duration
            )
            math_group.add(fuzzy_border)

        # --- Scene 3: Zooming in on the Boundary ---
        with self.voiceover(text="If we visualize the totality of math as a set, then its border cannot be clearly defined.") as tracker:
            # Zoom in by scaling the group and shifting it right (so the left edge centers)
            self.play(
                math_group.animate.scale(4).shift(RIGHT * 10),
                run_time=tracker.duration
            )

        # --- Scene 4: The Duality Split ---
        with self.voiceover(text="Note that we can either choose to visualize the totality of math syntactically or semantically.") as tracker:
            # Zoom back out to original position
            self.play(
                math_group.animate.scale(0.25).shift(LEFT * 10),
                run_time=tracker.duration / 3
            )
            
            # Prepare the split
            syntax_circle = Circle(radius=2.5, color=BLUE, stroke_width=4)
            semantics_circle = Circle(radius=2.5, color=GREEN, stroke_width=4)
            
            syntax_label = Text("Syntax", font_size=48, color=BLUE).next_to(syntax_circle, UP)
            semantics_label = Text("Semantics", font_size=48, color=GREEN).next_to(semantics_circle, UP)

            self.play(
                FadeOut(math_group),
                FadeIn(syntax_circle),
                FadeIn(semantics_circle),
                syntax_circle.animate.shift(LEFT * 3.5),
                semantics_circle.animate.shift(RIGHT * 3.5),
                run_time=tracker.duration / 3
            )
            self.play(
                Write(syntax_label),
                Write(semantics_label),
                run_time=tracker.duration / 3
            )

        # --- Scene 5: Syntax (Formulas) ---
        with self.voiceover(text="Syntactically this would be the set of all true mathematical formulas written in first order logic,") as tracker:
            # Generate random formulas
            f1 = MathTex("1+1=2").scale(0.8).move_to(syntax_circle.get_center() + UP * 0.8)
            f2 = MathTex("e^{i\pi}+1=0").scale(0.7).move_to(syntax_circle.get_center() + DOWN * 0.5 + LEFT * 0.8)
            f3 = MathTex("P \implies Q").scale(0.7).move_to(syntax_circle.get_center() + DOWN * 0.3 + RIGHT * 0.8)
            f4 = MathTex("x = \\frac{-b \pm \sqrt{b^2-4ac}}{2a}").scale(0.5).move_to(syntax_circle.get_center() + DOWN * 1.2)
            
            formulas = VGroup(f1, f2, f3, f4)
            
            self.play(
                syntax_circle.animate.set_fill(BLUE, opacity=0.1),
                FadeIn(formulas, shift=UP*0.5),
                run_time=tracker.duration
            )

        # --- Scene 6: Semantics (Structures) ---
        with self.voiceover(text="and semantically would be the totality of mathematical structures. Where mathematical structures can be seen as pre-existing eternal objects in a platonic world of forms.") as tracker:
            # Create representations of platonic solids/structures
            # A 2D projection of a sphere
            sphere = Circle(radius=0.8, color=GREEN_C, fill_opacity=0.3).move_to(semantics_circle.get_center() + LEFT * 1 + UP * 0.2)
            sphere_curve1 = ArcBetweenPoints(sphere.get_top(), sphere.get_bottom(), angle=-PI/2, color=GREEN_E)
            sphere_curve2 = ArcBetweenPoints(sphere.get_left(), sphere.get_right(), angle=-PI/2, color=GREEN_E)
            sphere_group = VGroup(sphere, sphere_curve1, sphere_curve2)

            # A pentagon to represent the dodecahedron
            dodecahedron_proxy = RegularPolygon(n=5, radius=0.8, color=TEAL, fill_opacity=0.3).move_to(semantics_circle.get_center() + RIGHT * 1 + DOWN * 0.3)
            # Add some internal lines to give a 3D wireframe illusion
            lines = VGroup(*[
                Line(dodecahedron_proxy.get_vertices()[i], dodecahedron_proxy.get_center(), stroke_width=1, color=TEAL_E)
                for i in range(5)
            ])
            dod_group = VGroup(dodecahedron_proxy, lines)

            structures = VGroup(sphere_group, dod_group)

            self.play(
                semantics_circle.animate.set_fill(GREEN, opacity=0.1),
                FadeIn(structures, shift=UP*0.5),
                run_time=tracker.duration / 2
            )
            
            # Slowly rotate the structures to mimic eternal objects in the background
            self.play(
                Rotate(sphere_group, angle=PI/4, about_point=sphere.get_center()),
                Rotate(dod_group, angle=-PI/4, about_point=dodecahedron_proxy.get_center()),
                run_time=tracker.duration / 2,
                rate_func=linear
            )

        self.wait(2)