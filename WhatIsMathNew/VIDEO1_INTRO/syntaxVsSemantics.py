from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class SyntaxVsSemantics(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # ==========================================
        # SETUP: LAYOUT & HELPERS
        # ==========================================
        divider = Line(UP * 4, DOWN * 4, stroke_width=2).set_color(WHITE)
        syntax_center = LEFT * 3.5
        semantics_center = RIGHT * 3.5

        # ==========================================
        # SCENE 1: THE SYNTAX (LEFT SIDE)
        # ==========================================
        script_1 = "On the one hand we have the syntax, which can be seen as manipulations of symbols being governed by a special theorem proving computer, which takes in axioms as input and outputs theorems."
        with self.voiceover(text=script_1) as tracker:
            self.play(Create(divider), run_time=1)
            
            # Theorem Proving Computer Setup
            prog_box = Rectangle(width=3, height=2, color=BLUE, fill_opacity=0.1).move_to(syntax_center + UP * 1)
            prog_text = Text("Prover", font_size=32).move_to(prog_box.get_center())
            computer = VGroup(prog_box, prog_text)

            in_arrow = Arrow(prog_box.get_left() + LEFT * 1.5, prog_box.get_left(), color=WHITE)
            in_label = MathTex(r"\Sigma", font_size=40).next_to(in_arrow, LEFT)
            out_arrow = Arrow(prog_box.get_right(), prog_box.get_right() + RIGHT * 1.5, color=WHITE)
            out_label = MathTex(r"\chi", font_size=40).next_to(out_arrow, RIGHT)

            self.play(FadeIn(computer), GrowArrow(in_arrow), FadeIn(in_label), run_time=1)
            self.play(prog_box.animate.set_fill(BLUE, opacity=0.4), run_time=0.5)
            self.play(prog_box.animate.set_fill(BLUE, opacity=0.1), run_time=0.5)
            self.play(GrowArrow(out_arrow), FadeIn(out_label), run_time=1)
            self.wait(max(0, tracker.duration - 3))

        script_2 = "Once it has proven a theorem, we can feed this theorem back into it's inputs to prove more theorems."
        with self.voiceover(text=script_2) as tracker:
            # Feedback loop animation
            feedback_arc = CurvedArrow(
                out_label.get_bottom(), 
                in_label.get_bottom(), 
                angle=PI/2, 
                color=YELLOW
            )
            self.play(Create(feedback_arc), run_time=1.5)
            
            # Pulse the computer to show processing
            self.play(prog_box.animate.set_fill(BLUE, opacity=0.4), run_time=0.3)
            self.play(prog_box.animate.set_fill(BLUE, opacity=0.1), run_time=0.3)
            self.wait(max(0, tracker.duration - 2.1))

        script_3 = "If chi is such a theorem and Sigma is out set of axioms then we denote this situation by this relation, which is read as Sigma proves chi. The theory of a given set of axioms is the set of all such theorems, which in our analogy is the set of all possible outputs from our theorem proving computer."
        with self.voiceover(text=script_3) as tracker:
            turnstile = MathTex(r"\Sigma \vdash \chi", font_size=48, color=YELLOW).move_to(syntax_center + DOWN * 1.5)
            self.play(FadeIn(turnstile), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        # ==========================================
        # SCENE 2: SEMANTICS (RIGHT SIDE)
        # ==========================================
        script_4 = "On the other side we have the intuitive world of semantics, where truth is based on Tarki's definition of truth, namely that something is true if and only if it is true in all models. We will now attempt to make this precise, which may be a bit boring, but it leads us to interesting places."
        with self.voiceover(text=script_4) as tracker:
            self.wait(tracker.duration)

        # Structure M Setup (From old code, adapted for right side)
        m_tex = MathTex(
            r"\mathcal{M}", r" = (", 
            r"M", r", ", 
            r"c_0^\mathcal{M}, \dots", r", ", 
            r"F_0^\mathcal{M}, \dots", r", ", 
            r"R_0^\mathcal{M}, \dots", 
            r")", font_size=36
        ).move_to(semantics_center + UP * 2.5)

        script_5 = "Formally, a structure --which we denote which this fancy M-- is given by this tuple of elements."
        with self.voiceover(text=script_5) as tracker:
            self.play(Write(m_tex), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        script_6 = "This is some arbitrary set, and denotes the universe or domain of the structure."
        with self.voiceover(text=script_6) as tracker:
            self.play(m_tex[2].animate.set_color(YELLOW), run_time=0.5)
            domain_label = Text("Domain", font_size=20, color=YELLOW).next_to(m_tex[2], DOWN, buff=0.1)
            self.play(FadeIn(domain_label), run_time=0.5)
            self.wait(max(0, tracker.duration - 1))

        script_7 = "And these are the interpretations of the symbols of the language."
        with self.voiceover(text=script_7) as tracker:
            self.play(m_tex[2].animate.set_color(WHITE), FadeOut(domain_label), run_time=0.5)
            self.play(
                m_tex[4].animate.set_color(TEAL),
                m_tex[6].animate.set_color(TEAL),
                m_tex[8].animate.set_color(TEAL),
                run_time=0.5
            )
            interp_label = Text("Interpretations", font_size=20, color=TEAL).next_to(m_tex[6], DOWN, buff=0.2)
            self.play(FadeIn(interp_label), run_time=0.5)
            self.wait(max(0, tracker.duration - 1.5))
            self.play(
                m_tex[4].animate.set_color(WHITE),
                m_tex[6].animate.set_color(WHITE),
                m_tex[8].animate.set_color(WHITE),
                FadeOut(interp_label)
            )

        # ==========================================
        # SCENE 3: LOGICAL VS NON-LOGICAL SYMBOLS
        # ==========================================
        script_8 = "In math there are certain symbols which are known as the logical symbols which include variables, quantifiers, Boolean connectives --such as conjunction, disjunction, implication and negation-- and brackets. For a mathematician, these exist in the background world of logic."
        with self.voiceover(text=script_8) as tracker:
            self.wait(tracker.duration)

        script_9 = "Then there are certain symbols know as the non-logical symbols which are the constants --like 0,1,e,pi etc., functions --such as addition multiplication and relations--such as <, or the set theoretic membership relation. These are the set of symbols specific to a given mathematical theory. As we saw earlier, constants simply get interpreted as certain elements of the domain."
        with self.voiceover(text=script_9) as tracker:
            self.wait(tracker.duration)

        # ==========================================
        # SCENE 4: INTERPRETING RELATIONS (<)
        # ==========================================
        num_line = NumberLine(x_range=[0, 4, 1], length=3.5, include_numbers=True, font_size=24).move_to(semantics_center)
        
        script_10 = "The formal definition of the interpretations of function and relation symbols is a bit strange at first, as they get interpreted as a sets of tuples which satisfy a given relationship. For example, the less than relation would be the set of all pairs of natural numbers (a,b) such that the interpretation of a is less than the interpretation of b."
        with self.voiceover(text=script_10) as tracker:
            self.play(Create(num_line), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_11 = "We could represent this on the number line by drawing every possible arrow between nodes which is going to the right."
        with self.voiceover(text=script_11) as tracker:
            # Draw arrows for 0->1, 0->2, 0->3, 1->2, 1->3, 2->3
            arrows = VGroup()
            for i in range(3):
                for j in range(i+1, 4):
                    arrow = CurvedArrow(num_line.n2p(i) + UP*0.2, num_line.n2p(j) + UP*0.2, angle=-PI/3, color=PINK)
                    arrows.add(arrow)
            
            self.play(Create(arrows, lag_ratio=0.1), run_time=2)
            self.wait(max(0, tracker.duration - 2.5))
            self.play(FadeOut(arrows), run_time=0.5)

        # ==========================================
        # SCENE 5: INTERPRETING FUNCTIONS (+)
        # ==========================================
        script_12 = "Earlier I said that function symbols can be interpreted as computer programs, well, formally they will be interpreted as a special type of relation."
        with self.voiceover(text=script_12) as tracker:
            self.wait(tracker.duration)

        plus_set = MathTex(
            r"+^\mathcal{M} = \{(a,b,c) \mid a+b=c\}", 
            font_size=32, color=ORANGE
        ).move_to(semantics_center + DOWN * 1.5)
        
        plus_examples = MathTex(
            r"\{(0,0,0), (0,1,1), (1,1,2), \dots \}", 
            font_size=28, color=ORANGE
        ).next_to(plus_set, DOWN, buff=0.2)

        script_13 = "For example the plus symbols will be interpreted as the set of triples (a,b,c) such that a+b=c. They are special relations, because we know that the output is uniquely determined by the inputs."
        with self.voiceover(text=script_13) as tracker:
            self.play(Write(plus_set), run_time=1)
            self.play(FadeIn(plus_examples), run_time=1)
            self.wait(max(0, tracker.duration - 2))