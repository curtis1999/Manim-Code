from manim import *

# ---------------------------------------------------------
# Scene 1: Zeno's Paradox (The Dichotomy)
# Visualizes the infinite subdivision of a path.
# ---------------------------------------------------------
class P1_Zeno_Dichotomy(Scene):
    def construct(self):
        # Title
        title = Text("Zeno's Paradox: The Dichotomy", font_size=40)
        title.to_edge(UP)
        self.play(Write(title), run_time=2)
        
        # Setup Path A to B
        line = NumberLine(x_range=[0, 10, 1], length=10, color=BLUE, include_numbers=False)
        label_a = Text("A", font_size=24).next_to(line.get_start(), DOWN)
        label_b = Text("B", font_size=24).next_to(line.get_end(), DOWN)
        
        self.play(Create(line), Write(label_a), Write(label_b), run_time=2)
        
        # The Runner
        dot = Dot(color=YELLOW).move_to(line.get_start())
        self.add(dot)
        
        # Iteration 1: Halfway
        halfway = line.number_to_point(5)
        brace1 = Brace(Line(line.get_start(), halfway), UP)
        t1 = brace1.get_text("1/2")
        
        self.play(dot.animate.move_to(halfway), FadeIn(brace1), Write(t1), run_time=3)
        self.wait(1)
        
        # Iteration 2: Halfway to B (3/4)
        three_quarter = line.number_to_point(7.5)
        brace2 = Brace(Line(halfway, three_quarter), UP)
        t2 = brace2.get_text("1/4")
        
        self.play(dot.animate.move_to(three_quarter), FadeIn(brace2), Write(t2), run_time=3)
        self.wait(1)
        
        # Iteration 3: Halfway again (7/8)
        seven_eighth = line.number_to_point(8.75)
        brace3 = Brace(Line(three_quarter, seven_eighth), UP)
        t3 = brace3.get_text("1/8")
        
        self.play(dot.animate.move_to(seven_eighth), FadeIn(brace3), Write(t3), run_time=2)
        
        # Rapid iterations indicating infinity
        remaining = 1.25
        for _ in range(4):
            remaining /= 2
            new_pos = line.get_end() - np.array([remaining * (10/10), 0, 0]) # approximate scaling
            self.play(dot.animate.move_to(new_pos), run_time=0.3)
            
        dots = Text("...", font_size=40).next_to(dot, UP)
        self.play(Write(dots))
        
        # Conclusion Text
        impossible = Text("Motion = Impossible?", color=RED, font_size=36).to_edge(DOWN)
        self.play(Write(impossible))
        self.wait(5)


# ---------------------------------------------------------
# Scene 2: Aristotelian Potential Infinity
# Visualizes counting that never ends but is never "finished".
# ---------------------------------------------------------
class P2_Aristotle_Potential(Scene):
    def construct(self):
        # Aristotle Profile
        aristotle = Text("Aristotle", font_size=48).to_edge(UP)
        self.play(Write(aristotle))
        
        # The concept
        concept = Text("Potential Infinity vs. Actual Infinity", font_size=30, color=GREY_B).next_to(aristotle, DOWN)
        self.play(FadeIn(concept))
        
        # The Number Line expanding
        number_line = NumberLine(x_range=[0, 6, 1], length=6, include_numbers=True).shift(DOWN * 0.5)
        self.play(Create(number_line))
        
        # Arrows showing potential
        arrow = Arrow(start=number_line.get_right(), end=number_line.get_right() + RIGHT*2, buff=0.1)
        inf_text = MathTex(r"\infty").next_to(arrow, RIGHT)
        
        self.play(GrowArrow(arrow), run_time=2)
        
        # The halting barrier (Physical World)
        barrier = Line(UP, DOWN, color=RED, stroke_width=5).move_to(RIGHT * 2)
        barrier_label = Text("Physical Intuition", color=RED, font_size=24).next_to(barrier, UP)
        
        self.play(Create(barrier), Write(barrier_label), run_time=2)
        
        # Attempt to cross
        cross_attempt = arrow.copy().set_color(YELLOW)
        self.play(cross_attempt.animate.next_to(barrier, LEFT), run_time=2)
        self.play(Indicate(barrier))
        
        # Explanation text
        expl = Text("For every N, there is N+1...", font_size=24).to_edge(DOWN)
        expl2 = Text("...but the set is never complete.", font_size=24).next_to(expl, DOWN)
        self.play(Write(expl))
        self.wait(1)
        self.play(Write(expl2))
        self.wait(4)


