from manim import *
import numpy as np

class BinaryTreeToRealLine(Scene):
    def construct(self):
        # Create the number line at the top
        number_line = NumberLine(
            x_range=[0, 1, 0.1],
            length=10,
            include_numbers=True,
            numbers_to_include=[0, 0.5, 1],
            font_size=24
        ).to_edge(UP, buff=1)
        
        # Display the number line
        self.play(Create(number_line))
        self.wait(1)
        
        # Define positions for the binary tree nodes
        # Level 0 (root): empty sequence
        root_pos = DOWN * 3.5
        
        # Level 1: <0>, <1>
        level1_positions = {
            "0": root_pos + UP * 0.7 + LEFT * 2.5,
            "1": root_pos + UP * 0.7 + RIGHT * 2.5
        }
        
        # Level 2: <0,0>, <0,1>, <1,0>, <1,1>
        level2_positions = {
            "00": level1_positions["0"] + UP * 0.7 + LEFT * 1.5,
            "01": level1_positions["0"] + UP * 0.7 + RIGHT * 1.5,
            "10": level1_positions["1"] + UP * 0.7 + LEFT * 1.5,
            "11": level1_positions["1"] + UP * 0.7 + RIGHT * 1.5
        }
        
        # Level 3: 8 nodes
        level3_positions = {}
        for seq2 in ["00", "01", "10", "11"]:
            level3_positions[seq2 + "0"] = level2_positions[seq2] + UP * 0.7 + LEFT * 0.8
            level3_positions[seq2 + "1"] = level2_positions[seq2] + UP * 0.7 + RIGHT * 0.8
        
        # Level 4: 16 nodes
        level4_positions = {}
        for seq3 in level3_positions.keys():
            level4_positions[seq3 + "0"] = level3_positions[seq3] + UP * 0.7 + LEFT * 0.5
            level4_positions[seq3 + "1"] = level3_positions[seq3] + UP * 0.7 + RIGHT * 0.5
        
        # Level 5: 32 nodes (new level)
        level5_positions = {}
        for seq4 in level4_positions.keys():
            level5_positions[seq4 + "0"] = level4_positions[seq4] + UP * 0.7 + LEFT * 0.25
            level5_positions[seq4 + "1"] = level4_positions[seq4] + UP * 0.7 + RIGHT * 0.25
        
        # Create nodes and edges
        nodes = {}
        edges = []
        
        # Root node
        root_circle = Circle(radius=0.08, color=WHITE, fill_opacity=1, fill_color=BLUE)
        root_circle.move_to(root_pos)
        root_text = MathTex(r"\langle \rangle", font_size=32, color=WHITE).next_to(root_circle, UP, buff=0.05)
        nodes[""] = VGroup(root_circle, root_text)
        
        # Level 1 nodes and edges
        for bit in ["0", "1"]:
            circle = Circle(radius=0.08, color=WHITE, fill_opacity=1, fill_color=GREEN)
            circle.move_to(level1_positions[bit])
            text = MathTex(rf"\langle {bit} \rangle", font_size=24, color=WHITE).next_to(circle, UP, buff=0.05)
            nodes[bit] = VGroup(circle, text)
            
            edge = Line(root_pos, level1_positions[bit], color=YELLOW, stroke_width=2)
            edges.append(edge)
        
        # Level 2 nodes and edges
        for seq in ["00", "01", "10", "11"]:
            parent = seq[0]
            circle = Circle(radius=0.08, color=WHITE, fill_opacity=1, fill_color=RED)
            circle.move_to(level2_positions[seq])
            text = MathTex(rf"\langle{seq[0]},{seq[1]}\rangle", font_size=24, color=WHITE).next_to(circle, UP, buff=0.05)
            nodes[seq] = VGroup(circle, text)
            
            edge = Line(level1_positions[parent], level2_positions[seq], color=YELLOW, stroke_width=2)
            edges.append(edge)
        
        # Level 3 nodes and edges
        for seq in level3_positions.keys():
            parent = seq[:-1]
            circle = Circle(radius=0.08, color=WHITE, fill_opacity=1, fill_color=ORANGE)
            circle.move_to(level3_positions[seq])
            text = MathTex(rf"\langle{','.join(seq)}\rangle", font_size=18, color=WHITE).next_to(circle, UP, buff=0.05)
            nodes[seq] = VGroup(circle, text)
            
            edge = Line(level2_positions[parent], level3_positions[seq], color=YELLOW, stroke_width=1.5)
            edges.append(edge)
        
        # Level 4 nodes and edges
        for seq in level4_positions.keys():
            parent = seq[:-1]
            circle = Circle(radius=0.08, color=WHITE, fill_opacity=1, fill_color=PURPLE)
            circle.move_to(level4_positions[seq])
            text = MathTex(rf"\langle{','.join(seq)}\rangle", font_size=12, color=WHITE).next_to(circle, UP, buff=0.05)
            nodes[seq] = VGroup(circle, text)
            
            edge = Line(level3_positions[parent], level4_positions[seq], color=YELLOW, stroke_width=1)
            edges.append(edge)
        
        # Level 5 nodes and edges (new level)
        for seq in level5_positions.keys():
            parent = seq[:-1]
            circle = Circle(radius=0.08, color=WHITE, fill_opacity=1, fill_color=PINK)
            circle.move_to(level5_positions[seq])
            # Very small text for level 5 to avoid clutter
            text = Text(rf"\langle{','.join(seq)}\rangle", font_size=4, color=WHITE).next_to(circle, UP, buff=0.05)
            nodes[seq] = VGroup(circle, text)
            
            edge = Line(level4_positions[parent], level5_positions[seq], color=YELLOW, stroke_width=0.8)
            edges.append(edge)
        
        # Root
        self.play(Create(nodes[""]))
        self.wait(0.5)
        
        # Level 1
        level1_anims = [Create(nodes[bit]) for bit in ["0", "1"]]
        edge1_anims = [Create(edge) for edge in edges[:2]]
        self.play(*level1_anims, *edge1_anims)
        self.wait(0.5)
        
        # Level 2
        level2_anims = [Create(nodes[seq]) for seq in ["00", "01", "10", "11"]]
        edge2_anims = [Create(edge) for edge in edges[2:6]]
        self.play(*level2_anims, *edge2_anims)
        self.wait(0.5)
        
        # Level 3
        level3_anims = [Create(nodes[seq]) for seq in level3_positions.keys()]
        edge3_anims = [Create(edge) for edge in edges[6:14]]
        self.play(*level3_anims, *edge3_anims)
        self.wait(0.25)
        
        # Level 4
        level4_anims = [Create(nodes[seq]) for seq in level4_positions.keys()]
        edge4_anims = [Create(edge) for edge in edges[14:30]]
        self.play(*level4_anims, *edge4_anims)
        self.wait(0.25)
        
        # Level 5 (new level)
        level5_anims = [Create(nodes[seq]) for seq in level5_positions.keys()]
        edge5_anims = [Create(edge) for edge in edges[30:]]
        self.play(*level5_anims, *edge5_anims)
        self.wait(0.25)
        
        # Add ellipses to suggest infinite continuation
        ellipses = Text("⋮", font_size=40).next_to(number_line, DOWN, buff=1.0)
        self.play(Write(ellipses))
        self.wait(1)
        
        # PATH FOR 0
        path_sequence = ["", "0", "00", "000", "0000", "00000"]
        path_edges = []
        
        # Highlight the chosen path
        for i in range(len(path_sequence) - 1):
            current = path_sequence[i]
            next_node = path_sequence[i + 1]
            
            if i == 0:  # Root to level 1
                start_pos = root_pos
                end_pos = level1_positions["0"]
            elif i == 1:  # Level 1 to level 2
                start_pos = level1_positions["0"]
                end_pos = level2_positions["00"]
            elif i == 2:  # Level 2 to level 3
                start_pos = level2_positions["00"]
                end_pos = level3_positions["000"]
            elif i == 3:  # Level 3 to level 4
                start_pos = level3_positions["000"]
                end_pos = level4_positions["0000"]
            elif i == 4:  # Level 4 to level 5
                start_pos = level4_positions["0000"]
                end_pos = level5_positions["00000"]
            
            path_edge = Line(start_pos, end_pos, color=RED, stroke_width=4)
            path_edges.append(path_edge)
        
        for edge in path_edges:
            self.play(Create(edge), run_time=0.5)
        
        # Continue the path upward to the number line
        final_path_edge = Line(
            level5_positions["00000"],
            number_line.number_to_point(0),  
            color=RED,
            stroke_width=4
        )
        self.play(Create(final_path_edge))
        self.wait(0.5)
        self.play(FadeOut(final_path_edge,path_edges[0],path_edges[1],path_edges[2],path_edges[3],path_edges[4])) 
        
        # Path for 1
        # Let's choose the path: root -> 0 -> 01 -> 010 -> 0101 -> 01010
        path_sequence = ["", "1", "11", "111", "1111", "11111"]
        path_edges = []
        
        # Highlight the chosen path
        for i in range(len(path_sequence) - 1):
            current = path_sequence[i]
            next_node = path_sequence[i + 1]
            
            if i == 0:  # Root to level 1
                start_pos = root_pos
                end_pos = level1_positions["1"]
            elif i == 1:  # Level 1 to level 2
                start_pos = level1_positions["1"]
                end_pos = level2_positions["11"]
            elif i == 2:  # Level 2 to level 3
                start_pos = level2_positions["11"]
                end_pos = level3_positions["111"]
            elif i == 3:  # Level 3 to level 4
                start_pos = level3_positions["111"]
                end_pos = level4_positions["1111"]
            elif i == 4:  # Level 4 to level 5
                start_pos = level4_positions["1111"]
                end_pos = level5_positions["11111"]
            
            path_edge = Line(start_pos, end_pos, color=RED, stroke_width=4)
            path_edges.append(path_edge)
        
        for edge in path_edges:
            self.play(Create(edge), run_time=0.5)
        
        # Continue the path upward to the number line
        final_path_edge = Line(
            level5_positions["11111"],
            number_line.number_to_point(1),
            color=RED,
            stroke_width=4
        )
        self.play(Create(final_path_edge))
        self.wait(1)
        self.play(FadeOut(final_path_edge,path_edges[0],path_edges[1],path_edges[2],path_edges[3],path_edges[4])) 
        
        # Now draw an arbitrary path from root to show correspondence
        # Let's choose the path: root -> 0 -> 01 -> 010 -> 0101 -> 01010
        path_sequence = ["", "0", "01", "010", "0101", "01010"]
        path_edges = []
        
        # Highlight the chosen path
        for i in range(len(path_sequence) - 1):
            current = path_sequence[i]
            next_node = path_sequence[i + 1]
            
            if i == 0:  # Root to level 1
                start_pos = root_pos
                end_pos = level1_positions["0"]
            elif i == 1:  # Level 1 to level 2
                start_pos = level1_positions["0"]
                end_pos = level2_positions["01"]
            elif i == 2:  # Level 2 to level 3
                start_pos = level2_positions["01"]
                end_pos = level3_positions["010"]
            elif i == 3:  # Level 3 to level 4
                start_pos = level3_positions["010"]
                end_pos = level4_positions["0101"]
            elif i == 4:  # Level 4 to level 5
                start_pos = level4_positions["0101"]
                end_pos = level5_positions["01010"]
            
            path_edge = Line(start_pos, end_pos, color=RED, stroke_width=4)
            path_edges.append(path_edge)
        
        for edge in path_edges:
            self.play(Create(edge), run_time=0.5)
        
        # Continue the path upward to the number line
        final_path_edge = Line(
            level5_positions["01010"],
            number_line.number_to_point(0.3333),  # Binary 0.010101... ≈ 1/3
            color=RED,
            stroke_width=4
        )
        
        # Mark the corresponding point on the number line
        # Binary 0.010101... = 1/3
        real_value = 1/3  # Approximate value for 0.010101...
        point_on_line = Dot(number_line.number_to_point(real_value), color=RED, radius=0.08)
        self.play(Create(final_path_edge), Create(point_on_line))
        self.wait(2)
        # Fade everything for a clean ending
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)