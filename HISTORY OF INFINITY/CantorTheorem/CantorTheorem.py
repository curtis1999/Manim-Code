from manim import *
import numpy as np

class CantorTheorem(Scene):
    def construct(self):
        
        # Part 1: Show initial set with 3 elements
        # Create initial set A = {a, b, c}
        set_a_label = Text("A = {a, b, c}", font_size=36)
        set_a_label.to_edge(LEFT).shift(UP*1.5)
        
        # Visual representation of the set
        set_a_circle = Circle(radius=1.2, color=BLUE)
        set_a_circle.move_to(LEFT*5)
        
        element_a = Text("a", font_size=24)
        element_b = Text("b", font_size=24)
        element_c = Text("c", font_size=24)
        
        element_a.move_to(LEFT*5 + UP*0.5)
        element_b.move_to(LEFT*5 + DOWN*0.5 + LEFT*0.3)
        element_c.move_to(LEFT*5 + DOWN*0.5 + RIGHT*0.3)
        
        self.set_a_group = VGroup(set_a_circle, element_a, element_b, element_c)
        
        self.play(Write(set_a_label))
        self.play(Create(set_a_circle))
        self.play(Write(element_a), Write(element_b), Write(element_c))
        
        self.set_a_label = set_a_label
        self.wait(2)
        
        
        # Part 2: Show power set as Boolean algebra
        
        
        # Create power set P(A) in Boolean algebra structure
        power_set_label = Text("P(A) (Power Set of A)", font_size=32)
        power_set_label.next_to(set_a_label, RIGHT, buff=1.2)
    
        
        # Boolean algebra arrangement (diamond shape)
        # Level 0 (bottom): empty set
        empty_set = Text("∅", font_size=20)
        empty_set.move_to(LEFT*1 + DOWN*2)
        
        # Level 1: singletons
        single_a = Text("{a}", font_size=18)
        single_b = Text("{b}", font_size=18)
        single_c = Text("{c}", font_size=18)
        
        single_a.move_to(LEFT*2.5 + DOWN*1)
        single_b.move_to(LEFT*1 + DOWN*1)
        single_c.move_to(RIGHT*0.5 + DOWN*1)
        
        # Level 2: pairs
        pair_ab = Text("{a,b}", font_size=16)
        pair_ac = Text("{a,c}", font_size=16)
        pair_bc = Text("{b,c}", font_size=16)
        
        pair_ab.move_to(LEFT*2.5)
        pair_ac.move_to(LEFT* 1)
        pair_bc.move_to(RIGHT*0.5)
        
        # Level 3 (top): whole set
        whole_set = Text("{a,b,c}", font_size=18)
        whole_set.move_to(LEFT * 1 + UP*1)
        
        # Draw connections
        connections = []
        # From empty set to singletons
        connections.extend([
            Line(empty_set.get_center(), single_a.get_center(), color=GRAY, stroke_width=1),
            Line(empty_set.get_center(), single_b.get_center(), color=GRAY, stroke_width=1),
            Line(empty_set.get_center(), single_c.get_center(), color=GRAY, stroke_width=1)
        ])
        
        # From singletons to pairs
        connections.extend([
            Line(single_a.get_center(), pair_ab.get_center(), color=GRAY, stroke_width=1),
            Line(single_a.get_center(), pair_ac.get_center(), color=GRAY, stroke_width=1),
            Line(single_b.get_center(), pair_ab.get_center(), color=GRAY, stroke_width=1),
            Line(single_b.get_center(), pair_bc.get_center(), color=GRAY, stroke_width=1),
            Line(single_c.get_center(), pair_ac.get_center(), color=GRAY, stroke_width=1),
            Line(single_c.get_center(), pair_bc.get_center(), color=GRAY, stroke_width=1)
        ])
        
        # From pairs to whole set
        connections.extend([
            Line(pair_ab.get_center(), whole_set.get_center(), color=GRAY, stroke_width=1),
            Line(pair_ac.get_center(), whole_set.get_center(), color=GRAY, stroke_width=1),
            Line(pair_bc.get_center(), whole_set.get_center(), color=GRAY, stroke_width=1)
        ])
        
        # Animate the power set structure
        self.play(Write(power_set_label), *[Create(line) for line in connections], Write(empty_set),
            Write(single_a), Write(single_b), Write(single_c),
            Write(pair_ab), Write(pair_ac), Write(pair_bc),
            Write(whole_set) )
        # Store for later use
        self.power_set_elements = VGroup(
            empty_set, single_a, single_b, single_c,
            pair_ab, pair_ac, pair_bc, whole_set
        )
        self.connections = VGroup(*connections)
        self.power_set_label = power_set_label
        self.wait(2)
        
        

        # Part 3: Show Cantor's theorem and proof
       
       
       
        theorem_title = Text("Cantor's Theorem", font_size=42, color=YELLOW)
        theorem_title.to_edge(UP)
        
        theorem_text = Text(
            "For any set S, there is no surjective function f: S → P(S)",
            font_size=32
        )
        theorem_text.next_to(theorem_title, DOWN, buff=0.25)
        
        self.play(Write(theorem_title))
        self.play(Write(theorem_text))
        # Transform A to arbitrary set S
        new_set_label = Text("S", font_size=36)
        new_set_label.move_to(set_a_circle.get_center())
        self.play(FadeOut(element_a), FadeOut(element_b), FadeOut(element_c),Transform(self.set_a_label, new_set_label))
        
        # Transform power set label

        powerSet = Square(side_length=2.75, color=YELLOW, fill_opacity=0.1)
        powerSet.next_to(set_a_circle, RIGHT, buff=1.2)
        powerSet.rotate(PI/4)
        new_power_label = Text("P(S)", font_size=32)
        new_power_label.move_to(powerSet.get_center())
        self.play(Transform(self.power_set_label, new_power_label), FadeOut(empty_set, single_a, single_b, single_c, pair_ab, pair_ac, pair_bc, whole_set,*self.connections))
        self.play(Write( powerSet ))
        
        # Store references for the proof visualization
        self.set_s = set_a_circle
        self.power_set_s = powerSet
        self.theorem_title = theorem_title
        self.theorem_text = theorem_text
                      
        self.wait(2)
             
        # Part 5: Show the proof visualization
        self.show_proof_visualization()
        
        
    def show_proof_visualization(self):
        # 1. Add thick arrow from S to P(S) labeled f
        arrow_f = Arrow(
            self.set_s.get_right(),
            self.power_set_s.get_left(),
            buff=0,
            stroke_width=32,
            color=GREEN
        )
        
        f_label = Text("f", font_size=28, color=GREEN)
        f_label.next_to(arrow_f, UP, buff=0.1)
        
        self.play(Create(arrow_f))
        self.play(Write(f_label))
        self.wait(1)
        
        # 2. Write definition of set D on the right side
        d_definition = MathTex(
            r"D = \{x \in S : x \notin f(x)\}"
        )
        d_definition.to_edge(RIGHT).shift(LEFT*1 + UP*1)
        
        self.play(Write(d_definition))
        self.wait(2)
        
        # Display D as a point in P(S)
        d_point = Dot(color=RED, radius=0.08)
        d_point.move_to(self.power_set_s.get_center() + UP*1 + RIGHT*0.2)
        
        d_label = Text("D", font_size=24, color=RED)
        d_label.next_to(d_point, RIGHT, buff=0.1)
        
        self.play(Create(d_point))
        self.play(Write(d_label))
        self.wait(1)
        
        # 3. Display element a in S and arrow to D
        a_dot = Dot(color=BLUE, radius=0.06)
        a_dot.move_to(self.set_s.get_center() + UP*0.7)
        
        a_label = Text("a", font_size=20, color=BLUE)
        a_label.next_to(a_dot, UP, buff=0.1)
        
        self.play(Create(a_dot))
        self.play(Write(a_label))
        
        # Thin arrow from a to D
        arrow_a_to_d = Arrow(
            a_dot.get_center(),
            d_point.get_center(),
            buff=0.05,
            stroke_width=1,
            color=BLUE
        )
        
        self.play(Create(arrow_a_to_d))
        self.wait(2)
        
        # 4. Write out the contradiction formulas below D definition
        assumption_text = Text("f(a)=D", font_size=36)
        assumption_text.next_to(d_definition, DOWN, buff=0.5)
        
        self.play(Write(assumption_text))
        self.wait(2)
        
        contradiction_text = MathTex(r"a \in D \leftrightarrow a \notin f(a)")
        contradiction_text.next_to(assumption_text, DOWN, buff=0.3)
        self.play(Write(contradiction_text))
        self.wait(1)    
        contradiction_text2 = MathTex(r"a \in D \leftrightarrow a \notin D")
        contradiction_text2.move_to(contradiction_text.get_center())
        self.play(Transform(contradiction_text, contradiction_text2))
        
        bottom = MathTex(r"\bot", font_size = 100, color=RED)
        bottom.next_to(contradiction_text, RIGHT, buff=1)
        self.play(Write(bottom))
        self.wait(2)