# ---------------------------------------------------------
# Scene 3: Constructivism vs Platonism
# A split screen comparison.
# ---------------------------------------------------------
class P3_Construct_vs_Plato(Scene):
    def construct(self):
        # Split screen line
        div_line = Line(UP*4, DOWN*4)
        self.add(div_line)
        
        # Left Side: Constructivism
        title_c = Text("Generative / Constructivist", font_size=30, color=BLUE).move_to(UP*3 + LEFT*3.5)
        self.play(Write(title_c))
        
        bricks = VGroup()
        for i in range(5):
            brick = Square(side_length=0.5, color=BLUE, fill_opacity=0.5)
            label = Integer(i+1).scale(0.5).move_to(brick)
            group = VGroup(brick, label).move_to(LEFT*3.5 + DOWN*2 + UP*i*0.6)
            bricks.add(group)
            self.play(FadeIn(group, shift=UP), run_time=0.8)
        
        c_text = Text("We 'make' numbers", font_size=20).next_to(bricks, DOWN)
        self.play(Write(c_text))

        # Right Side: Platonism
        title_p = Text("Mathematical Platonism", font_size=30, color=GOLD).move_to(UP*3 + RIGHT*3.5)
        self.play(Write(title_p))
        
        # Reveal a pre-existing set
        cloud = Ellipse(width=4, height=3, color=GOLD).move_to(RIGHT*3.5)
        stars = VGroup(*[Dot(point=cloud.get_center() + np.random.uniform(-1,1,3), color=GOLD_A, radius=0.05) for _ in range(20)])
        
        self.play(Create(cloud), FadeIn(stars), run_time=3)
        
        p_text = Text("We 'discover' numbers", font_size=20).next_to(cloud, DOWN)
        p_text2 = Text("(Completed Infinite)", font_size=20).next_to(p_text, DOWN)
        self.play(Write(p_text), Write(p_text2))
        self.wait(4)


# ---------------------------------------------------------
# Scene 4: Nuance of Aristotle and Plato
# Venn Diagram style overlap logic.
# ---------------------------------------------------------
class P4_Philosophy_Conflict(Scene):
    def construct(self):
        # Circles
        physical = Circle(radius=2, color=BLUE, fill_opacity=0.1).shift(LEFT*1.5)
        abstract = Circle(radius=2, color=PURPLE, fill_opacity=0.1).shift(RIGHT*1.5)
        
        p_label = Text("Physical World", font_size=24).move_to(physical.get_center())
        a_label = Text("Abstract / Forms", font_size=24).move_to(abstract.get_center())
        
        self.play(DrawBorderThenFill(physical), Write(p_label))
        self.play(DrawBorderThenFill(abstract), Write(a_label))
        
        # Aristotle's limit
        limit_text = Text("No Actual Infinity", font_size=20, color=RED).move_to(physical.get_center() + DOWN*0.5)
        self.play(Write(limit_text))
        
        # Platonism's Potential
        allow_text = Text("Infinity Possible?", font_size=20, color=GREEN).move_to(abstract.get_center() + DOWN*0.5)
        self.play(Write(allow_text))
        
        # Eternal Universe Text
        eternal = Text("Aristotle: The Universe is Eternal", font_size=32).to_edge(UP)
        self.play(Write(eternal))
        self.wait(3)


