from manim import *

class VonNeumannUniverse(Scene):
    def construct(self):
        # Configuration
        level_spacing = 1.0
        start_y = -3
        side_offset = 1.5  # horizontal distance for non-ordinal sets
        
        # Store all elements for later manipulation
        all_elements = VGroup()
        v_lines = VGroup()  # For the V boundary lines
        
        # Cardinality counter (far left)
        card_label = MathTex(r"|V_n|:").scale(0.8)
        card_label.to_edge(LEFT, buff=0.5).shift(UP * 2)
        self.play(Write(card_label))
        
        # Level 0: empty set (center)
        v0 = MathTex(r"\emptyset").move_to(UP * start_y)
        v0.set_color(YELLOW)
        
        # Cardinality for level 0
        card_0_formula = MathTex(r"2^0").scale(0.8).next_to(card_label, DOWN, buff=0.3)
        card_0 = MathTex(r"1").scale(0.8).move_to(card_0_formula.get_center())
        
        self.play(Write(v0), Write(card_0_formula))
        all_elements.add(v0)
        self.wait(0.3)
        self.play(Transform(card_0_formula, card_0))
        self.wait(0.5)
        
        # Level 1: {∅} (center)
        v1 = MathTex(r"\{\emptyset\}").move_to(UP * (start_y + level_spacing))
        v1.set_color(YELLOW)
        v1_left = MathTex(r"\emptyset").scale(0.8).next_to(v1, LEFT, buff=0.8)
        v1_left.set_color(WHITE)
        
        card_1_formula = MathTex(r"2^1").scale(0.8).move_to(card_0_formula.get_center())
        card_1 = MathTex(r"2").scale(0.8).move_to(card_0_formula.get_center())
        
        self.play(Write(v1), Write(v1_left), Transform(card_0_formula, card_1_formula))
        all_elements.add(v1, v1_left)
        self.wait(0.3)
        self.play(Transform(card_0_formula, card_1))
        self.wait(0.5)
        
        # Level 2: ordinal {∅, {∅}} (center)
        v2_ordinal = MathTex(r"\{\emptyset, \{\emptyset\}\}").scale(0.7)
        v2_ordinal.move_to(UP * (start_y + 2 * level_spacing))
        v2_ordinal.set_color(YELLOW)
        
        # Other sets at level 2 (to the sides)
        v2_left = MathTex(r"\emptyset, \{\emptyset\}").scale(0.55)
        v2_left.next_to(v2_ordinal, LEFT, buff=0.8)
        v2_right = MathTex(r"\{\{\emptyset\}\}").scale(0.6)
        v2_right.next_to(v2_ordinal, RIGHT, buff=0.8)
        
        card_2_formula = MathTex(r"2^2").scale(0.8).move_to(card_0_formula.get_center())
        card_2 = MathTex(r"4").scale(0.8).move_to(card_0_formula.get_center())
        
        self.play(Write(v2_ordinal), Write(v2_left), Write(v2_right), Transform(card_0_formula, card_2_formula))
        all_elements.add(v2_ordinal, v2_left, v2_right)
        self.wait(0.3)
        self.play(Transform(card_0_formula, card_2))
        self.wait(0.5)
        
        # Level 3: ordinal {∅, {∅}, {∅, {∅}}} (center) and other sets
        v3_ordinal = MathTex(r"\{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}\}").scale(0.5)
        v3_ordinal.move_to(UP * (start_y + 3 * level_spacing))
        v3_ordinal.set_color(YELLOW)
        
        # Singletons (left side, closer to center)
        v3_singletons = MathTex(
            r"\{\emptyset\}, \{\{\emptyset\}\}, \{\{\emptyset, \{\emptyset\}\}\}"
        ).scale(0.4)
        v3_singletons.next_to(v3_ordinal, LEFT, buff=1.2)
        
        # Size 2 subsets (left side, further out)
        v3_pairs = MathTex(
            r"\{\emptyset, \{\emptyset\}\}, \{\emptyset, \{\{\emptyset\}\}\},"
            r"\{\emptyset, \{\emptyset, \{\emptyset\}\}\},"
            r"\{\{\emptyset\}, \{\{\emptyset\}\}\},"
            r"\{\{\emptyset\}, \{\emptyset, \{\emptyset\}\}\},"
            r"\{\{\{\emptyset\}\}, \{\emptyset, \{\emptyset\}\}\}"
        ).scale(0.28)
        v3_pairs.next_to(v3_singletons, LEFT, buff=0.3)
        
        # Size 3 subsets (right side)
        v3_triples = MathTex(
            r"\{\emptyset, \{\emptyset\}, \{\{\emptyset\}\}\},"
            r"\{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}\},"
            r"\{\emptyset, \{\{\emptyset\}\}, \{\emptyset, \{\emptyset\}\}\},"
            r"\{\{\emptyset\}, \{\{\emptyset\}\}, \{\emptyset, \{\emptyset\}\}\}"
        ).scale(0.28)
        v3_triples.next_to(v3_ordinal, RIGHT, buff=0.8)
        
        card_3_formula = MathTex(r"2^4").scale(0.8).move_to(card_0_formula.get_center())
        card_3 = MathTex(r"16").scale(0.8).move_to(card_0_formula.get_center())
        
        self.play(
            Write(v3_ordinal), 
            Write(v3_singletons),
            Write(v3_pairs),
            Write(v3_triples),
            Transform(card_0_formula, card_3_formula)
        )
        all_elements.add(v3_ordinal, v3_singletons, v3_pairs, v3_triples)
        self.wait(0.3)
        self.play(Transform(card_0_formula, card_3))
        self.wait(0.5)
        
        # Level 4: ordinal (center) and some other sets
        v4_ordinal = MathTex(
            r"\{\emptyset,\{\emptyset\},\{\emptyset,\{\emptyset\}\},\{\emptyset,\{\emptyset\},\{\emptyset,\{\emptyset\}\}\}\}"
        ).scale(0.38)
        v4_ordinal.move_to(UP * (start_y + 4 * level_spacing))
        v4_ordinal.set_color(YELLOW)
        
        # Various subsets at level 4
        v4_left1 = MathTex(r"\{\emptyset\},\{\{\emptyset\}\},\ldots").scale(0.35)
        v4_left1.next_to(v4_ordinal, LEFT, buff=2.5)
        
        v4_right1 = MathTex(r"\ldots, \{\{\{\emptyset, \{\emptyset\}\}\}\}").scale(0.35)
        v4_right1.next_to(v4_ordinal, RIGHT, buff=2.5)
        
        card_4_formula = MathTex(r"2^{16}").scale(0.8).move_to(card_0_formula.get_center())
        card_4 = MathTex(r"65536").scale(0.7).move_to(card_0_formula.get_center())
        
        self.play(
            Write(v4_ordinal), 
            Write(v4_left1), 
            Write(v4_right1),
            Transform(card_0_formula, card_4_formula)
        )
        all_elements.add(v4_ordinal, v4_left1, v4_right1)
        self.wait(0.3)
        self.play(Transform(card_0_formula, card_4))
        self.wait(0.5)
        
        # Ellipses indicating continuation
        vdots = MathTex(r"\vdots").move_to(UP * (start_y + 5 * level_spacing))
        dots_left = MathTex(r"\cdots").scale(0.7).move_to(UP * (start_y + 5 * level_spacing) + LEFT * 3)
        dots_right = MathTex(r"\cdots").scale(0.7).move_to(UP * (start_y + 5 * level_spacing) + RIGHT * 3)
        
        self.play(Write(vdots), Write(dots_left), Write(dots_right))
        all_elements.add(vdots, dots_left, dots_right)
        self.wait(0.5)
        
        # V_ω at the top
        v_omega_y = start_y + 6.2 * level_spacing
        v_omega = MathTex(r"V_\omega = \omega").move_to(UP * v_omega_y)
        v_omega.set_color(RED)
        
        card_omega = MathTex(r"\aleph_0").scale(0.8).move_to(card_0_formula.get_center())
        
        self.play(Write(v_omega), Transform(card_0_formula, card_omega))
        all_elements.add(v_omega)
        self.wait(1)
        
        # Draw V-shaped boundary lines (positioned outside the sets)
        v_bottom = start_y
        v_top = v_omega_y - 0.5
        v_width = 4.0  # Wide enough to be outside all displayed sets
        
        left_line = Line(
            start=UP * v_bottom,
            end=UP * v_top + LEFT * v_width,
            color=BLUE
        )
        right_line = Line(
            start=UP * v_bottom,
            end=UP * v_top + RIGHT * v_width,
            color=BLUE
        )
        
        self.play(Create(left_line), Create(right_line))
        v_lines.add(left_line, right_line)
        self.wait(1.5)
        
        # Create a group of everything for zooming
        everything = VGroup(all_elements, v_lines)
        
        # Function to zoom out and add new ordinal
        def zoom_and_add_ordinal(new_ordinal_tex, new_color=YELLOW, wait_time=0.6):
            # Calculate new top position
            current_top = v_omega.get_y()
            new_top = current_top + 0.8
            
            # Zoom out
            scale_factor = current_top / new_top
            self.play(
                everything.animate.scale(scale_factor).shift(DOWN * (new_top - current_top) * scale_factor),
                run_time=1.2
            )
            
            # Add new ordinal at the top
            new_ordinal = MathTex(new_ordinal_tex).move_to(UP * new_top)
            new_ordinal.set_color(new_color)
            self.play(Write(new_ordinal))
            everything.add(new_ordinal)
            
            # Extend V lines
            new_v_width = v_width * (new_top - v_bottom) / (current_top - v_bottom)
            new_left_line = Line(
                start=left_line.get_start(),
                end=UP * (new_top - 0.3) + LEFT * new_v_width,
                color=BLUE
            )
            new_right_line = Line(
                start=right_line.get_start(),
                end=UP * (new_top - 0.3) + RIGHT * new_v_width,
                color=BLUE
            )
            
            self.play(
                Transform(left_line, new_left_line),
                Transform(right_line, new_right_line),
                run_time=0.8
            )
            
            self.wait(wait_time)
            return new_top
        
        # V_{ω+1}
        zoom_and_add_ordinal(r"V_{\omega+1}")
        
        # V_{ω+2}
        zoom_and_add_ordinal(r"V_{\omega+2}")
        
        # V_{ω+3}
        zoom_and_add_ordinal(r"V_{\omega+3}", wait_time=0.5)
        
        # V_{ω+ω} = V_{ω·2}
        zoom_and_add_ordinal(r"V_{\omega \cdot 2}", wait_time=0.7)
        
        # V_{ω·3}
        zoom_and_add_ordinal(r"V_{\omega \cdot 3}", wait_time=0.5)
        
        # V_{ω²}
        zoom_and_add_ordinal(r"V_{\omega^2}", wait_time=0.7)
        
        # V_{ω³}
        zoom_and_add_ordinal(r"V_{\omega^3}", wait_time=0.6)
        
        # V_{ε₀}
        zoom_and_add_ordinal(r"V_{\varepsilon_0}", new_color=BLUE, wait_time=0.8)
        
        # V_{ε₁}
        zoom_and_add_ordinal(r"V_{\varepsilon_1}", new_color=BLUE, wait_time=0.6)
        
        # V_{ω₁}
        zoom_and_add_ordinal(r"V_{\omega_1}", new_color=GREEN, wait_time=2)
        
        # Fade out
        self.play(FadeOut(card_label), FadeOut(card_0_formula), FadeOut(everything), run_time=1.5)
        self.wait(0.5)