from manim import *
import numpy as np

class AlephCardinals(Scene):
    def construct(self):
        # Title
        title = Text("The Aleph Cardinals", font_size=48, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Subtitle
        subtitle = Text("Infinite Cardinal Numbers", font_size=32)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))
        self.wait(1)
        
        # Create initial alephs that will be visible
        alephs = []
        descriptions = []
        
        # Define the alephs with their descriptions
        aleph_data = [
            ("\\aleph_0", "Countable infinity\n(Natural numbers)", BLUE),
            ("\\aleph_1", "First uncountable\n(Real numbers?)", GREEN),
            ("\\aleph_2", "Second uncountable", RED),
            ("\\aleph_3", "Third uncountable", PURPLE),
            ("\\aleph_4", "Fourth uncountable", ORANGE),
            ("\\aleph_5", "Fifth uncountable", PINK),
            ("\\aleph_6", "Sixth uncountable", TEAL),
            ("\\aleph_7", "Seventh uncountable", YELLOW),
            ("\\aleph_8", "Eighth uncountable", MAROON),
            ("\\aleph_9", "Ninth uncountable", DARK_BROWN),
        ]
        
        # Create the initial set of alephs
        spacing = 3.0  # Horizontal spacing between alephs
        start_x = -12  # Start position (off-screen left)
        
        for i, (aleph_tex, desc, color) in enumerate(aleph_data):
            # Create the aleph symbol
            aleph = MathTex(aleph_tex, font_size=60, color=color)
            aleph.move_to(RIGHT * (start_x + i * spacing))
            
            # Create description
            description = Text(desc, font_size=20, color=WHITE)
            description.next_to(aleph, DOWN, buff=0.5)
            
            alephs.append(aleph)
            descriptions.append(description)
        
        # Create dots to show continuation
        dots = MathTex("\\cdots", font_size=60, color=GRAY)
        dots.move_to(RIGHT * (start_x + len(aleph_data) * spacing))
        
        # Add all elements to groups for easy manipulation
        aleph_group = VGroup(*alephs)
        desc_group = VGroup(*descriptions)
        all_content = VGroup(aleph_group, desc_group, dots)
        
        # Initially show first few alephs
        initial_alephs = VGroup(alephs[0], descriptions[0])
        self.play(Write(initial_alephs))
        self.wait(2)
        
        # Add explanation for aleph_0
        explanation = Text("ℵ₀ = |ℕ| = size of countable sets", font_size=28)
        explanation.next_to(subtitle, DOWN, buff=1)
        self.play(Write(explanation))
        self.wait(2)
        
        # Show aleph_1
        self.play(Write(VGroup(alephs[1], descriptions[1])))
        
        # Update explanation
        new_explanation = Text("ℵ₁ = first uncountable cardinal (Continuum Hypothesis: ℵ₁ = 2^ℵ₀?)", font_size=24)
        self.play(Transform(explanation, new_explanation))
        self.wait(2)
        
        # Show more alephs
        for i in range(2, 5):
            self.play(Write(VGroup(alephs[i], descriptions[i])), run_time=0.8)
            self.wait(0.5)
        
        # Update explanation for the sequence
        sequence_explanation = Text("Each ℵₙ₊₁ is the smallest cardinal larger than ℵₙ", font_size=28)
        self.play(Transform(explanation, sequence_explanation))
        self.wait(2)
        
        # Pan across to show more alephs
        self.play(
            all_content.animate.shift(LEFT * 6),
            run_time=3
        )
        
        # Show the remaining alephs
        for i in range(5, len(aleph_data)):
            self.add(alephs[i], descriptions[i])
        
        self.add(dots)
        self.wait(1)
        
        # Continue panning to show the limit
        self.play(
            all_content.animate.shift(LEFT * 8),
            run_time=3
        )
        
        # Create aleph_omega
        aleph_omega = MathTex("\\aleph_\\omega", font_size=80, color=GOLD)
        aleph_omega.move_to(RIGHT * 2)
        
        omega_desc = Text("Limit of all finite alephs\nℵω = sup{ℵ₀, ℵ₁, ℵ₂, ...}", font_size=24, color=GOLD)
        omega_desc.next_to(aleph_omega, DOWN, buff=0.5)
        
        # Dramatic entrance for aleph_omega
        self.play(
            DrawBorderThenFill(aleph_omega),
            run_time=2
        )
        self.play(Write(omega_desc))
        
        # Update main explanation
        omega_explanation = Text("ℵω is the supremum of all finite-indexed alephs", font_size=28)
        self.play(Transform(explanation, omega_explanation))
        self.wait(2)
        
        # Show that it continues beyond omega
        beyond_text = Text("And it continues: ℵω+1, ℵω+2, ..., ℵω·2, ..., ℵω², ...", font_size=24)
        beyond_text.next_to(omega_desc, DOWN, buff=0.8)
        self.play(Write(beyond_text))
        self.wait(2)
        
        # Final dramatic text
        infinity_text = Text("The hierarchy of infinities has no end!", font_size=36, color=YELLOW)
        infinity_text.next_to(beyond_text, DOWN, buff=0.8)
        self.play(Write(infinity_text))
        self.wait(2)
        
        # Create a visual representation of the hierarchy
        hierarchy_title = Text("Cardinal Hierarchy", font_size=32, color=GOLD)
        hierarchy_title.to_edge(UP)
        
        # Clear screen for hierarchy view
        self.play(FadeOut(VGroup(title, subtitle, explanation, all_content, aleph_omega, omega_desc, beyond_text, infinity_text)))
        self.play(Write(hierarchy_title))
        
        # Create tower of alephs
        tower_alephs = []
        tower_positions = [
            DOWN * 2,
            DOWN * 1,
            ORIGIN,
            UP * 1,
            UP * 2
        ]
        
        tower_labels = ["\\aleph_0", "\\aleph_1", "\\aleph_2", "\\aleph_\\omega", "\\aleph_{\\omega+1}"]
        tower_colors = [BLUE, GREEN, RED, GOLD, PURPLE]
        
        for i, (label, pos, color) in enumerate(zip(tower_labels, tower_positions, tower_colors)):
            aleph = MathTex(label, font_size=50, color=color)
            aleph.move_to(pos)
            tower_alephs.append(aleph)
            
            # Animate each level appearing
            self.play(Write(aleph), run_time=0.8)
            
            # Add arrows between levels
            if i < len(tower_labels) - 1:
                arrow = Arrow(pos + UP*0.3, tower_positions[i+1] + DOWN*0.3, buff=0.1)
                self.play(Create(arrow), run_time=0.5)
        
        # Add side text
        side_text = Text("Each level is\n'much larger'\nthan the last", font_size=24)
        side_text.to_edge(RIGHT)
        self.play(Write(side_text))
        
        self.wait(3)
        
        # Final fade out
        final_objects = VGroup(hierarchy_title, *tower_alephs, side_text)
        # Also need to include the arrows - let's get all remaining objects
        remaining_objects = VGroup(*[mob for mob in self.mobjects if isinstance(mob, VMobject)])
        self.play(FadeOut(remaining_objects))

# To render this animation, save as aleph_cardinals.py and run:
# manim aleph_cardinals.py AlephCardinals -pql