# ---------------------------------------------------------
# Scene 5: Philoponus and the Orbits
# Comparing two infinities via orbits.
# ---------------------------------------------------------
class P5_Philoponus_Orbits(Scene):
    def construct(self):
        title = Text("John Philoponus (5th Century)", font_size=36).to_edge(UP)
        self.play(Write(title))
        
        # Orbits
        saturn_orbit = Circle(radius=1.5, color=ORANGE)
        stars_orbit = Circle(radius=3, color=WHITE)
        
        sun = Dot(color=YELLOW, radius=0.2)
        saturn = Dot(color=ORANGE).move_to(saturn_orbit.get_right())
        star = Dot(color=WHITE).move_to(stars_orbit.get_right())
        
        self.add(sun, saturn_orbit, stars_orbit, saturn, star)
        
        # Counters
        saturn_count = Integer(0).next_to(saturn_orbit, LEFT)
        stars_count = Integer(0).next_to(stars_orbit, RIGHT)
        
        s_label = Text("Saturn", font_size=20, color=ORANGE).next_to(saturn_count, UP)
        st_label = Text("Stars (10,000x)", font_size=20, color=WHITE).next_to(stars_count, UP)
        
        self.play(Write(s_label), Write(st_label), FadeIn(saturn_count), FadeIn(stars_count))
        
        # Animation of orbits
        # We can't actually do 10,000x speed, but we imply it
        dt = 0
        
        # Equation
        equation = MathTex(r"\infty_{stars} \gg \infty_{saturn} ?").to_edge(DOWN)
        
        self.play(
            Rotate(saturn, angle=2*PI, about_point=ORIGIN, rate_func=linear),
            Rotate(star, angle=10*PI, about_point=ORIGIN, rate_func=linear), # Star moves faster
            ChangeDecimalToValue(saturn_count, 1),
            ChangeDecimalToValue(stars_count, 10000),
            run_time=4
        )
        
        self.play(Write(equation))
        
        absurd = Text("Absurdity implies Finite Past", color=RED, font_size=30).next_to(equation, UP)
        self.play(Write(absurd))
        self.wait(3)


# ---------------------------------------------------------
# Scene 6: Galileo's Paradox
# One-to-one correspondence between integers and squares.
# ---------------------------------------------------------
class P6_Galileo_Paradox(Scene):
    def construct(self):
        title = Text("Galileo's Two New Sciences", font_size=36).to_edge(UP)
        self.play(Write(title))
        
        # Columns
        col1 = VGroup()
        col2 = VGroup()
        
        for n in range(1, 7):
            num = MathTex(str(n)).scale(0.8)
            sq = MathTex(str(n*n)).scale(0.8)
            col1.add(num)
            col2.add(sq)
            
        col1.arrange(DOWN, buff=0.5).shift(LEFT*2)
        col2.arrange(DOWN, buff=0.5).shift(RIGHT*2)
        
        header1 = Text("Numbers", font_size=24).next_to(col1, UP)
        header2 = Text("Squares", font_size=24).next_to(col2, UP)
        
        self.play(Write(header1), Write(header2))
        
        # Reveal numbers
        for i in range(6):
            self.play(FadeIn(col1[i]), FadeIn(col2[i]), run_time=0.3)
            # Draw connecting line
            arrow = Arrow(col1[i].get_right(), col2[i].get_left(), buff=0.2, stroke_width=2)
            self.play(Create(arrow), run_time=0.2)
        
        # Paradox text
        paradox = Text("1-to-1 Correspondence", color=YELLOW, font_size=28).to_edge(DOWN)
        self.play(Write(paradox))
        
        # Highlight subset logic
        rect = SurroundingRectangle(col2, color=RED, buff=0.1)
        subset_text = Text("But squares are rarer!", color=RED, font_size=24).next_to(paradox, UP)
        
        self.play(Create(rect), Write(subset_text))
        self.wait(4)


class P7_Calculus_Limits(Scene):
    def construct(self):
        title = Text("The 17th Century: Calculus", font_size=40).to_edge(UP)
        self.play(Write(title))
        
        axes = Axes(x_range=[0, 10], y_range=[0, 5], axis_config={"include_tip": False})
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        
        # Function 1/x + 1 (converges to 1)
        graph = axes.plot(lambda x: 1/x + 1 if x > 0 else 5, x_range=[0.2, 10], color=BLUE)
        
        # FIX: Create the line first, then turn it into a DashedVMobject
        solid_limit_line = axes.plot(lambda x: 1, color=RED)
        limit_line = DashedVMobject(solid_limit_line, num_dashes=20)
        
        self.play(Create(axes), Write(labels))
        self.play(Create(graph), run_time=2)
        self.play(Create(limit_line))
        
        limit_text = MathTex(r"\lim_{x \to \infty} f(x) = 1").next_to(limit_line, RIGHT).shift(UP*0.5)
        self.play(Write(limit_text))
        
        # Utility Text
        utility = Text("'Points at Infinity' as tools", font_size=30).to_edge(DOWN)
        self.play(Write(utility))
        
        # Moving point along curve
        dot = Dot(color=YELLOW)
        dot.move_to(axes.c2p(0.5, 3))
        self.play(MoveAlongPath(dot, graph, rate_func=linear), run_time=4)
        self.wait(2)


