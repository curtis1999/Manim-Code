from manim import *
import numpy as np

class SqrtTwoProof(Scene):
    def construct(self):
        # Title
        title = Text("Proof: √2 is Irrational", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # Create the triangle on the left side
        self.create_triangle()
        
        # Show the proof steps on the right side
        self.show_proof_steps()

    def create_triangle(self):
        # Position triangle on the left side
        triangle_center = LEFT * 3
        
        # Create unit right triangle
        triangle_points = [
            triangle_center + DOWN + LEFT,
            triangle_center + DOWN + RIGHT,
            triangle_center + UP + RIGHT
        ]
        triangle = Polygon(*triangle_points, color=BLUE, fill_opacity=0.3)
        
        # Add labels for sides
        base_label = MathTex("1").next_to(triangle_center + DOWN, DOWN)
        height_label = MathTex("1").next_to(triangle_center + RIGHT, RIGHT)
        hypotenuse_label = MathTex(r"\sqrt{2}").next_to(triangle_center + 0.1*UP + 0.1*LEFT, UP + LEFT)
        
        # Add right angle marker
        corner = triangle_center + DOWN + RIGHT
        right_angle = RightAngle(
            Line(corner, triangle_center + DOWN + LEFT), 
            Line(corner, triangle_center + UP + RIGHT), 
            length=0.4
        )
        
        self.play(Create(triangle))
        self.play(Write(base_label), Write(height_label))
        self.play(Create(right_angle))
        self.play(Write(hypotenuse_label))
        self.wait(1)

    def show_proof_steps(self):
        # Position proof on the right side
        proof_start = RIGHT * 1.5 + UP * 3.5
        
        # Step 1 title
        step1_title = MathTex(r"\text{1: Suppose } \sqrt{2} = \frac{a}{b}, \quad \gcd(a,b) = 1, a,b \in {\mathbb{N}}", font_size=40, color=BLUE)
        step1_title.next_to(proof_start, DOWN, buff=0.3)
        self.play(Write(step1_title))
        self.wait(0.5)
        
        # Step 1: Start with assumption
        equation_pos = step1_title.get_center() + DOWN * 0.8
        
        eq1 = MathTex(r"\sqrt{2} = \frac{a}{b}")
        eq1.move_to(equation_pos)
        self.play(Write(eq1))
        self.wait(1)
        
        # Transform to squared version
        eq2 = MathTex(r"(\sqrt{2})^2 = \left(\frac{a}{b}\right)^2")
        eq2.move_to(equation_pos)
        self.play(Transform(eq1, eq2))
        self.wait(1)
        
        # Transform to simplified
        eq3 = MathTex(r"2 = \frac{a^2}{b^2}")
        eq3.move_to(equation_pos)
        self.play(Transform(eq1, eq3))
        self.wait(1)
        
        # Transform to final form
        eq4 = MathTex(r"2b^2 = a^2")
        eq4.move_to(equation_pos)
        self.play(Transform(eq1, eq4))
        self.wait(1)
        
        # Conclude a is even
        conclusion1 = MathTex(r"\therefore a \text{ is even}")
        conclusion1.next_to(eq1, DOWN, buff=0.5)
        self.play(Write(conclusion1))
        self.wait(1)
        
        conclusion12 = MathTex(r"\implies a = 2k, k \in {\mathbb{N}}")
        conclusion12.next_to(conclusion1, RIGHT, buff=0.2)
        self.play(Write(conclusion12))
        self.wait(1)
        
        # Step 2: Start with a = 2k
        equation2_pos = conclusion1.get_center() + DOWN * 0.8
        
        eq5 = MathTex(r"\sqrt{2} = \frac{2k}{b}")
        eq5.move_to(equation2_pos)
        self.play(Write(eq5))
        self.wait(1)
        
        # Transform to substitution
        eq6 = MathTex(r"2 = \frac{(2k)^2}{b^2}")
        eq6.move_to(equation2_pos)
        self.play(Transform(eq5, eq6))
        self.wait(1)
        
        # Transform to substitution
        eq7 = MathTex(r"2 = \frac{4k^2}{b^2}")
        eq7.move_to(equation2_pos)
        self.play(Transform(eq5, eq7))
        self.wait(1)
        
         # Transform to substitution
        eq8 = MathTex(r"2b^2 = 4k^2")
        eq8.move_to(equation2_pos)
        self.play(Transform(eq5, eq8))
        self.wait(1)
        
        # Transform to simplified
        eq9 = MathTex(r"b^2 = 2k^2")
        eq9.move_to(equation2_pos)
        self.play(Transform(eq5, eq9))
        self.wait(1)
        
        # Conclude b is even
        conclusion2 = MathTex(r"\therefore b \text{ is even}")
        conclusion2.next_to(eq5, DOWN, buff=0.5)
        self.play(Write(conclusion2))
        self.wait(1)
       
        
        # Final contradiction
        contradiction = MathTex(r"\text{Both } a \text{ and } b \text{ are even}")
        contradiction.next_to(conclusion2, DOWN, buff=0.5)
        self.play(Write(contradiction))
        self.wait(1)
        
        # No maximally reduced form
        no_reduced = MathTex(r"\text{No maximally reduced fractional representation}")
        no_reduced.next_to(contradiction, DOWN, buff=0.3)
        no_reduced.scale(0.8)
        self.play(Write(no_reduced))
        self.wait(1)
        
        # Final conclusion
        final_conclusion = Text("√2 is irrational", font_size=36, color=GREEN)
        final_conclusion.next_to(no_reduced, DOWN, buff=0.8)
        self.play(Write(final_conclusion))
        
        # Add QED symbol
        qed = MathTex(r"\square", font_size=36)
        qed.next_to(final_conclusion, RIGHT, buff=0.5)
        self.play(Write(qed))
        
        self.wait(3)