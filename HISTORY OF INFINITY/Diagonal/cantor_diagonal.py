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
            num_text.move_to(LEFT * 4.5 + UP * (2 - i * 0.5))
            nat_numbers.add(num_text)
        
        # Add vertical ellipsis below the last natural number
        vertical_ellipsis = MathTex(r"\vdots", font_size=24)
        vertical_ellipsis.move_to(LEFT * 4.5 + UP * (2 - num_rows * 0.5))
        nat_numbers.add(vertical_ellipsis)
        
        # Binary strings grid
        binary_grid = VGroup()
        digit_objects = {}  # Store individual digit objects for later reference
        
        for i in range(num_rows):
            row_group = VGroup()
            for j in range(num_cols):
                digit = Text(str(binary_strings[i][j]), font_size=20)
                digit.move_to(LEFT * 3 + RIGHT * j * 0.4 + UP * (2 - i * 0.5))
                row_group.add(digit)
                digit_objects[(i, j)] = digit
            
            # Add horizontal ellipsis at the end of each row
            h_ellipsis = MathTex(r"\cdots", font_size=20)
            h_ellipsis.move_to(LEFT * 3 + RIGHT * num_cols * 0.4 + UP * (2 - i * 0.5))
            row_group.add(h_ellipsis)
            binary_grid.add(row_group)
        
        # Add a row of horizontal ellipses below the grid
        bottom_ellipses = VGroup()
        for j in range(num_cols + 1):  # +1 to include the final ellipsis position
            if j < num_cols:
                h_ellipsis = MathTex(r"\vdots", font_size=20)
                h_ellipsis.move_to(LEFT * 3 + RIGHT * j * 0.4 + UP * (2 - num_rows * 0.5))
            else:
                # Diagonal ellipsis at the bottom right
                diag_ellipsis = MathTex(r"\ddots", font_size=20)
                diag_ellipsis.move_to(LEFT * 3 + RIGHT * j * 0.4 + UP * (2 - num_rows * 0.5))
                h_ellipsis = diag_ellipsis
            bottom_ellipses.add(h_ellipsis)
        
        # Add labels
        nat_label = MathTex(r"\mathbb{N}", font_size=32)
        nat_label.move_to(LEFT * 5 + UP * 0)
        
        real_label = MathTex(r"\mathbb{R}", font_size=32)
        real_label.move_to(LEFT * 0.5 + UP * 2.5)
        
        # Add arrow showing the mapping
        arrow = Arrow(LEFT * 4.4, LEFT * 3, buff=0.1)
        arrow_label = Text("→", font_size=20)
        arrow_label.next_to(arrow, UP, buff=0.1)
        
        grid_group.add(nat_numbers, binary_grid, bottom_ellipses, arrow, nat_label, real_label)
        
        # Animate the creation of the grid
        self.play(Write(nat_label), Write(real_label),Write(nat_numbers))
        self.play(Create(arrow))
        
        # Animate binary strings row by row
        for i in range(num_rows):
            self.play(Write(binary_grid[i]), run_time=0.1)
        self.play(Write(bottom_ellipses), run_time=0.01)
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
        
        # Create diagonal number grid on the right (positioned higher)
        diagonal_grid_pos = RIGHT * 2 + UP * 2
        diagonal_label = Text("D:", font_size=24, color=RED)
        diagonal_label.move_to(diagonal_grid_pos + LEFT * 0.6)
        diagonal_label.shift(RIGHT*0.3)
        
        diagonal_number_grid = VGroup()
        diagonal_digit_objects = {}
        
        for i, digit in enumerate(diagonal_digits):
            digit_text = Text(str(digit), font_size=24, color=RED)
            digit_text.move_to(diagonal_grid_pos + RIGHT * i * 0.3)
            diagonal_number_grid.add(digit_text)
            diagonal_digit_objects[i] = digit_text
        
        # Add ellipsis to diagonal display
        diagonal_ellipsis = Text("...", font_size=24, color=RED)
        diagonal_ellipsis.move_to(diagonal_grid_pos + RIGHT * len(diagonal_digits) * 0.3)
        diagonal_number_grid.add(diagonal_ellipsis)
        
        self.play(
            Create(diagonal_squares), 
            Write(diagonal_label),
            Write(diagonal_number_grid), 
            run_time=2)
        self.wait(2)
        
        # Create new number grid (positioned below diagonal)
        new_grid_pos = diagonal_grid_pos + DOWN * 0.8
        new_label = Text("N:", font_size=24, color=BLUE)
        new_label.move_to(new_grid_pos + LEFT * 0.6)
        new_label.shift(RIGHT*0.3)
        
        new_number_grid = VGroup()
        new_digit_objects = {}
        
        # Initialize empty positions for new number digits
        for i in range(len(diagonal_digits)):
            digit_text = Text("", font_size=24, color=BLUE)  # Start empty
            digit_text.move_to(new_grid_pos + RIGHT * i * 0.3)
            new_number_grid.add(digit_text)
            new_digit_objects[i] = digit_text
        
        # Add ellipsis to new number display
        #new_ellipsis = Text("...", font_size=24, color=BLUE)
        #new_ellipsis.move_to(new_grid_pos + RIGHT * len(diagonal_digits) * 0.3)
        #new_number_grid.add(new_ellipsis)
        
        self.play(Write(new_label), Write(new_number_grid))
        self.wait(1)
        # Sequential highlighting to display new number
        for i in range(min(len(diagonal_digits), num_rows)):
            # Highlight diagonal element
            diagonal_crossout = Line(0 * RIGHT, 0.3 * RIGHT)
            diagonal_crossout .move_to(digit_objects[(i, i)].get_center())
            diagonal_crossout .set_stroke(YELLOW)
            diagonal_crossout.rotate(45 * DEGREES)            
            
            # Create blue digit next to diagonal element
            flipped_digit = 1 - diagonal_digits[i]
            blue_digit = Text(str(flipped_digit), font_size=20, color=BLUE)
            blue_digit.move_to(digit_objects[(i, i)].get_center() + RIGHT * 0.2 + UP * 0.2)
        
            
            self.wait(0.1)
            
            # Add digit to new number grid
            new_digit_objects[i].become(Text(str(flipped_digit), font_size=24, color=BLUE))
            new_digit_objects[i].move_to(new_grid_pos + RIGHT * i * 0.3)
            
                        # Animate highlighting and blue digit appearance
            self.play(
                Create(diagonal_crossout),
                Write(blue_digit),
                Write(new_digit_objects[i]),
                run_time=0.4
            )
            self.wait(0.2)
            
            # Fade out highlights and blue digit
            self.play(
                FadeOut(diagonal_crossout),
                FadeOut(blue_digit),
                run_time=0.25
            )
        # Add ellipsis to new number display
        new_ellipsis = Text("...", font_size=24, color=BLUE)
        new_ellipsis.move_to(new_grid_pos + RIGHT * len(diagonal_digits) * 0.3)
        self.play(Write(new_ellipsis))
        self.wait(2)
        # Sequential highlighting and digit-by-digit construction
        for i in range(min(len(diagonal_digits), num_rows)):
            # Highlight diagonal element
            diagonal_highlight = Square(side_length=0.3)
            diagonal_highlight.move_to(digit_objects[(i, i)].get_center())
            diagonal_highlight.set_stroke(YELLOW, width=4)
            diagonal_highlight.set_fill(YELLOW, opacity=0.4)

            
            # Highlight the new digit being added
            new_digit_highlight = Square(side_length=0.25)
            new_digit_highlight.move_to(new_digit_objects[i].get_center())
            new_digit_highlight.set_stroke(YELLOW, width=3)
            new_digit_highlight.set_fill(YELLOW, opacity=0.3)
            
            self.play(
                Create(diagonal_highlight),
                Create(new_digit_highlight)
            )
            
            self.wait(0.3)
            
            # Fade out highlights and blue digit
            self.play(
                FadeOut(diagonal_highlight),
                FadeOut(new_digit_highlight),
                run_time=0.5
            )
        
        
        # Hold the final state for a moment
        self.wait(2)
        
        
        # Fade everything out
        all_objects = VGroup(
            grid_group, diagonal_squares, 
            diagonal_label, diagonal_number_grid,
            new_label, new_number_grid
        )
        self.play(FadeOut(all_objects))