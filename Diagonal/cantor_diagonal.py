from manim import *
import random

class CantorDiagonal(Scene):
    def construct(self):
    
        # Create grid dimensions
        num_rows = 10
        num_cols = 10
        
        # Generate random binary strings for each row
        random.seed(42)  # For reproducible results
        binary_strings = []
        for i in range(num_rows):
            string = [random.choice([0, 1]) for _ in range(num_cols)]
            binary_strings.append(string)
        
        # Create the grid
        grid_group = VGroup()
        
        # Natural numbers column (left side)
        nat_numbers = VGroup()
        for i in range(num_rows):
            num_text = Text(str(i + 1), font_size=24)
            num_text.move_to(LEFT * 4 + UP * (2 - i * 0.5))
            nat_numbers.add(num_text)
        
        # Binary strings grid
        binary_grid = VGroup()
        digit_objects = {}  # Store individual digit objects for later reference
        
        for i in range(num_rows):
            row_group = VGroup()
            for j in range(num_cols):
                digit = Text(str(binary_strings[i][j]), font_size=20)
                digit.move_to(LEFT * 2.5 + RIGHT * j * 0.4 + UP * (2 - i * 0.5))
                row_group.add(digit)
                digit_objects[(i, j)] = digit
            binary_grid.add(row_group)
        
        # Add arrow showing the mapping
        arrow = Arrow(LEFT * 3.5, LEFT * 2.8, buff=0.1)
        arrow_label = Text("→", font_size=20)
        arrow_label.next_to(arrow, UP, buff=0.1)
        
        grid_group.add(nat_numbers, binary_grid, arrow)
        
        # Animate the creation of the grid
        self.play(Write(nat_numbers))
        self.play(Create(arrow))
        
        # Animate binary strings row by row
        for i in range(num_rows):
            self.play(Write(binary_grid[i]), run_time=0.1)
        
        self.wait(2)
        
        # Highlight the diagonal
        diagonal_squares = VGroup()
        diagonal_digits = []
        
        for i in range(min(num_rows, num_cols)):
            # Create a square around the diagonal element
            square = Square(side_length=0.3)
            square.move_to(digit_objects[(i, i)].get_center())
            square.set_stroke(RED, width=3)
            square.set_fill(RED, opacity=0.2)
            diagonal_squares.add(square)
            diagonal_digits.append(binary_strings[i][i])
        
        # Highlight diagonal elements
        self.play(Create(diagonal_squares))
        self.wait(2)
        
        # Show the diagonal number
        diagonal_text = "Diagonal: "
        for digit in diagonal_digits:
            diagonal_text += str(digit)
        diagonal_text += "..."
        diagonal_display = Text(diagonal_text, font_size=28, color = RED)
        diagonal_display.next_to(diagonal_squares, RIGHT, buff=0.5)
        diagonal_display.shift(UP * 1.5)
        self.play(Write(diagonal_display))
        self.wait(2)
        
        # Create the new number by flipping bits
        new_digits = []
        for digit in diagonal_digits:
            new_digits.append(1 - digit)  # Flip 0→1, 1→0
        
        new_text = "New number: "
        for digit in new_digits:
            new_text += str(digit)
        new_text += "..."
        new_display = Text(new_text, font_size=28, color=BLUE)
        new_display.next_to(diagonal_display, DOWN, buff=0.3)
        self.play(Write(new_display))
        self.wait(2)
        
        # Highlight differences
        difference_squares = VGroup()
        for i in range(min(num_rows, num_cols)):
            if new_digits[i] != binary_strings[i][i]:
                square = Square(side_length=0.3)
                square.move_to(digit_objects[(i, i)].get_center())
                square.set_stroke(BLUE, width=4)
                square.set_fill(BLUE, opacity=0.3)
                difference_squares.add(square)
        
        self.play(Transform(diagonal_squares, difference_squares))
        self.wait(1)

        # NEW SECTION: Highlight each digit comparison
        # Sequential highlighting with narration timing
        yellow_highlights = VGroup()
        diagonal_highlights = VGroup()
        
        for i in range(min(len(new_digits), num_rows)):
            # Create yellow box for the specific digit in "New number" text
            yellow_box = Rectangle(width=0.25, height=0.35)
            yellow_box.move_to(new_display)
            yellow_box.shift(RIGHT * (i * 0.21 + 0.13))  # Adjust position based on index
            yellow_box.set_stroke(YELLOW, width=3)
            yellow_box.set_fill(YELLOW, opacity=0.3)
            
            # Create highlighting for the corresponding diagonal element in grid
            diagonal_highlight = Square(side_length=0.3)
            diagonal_highlight.move_to(digit_objects[(i, i)].get_center())
            diagonal_highlight.set_stroke(YELLOW, width=4)
            diagonal_highlight.set_fill(YELLOW, opacity=0.4)
            
            # Animate the highlighting
            self.play(  # Remove previous highlights
                Create(yellow_box),
                Create(diagonal_highlight),
                run_time=0.8
            )
            
            #yellow_highlights.add(yellow_box)
            #diagonal_highlights.add(diagonal_highlight)
            
            # Brief pause between each comparison
            self.wait(0.5)
            self.play(FadeOut(yellow_box, diagonal_highlight))
        
        # Hold the final state for a moment
        self.wait(2)
        
        # Fade everything out
        all_objects = VGroup(
            grid_group, diagonal_squares, 
            diagonal_display, new_display,
            yellow_highlights, diagonal_highlights
        )
        self.play(FadeOut(all_objects))

        Naturals = Circle(color=YELLOW, radius=0.9, fill_opacity=0.5).shift(LEFT*2)
        Reals = Circle(color=RED, radius=0.9, fill_opacity=0.5).next_to(naturals, RIGHT, buff=2)