from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
import numpy as np
import random
import math

# --- COMMON CONFIG ---
# Font for "Old Fashioned" look
SERIF_FONT = "Calibri"

# 1. Define the specific cluster of Omega-Stable Theories
OMEGA_STABLE_THEORIES = [
    "ACF", "Infinite Sets", "Q-Vector Spaces", "Z with Successor",
    "Everywhere Infinite Forest(Free Pseudoplane)", "Farey Graph",
    r"((Z/4Z)$^\omega$, +)", "DCF_0"
]

# 2. Define the background theories
OTHER_THEORIES = [
    "Random Graph", "Manifolds", "Hilbert Spaces", "Graphs", "Trees",
    "Topologies", "Groups", "Categories", "Rings", "K-Theory",
    "Atomless Boolean Algebras", "Complete Lattices", "ZFC",
    "Model Theory", "Set Theory", "Banach Spaces", "Lie Algebras",
    "Matroids", "Turing Machines", "Neural Networks", 
    "Knots", "Surfaces", "Peano Arithmetic", "DLOWE", "lattices", "pre-orders","partial orders"
]

#############################################################################
# SCENE 1: THE INFINITE WEB (Intro)
#############################################################################
class Part1_Intro(VoiceoverScene, ThreeDScene):
    def construct(self):
        # 1. Voiceover Setup
        self.set_speech_service(RecorderService(transcription_model=None))

        # 2. Camera Setup (Fixed, wide view)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.renderer.camera.frame_center = np.array([0, 0, 0])
        self.move_camera(zoom=0.6) # Zoom out to see the whole universe

        # --- OBJECT GENERATION ---
        
        # A. THE KLEIN BOTTLE (Manifolds) - Top Left
        # Using a parametric surface to generate the "Bottle" immersion
        klein_bottle = self.get_klein_bottle()
        klein_bottle.scale(1.5).move_to(np.array([-5, 3, 2]))
        klein_bottle.rotate(PI/2, axis=RIGHT)

        # B. THE FAREY GRAPH (Hyperbolic Geometry) - Top Right
        # Approximated by a Poincare Disk tessellation style
        farey_graph = self.get_farey_graph(radius=2, depth=3)
        farey_graph.move_to(np.array([5, 3, -1]))
        farey_graph.rotate(PI/4, axis=UP)

        # C. RANDOM GRAPH (Complex Cyclic) - Bottom Right
        # A circular layout with dense connections
        random_graph = self.get_complex_graph(n_nodes=12)
        random_graph.move_to(np.array([4, -3, 1]))

        # D. TREE (Arbitrary Branching) - Bottom Left
        # A recursive fractal tree structure
        tree_struct = self.get_fractal_tree(iterations=4)
        tree_struct.move_to(np.array([-4, -3, -1]))
        
        # E. DLO (Dense Linear Order / Rationals) - Center Back
        # A dense, glowing number line
        dlo_line = self.get_dlo_visualization()
        dlo_line.move_to(np.array([0, 2, -4]))
        dlo_line.rotate(PI/6, axis=RIGHT)

        # F. ACF_p (Algebraic Closed Field / Complex Plane) - Center Bottom
        # A plane of scattered "algebraic" points
        acf_plane = self.get_acf_plane()
        acf_plane.move_to(np.array([0, -2, -3]))
        acf_plane.rotate(PI/3, axis=RIGHT)

        # --- ANIMATION ---
        
        # Add all objects to the scene
        # We fade them in to look like they are emerging from the void
        self.play(
            FadeIn(klein_bottle),
            FadeIn(farey_graph),
            FadeIn(random_graph),
            FadeIn(tree_struct),
            FadeIn(dlo_line),
            FadeIn(acf_plane),
            run_time=3
        )

        # Voiceover with slight ambient rotation to show depth
        text_intro = (
            "What is the mathematical Universe? What are the objects which exist in it? "
            "And which do not? To answer these questions, we will first have to understand "
            "the basics of mathematical logic."
        )

        with self.voiceover(text=text_intro) as tracker:
            # Subtle rotation to make the universe feel alive (floating)
            self.begin_ambient_camera_rotation(rate=0.05) 
            self.wait(tracker.duration)
            self.stop_ambient_camera_rotation()

        self.wait(2)

    # --- HELPER FUNCTIONS ---

    def get_klein_bottle(self):
        """Generates a parametric surface representing a Klein Bottle."""
        # Using a simplified 'Figure-8' immersion for visual clarity in Manim
        def func(u, v):
            u = u * PI # Map [0, 1] to [0, PI] if needed, standardizing range
            v = v * TAU
            
            # Parametric equations
            r = 1.0 # Radius constant
            # Standard Figure-8 Klein Bottle
            x = (r + np.cos(u/2) * np.sin(v) - np.sin(u/2) * np.sin(2*v)) * np.cos(u)
            y = (r + np.cos(u/2) * np.sin(v) - np.sin(u/2) * np.sin(2*v)) * np.sin(u)
            z = np.sin(u/2) * np.sin(v) + np.cos(u/2) * np.sin(2*v)
            return np.array([x, y, z])

        surface = Surface(
            lambda u, v: func(u, v),
            u_range=[0, TAU],
            v_range=[0, TAU],
            resolution=(24, 24),
            should_make_jagged=False
        )
        surface.set_style(fill_opacity=0.3, stroke_color=GREEN, stroke_width=0.5)
        surface.set_fill_by_checkerboard(GREEN_E, GREEN_C, opacity=0.2)
        return surface

    def get_farey_graph(self, radius=2, depth=3):
        """Generates a visual approximation of a hyperbolic Farey graph."""
        farey_group = VGroup()
        
        # Boundary Circle
        boundary = Circle(radius=radius, color=WHITE, stroke_opacity=0.5)
        farey_group.add(boundary)

        # Recursive function to draw geodesic arcs
        def add_arcs(a, b, level):
            if level == 0:
                return
            
            # Midpoint in angle space
            mid = (a + b) / 2
            
            # Convert angles to points on circle
            p1 = np.array([radius * np.cos(a), radius * np.sin(a), 0])
            p2 = np.array([radius * np.cos(b), radius * np.sin(b), 0])
            
            # Draw Arc (Orthogonal to boundary - simplified as straight lines or slight curves for aesthetic)
            # For true hyperbolic geodesics, we use arcs. Here we use Bezier for style.
            arc = ArcBetweenPoints(p1, p2, angle=-PI/2) # Negative angle pushes it inward
            arc.set_stroke(color=BLUE_A, width=2 * (level/depth), opacity=0.8)
            farey_group.add(arc)
            
            # Recurse
            add_arcs(a, mid, level - 1)
            add_arcs(mid, b, level - 1)

        # Start with a few main sectors
        sectors = [0, PI/2, PI, 3*PI/2, 2*PI]
        for i in range(len(sectors)-1):
            add_arcs(sectors[i], sectors[i+1], depth)
            
        return farey_group

    def get_complex_graph(self, n_nodes=10):
        """Generates a complete-like cyclic graph."""
        # Manually creating nodes and edges for 3D compatibility
        g_group = VGroup()
        nodes = []
        radius = 1.5
        
        # Create Nodes
        for i in range(n_nodes):
            angle = i * (TAU / n_nodes)
            pos = np.array([radius * np.cos(angle), radius * np.sin(angle), 0])
            dot = Dot3D(point=pos, radius=0.08, color=TEAL)
            nodes.append(dot)
            g_group.add(dot)
        
        # Create Edges (connect to neighbors and some random across)
        for i in range(n_nodes):
            # Connect to immediate neighbor
            line = Line(nodes[i].get_center(), nodes[(i+1)%n_nodes].get_center(), color=TEAL_E, stroke_width=2)
            g_group.add(line)
            
            # Connect to random other nodes
            others = random.sample(range(n_nodes), 2)
            for o in others:
                if o != i:
                    line = Line(nodes[i].get_center(), nodes[o].get_center(), color=TEAL_A, stroke_width=1, stroke_opacity=0.5)
                    g_group.add(line)
                    
        return g_group

    def get_fractal_tree(self, iterations=4):
        """Generates a 3D branching tree."""
        tree_group = VGroup()
        
        def branch(start_pos, length, angle, theta_offset, depth):
            if depth == 0:
                return
            
            # Calculate end position (simplified 2D logic rotated in 3D)
            end_pos = start_pos + np.array([
                length * np.cos(angle),
                length * np.sin(angle),
                length * np.sin(angle + theta_offset) # Add Z variation
            ])
            
            line = Line3D(start=start_pos, end=end_pos, color=interpolate_color(ORANGE, WHITE, depth/iterations))
            line.set_stroke(width=depth)
            tree_group.add(line)
            
            # Recurse
            branch(end_pos, length * 0.7, angle + PI/6, theta_offset + 0.5, depth - 1)
            branch(end_pos, length * 0.7, angle - PI/6, theta_offset - 0.5, depth - 1)

        branch(np.array([0, -1.5, 0]), 1.0, PI/2, 0, iterations)
        return tree_group

    def get_dlo_visualization(self):
        """Generates a dense linear order (like Rationals) visualization."""
        dlo = VGroup()
        line = Line(start=LEFT*3, end=RIGHT*3, color=BLUE)
        dlo.add(line)
        
        # Add "dense" ticks
        for _ in range(50):
            x = random.uniform(-3, 3)
            tick = Line(start=UP*0.1, end=DOWN*0.1, color=BLUE_A).move_to(np.array([x, 0, 0]))
            dlo.add(tick)
            
        return dlo

    def get_acf_plane(self):
        """Generates a complex plane visualization (ACF)."""
        acf = VGroup()
        # Grid
        grid = NumberPlane(
            x_range=(-3, 3, 1), 
            y_range=(-3, 3, 1), 
            background_line_style={"stroke_color": PURPLE, "stroke_width": 1, "stroke_opacity": 0.5}
        )
        acf.add(grid)
        
        # Algebraic points (random scatter)
        for _ in range(30):
            x = random.uniform(-3, 3)
            y = random.uniform(-3, 3)
            dot = Dot3D(point=np.array([x, y, 0]), radius=0.05, color=PURPLE_A)
            acf.add(dot)
            
        return acf


