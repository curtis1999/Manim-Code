from manim import *

class CantorParadise(Scene):
    def construct(self):
        # Display empty set with label 0 (shifted left)
        label_0 = MathTex("0").move_to(DOWN * 3.5 + LEFT * 2)
        empty_set = MathTex(r"=\emptyset").next_to(label_0, RIGHT, buff=0.2)
        empty_set.set_color(RED)
        self.play(Write(empty_set), Write(label_0))
        self.wait(0.5)
        
        # Create a group to hold everything except the empty set (for zooming)
        ordinals_group = VGroup()
        
        # Display first ordinal {∅} with label 1 directly above 0
        current_y = -2.7
        v_bottom = -3.5  # Empty set position
        
        label_1 = MathTex("1").next_to(label_0, UP, buff=0.2)
        ordinal_1 = MathTex(r"=\{\emptyset\}").next_to(label_1, RIGHT, buff=0.2)
        ordinal_1.set_color(ORANGE)
        self.play(Write(ordinal_1), Write(label_1), run_time=0.8)
        ordinals_group.add(ordinal_1, label_1)
        current_y += 0.8
        self.wait(0.5)
        
        # Display second ordinal - set representation first
        label_2 = MathTex("2").next_to(label_1, UP, buff=0.2)
        ordinal_2_set = MathTex(r"=\{\emptyset, \{\emptyset\}\}").next_to(label_2, RIGHT, buff=0.2)
        ordinal_2_set.set_color(ORANGE)
        if ordinal_2_set.width > 6:
            ordinal_2_set.scale(6 / ordinal_2_set.width)
        
        self.play(Write(ordinal_2_set), Write(label_2), run_time=1.5)
        self.wait(0.5)
        
        # Highlight empty set at bottom and in the ordinal
        self.play(
            empty_set.animate.set_color(GREEN),
            ordinal_2_set[0][2].animate.set_color(GREEN),  # First ∅ in the set
            run_time=0.5
        )
        self.wait(0.5)
        
        # Return to original colors
        self.play(
            empty_set.animate.set_color(RED),
            ordinal_2_set[0][2].animate.set_color(ORANGE),
            run_time=0.3
        )
        
        # Highlight ordinal 1 and second member of ordinal 2
        self.play(
            ordinal_1.animate.set_color(GREEN),
            ordinal_2_set[0][4:7].animate.set_color(GREEN),  # {∅} part
            run_time=0.5
        )
        self.wait(0.5)
        
        # Return to original colors
        self.play(
            ordinal_1.animate.set_color(ORANGE),
            ordinal_2_set[0][4:7].animate.set_color(ORANGE),
            run_time=0.3
        )
        self.wait(0.5)
        
        # Add simple representation beside it
        ordinal_2_simple = MathTex(r"= \{0, 1\}").next_to(ordinal_2_set, RIGHT, buff=0.2)
        ordinal_2_simple.set_color(ORANGE)
        self.play(Write(ordinal_2_simple), run_time=0.8)
        ordinals_group.add(ordinal_2_set, ordinal_2_simple, label_2)
        current_y += 0.8
        self.wait(0.5)
        
        # Display and explain ordinal 3
        label_3 = MathTex("3").next_to(label_2, UP, buff=0.2)
        ordinal_3_set = MathTex(r"=\{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}\}").next_to(label_3, RIGHT, buff=0.2)
        ordinal_3_set.set_color(ORANGE)
        if ordinal_3_set.width > 6:
            ordinal_3_set.scale(6 / ordinal_3_set.width)
        
        self.play(Write(ordinal_3_set), Write(label_3), run_time=0.8)
        self.wait(0.5)
        
        # Highlight predecessors for 3 (0, 1, 2)
        self.play(
            empty_set.animate.set_color(GREEN),
            ordinal_3_set[0][2].animate.set_color(GREEN),
            run_time=0.5
        )
        self.wait(0.3)
        self.play(
            empty_set.animate.set_color(RED),
            ordinal_3_set[0][2].animate.set_color(ORANGE),
            ordinal_1.animate.set_color(GREEN),
            ordinal_3_set[0][4:7].animate.set_color(GREEN),
            run_time=0.5
        )
        self.wait(0.3)
        self.play(
            ordinal_1.animate.set_color(ORANGE),
            ordinal_3_set[0][4:7].animate.set_color(ORANGE),
            ordinal_2_set.animate.set_color(GREEN),
            ordinal_3_set[0][8:15].animate.set_color(GREEN),
            run_time=0.5
        )
        self.wait(0.3)
        self.play(
            ordinal_2_set.animate.set_color(ORANGE),
            ordinal_3_set[0][8:15].animate.set_color(ORANGE),
            run_time=0.3
        )
        self.wait(0.5)
        
        # Add simple representation beside it
        ordinal_3_simple = MathTex(r"= \{0, 1, 2\}").next_to(ordinal_3_set, RIGHT, buff=0.2)
        ordinal_3_simple.set_color(ORANGE)
        self.play(Write(ordinal_3_simple), run_time=0.8)
        ordinals_group.add(ordinal_3_set, ordinal_3_simple, label_3)
        current_y += 0.8
        self.wait(0.5)
        
        # Display and explain ordinal 4
        label_4 = MathTex("4").next_to(label_3, UP, buff=0.2)
        ordinal_4_set = MathTex(r"\{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}, \{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}\}\}").next_to(label_4, RIGHT, buff=0.2)
        ordinal_4_set.set_color(ORANGE)
        if ordinal_4_set.width > 6:
            ordinal_4_set.scale(6 / ordinal_4_set.width)
        
        self.play(Write(ordinal_4_set), Write(label_4), run_time=0.8)
        self.wait(0.5)
        
        # Quick highlight of all predecessors for 4
        self.play(
            empty_set.animate.set_color(GREEN),
            ordinal_1.animate.set_color(GREEN),
            ordinal_2_set.animate.set_color(GREEN),
            ordinal_3_set.animate.set_color(GREEN),
            run_time=0.5
        )
        self.wait(0.5)
        self.play(
            empty_set.animate.set_color(RED),
            ordinal_1.animate.set_color(ORANGE),
            ordinal_2_set.animate.set_color(ORANGE),
            ordinal_3_set.animate.set_color(ORANGE),
            run_time=0.3
        )
        self.wait(0.5)
        
        # Add simple representation beside it
        ordinal_4_simple = MathTex(r"= \{0, 1, 2, 3\}").next_to(ordinal_4_set, RIGHT, buff=0.2)
        ordinal_4_simple.set_color(ORANGE)
        self.play(Write(ordinal_4_simple), run_time=0.8)
        ordinals_group.add(ordinal_4_set, ordinal_4_simple, label_4)
        current_y += 0.8
        self.wait(0.5)
        
        # Add vertical ellipsis (dots)
        dots = MathTex(r"\vdots").move_to(UP * current_y)
        dots.set_color(WHITE)
        self.play(FadeIn(dots))
        ordinals_group.add(dots)
        current_y += 0.8
        self.wait(0.3)
        
        # Add omega
        v_omega = MathTex(r"\omega").move_to(UP * current_y)
        v_omega.set_color(GREEN)
        self.play(Write(v_omega))
        ordinals_group.add(v_omega)
        self.wait(1)
        
        # Add omega+1, omega+2, omega+3 without zooming
        v_omegaPlus1 = MathTex(r"\omega + 1").move_to(UP * (current_y + 0.8))
        v_omegaPlus1.set_color(GREEN)
        self.play(Write(v_omegaPlus1))
        ordinals_group.add(v_omegaPlus1)
        self.wait(0.5)
        
        v_omegaPlus2 = MathTex(r"\omega + 2").move_to(UP * (current_y + 1.6))
        v_omegaPlus2.set_color(GREEN)   
        self.play(Write(v_omegaPlus2))
        ordinals_group.add(v_omegaPlus2)
        self.wait(0.5)
        
        v_omegaPlus3 = MathTex(r"\omega + 3").move_to(UP * (current_y + 2.4))
        v_omegaPlus3.set_color(GREEN)
        self.play(Write(v_omegaPlus3))
        ordinals_group.add(v_omegaPlus3)
        current_y += 2.4
        self.wait(1)
        
        # Simplified zoom function - constant scale factor
        def zoom_and_add_ordinal(new_ordinal_tex, new_color=YELLOW, wait_time=0.6):
            # Fixed scale factor for all limit ordinals
            scale_factor = 0.85
            
            # Scale around the empty set position
            empty_pos = empty_set.get_center()
            
            self.play(
                ordinals_group.animate.scale(scale_factor, about_point=empty_pos),
                run_time=1.2
            )
            
            # Add new ordinal at a fixed position above
            new_top = 3.0  # Fixed top position
            new_ordinal = MathTex(new_ordinal_tex).move_to(UP * new_top)
            new_ordinal.set_color(new_color)
            self.play(Write(new_ordinal))
            ordinals_group.add(new_ordinal)
            
            self.wait(wait_time)
        
        # Add dots
        zoom_and_add_ordinal(r"\vdots", WHITE, wait_time=0.4)
        
        # Add limit ordinals with constant zoom
        zoom_and_add_ordinal(r"\omega + \omega", YELLOW)
        zoom_and_add_ordinal(r"\omega \times \omega", PINK)
        zoom_and_add_ordinal(r"\omega^{\omega}", PURPLE)
        zoom_and_add_ordinal(r"\epsilon_0", RED)
        zoom_and_add_ordinal(r"\epsilon_1", RED)
        zoom_and_add_ordinal(r"\vdots", WHITE, wait_time=0.4)
        zoom_and_add_ordinal(r"\omega_1", GOLD, wait_time=2)
        
        # Final pause
        self.wait(2)