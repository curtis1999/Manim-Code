from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
import networkx as nx
import random

# ==========================================
# SCENE 1: INTRODUCTION
# ==========================================
class MathIntro(VoiceoverScene, ThreeDScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # Camera Setup
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.08)

        # Generate Floating Objects
        math_universe = VGroup(
            Cube(side_length=1.5).set_color(RED).move_to(RIGHT * 3 + UP * 2),
            Tetrahedron().set_color(GREEN).move_to(LEFT * 4 + DOWN * 1),
            Octahedron().set_color(PURPLE).move_to(RIGHT * 2 + DOWN * 3),
            Dodecahedron().set_color(YELLOW).move_to(LEFT * 2 + UP * 3),
            Cone().set_color(ORANGE).move_to(UP * 1 + LEFT * 1),
            Torus(major_radius=1, minor_radius=0.5).set_color(BLUE).move_to(RIGHT * 4 + UP * 0),
        )

        for mob in math_universe:
            mob.rotate(random.uniform(0, PI), axis=RIGHT)
            mob.rotate(random.uniform(0, PI), axis=UP)

        # Voiceover
        script = (
            "WHAT IS MATH AND WHY IS IT INCOMPLETE? "
            "In this video we are going deep into mathematical logic to try and figure out "
            "what math is and where it's limits are."
        )
        
        with self.voiceover(text=script) as tracker:
            self.play(FadeIn(math_universe, lag_ratio=0.1), run_time=2)
            self.wait(max(0, tracker.duration - 2))

        self.stop_ambient_camera_rotation()
        self.play(FadeOut(math_universe))
        self.wait(1)




