from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
import random

class Diagonal(VoiceoverScene):
    def construct(self):
        # Setup voiceover service
        self.set_speech_service(RecorderService(transcription_model=None))

        # --- SETUP GRID DATA ---
        num_rows = 10
        num_cols = 10
        
        # Generate random binary strings for each row
        random.seed(42)  # For reproducible results
        binary_strings = []
        for i in range(num_rows):
            string = [random.choice([0, 1]) for _ in range(num_cols)]
            binary_strings.append(string)
        
        # Create the grid components
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

        # --- PART 1: INTRODUCTION & GRID CREATION ---
        with self.voiceover(text="Suppose towards a contradiction that there is a bijection from the naturals to the set of reals, which we represent as all infinite binary strings.") as tracker:
            self.play(Write(nat_label), Write(real_label), Write(nat_numbers))
            self.play(Create(arrow))
            
            for i in range(num_rows):
                self.play(Write(binary_grid[i]), run_time=0.15)
            self.play(Write(bottom_ellipses), run_time=0.5)

        # --- PART 2: HIGHLIGHTING THE DIAGONAL ---
        # Prepare diagonal objects
        diagonal_squares = VGroup()
        diagonal_digits = []
        for i in range(min(num_rows, num_cols)):
            square = Square(side_length=0.3)
            square.move_to(digit_objects[(i, i)].get_center())
            square.set_stroke(RED, width=3)
            square.set_fill(RED, opacity=0.2)
            diagonal_squares.add(square)
            diagonal_digits.append(binary_strings[i][i])
        
        diagonal_grid_pos = RIGHT * 2 + UP * 2
        diagonal_label = Text("D:", font_size=24, color=RED)
        diagonal_label.move_to(diagonal_grid_pos + LEFT * 0.6).shift(RIGHT*0.3)
        
        diagonal_number_grid = VGroup()
        for i, digit in enumerate(diagonal_digits):
            digit_text = Text(str(digit), font_size=24, color=RED)
            digit_text.move_to(diagonal_grid_pos + RIGHT * i * 0.3)
            diagonal_number_grid.add(digit_text)
        
        diagonal_ellipsis = Text("...", font_size=24, color=RED)
        diagonal_ellipsis.move_to(diagonal_grid_pos + RIGHT * len(diagonal_digits) * 0.3)
        diagonal_number_grid.add(diagonal_ellipsis)

        with self.voiceover(text="Next we will focus on the diagonal, which is just another infinite string of 0's and 1's, and therefore another real number, which we call D.") as tracker:
            self.play(
                Create(diagonal_squares), 
                Write(diagonal_label),
                Write(diagonal_number_grid), 
                run_time=tracker.duration *0.6
            )

        # --- PART 3: CREATING D* ---
        new_grid_pos = diagonal_grid_pos + DOWN * 0.8
        # Changed label to D^* to match the voiceover script instead of "N:"
        new_label = MathTex(r"D^*:", font_size=28, color=BLUE)
        new_label.move_to(new_grid_pos + LEFT * 0.6).shift(RIGHT*0.3)
        
        new_number_grid = VGroup()
        new_digit_objects = {}
        for i in range(len(diagonal_digits)):
            digit_text = Text("", font_size=24, color=BLUE) 
            digit_text.move_to(new_grid_pos + RIGHT * i * 0.3)
            new_number_grid.add(digit_text)
            new_digit_objects[i] = digit_text

        with self.voiceover(text="We can use this number to define a new number D star, which is just the opposite of D, meaning if there is a 0 we put a 1, and if there's a 1 we put a 0. So, we obtain a new infinite string of 0's and 1's,") as tracker:
            self.play(Write(new_label), Write(new_number_grid))
            
            # Sequential highlighting to display new number
            for i in range(min(len(diagonal_digits), num_rows)):
                diagonal_crossout = Line(0 * RIGHT, 0.3 * RIGHT)
                diagonal_crossout.move_to(digit_objects[(i, i)].get_center())
                diagonal_crossout.set_stroke(YELLOW)
                diagonal_crossout.rotate(45 * DEGREES)            
                
                flipped_digit = 1 - diagonal_digits[i]
                blue_digit = Text(str(flipped_digit), font_size=20, color=BLUE)
                blue_digit.move_to(digit_objects[(i, i)].get_center() + RIGHT * 0.2 + UP * 0.2)
                
                new_digit_objects[i].become(Text(str(flipped_digit), font_size=24, color=BLUE))
                new_digit_objects[i].move_to(new_grid_pos + RIGHT * i * 0.3)
                
                self.play(
                    Create(diagonal_crossout),
                    Write(blue_digit),
                    Write(new_digit_objects[i]),
                    run_time=0.75
                )
                self.play(
                    FadeOut(diagonal_crossout),
                    FadeOut(blue_digit),
                    run_time=0.25
                )
            
            new_ellipsis = Text("...", font_size=24, color=BLUE)
            new_ellipsis.move_to(new_grid_pos + RIGHT * len(diagonal_digits) * 0.3)
            self.play(Write(new_ellipsis))

        # --- PART 4: THE CONTRADICTION ---
        with self.voiceover(text="so by our assumption that our map was 1 to 1, this new real D star should exist somewhere in our list. But we know that it cannot be the first element in the list, since D^* differs from this real on teh first coordinate") as tracker:
            self.wait(tracker.duration *0.5)
        
            diagonal_highlight = Square(side_length=0.3)
            diagonal_highlight.move_to(digit_objects[(0, 0)].get_center())
            diagonal_highlight.set_stroke(YELLOW, width=4)
            diagonal_highlight.set_fill(YELLOW, opacity=0.4)

            new_digit_highlight = Square(side_length=0.25)
            new_digit_highlight.move_to(new_digit_objects[0].get_center())
            new_digit_highlight.set_stroke(YELLOW, width=3)
            new_digit_highlight.set_fill(YELLOW, opacity=0.3)
                
            self.play(Create(diagonal_highlight), Create(new_digit_highlight), run_time=2)
            self.wait(1.5)
            self.play(FadeOut(diagonal_highlight), FadeOut(new_digit_highlight), run_time=1)

        with self.voiceover(text = "But it also cannot be the second element, since it differs on the second coordinate.") as tracker:
            diagonal_highlight = Square(side_length=0.3)
            diagonal_highlight.move_to(digit_objects[(1, 1)].get_center())
            diagonal_highlight.set_stroke(YELLOW, width=4)
            diagonal_highlight.set_fill(YELLOW, opacity=0.4)

            new_digit_highlight = Square(side_length=0.25)
            new_digit_highlight.move_to(new_digit_objects[1].get_center())
            new_digit_highlight.set_stroke(YELLOW, width=3)
            new_digit_highlight.set_fill(YELLOW, opacity=0.3)
                
            self.play(Create(diagonal_highlight), Create(new_digit_highlight), run_time=2)
            self.wait()
            self.play(FadeOut(diagonal_highlight), FadeOut(new_digit_highlight), run_time=1)  
            
        with self.voiceover(text = "It can't be the 7'th element, since it differs on the 7'th coordinate.  And so, it cannot be equal to any of the elements in our list") as tracker:
            diagonal_highlight = Square(side_length=0.3)
            diagonal_highlight.move_to(digit_objects[(6, 6)].get_center())
            diagonal_highlight.set_stroke(YELLOW, width=4)
            diagonal_highlight.set_fill(YELLOW, opacity=0.4)
    
            new_digit_highlight = Square(side_length=0.25)
            new_digit_highlight.move_to(new_digit_objects[6].get_center())
            new_digit_highlight.set_stroke(YELLOW, width=3)
            new_digit_highlight.set_fill(YELLOW, opacity=0.3)
                    
            self.play(Create(diagonal_highlight), Create(new_digit_highlight), run_time=2)
            self.wait()
            self.play(FadeOut(diagonal_highlight), FadeOut(new_digit_highlight), run_time=1)               
        # --- PART 5: CONCLUSION ---
        with self.voiceover(text="But this contradicts our assumption that all real numbers would appear somewhere in our list.") as tracker:
            self.wait(tracker.duration * 0.8)
            
            all_objects = VGroup(
                grid_group, diagonal_squares, 
                diagonal_label, diagonal_number_grid,
                new_label, new_number_grid, new_ellipsis
            )
            self.play(FadeOut(all_objects))
            
        text_pt1 = "This argument may not convince you, in fact many mathematicians at the time did not accept such arguments. But note that there are multiple ways of proving this, and in fact this argument was not Cantor's original one. And in some sense, continuous sets do clearly have different properties from discrete ones, so it makes sense that"
        
        with self.voiceover(text=text_pt1) as tracker:
            self.wait(tracker.duration)

        text_pt2 = "omega, which is the limit of some discrete operation, is smaller than the continuum"
        with self.voiceover(text=text_pt2) as tracker:
            # Discrete Sequence
            discrete_seq = MathTex(r"0, 1, 2, 3, 4, 5, \dots, \omega", font_size=36)
            discrete_seq.move_to(LEFT * 3)
            
            # Continuum Line (Gradient)
            continuum_line = Line(LEFT * 2, RIGHT * 2, stroke_width=6)
            continuum_line.set_color(color=[BLUE, PURPLE, RED, ORANGE])
            continuum_line.move_to(RIGHT * 3)
            continuum_label = Text("Continuum", font_size=24).next_to(continuum_line, DOWN)
            
            less_than = MathTex("<", font_size=48).move_to(ORIGIN)

            self.play(Write(discrete_seq), run_time=1)
            self.play(Write(less_than), Create(continuum_line), Write(continuum_label), run_time=1)
            self.wait(tracker.duration - 2)
        with self.voiceover(text="However, once we accept this fact that some infinities are larger then others, we enter a bit of a slippery slope, where we suddenly have to accept infinitely many increasing infinities.") as tracker:
            self.wait(tracker.duration - 1)

        with self.voiceover(text="This follows from Cantor's theorem, which states that given any set X, the size of the power set is strictly larger than the size of X.") as tracker:
            # Displaying the hierarchy of power sets
            self.play(FadeOut(discrete_seq, less_than, continuum_line, continuum_label))
            hierarchy = MathTex(r" |\omega|< |\mathcal{P}(\omega)|<|\mathcal{P}(\mathcal{P}(\omega))|<\dots\}", font_size=42)
            self.play(Write(hierarchy))
            self.wait(tracker.duration - 1)
            
        self.play(FadeOut(hierarchy))