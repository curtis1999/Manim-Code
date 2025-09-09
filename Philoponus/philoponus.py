from manim import *
import numpy as np

class PhiloponusArgument(Scene):
    def construct(self):
        
        # Earth at the origin (larger blue dot)
        earth = Dot(ORIGIN, radius=0.15, color=BLUE)
        earth_label = Text("Earth", font_size=20).next_to(earth, DOWN, buff=0.3)
        
        # Orbit radii
        inner_radius = 1.5
        outer_radius = 2.5
        
        # Create orbit circles
        inner_orbit = Circle(radius=inner_radius, color=WHITE, stroke_opacity=0.3)
        outer_orbit = Circle(radius=outer_radius, color=WHITE, stroke_opacity=0.3)
        
        # Celestial bodies
        # Inner planet (faster, like the moon - 360x Saturn's speed)
        inner_planet = Dot(radius=0.08, color=YELLOW)
        inner_planet.move_to([inner_radius, 0, 0])
        inner_label = Text("Mercury", font_size=16, color=YELLOW)
        inner_label.next_to(inner_planet, RIGHT, buff=0.1)
        
        # Outer planet (slower, like Saturn)
        outer_planet = Dot(radius=0.08, color=RED)
        outer_planet.move_to([outer_radius, 0, 0])
        outer_label = Text("MARS", font_size=16, color=RED)
        outer_label.next_to(outer_planet, RIGHT, buff=0.1)
        
        # Revolution counters
        inner_counter = Text("Revolutions: 0", font_size=20, color=YELLOW)
        inner_counter.to_corner(UL, buff=1)
        
        outer_counter = Text("Revolutions: 0", font_size=20, color=RED)
        outer_counter.next_to(inner_counter, DOWN, buff=0.3)
        
        # Ratio display
        ratio_text = Text("Ratio: 4:1", font_size=20, color=WHITE)
        ratio_text.next_to(outer_counter, DOWN, buff=0.3)
            
        self.play(
            Create(earth),
            Write(earth_label),
            Create(inner_orbit),
            Create(outer_orbit)
        )
        
        self.play(
            Create(inner_planet),
            Create(outer_planet),
            Write(inner_label),
            Write(outer_label)
        )
        
        self.play(
            Write(inner_counter),
            Write(outer_counter),
        )
        
        self.wait(1)
        
        # Animation parameters
        inner_speed = 8  # Fast body completes 2 radians per unit time
        outer_speed = 2  # Slow body completes 0.2 radians per unit time (10x slower)
        total_time = 9.3
        dt = 0.1
        
        inner_revolutions = 0
        outer_revolutions = 0
        inner_angle = 0
        outer_angle = 0
        
        # Create updater functions for the planets
        def update_inner_planet(mob, dt):
            nonlocal inner_angle, inner_revolutions
            inner_angle += inner_speed * dt
            if inner_angle >= 2 * PI:
                inner_revolutions += 1
                inner_angle -= 2 * PI
            
            x = inner_radius * np.cos(inner_angle)
            y = inner_radius * np.sin(inner_angle)
            mob.move_to([x, y, 0])
            
            # Update label position
            inner_label.next_to(mob, RIGHT, buff=0.2)
        
        def update_outer_planet(mob, dt):
            nonlocal outer_angle, outer_revolutions
            outer_angle += outer_speed * dt
            if outer_angle >= 2 * PI:
                outer_revolutions += 1
                outer_angle -= 2 * PI
            
            x = outer_radius * np.cos(outer_angle)
            y = outer_radius * np.sin(outer_angle)
            mob.move_to([x, y, 0])
            
            # Update label position
            outer_label.next_to(mob, RIGHT, buff=0.2)
        
        # Add updaters
        inner_planet.add_updater(update_inner_planet)
        outer_planet.add_updater(update_outer_planet)
        
        # Update counters
        def update_counters():
            new_inner_counter = Text(f"Revolutions: {inner_revolutions}", font_size=20, color=YELLOW)
            new_inner_counter.to_corner(UL, buff=1)
            
            new_outer_counter = Text(f"Revolutions: {outer_revolutions}", font_size=20, color=RED)
            new_outer_counter.next_to(new_inner_counter, DOWN, buff=0.3)
            
            return new_inner_counter, new_outer_counter
        
        # Run the animation
        for t in np.arange(0, total_time, dt):
            self.wait(dt)
            
            # Update counters every second
            if abs(t % 1.0) < dt:
                new_inner_counter, new_outer_counter = update_counters()
                
                self.play(
                    Transform(inner_counter, new_inner_counter),
                    Transform(outer_counter, new_outer_counter),
                    run_time=0.3
                )
        
        # Remove updaters
        inner_planet.clear_updaters()
        outer_planet.clear_updaters()
        
        # Final update of counters
        new_inner_counter, new_outer_counter = update_counters()
        self.play(
            Transform(inner_counter, new_inner_counter),
            Transform(outer_counter, new_outer_counter),
        )
        self.play(Write(ratio_text))
        self.wait()
        # Clear the scene and show the argument
        dt = 0.1
        # Run the animation
        for t in np.arange(0, total_time, dt):
            self.wait(dt)
            
            # Update counters every second
            if abs(t % 1.0) < dt:
                new_inner_counter, new_outer_counter = update_counters()
                
                self.play(
                    Transform(inner_counter, new_inner_counter),
                    Transform(outer_counter, new_outer_counter),
                    run_time=0.3
                )
                
        self.play(
            FadeOut(earth),
            FadeOut(earth_label),
            FadeOut(inner_orbit),
            FadeOut(outer_orbit),
            FadeOut(inner_planet),
            FadeOut(outer_planet),
            FadeOut(inner_label),
            FadeOut(outer_label),
            FadeOut(inner_counter),
            FadeOut(outer_counter),
            FadeOut(ratio_text)
        )