# ---------------------------------------------------------
# Scene 8: Philosophical Resistance
# Maclaurin and Locke quotes/concepts.
# ---------------------------------------------------------
class P8_Resistance(Scene):
    def construct(self):
        # Geometry vs "Vitiated" Geometry
        square = Square(color=WHITE).shift(LEFT*3)
        label_geo = Text("Strict Geometry", font_size=24).next_to(square, UP)
        
        blob = RegularPolygon(n=8, color=RED).shift(RIGHT*3) # Represents "confused" shape
        # Distort the blob slightly to look "vitiated"
        blob.points[0] += np.array([0.2, 0.2, 0])
        blob.points[3] -= np.array([0.2, 0.1, 0])
        
        label_bad = Text("Absurd Philosophy", font_size=24, color=RED).next_to(blob, UP)
        
        self.play(Create(square), Write(label_geo))
        self.play(Create(blob), Write(label_bad))
        
        # Locke Quote Highlight
        quote_box = RoundedRectangle(corner_radius=0.5, height=3, width=10, fill_color=BLACK, fill_opacity=0.8)
        quote_text = Text(
            '"...minds be overlaid by an object too large\nand mighty to be surveyed..."', 
            font_size=32, slant=ITALIC
        )
        locke = Text("- John Locke", font_size=24).next_to(quote_text, DOWN, aligned_edge=RIGHT)
        
        self.play(FadeIn(quote_box), Write(quote_text), run_time=3)
        self.play(Write(locke))
        self.wait(4)


# ---------------------------------------------------------
# Scene 9: The Divergence
# The split between Intuitionists and Platonists.
# ---------------------------------------------------------
class P9_The_Divergence(Scene):
    def construct(self):
        # Center point
        start = Dot(point=DOWN*2)
        
        # Two paths
        path_left = Line(start.get_center(), UP*2 + LEFT*3)
        path_right = Line(start.get_center(), UP*2 + RIGHT*3)
        
        self.add(start)
        self.play(Create(path_left), Create(path_right), run_time=2)
        
        # Labels
        lbl_left = Text("Finite Intuition", font_size=24, color=BLUE).next_to(path_left.get_end(), UP)
        lbl_right = Text("Expressive Power", font_size=24, color=GOLD).next_to(path_right.get_end(), UP)
        
        self.play(Write(lbl_left), Write(lbl_right))
        
        # Divergence text
        div_text = Text("The Great Divergence", font_size=36).to_edge(DOWN)
        self.play(Write(div_text))
        
        # Hinting at Cantor
        cantor_hint = Text("Awaiting a breakthrough...", font_size=24, color=GREY).move_to(UP*0.5)
        self.play(FadeIn(cantor_hint))
        self.wait(3)


# ---------------------------------------------------------
# Scene 10: Russell Quote / Cantor Intro
# Skeleton in the cupboard metaphor.
# ---------------------------------------------------------
class P10_Cantor_Intro(Scene):
    def construct(self):
        # Russell Quote
        quote = Text(
            '"Cantor has abandoned this cowardly policy\nand has brought the skeleton out of its cupboard."',
            font_size=28, t2c={"skeleton": WHITE, "cupboard": WHITE}
        ).to_edge(UP)
        
        self.play(Write(quote), run_time=4)
        
        # Visual Metaphor
        cupboard = Rectangle(height=4, width=2.5, color=WHITE, fill_opacity=0.5).move_to(DOWN)
        door = Rectangle(height=4, width=2.5, color=WHITE).move_to(DOWN) # Closed door
        
        self.play(FadeIn(cupboard))
        
        # Open door animation (scale width to 0)
        self.play(door.animate.stretch_to_fit_width(0.1).move_to(cupboard.get_left()), run_time=1)
        
        # Skeleton / Infinity symbol
        inf_symbol = MathTex(r"\infty", font_size=100, color=WHITE).move_to(cupboard.get_center())
        
        self.play(FadeIn(inf_symbol))
        
        # Transformation to Aleph Null (Cantor's contribution)
        aleph = MathTex(r"\aleph_0", font_size=100, color=GOLD).move_to(cupboard.get_center())
        
        self.play(Transform(inf_symbol, aleph), run_time=2)
        
        # Final credit
        name = Text("Georg Cantor", font_size=40, color=GOLD).next_to(cupboard, RIGHT)
        self.play(Write(name))
        
        self.wait(3)