#############################################################################
# SCENE 2: SYMBOLS & RESTRICTIONS
#############################################################################
class Part2_Symbols(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # Title with Serif Font
        title = Text("The Symbols of First Order Logic", font=SERIF_FONT, font_size=40).to_edge(UP) #TODO: MAKE THE FONT MORE OLD-SCHOOL
        self.play(FadeIn(title))

        # Split headers
        header_logical = Text("Logical Symbols", font=SERIF_FONT, color=YELLOW, font_size=32).move_to(UP*2 + LEFT*3.5)
        header_nonlogical = Text("Non-Logical Symbols", font=SERIF_FONT, color=BLUE, font_size=32).move_to(UP*2 + RIGHT*3.5)
        
        
        # Intro text
        with self.voiceover(text="It was Frege in the 19th century, who first realized that mathematics involved manipulations involving a specific set of symbols."):
            self.play(FadeIn(header_logical), FadeIn(header_nonlogical))
        
        # --- 1. Populate Lists ---
        # Logical
        sym_bool = MathTex(r"\land, \lor, \rightarrow, \neg").scale(1).next_to(header_logical, DOWN, buff=0.8)
        sym_quant = MathTex(r"\exists, \forall").scale(1).next_to(sym_bool, DOWN, buff=0.5)
        sym_vars = MathTex(r"x_0, x_1, x_2, \dots").scale(1).next_to(sym_quant, DOWN, buff=0.5)
        sym_aux = MathTex(r"),(").scale(1).next_to(sym_vars, DOWN, buff=0.5)
        # Non-Logical
        sym_const = MathTex(r"c_0, c_1, \dots").scale(1).next_to(header_nonlogical, DOWN, buff=0.8)
        sym_func = MathTex(r"F_0, F_1, \dots").scale(1).next_to(sym_const, DOWN, buff=0.5)
        sym_rel = MathTex(r"R_0, R_1, \dots").scale(1).next_to(sym_func, DOWN, buff=0.5)
        
        grp_logical = VGroup(sym_bool, sym_quant, sym_vars, sym_aux)
        grp_nonlogical = VGroup(sym_const, sym_func, sym_rel)

        # Listing them
        with self.voiceover(text="These included the logical symbols such as the boolean connectives: conjunction, disjunction, implication and negation:") as tracker:
            self.play(Write(sym_bool), run_time=tracker.duration/2) #TODO: MAKE A 2x2 matrix defining the boolean connectives
        with self.voiceover(text="The quantifiers forall and exists") as tracker:
            self.play(Write(sym_quant), run_time=tracker.duration/2)
        with self.voiceover(text="The variables") as tracker:
            self.play(Write(sym_vars), run_time=tracker.duration/2)
        with self.voiceover(text="And finally brackets") as tracker:
            self.play(Write(sym_aux), run_time=tracker.duration/2)
            
        with self.voiceover(text="The non-logical symbols include the constants, function symbols and relation symbols:") as tracker:
            self.play(Write(grp_nonlogical), run_time=tracker.duration/2)
        
        # --- 2. Focus on Logic ---
        with self.voiceover(text="The reason for the distinction, is that the non-logical symbols are specific to a given theory. So, if we just restrict our attention to the logical symbols, we are in the domain of logic, since whatever we prove holds in all possible theories.") as tracker:
            self.play(
                FadeOut(grp_nonlogical),
                FadeOut(header_nonlogical),
                #grp_logical.animate.move_to(ORIGIN),
                #header_logical.animate.move_to(UP*2),
                run_time=2
            )
        header_alphabet = Text("Propositional Alphabet", font=SERIF_FONT, color=YELLOW, font_size=32).move_to(UP*2 + LEFT*3.5)
        # --- 3. Restrict to Propositional (Remove Quantifiers) ---
        with self.voiceover(text="Now, if we restrict ourselves further, omitting the quantifiers, then we are in the domain of Propositional logic, also known as 0th order logic.") as tracker:
            # Fade out Quantifiers
            self.play(
                sym_quant.animate.set_opacity(0.1),
                Transform(header_logical, header_alphabet),
                run_time=2
            )

        # --- 4. Restrict to Minimal Set (Negation and Implication) ---
        # "prove that if we only use implies and neg..."
        with self.voiceover(text="In fact we can prove that if we only use implies and negation we don't lose any expressive power.") as tracker:
            # Fade out vars and the other booleans (\land, \lor)
            # Create a new MathTex for just \implies and \neg to highlight them
            minimal_syms = MathTex(r"\rightarrow, \neg", color=YELLOW).move_to(sym_bool.get_center())
            minimal_vars = MathTex(r"p, p, r\ldots", color =YELLOW).next_to(minimal_syms, DOWN, buff=0.5)
            minimal_aux = MathTex(r"),(", color =YELLOW).next_to(minimal_vars, DOWN, buff=0.5)
            self.play(
                Transform(sym_vars, minimal_vars), Transform(sym_aux, minimal_aux),
                FadeIn(minimal_aux),
                run_time=2
            )

        self.wait(1)
        
        # --- 1. The Propositional Sentence ---
        # Sentence: (phi -> psi) -> (neg psi -> neg phi)
        sentence = MathTex(r"\varphi = p \rightarrow q) \rightarrow (\neg q \rightarrow \neg p)").next_to(header_alphabet, RIGHT, buff=1.5)

        with self.voiceover(text="Here we can write down a propositional sentence phi by combining propositional variables according to the connectives.") as tracker:
            self.play(Write(sentence), run_time=tracker.duration/3)

        # --- 2. Truth Table Validation ---
        
        # Header
        headers = [r"p", r"q", r"p\to q", r"\neg q \to \neg p", r"\varphi"]
        
        t_vals = [
            ["0", "0", "1", "1", "1"],
            ["0", "1", "1", "1", "1"],
            ["1", "0", "0", "0", "1"],
            ["1", "1", "1", "1", "1"],
        ]
        
        table = Table(
            t_vals,
            col_labels=[MathTex(h) for h in headers],
            include_outer_lines=True
        ).scale(0.6).next_to(sentence, DOWN, buff=0.5)

        with self.voiceover(text="In classical logic, to check if phi is true, we can simply create the truth table and check if there is a satisfying assignment, that is, a row where our formulas are 1.") as tracker:
            self.play(Create(table), run_time=tracker.duration)
            # Highlight a satisfying row (e.g., Row 1)
            self.play(Indicate(table.get_rows()[1], color=GREEN))

        with self.voiceover(text="We can check if it is valid, by checking if all of the rows evaluate to 1. This truth table can be seen as a model in which this sentence holds.") as tracker:
            # Highlight the 'Whole' column showing all 1s
            col_cells = table.get_col_labels()[-1] # The label "Whole"
            # Get the actual cells in the last column (excluding header)
            last_col = VGroup(*[table.get_cell((i, 5)) for i in range(2, 6)]) 
            self.play(Indicate(last_col, color=YELLOW, scale_factor=1.2))

        self.play(FadeOut(table), FadeOut(sentence))

        # --- 3. The Truth Matrix (Implication) ---
        # "In classical logic, this truth assignment is black and white"
        # Show the 2x2 matrix for Implication
        #     0  1
        # 0 [ 1  1 ]
        # 1 [ 0  1 ]
        
        matrix_2x2 = IntegerTable(
            [[1, 1], [0, 1]],
            col_labels=[MathTex("0"), MathTex("1")],
            row_labels=[MathTex("0"), MathTex("1")],
            include_outer_lines=True
        ).scale(0.7)
        matrix_label = Text("Classical (2-Valued)", font=SERIF_FONT, font_size=24).next_to(matrix_2x2, UP)

        with self.voiceover(text="In classical logic, this truth assignment is black and white. Display the truth table for phi implies psi, a 2 by 2 matrix with 1s and 0s.") as tracker:
            self.play(FadeIn(matrix_2x2), Write(matrix_label))

        # --- 4. Many-Valued Logic ---
        # "Generalize to create a many-valued logic... stretched over an arbitrary number"
        # 3x3 Matrix
        matrix_3x3 = DecimalTable(
            [[1.0, 1.0, 1.0], [0.5, 1.0, 1.0], [0.0, 0.5, 1.0]], # Lukasiewicz implication approx
            col_labels=[MathTex("0"), MathTex(".5"), MathTex("1")],
            row_labels=[MathTex("0"), MathTex(".5"), MathTex("1")],
            include_outer_lines=True
        ).scale(0.6)
        matrix_3x3_label = Text("Many-Valued (3-Valued)", font=SERIF_FONT, font_size=24).next_to(matrix_3x3, UP)

        with self.voiceover(text="We can generalize to create a many-valued logic, where the concept of truth is stretched out over an arbitrary number. Extend the matrix one box at a time.") as tracker:
            self.play(
                ReplacementTransform(matrix_2x2, matrix_3x3),
                ReplacementTransform(matrix_label, matrix_3x3_label),
                run_time=2
            )
        spectrum = Square(side_length=3)
        spectrum.set_fill(color=[BLACK, WHITE], opacity=1) # Simple gradient approximation
        spectrum = Rectangle(height=3, width=3)
        spectrum.set_fill(color=BLUE, opacity=1)
        # Manim's sheen support is limited in basic shapes, let's use a group of lines to simulate gradient
        gradient_group = VGroup()
        for i in range(100):
            alpha = i/100.0
            line = Line(start=np.array([-1.5 + 3*alpha, -1.5, 0]), end=np.array([-1.5 + 3*alpha, 1.5, 0]))
            # Color goes from Black (0) to White (1)
            col = interpolate_color(BLACK, WHITE, alpha)
            line.set_color(col)
            line.set_stroke(width=4)
            gradient_group.add(line)
        
        spectrum_label = Text("Infinite Valued ([0, 1])", font=SERIF_FONT, font_size=24).next_to(gradient_group, UP)

        with self.voiceover(text="It can even be a real number between 0 and 1. Now make there be an open interval and display something resembling a color selection window.") as tracker:
            self.play(
                FadeOut(matrix_3x3),
                FadeOut(matrix_3x3_label),
                FadeIn(gradient_group),
                Write(spectrum_label),
                run_time=2
            )

        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))
