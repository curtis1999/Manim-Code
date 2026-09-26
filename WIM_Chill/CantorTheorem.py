from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class CantorTheorem(VoiceoverScene):
    def construct(self):
        # Set up the voiceover service
        self.set_speech_service(RecorderService(transcription_model=None))

        # --- PART 1: SETUP SET X AND P(X) DIRECTLY ---
        with self.voiceover(text="Let X be some arbitrary set and suppose towards a contradiction that there is a 1-1 and onto map f from X to the power set of X.") as tracker:
            
            # Abstract set X
            set_x_circle = Circle(radius=1.2, color=BLUE).move_to(LEFT*5)
            set_x_label = Text("X", font_size=36).move_to(set_x_circle.get_center())
            
            # Power set P(X)
            powerSet = Square(side_length=2.75, color=YELLOW, fill_opacity=0.1)
            powerSet.next_to(set_x_circle, RIGHT, buff=1.2)
            powerSet.rotate(PI/4)
            power_label = Text("P(X)", font_size=32).move_to(powerSet.get_center())
            
            # Map f
            arrow_f = Arrow(set_x_circle.get_right(), powerSet.get_left(), buff=0, stroke_width=32, color=GREEN)
            f_label = Text("f", font_size=28, color=GREEN).next_to(arrow_f, UP, buff=0.1)

            self.play(
                Create(set_x_circle), Write(set_x_label))
            self.wait()
            self.play(Create(powerSet), Write(power_label))
            self.play(Create(arrow_f), Write(f_label))

        with self.voiceover(text="Where onto just means that every element in the power set of X gets mapped to by some element from X.") as tracker:
            self.wait(tracker.duration)

        # --- PART 2: PROOF VISUALIZATION ---
        with self.voiceover(text="We can define the diagonal set D as the subset of X consisting of the elements which are not contained in their image under f.") as tracker:
            d_definition = MathTex(r"D = \{x \in X : x \notin f(x)\}")
            d_definition.to_edge(RIGHT).shift(LEFT*1 + UP*1)
            self.play(Write(d_definition))
            
        with self.voiceover(text="This is a subset of X, and therefore by definition exists somewhere in the power set.") as tracker:
            d_point = Dot(color=RED, radius=0.08).move_to(powerSet.get_center() + UP*1 + RIGHT*0.2)
            d_label = Text("D", font_size=24, color=RED).next_to(d_point, RIGHT, buff=0.1)
            self.play(Create(d_point), Write(d_label))

        with self.voiceover(text="By our assumption that the map is onto, there should be some element a in X, such that f(a)=D.") as tracker:
            a_dot = Dot(color=BLUE, radius=0.06).move_to(set_x_circle.get_center() + UP*0.7)
            a_label = Text("a", font_size=20, color=BLUE).next_to(a_dot, UP, buff=0.1)
            self.play(Create(a_dot), Write(a_label))
            
            arrow_a_to_d = Arrow(a_dot.get_center(), d_point.get_center(), buff=0.05, stroke_width=1, color=BLUE)
            self.play(Create(arrow_a_to_d))
            
            assumption_text = Text("f(a)=D", font_size=36).next_to(d_definition, DOWN, buff=0.5)
            self.play(Write(assumption_text))

        with self.voiceover(text="By definition of D, we know that a in D iff a not in f(a).") as tracker:
            contradiction_text = MathTex(r"a \in D \leftrightarrow a \notin f(a)")
            contradiction_text.next_to(assumption_text, DOWN, buff=0.3)
            self.play(Write(contradiction_text))

        with self.voiceover(text="But D=f(a), so we get that a in f(a) iff a not in f(a), which is a contradiction.") as tracker:
            contradiction_text2 = MathTex(r"a \in f(a) \leftrightarrow a \notin f(a)")
            contradiction_text2.move_to(contradiction_text.get_center())
            self.play(Transform(contradiction_text, contradiction_text2))
            
            bottom = MathTex(r"\bot", font_size=100, color=RED)
            bottom.next_to(contradiction_text, RIGHT, buff=1)
            self.wait(4)
            self.play(Write(bottom))

        with self.voiceover(text="So, it must be that our map was not onto, and therefore the size of the power set of D is larger than the size of D.") as tracker:
            self.wait(tracker.duration * 0.5)
            self.play(*[FadeOut(m) for m in self.mobjects])