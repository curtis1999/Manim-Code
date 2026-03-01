from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
import random
import numpy as np

# ==========================================
# SCENE 1: INTRODUCTION
# ==========================================
class MathIntro(VoiceoverScene, ThreeDScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # ------------------------------------------
        # 1. SETUP THE ETERNAL PLATONIC UNIVERSE
        # ------------------------------------------
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.04)

        # --- Helper Functions for Complex 3D Structures ---
        
        def get_gabriels_horn():
            return Surface(
                lambda u, v: np.array([u, np.cos(v)/(u+0.5), np.sin(v)/(u+0.5)]),
                u_range=[0.1, 4], v_range=[0, 2*PI], resolution=(20, 20)
            ).set_color(YELLOW)

        def get_seifert_surface():
            # Approximated by a 3-twisted ribbon (Trefoil knot spanning surface)
            return Surface(
                lambda u, v: np.array([
                    (2 + v * np.cos(3*u/2)) * np.cos(u),
                    (2 + v * np.cos(3*u/2)) * np.sin(u),
                    v * np.sin(3*u/2)
                ]),
                u_range=[0, 2*PI], v_range=[-1, 1], resolution=(30, 10)
            ).set_color([BLUE, PURPLE])

        def get_boys_surface():
            # A simplified topological immersion (Cross-cap/Roman surface variant)
            return Surface(
                lambda u, v: np.array([
                    np.sin(2*u) * np.cos(v)**2,
                    np.sin(u) * np.sin(2*v),
                    np.cos(u) * np.sin(2*v)
                ]),
                u_range=[0, PI], v_range=[0, PI/2], resolution=(24, 24)
            ).set_color(PINK)

        def get_monkey_saddle():
            return Surface(
                lambda u, v: np.array([u, v, (u**3 - 3*u*v**2) * 0.2]),
                u_range=[-2, 2], v_range=[-2, 2], resolution=(20, 20)
            ).set_color(MAROON)

        def get_sierpinski_tetrahedron(depth=3, size=2):
            if depth == 0:
                return Tetrahedron().scale(size)
            # Recursive generation for the 4 corners
            group = VGroup()
            offsets = [UP, DOWN + LEFT + OUT, DOWN + RIGHT + OUT, DOWN + IN * 1.5]
            for offset in offsets:
                child = get_sierpinski_tetrahedron(depth - 1, size / 2)
                child.move_to(offset * size * 0.5)
                group.add(child)
            return group.set_color(GREEN_C)

        def get_kepler_poinsot_compound():
            # Compound of 5 tetrahedra (Stellated look)
            compound = VGroup()
            angles = [0, 72, 144, 216, 288]
            for angle in angles:
                tet = Tetrahedron().set_color(GOLD).set_opacity(0.8)
                tet.rotate(angle * DEGREES, axis=OUT).rotate(45 * DEGREES, axis=UP)
                compound.add(tet)
            return compound

        def get_3d_fractal_leaf():
            # Barnsley fern algorithm mapped onto a 3D curved surface
            dots = VGroup()
            x, y = 0, 0
            for _ in range(800): # 800 points so it renders smoothly
                r = random.random()
                if r < 0.01:
                    nx, ny = 0, 0.16 * y
                elif r < 0.86:
                    nx, ny = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
                elif r < 0.93:
                    nx, ny = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
                else:
                    nx, ny = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
                x, y = nx, ny
                
                # Add 3D curvature to the leaf
                z = np.sin(y * 0.5) * 0.5
                dots.add(Dot3D(np.array([x * 0.5, y * 0.5 - 2, z]), radius=0.03, color=GREEN))
            return dots

        def get_hopf_fibration():
            # Interlocking circles forming a torus-like structure
            fibration = VGroup()
            for i in range(12):
                angle = i * (PI / 6)
                ring = Circle(radius=1.5, color=TEAL_B, stroke_width=4)
                # Rotate to form Villarceau circles
                ring.rotate(PI/2, axis=RIGHT).rotate(angle, axis=OUT).rotate(PI/4, axis=UP)
                fibration.add(ring)
            return fibration
        
        def get_torus_knot(p=3, q=4, R=1.5, r=0.5):
            return ParametricFunction(
                lambda t: np.array([
                    (R + r * np.cos(p * t)) * np.cos(q * t),
                    (R + r * np.cos(p * t)) * np.sin(q * t),
                    r * np.sin(p * t)
                ]),
                t_range=[0, 2 * PI],
                stroke_width=8
            ).set_color(RED)

        # --- Instantiate the Universe ---
        # Spread out across a massive coordinate plane [X, Y, Z]
        math_universe = VGroup(
            get_gabriels_horn().move_to(RIGHT * 6 + UP * 2 + IN * 2),
            get_seifert_surface().move_to(LEFT * 5 + DOWN * 2 + OUT * 2),
            get_boys_surface().move_to(RIGHT * 4 + DOWN * 4 + IN * 3),
            get_monkey_saddle().move_to(LEFT * 3 + UP * 4 + OUT * 4),
            get_sierpinski_tetrahedron().move_to(RIGHT * 2 + UP * 3 + OUT * 2),
            get_kepler_poinsot_compound().move_to(LEFT * 6 + DOWN * 1 + IN * 2),
            get_3d_fractal_leaf().move_to(RIGHT * 5 + DOWN * 2 + OUT * 4),
            get_hopf_fibration().move_to(LEFT * 2 + DOWN * 4 + IN * 4),
            get_torus_knot(p=3, q=4).move_to(LEFT * 4 + UP * 1 + IN * 2),
            Icosahedron().set_color(BLUE).move_to(RIGHT * 3 + DOWN * 1 + IN * 3),
            Torus().set_color(ORANGE).move_to(UP * 1 + LEFT * 1),
            Cube().set_color(WHITE).move_to(RIGHT * 1 + UP * 5 + IN * 1)
        )

        # Give 3D objects organic starting rotations
        for mob in math_universe:
            mob.rotate(random.uniform(0, PI), axis=RIGHT)
            mob.rotate(random.uniform(0, PI), axis=UP)

        # Add them immediately to the scene
        self.add(math_universe)

        # ------------------------------------------
        # 2. INTRO VOICEOVER & ANIMATION
        # ------------------------------------------
        script_intro = (
            "In this video series, we are going to go deep into mathematical logic "
            "to try to figure out what math is, and where its limits are."
        )
        
        with self.voiceover(text=script_intro) as tracker:
            self.play(
                *[Rotate(mob, angle=PI/3, axis=UP, about_point=mob.get_center(), rate_func=linear) for mob in math_universe],
                run_time=tracker.duration
            )

        # ------------------------------------------
        # 3. TRANSITION TO THE LIST
        # ------------------------------------------
        self.stop_ambient_camera_rotation()
        
        self.move_camera(
            phi=0, 
            theta=-90 * DEGREES,
            added_anims=[FadeOut(math_universe)],
            run_time=1.5
        )

        # ------------------------------------------
        # 4. THE OUTLINE VOICEOVER
        # ------------------------------------------
        title = Text("Series Outline", font_size=48, weight=BOLD).to_edge(UP)
        part1 = Text("Part 1: Syntax vs. Semantics", font_size=32)
        part2 = Text("Part 2: Basic Set Theory", font_size=32)
        part3 = Text("Part 3: Skolem's Paradox", font_size=32)
        part4 = Text("Part 4: Deductive Completeness", font_size=32)
        part5 = Text("Part 5: Primitive Recursion & Computability", font_size=32)
        part6 = Text("Part 6: Gödel's Incompleteness Theorem", font_size=32)
        bonus = Text("Bonus: Non-Classical Logics", font_size=32, color=YELLOW)

        list_group = VGroup(part1, part2, part3, part4, part5, part6, bonus)
        list_group.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        list_group.next_to(title, DOWN, buff=1).shift(LEFT * 1.5)

        self.play(Write(title))

        with self.voiceover(text="In the first video, we will cover syntax vs. semantics, define what a formal proof is, and the definition of mathematical structures."):
            self.play(Write(part1))

        with self.voiceover(text="In the second video, we will cover basic set theory, since theories are defined using sets, and yet sets are defined using a theory."):
            self.play(Write(part2))

        with self.voiceover(text="In the third video, we will cover Skolem's paradox, showing how first order logic cannot fully capture or determine certain properties."):
            self.play(Write(part3))

        with self.voiceover(text="In the fourth video, we will cover the deductive completeness of first order logic, providing a bridge between syntax and semantics."):
            self.play(Write(part4))

        with self.voiceover(text="In the fifth video, we will see the basics of primitive recursion, decidability, and the Halting problem."):
            self.play(Write(part5))

        with self.voiceover(text="Finally, we will cover Godel's incompleteness theorem and discuss its implications."):
            self.play(Write(part6))

        with self.voiceover(text="As a bonus video, we will cover non-classical logics, and see how they give rise to different visions of mathematics."):
            self.play(Write(bonus))

        self.wait(2)
        self.play(FadeOut(Group(title, list_group)))