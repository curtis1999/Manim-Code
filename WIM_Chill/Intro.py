from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class Chill_intro(VoiceoverScene):
    def construct(self):
        # The RecorderService will prompt you in the terminal to record your own voice 
        # or press Enter to skip and use estimated text-length timings.
        self.set_speech_service(RecorderService(transcription_model=None))

        # --- Helper Functions ---
        def create_tp_box(label_text="Theorem\nProver", num_inputs=3, box_height=2.0, box_width=2.0):
            label = Text(label_text, font_size=24)
            rect = Rectangle(width=box_width, height=box_height, color=BLUE, fill_opacity=0.1, stroke_width=4)
            label.move_to(rect.get_center())
            
            inputs = VGroup()
            if num_inputs > 1:
                spacing = (box_height - 0.5) / (num_inputs - 1)
            else:
                spacing = 0
                
            start_y = (box_height / 2) - 0.25
            for i in range(num_inputs):
                y_pos = start_y - i * spacing
                line = Line(LEFT * 0.5, ORIGIN).next_to(rect, LEFT, buff=0, aligned_edge=UP).shift(DOWN * (box_height/2 - y_pos))
                inputs.add(line)
            
            output = Line(ORIGIN, RIGHT * 0.8).next_to(rect, RIGHT, buff=0)
            return VGroup(rect, label, inputs, output)

        # --- Data Preparation ---
        zfc_data = [
            ("Extensionality", r"\forall x \forall y (\forall z (z \in x \leftrightarrow z \in y) \rightarrow x = y)"),
            ("Separation", r"\forall x \exists y \forall z (z \in y \leftrightarrow z \in x \land \varphi(z))"),
            ("Pairing", r"\forall x \forall y \exists z \forall w (w \in z \leftrightarrow w = x \lor w = y)"),
            ("Union", r"\forall x \exists y \forall z (z \in y \leftrightarrow \exists w (z \in w \land w \in x))"),
            ("Regularity", r"\forall x (x \neq \emptyset \rightarrow \exists y \in x (x \cap y = \emptyset))"),
            ("Power Set", r"\forall x \exists y \forall z (z \in y \leftrightarrow z \subseteq x)"),
            ("Replacement", r"\forall x (\forall y \in x \exists! z \varphi(y,z) \rightarrow \exists w \forall y \in x \exists z \in w \varphi(y,z))"),
            ("Infinity", r"\exists x (\emptyset \in x \land \forall y \in x (y \cup \{y\} \in x))"),
            ("Choice", r"\forall X (\emptyset \notin X \rightarrow \exists f: X \rightarrow \cup X \dots)")
        ]
        
        zfc_names = VGroup()
        zfc_formulas = VGroup()
        zfc_axioms_full = VGroup()
        
        for name, formula in zfc_data:
            name_tex = Text(name + ": ", font_size=28, color=TEAL)
            form_tex = MathTex(formula, font_size=32)
            row = VGroup(name_tex, form_tex).arrange(RIGHT, aligned_edge=DOWN)
            zfc_names.add(name_tex)
            zfc_formulas.add(form_tex)
            zfc_axioms_full.add(row)
        
        zfc_axioms_full.arrange(DOWN, aligned_edge=LEFT, buff=0.4)


        # --- Scene 1: Introduction ---
        with self.voiceover(text="Alright in this video we're gonna go deep into mathematical logic and set theory to try and figure out what Math is. Right off the bat, because of Godel's incompleteness theorems, there is no clear cut answer to this, but one possible answer is that math is the theory of ZFC.") as tracker:
            self.wait(tracker.duration)

        # --- Scene 2: Display ZFC ---
        with self.voiceover(text="Which is just the set of all first order consequences of these axioms right here.") as tracker:
            # Display names and formulas directly for easier isolation later
            self.add(zfc_names, zfc_formulas)
            self.wait(tracker.duration)

        with self.voiceover(text="We'll try and figure out what that means right now.") as tracker:
            self.wait(tracker.duration)

        # --- Scene 3: Theorem Prover Box ---
        with self.voiceover(text="To keep things simple, we can imagine a black box theorem proving computer.") as tracker:
            # Create Theorem Prover directly in the center
            tp_box = create_tp_box("Theorem\nProver", num_inputs=9, box_height=6.0, box_width=3.0).move_to(ORIGIN)
            input_lines = tp_box[2]
            output_line = tp_box[3]
            
            # Generate the target positions for only the formulas
            target_formulas = zfc_formulas.copy().scale(0.5)
            for i, form in enumerate(target_formulas):
                form.next_to(input_lines[i], LEFT, buff=0.1)

            # Fade out names, shrink formulas, and draw the box all at once
            self.play(
                FadeOut(zfc_names),
                Transform(zfc_formulas, target_formulas),
                Create(tp_box),
                run_time=tracker.duration
            )

        # --- Scene 4: Inputs and Outputs ---
        with self.voiceover(text="In a later video we will open the hood of this black box computer, but for this video, just see it as some computer which takes in sentences written in first order logic, and it outputs the logical consequences of these sentences.") as tracker:
            
            # Output x = x
            thm_output = MathTex(r"x = x").next_to(output_line, RIGHT, buff=0.2)
            self.play(FadeIn(thm_output, shift=RIGHT), run_time=tracker.duration * 0.4)
            
            self.wait(tracker.duration * 0.2)

            # Transition x = x into x \notin x
            thm_2 = MathTex(r"x \notin x").move_to(thm_output).align_to(thm_output, LEFT)
            self.play(Transform(thm_output, thm_2), run_time=tracker.duration * 0.4)

        # --- Scene 5: General Axioms and ALL OF MATH ---
        with self.voiceover(text="The ultimate goal, is to find some set of axioms which we could feed into our theorem prover such that it outputs every true mathematical statement, without ever outputting a false mathematical statement.") as tracker:
            
            # Create generic axioms A1, A2, ..., An aligned directly to the inputs
            general_axioms = VGroup()
            for i in range(8):
                ax = MathTex(f"A_{i+1}").scale(0.8).next_to(input_lines[i], LEFT, buff=0.1)
                general_axioms.add(ax)
            
            # Last one is An
            an = MathTex(r"A_n").scale(0.8).next_to(input_lines[-1], LEFT, buff=0.1)
            general_axioms.add(an)

            # ALL OF MATH output
            all_of_math = Text("ALL OF MATH", color=GOLD, font_size=36).next_to(output_line, RIGHT, buff=0.2)
            
            fast_transition_time = 0.6
            self.play(
                Transform(zfc_formulas, general_axioms),
                Transform(thm_output, all_of_math),
                run_time=fast_transition_time
            )
            self.wait(max(0, tracker.duration - fast_transition_time))

        # --- Scene 6: Godel ---
        with self.voiceover(text="Again, this is impossible due to this guy,") as tracker:
            # Updated to requested image name
            godel_img = ImageMobject("image_Godel.jpg").scale(1.5).to_edge(UP)
            self.play(FadeIn(godel_img), run_time=tracker.duration)

        # --- Scene 7: Return to ZFC ---
        with self.voiceover(text="so the best we can hope for is some set of axioms which can output pretty much all of math, and that's where ZFC comes in.") as tracker:
            
            # Re-generate clean target explicit formulas to match the earlier step
            zfc_return_target = VGroup()
            for i, (name, formula) in enumerate(zfc_data):
                f_tex = MathTex(formula, font_size=32).scale(0.5).next_to(input_lines[i], LEFT, buff=0.1)
                zfc_return_target.add(f_tex)
            
            # Update to MOST OF MATH
            most_of_math = Text("MOST OF MATH", color=GOLD, font_size=36).move_to(thm_output).align_to(thm_output, LEFT)

            fast_transition_time = 0.6
            self.play(
                FadeOut(godel_img),
                Transform(zfc_formulas, zfc_return_target),
                Transform(thm_output, most_of_math),
                run_time=fast_transition_time
            )
            
            self.wait(max(0, tracker.duration - fast_transition_time) + 1)
            
class SetTheoryUniverseScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # --- Helper for Hasse Diagram ---
        def get_hasse_diagram():
            diagram = VGroup()
            # Levels
            l0 = MathTex(r"\emptyset").scale(0.6)
            l1_1 = MathTex(r"\{1\}").scale(0.6)
            l1_2 = MathTex(r"\{2\}").scale(0.6)
            l1_3 = MathTex(r"\{3\}").scale(0.6)
            l2_12 = MathTex(r"\{1,2\}").scale(0.6)
            l2_13 = MathTex(r"\{1,3\}").scale(0.6)
            l2_23 = MathTex(r"\{2,3\}").scale(0.6)
            l3 = MathTex(r"\{1,2,3\}").scale(0.6)

            # Positions
            l0.move_to(DOWN * 1.5)
            VGroup(l1_1, l1_2, l1_3).arrange(RIGHT, buff=0.5).move_to(DOWN * 0.5)
            VGroup(l2_12, l2_13, l2_23).arrange(RIGHT, buff=0.5).move_to(UP * 0.5)
            l3.move_to(UP * 1.5)

            nodes = VGroup(l0, l1_1, l1_2, l1_3, l2_12, l2_13, l2_23, l3)
            
            # Edges
            edges = VGroup()
            edges.add(Line(l0.get_top(), l1_1.get_bottom(), stroke_width=2, color=GRAY))
            edges.add(Line(l0.get_top(), l1_2.get_bottom(), stroke_width=2, color=GRAY))
            edges.add(Line(l0.get_top(), l1_3.get_bottom(), stroke_width=2, color=GRAY))
            
            edges.add(Line(l1_1.get_top(), l2_12.get_bottom(), stroke_width=2, color=GRAY))
            edges.add(Line(l1_1.get_top(), l2_13.get_bottom(), stroke_width=2, color=GRAY))
            edges.add(Line(l1_2.get_top(), l2_12.get_bottom(), stroke_width=2, color=GRAY))
            edges.add(Line(l1_2.get_top(), l2_23.get_bottom(), stroke_width=2, color=GRAY))
            edges.add(Line(l1_3.get_top(), l2_13.get_bottom(), stroke_width=2, color=GRAY))
            edges.add(Line(l1_3.get_top(), l2_23.get_bottom(), stroke_width=2, color=GRAY))

            edges.add(Line(l2_12.get_top(), l3.get_bottom(), stroke_width=2, color=GRAY))
            edges.add(Line(l2_13.get_top(), l3.get_bottom(), stroke_width=2, color=GRAY))
            edges.add(Line(l2_23.get_top(), l3.get_bottom(), stroke_width=2, color=GRAY))

            diagram.add(edges, nodes)
            return diagram

        # --- Scene 1: The V Hierarchy ---
        with self.voiceover(text="These axioms essentially define what is and what is not a valid mathematical set. If we view math platonically, then there is some pre-existing Universe of sets, which these axioms try to describe.") as tracker:
            
            v_hierarchy = VGroup()
            bottom_point = DOWN * 3
            left_line = Line(bottom_point, UP * 3 + LEFT * 4, color=GREEN)
            right_line = Line(bottom_point, UP * 3 + RIGHT * 4, color=GREEN)
            middle_line = Line(bottom_point, UP * 3, color=GREEN)
            
            ticks = VGroup()
            labels = VGroup()
            
            tick_data = [
                (DOWN * 3, r"\emptyset"),
                (DOWN * 1, r"\omega"),
                (UP * 1, r"\omega_1"),
                (UP * 2.5, r"\dots")
            ]
            
            for pos, tex in tick_data:
                tick = Line(LEFT * 0.1, RIGHT * 0.1, color=GREEN).move_to(pos)
                label = MathTex(tex, color=GREEN).next_to(tick, RIGHT, buff=0.2)
                ticks.add(tick)
                labels.add(label)
                
            v_hierarchy.add(left_line, right_line, middle_line, ticks, labels)
            
            self.play(Create(v_hierarchy), run_time=tracker.duration)

        with self.voiceover(text="Again, due to this guy, there are many different possible set theoretic universes, so we cannot pin down THE Universe of Sets, but for now, we won't worry about that, and we will imagine that this as the Universe of sets.") as tracker:
            godel_img = ImageMobject("image_Godel.jpg").scale(1.2).to_edge(RIGHT)
            self.play(FadeIn(godel_img), run_time=tracker.duration * 0.2)
            self.wait(tracker.duration * 0.6)
            self.play(FadeOut(godel_img), run_time=tracker.duration * 0.2)

        with self.voiceover(text="Since a set is so general, everything in math can be seen as a set. Meaning that every mathematical object will exist somewhere in here.") as tracker:
            torus = VGroup(
                Ellipse(width=2, height=1, color=BLUE),
                ArcBetweenPoints(LEFT*0.6, RIGHT*0.6, angle=PI/3, color=BLUE),
                ArcBetweenPoints(LEFT*0.5, RIGHT*0.5, angle=-PI/3, color=BLUE)
            ).scale(0.8).to_edge(LEFT).shift(UP)

            # Changed target coordinate to land to the left of the spine
            torus_arrow = CurvedArrow(torus.get_right(), LEFT * 1.5 + UP * 0.5, angle=-PI/4, color=YELLOW)
            
            self.play(FadeIn(torus), Create(torus_arrow), run_time=tracker.duration)

        with self.voiceover(text="So, if we can define what is, and what is not a valid set, then we will have defined what is and what is not part of math.") as tracker:
            self.wait(tracker.duration)

        with self.voiceover(text="Now if you try to define a set, you will likely say something like a collection of things or a class of objects.") as tracker:
            self.play(
                FadeOut(v_hierarchy),
                FadeOut(torus),
                FadeOut(torus_arrow),
                run_time=tracker.duration
            )

        with self.voiceover(text="But then, how do you define a collection or a class? So a set is too basic to be defined in terms of anything simpler. Now, when we want to start defining the set theoretic universe, we run into a fundamental issue with definitions. Words are defined using other words, so how can we define the first word? So there has to be some sort of a-priori assumptions, which are the axioms.") as tracker:
            def_text = Text("Def: WORD = MORE WORDS", font_size=40, color=YELLOW)
            self.play(FadeIn(def_text), run_time=tracker.duration * 0.2)
            self.wait(tracker.duration * 0.6)
            self.play(FadeOut(def_text), run_time=tracker.duration * 0.2)

        # --- Scene 2: Building the Ordinals and Axioms ---
        # Shifted coordinates right to avoid cutting off long axioms
        ordinals_x = 3.2
        axioms_x = -3.2

        with self.voiceover(text="The simplest axiom, is the axiom of existence, which simply asserts that there is some set. Specifically, that the empty set exists.") as tracker:
            ax_existence = MathTex(r"\text{Existence: } \exists x \forall y (y \notin x)").scale(0.7).move_to(RIGHT * axioms_x + DOWN * 3)
            set_empty = MathTex(r"\emptyset").move_to(RIGHT * ordinals_x + DOWN * 3)
            
            self.play(FadeIn(ax_existence, shift=RIGHT), FadeIn(set_empty, shift=UP), run_time=tracker.duration)

        with self.voiceover(text="So at the base of this whole set theoretic Universe, is that assumption that nothing exists. Once we have this emptyset, we add other axioms which allow us to define other sets. For example, we can assert that given any set, there is a set whose sole member is that set.") as tracker:
            ax_singleton = MathTex(r"\forall x \exists y (x \in y \land \forall z (z \in y \implies z=x))").scale(0.6).next_to(ax_existence, UP, buff=0.8)
            self.play(FadeIn(ax_singleton, shift=RIGHT), run_time=tracker.duration)

        with self.voiceover(text="Meaning that we can define the set containing the emptyset. So, we start with nothing, then we can put a bag around it and so we no longer have nothing, we have a bag with nothing in it. Then we can define the set containing the set with the emptyset, so a bag containing a bag with nothing in it.") as tracker:
            set_1 = MathTex(r"\{\emptyset\}").move_to(RIGHT * ordinals_x + DOWN * 2)
            set_2 = MathTex(r"\{\{\emptyset\}\}").move_to(RIGHT * ordinals_x + DOWN * 1)
            
            self.play(FadeIn(set_1, shift=UP), run_time=tracker.duration * 0.4)
            self.wait(tracker.duration * 0.2)
            self.play(FadeIn(set_2, shift=UP), run_time=tracker.duration * 0.4)

        with self.voiceover(text="A less idiotic way to look at this, is that we start with 0, and then we can define 1 and 2 and so on, and 3, and 4.") as tracker:
            label_0 = Text("0", font_size=24, color=YELLOW).next_to(set_empty, RIGHT, buff=0.5)
            label_1 = Text("1", font_size=24, color=YELLOW).next_to(set_1, RIGHT, buff=0.5)
            label_2 = Text("2", font_size=24, color=YELLOW).next_to(set_2, RIGHT, buff=0.5)
            
            set_3 = MathTex(r"\{\{\{\emptyset\}\}\}").move_to(RIGHT * ordinals_x + ORIGIN)
            label_3 = Text("3", font_size=24, color=YELLOW).next_to(set_3, RIGHT, buff=0.5)
            
            set_4 = MathTex(r"\{\{\{\{\emptyset\}\}\}\}").move_to(RIGHT * ordinals_x + UP * 1)
            label_4 = Text("4", font_size=24, color=YELLOW).next_to(set_4, RIGHT, buff=0.5)

            self.play(FadeIn(label_0), FadeIn(label_1), FadeIn(label_2), run_time=tracker.duration * 0.4)
            self.play(FadeIn(set_3, shift=UP), FadeIn(label_3), run_time=tracker.duration * 0.3)
            self.play(FadeIn(set_4, shift=UP), FadeIn(label_4), run_time=tracker.duration * 0.3)

        with self.voiceover(text="Then given two sets, we can form a set whose members are the pair of these sets.") as tracker:
            ax_pairing = MathTex(r"\text{Pairing: } \forall x \forall y \exists z \forall w (w \in z \leftrightarrow w = x \lor w = y)").scale(0.6).next_to(ax_singleton, UP, buff=0.8)
            self.play(FadeIn(ax_pairing, shift=RIGHT), run_time=tracker.duration)

        with self.voiceover(text="So given 0 and 2, we can define the set containing 0 and 2.") as tracker:
            set_0_2 = MathTex(r"\{0, 2\}").move_to(RIGHT * (ordinals_x + 1.5) + UP * 0.5)
            self.play(FadeIn(set_0_2, shift=LEFT), run_time=tracker.duration)

        with self.voiceover(text="We also have the power set axioms, which is more interesting that it seems at first, which just states that given any set X, there exists a set made up of all subsets of X.") as tracker:
            ax_powerset = MathTex(r"\text{Power Set: } \forall x \exists y \forall z (z \in y \leftrightarrow z \subseteq x)").scale(0.6).next_to(ax_pairing, UP, buff=0.8)
            self.play(FadeIn(ax_powerset, shift=RIGHT), run_time=tracker.duration)

        with self.voiceover(text="For example, if we have the set {1,2,3}, then this axiom asserts that there is also the following set.") as tracker:
            # Fade out everything built so far
            self.play(
                FadeOut(ax_existence, set_empty, ax_singleton, set_1, set_2, label_0, label_1, label_2, set_3, label_3, set_4, label_4, ax_pairing, set_0_2, ax_powerset),
                run_time=tracker.duration * 0.3
            )
            
            # Since everything else is gone, we can display the Hasse Diagram cleanly in the center
            hasse_diag = get_hasse_diagram().move_to(ORIGIN)
            self.play(Create(hasse_diag), run_time=tracker.duration * 0.7)
            
            self.wait(1)
            
class VHierarchyScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # --- Scene 1: Building the Hasse Diagram ---
        hasse_x = 3.0

        # Define elements for the linear left-side set definition
        set_x_tex = MathTex(r"X = \{1, 2, 3\}").to_edge(LEFT).shift(UP * 1.5 + RIGHT * 1)
        powerset_str = r"\mathcal{P}(X) = \{\emptyset, \{1\}, \{2\}, \{3\}, \\ \{1, 2\}, \{1, 3\}, \{2, 3\}, \{1, 2, 3\}\}"
        set_px_tex = MathTex(powerset_str).scale(0.8).next_to(set_x_tex, DOWN, aligned_edge=LEFT, buff=0.5)

        # Define Hasse diagram nodes 
        l0 = MathTex(r"\emptyset").scale(0.7).move_to(RIGHT * hasse_x + DOWN * 2)
        l1_1 = MathTex(r"\{1\}").scale(0.7)
        l1_2 = MathTex(r"\{2\}").scale(0.7)
        l1_3 = MathTex(r"\{3\}").scale(0.7)
        VGroup(l1_1, l1_2, l1_3).arrange(RIGHT, buff=0.8).move_to(RIGHT * hasse_x + DOWN * 0.75)
        
        l2_12 = MathTex(r"\{1,2\}").scale(0.7)
        l2_13 = MathTex(r"\{1,3\}").scale(0.7)
        l2_23 = MathTex(r"\{2,3\}").scale(0.7)
        VGroup(l2_12, l2_13, l2_23).arrange(RIGHT, buff=0.8).move_to(RIGHT * hasse_x + UP * 0.75)
        
        l3 = MathTex(r"\{1,2,3\}").scale(0.7).move_to(RIGHT * hasse_x + UP * 2)

        # Define edges
        edges = VGroup(
            Line(l0.get_top(), l1_1.get_bottom(), stroke_width=2, color=GRAY),
            Line(l0.get_top(), l1_2.get_bottom(), stroke_width=2, color=GRAY),
            Line(l0.get_top(), l1_3.get_bottom(), stroke_width=2, color=GRAY),
            Line(l1_1.get_top(), l2_12.get_bottom(), stroke_width=2, color=GRAY),
            Line(l1_1.get_top(), l2_13.get_bottom(), stroke_width=2, color=GRAY),
            Line(l1_2.get_top(), l2_12.get_bottom(), stroke_width=2, color=GRAY),
            Line(l1_2.get_top(), l2_23.get_bottom(), stroke_width=2, color=GRAY),
            Line(l1_3.get_top(), l2_13.get_bottom(), stroke_width=2, color=GRAY),
            Line(l1_3.get_top(), l2_23.get_bottom(), stroke_width=2, color=GRAY),
            Line(l2_12.get_top(), l3.get_bottom(), stroke_width=2, color=GRAY),
            Line(l2_13.get_top(), l3.get_bottom(), stroke_width=2, color=GRAY),
            Line(l2_23.get_top(), l3.get_bottom(), stroke_width=2, color=GRAY)
        )

        with self.voiceover(text="For example, if we have the set with {1,2,3} the power set is the following set.") as tracker:
            self.play(FadeIn(set_x_tex, shift=RIGHT), run_time=tracker.duration * 0.4)
            self.play(FadeIn(set_px_tex, shift=UP), run_time=tracker.duration * 0.6)

        with self.voiceover(text="So, it contains the individual elements,") as tracker:
            self.play(FadeIn(VGroup(l1_1, l1_2, l1_3), shift=UP), run_time=tracker.duration)

        with self.voiceover(text="the pairs of elements,") as tracker:
            self.play(FadeIn(VGroup(l2_12, l2_13, l2_23), shift=UP), run_time=tracker.duration)

        with self.voiceover(text="the whole set and the emptyset at the bottom, which is a subset of every set.") as tracker:
            self.play(FadeIn(l3, shift=DOWN), FadeIn(l0, shift=UP), run_time=tracker.duration * 0.4)
            self.play(Create(edges), run_time=tracker.duration * 0.6)

        with self.voiceover(text="We will now use this to define the so-called Von Neuman Hierarchy of sets V, which is often considered to be THE Universe of sets.") as tracker:
            self.wait(tracker.duration)

        # --- Scene 2: The Von Neumann Hierarchy ---
        with self.voiceover(text="Again, we start with the empty set, and then successively take the power set of the previous level.") as tracker:
            self.play(
                FadeOut(set_x_tex, set_px_tex, l0, l1_1, l1_2, l1_3, l2_12, l2_13, l2_23, l3, edges),
                run_time=tracker.duration * 0.4
            )
            v0 = MathTex(r"V_0 = \emptyset").move_to(DOWN * 3)
            self.play(FadeIn(v0, shift=UP), run_time=tracker.duration * 0.6)

        # V Hierarchy sets
        v1 = MathTex(r"V_1 = \{\emptyset\}").move_to(DOWN * 2)
        v2 = MathTex(r"V_2 = \{\emptyset, \{\emptyset\}\}").move_to(DOWN * 1)
        v3 = MathTex(r"V_3 = \{\emptyset, \{\emptyset\}, \{\{\emptyset\}\}, \{\emptyset, \{\emptyset\}\}\}").move_to(ORIGIN)
        v4 = MathTex(r"\dots \quad V_4 \quad \dots").move_to(UP * 1)
        v5 = MathTex(r"\dots \quad V_5 \quad \dots").move_to(UP * 2)
        v_dots_top = MathTex(r"\vdots").move_to(UP * 3)
                # Number sizing labels
        sz_x = 4.0
        s0 = MathTex(r"0", color=YELLOW).move_to(RIGHT * sz_x + DOWN * 3).align_to(v0, DOWN)
        s1 = MathTex(r"2^0 = 1", color=YELLOW).move_to(RIGHT * sz_x + DOWN * 2).align_to(v1, DOWN)
        s2 = MathTex(r"2^1 = 2", color=YELLOW).move_to(RIGHT * sz_x + DOWN * 1).align_to(v2, DOWN)
        s3 = MathTex(r"2^2 = 4", color=YELLOW).move_to(RIGHT * sz_x + ORIGIN).align_to(v3, DOWN)
        s4 = MathTex(r"2^4 = 16", color=YELLOW).move_to(RIGHT * sz_x + UP * 1).align_to(v4, DOWN)
        s5 = MathTex(r"2^{16} = 65,536", color=YELLOW).move_to(RIGHT * sz_x + UP * 2).align_to(v5, DOWN)
        s6 = MathTex(r"2^{65,536}", color=YELLOW).move_to(RIGHT * sz_x + UP * 3).align_to(v_dots_top, DOWN)

        with self.voiceover(text="So we get the set with the emptyset at the first level, then the emptyset plus the set with the emptyset at the second level,") as tracker:
            self.play(FadeIn(v1, shift=UP), run_time=tracker.duration * 0.5)
            self.play(FadeIn(v2, shift=UP), run_time=tracker.duration * 0.5)

        with self.voiceover(text="then the emptyset, set with the emptyset and then set with the set with the emptyset set.") as tracker:
            self.play(FadeIn(v3, shift=UP), run_time=tracker.duration)

        with self.voiceover(text="This seems tame and boring, but this is a hyper-exponential function, the size of each level is the size of the previous level raised to the power of 2.") as tracker:
            self.play(FadeIn(v4, shift=UP), FadeIn(s0, shift=LEFT),
                FadeIn(s1, shift=LEFT),
                FadeIn(s2, shift=LEFT),
                run_time=tracker.duration)
            
            
        with self.voiceover(text="So, the third level has 16 elements, the fourth level has 65 Thousand, and the fifth level has more atoms then there are in the Universe.") as tracker:
            self.play(FadeIn(v5, shift=UP),  run_time=tracker.duration * 0.6)
            self.play(FadeIn(v_dots_top), run_time=tracker.duration * 0.4)
        
        
            self.play(
                FadeIn(s3, shift=LEFT),
                FadeIn(s4, shift=LEFT),
                FadeIn(s5, shift=LEFT),
                FadeIn(s6, shift=LEFT),
                run_time=tracker.duration * 0.6
            )
