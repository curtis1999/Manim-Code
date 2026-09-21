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
            ("Pairing", r"\forall x \forall y \exists z \forall w (w \in z \leftrightarrow w = x \lor w = y)"),
            ("Union", r"\forall x \exists y \forall z (z \in y \leftrightarrow \exists w (z \in w \land w \in x))"),
            ("Power Set", r"\forall x \exists y \forall z (\forall w\in z (w \in z \rightarrow w\in y)"),
            ("Regularity", r"\forall x (x \neq \emptyset \rightarrow \exists y \in x (x \cap y = \emptyset))"),           
            ("Separation", r"\forall x \exists y \forall z (z \in y \leftrightarrow z \in x \land \varphi(z))"),
            ("Replacement", r"\forall x (\forall y \in x \exists! z \varphi(y,z) \rightarrow \exists w \forall y \in x \exists z \in w \varphi(y,z))"),
            ("Infinity", r"\exists x (\emptyset \in x \land \forall y \in x (y \cup \{y\} \in x))"),
            ("Choice", r"\forall X (\emptyset \notin X \rightarrow \exists f: X \rightarrow \cup X \land \forall Y \in X(f(Y)\in Y))")
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
            self.wait(tracker.duration * 0.9)
            self.add(zfc_names, zfc_formulas)

        # --- Scene 2: Display ZFC ---
        with self.voiceover(text="Which is just the set of all first order consequences of these axioms right here.") as tracker:
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
                run_time=tracker.duration * 0.25
            )

        # --- Scene 4: Inputs and Outputs ---
        with self.voiceover(text="In a later video we will open the hood of this black box computer, but for this video, just see it as some computer which takes in sentences written in first order logic, and it outputs the logical consequences of these sentences.") as tracker:
            
            # Output x = x
            thm_output = MathTex(r"x = x").next_to(output_line, RIGHT, buff=0.2)
            self.wait(tracker.duration * 0.6)
            self.play(FadeIn(thm_output, shift=RIGHT), run_time=tracker.duration * 0.2)

            # Transition x = x into x \notin x
            thm_2 = MathTex(r"x \notin x").move_to(thm_output).align_to(thm_output, LEFT)
            self.play(Transform(thm_output, thm_2), run_time=tracker.duration * 0.2)

        # --- Scene 5: General Axioms and ALL OF MATH ---
        with self.voiceover(text="The ultimate goal, is to find some set of axioms which we could feed into our theorem prover such that it outputs every true mathematical statement, without ever outputting a false statement.") as tracker:
            
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
                run_time=tracker.duration * 0.2
            )
            self.wait()

        # --- Scene 6: Godel ---
        with self.voiceover(text="Again, this is impossible due to this guy,") as tracker:
            # Updated to requested image name
            godel_img = ImageMobject("image_Godel.jpg").scale(1.5).to_edge(UP*1.3).shift(RIGHT*2.5)
            self.play(FadeIn(godel_img), run_time=tracker.duration)

        # --- Scene 7: Return to ZFC ---
        with self.voiceover(text="so the best we can hope for is some set of axioms which can output pretty much all of math.  So then the question is, what axioms should we feed in?") as tracker:
            
            
            # Update to MOST OF MATH
            most_of_math = Text("MOST OF MATH", color=GOLD, font_size=36).move_to(thm_output).align_to(thm_output, LEFT)
            self.play(
                FadeOut(godel_img),
                Transform(thm_output, most_of_math),
                run_time=tracker.duration * 0.25
            )
            
            self.wait()
            
class SetTheoryUniverseScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # --- Helper: Theorem Prover Box ---
        def create_tp_box(label_text="Theorem\nProver", num_inputs=3, box_height=2.0, box_width=2.0):
            label = Text(label_text, font_size=24)
            rect = Rectangle(width=box_width, height=box_height, color=BLUE, fill_opacity=0.1, stroke_width=4)
            label.move_to(rect.get_center())
            inputs = VGroup()
            spacing = (box_height - 0.5) / (num_inputs - 1) if num_inputs > 1 else 0
            start_y = (box_height / 2) - 0.25
            for i in range(num_inputs):
                y_pos = start_y - i * spacing
                line = Line(LEFT * 0.5, ORIGIN).next_to(rect, LEFT, buff=0, aligned_edge=UP).shift(DOWN * (box_height/2 - y_pos))
                inputs.add(line)
            output = Line(ORIGIN, RIGHT * 0.8).next_to(rect, RIGHT, buff=0)
            return VGroup(rect, label, inputs, output)

        # --- Initial Setup ---
        tp_box = create_tp_box("Theorem\nProver", num_inputs=9, box_height=6.0, box_width=3.0).move_to(ORIGIN)
        input_lines = tp_box[2]
        
        general_axioms = VGroup()
        for i in range(8):
            ax = MathTex(f"A_{i+1}").scale(0.8).next_to(input_lines[i], LEFT, buff=0.1)
            general_axioms.add(ax)
        an = MathTex(r"A_n").scale(0.8).next_to(input_lines[-1], LEFT, buff=0.1)
        general_axioms.add(an)
        
        self.add(tp_box, general_axioms)

        # --- Scene 1: Peano Arithmetic & Number Line ---
        pa_data = [
            r"\forall x (x=x)\land \forall x,y (x=y\rightarrow y=x)",
            r"\forall x,y,z (x=y\land y=z\rightarrow x=z)",
            r"\forall x (0 \neq S(x))",
            r"\forall x \forall y (S(x) = S(y) \rightarrow x = y)",
            r"\forall x (x + 0 = x)",
            r"\forall x \forall y (x + S(y) = S(x + y))",
            r"\forall x (x \times 0 = 0)",
            r"\forall x \forall y (x \times S(y) = (x \times y) + x)",
            r"\forall X (0\in X \land \forall n (n\in X\rightarrow S(n)\in X) \rightarrow X=\mathbb{N})"
        ]
        
        pa_axioms = VGroup()
        for i, formula in enumerate(pa_data):
            f_tex = MathTex(formula, font_size=25).next_to(input_lines[i], LEFT, buff=0.1)
            pa_axioms.add(f_tex)

        with self.voiceover(text="We can consider these axioms right here, which define Peano Arithmetic, which essentially just describe the number line.  Which would be fine if math stopped around grade 3, but if we want to be able to describe all of math, we will need more than just the natural numbers with addition and multiplication.") as tracker:
            self.play(Transform(general_axioms, pa_axioms), run_time=tracker.duration * 0.2)
            
            number_line = NumberLine(
                x_range=[0, 7, 1], length=10, color=WHITE,
                include_numbers=True, numbers_to_include=[0, 1, 2, 3, 4, 5, 6, 7]
            ).move_to(DOWN * 4)
            self.wait(tracker.duration * 0.3)
            self.play(Create(number_line), run_time=tracker.duration * 0.1)

        with self.voiceover(text="This is where set theory comes in.") as tracker:
            self.play(
                FadeOut(general_axioms), FadeOut(tp_box), FadeOut(number_line),
                run_time=tracker.duration * 0.4
            )

        with self.voiceover(text="Everything in math can be seen as a set, obviously numbers are sets, but also functions are sets of pairs, graphs are sets of points and edges and even proofs are sets of formulas.") as tracker:
            # 1. Numbers at the top
            number_sets = MathTex(r"\mathbb{N}, \mathbb{Q}, \mathbb{A}, \mathbb{R}").scale(1.2).to_edge(UP)
            self.wait(tracker.duration*0.1)
            self.play(FadeIn(number_sets, shift=DOWN), run_time=tracker.duration * 0.15)
            
            # 2. Abstract topological spaces and function
            space_X = Ellipse(width=1.5, height=2.2, color=TEAL, fill_opacity=0.2).shift(UP * 1.5 + LEFT * 1)
            space_Y = Ellipse(width=1.5, height=2.2, color=PURPLE, fill_opacity=0.2).shift(UP * 1.5 + RIGHT * 2)
            label_X = MathTex("X").move_to(space_X.get_top() + DOWN*0.4)
            label_Y = MathTex("Y").move_to(space_Y.get_top() + DOWN*0.4)
            func_arrow = CurvedArrow(space_X.get_right(), space_Y.get_left(), angle=-PI/4, color=YELLOW)
            func_label = MathTex("f").next_to(func_arrow, UP, buff=0.1)
            abstract_func = VGroup(space_X, space_Y, label_X, label_Y, func_arrow, func_label)
            
            self.play(FadeIn(abstract_func), run_time=tracker.duration * 0.2)
            
            # 3. Complex Graph as a set
            v1 = Dot(point=UP*0.8 + LEFT*0.8, color=BLUE)
            v2 = Dot(point=UP*0.8 + RIGHT*0.8, color=BLUE)
            v3 = Dot(point=LEFT*1.8, color=BLUE)
            v4 = Dot(point=ORIGIN, color=BLUE)
            v5 = Dot(point=RIGHT*1.8, color=BLUE)
            v6 = Dot(point=DOWN*1.2 + LEFT*1.2, color=BLUE)
            v7 = Dot(point=DOWN*1.2 + ORIGIN, color=BLUE)
            v8 = Dot(point=DOWN*1.2 + RIGHT*1.2, color=BLUE)
            
            edges = [
                (v1,v2), (v1,v3), (v1,v4), (v2,v4), (v2,v5),
                (v3,v6), (v4,v6), (v4,v7), (v6,v7), (v7,v8), (v5,v8)
            ]
            graph_group = VGroup(*[v1,v2,v3,v4,v5,v6,v7,v8])
            for edge in edges:
                graph_group.add(Line(edge[0].get_center(), edge[1].get_center(), stroke_width=3, color=ORANGE))
            
            for v in [v1,v2,v3,v4,v5,v6,v7,v8]:
                v.set_z_index(1)
            self.wait(tracker.duration * 0.2)
            graph_group.scale(0.8).move_to(DOWN*1.5 + LEFT*2)
            self.play(FadeIn(graph_group), run_time=tracker.duration * 0.25)
            
            # 4. Abstract proof tree
            pt_node1 = MathTex(r"\Gamma \vdash A")
            pt_node2 = MathTex(r"\Gamma \vdash A \rightarrow B")
            pt_line = Line(LEFT*1.5, RIGHT*1.5)
            pt_node3 = MathTex(r"\Gamma \vdash B")
            
            pt_node1.shift(LEFT*1 + UP*0.5)
            pt_node2.shift(RIGHT*1 + UP*0.5)
            pt_line.next_to(VGroup(pt_node1, pt_node2), DOWN, buff=0.2)
            pt_node3.next_to(pt_line, DOWN, buff=0.2)
            
            proof_tree = VGroup(pt_node1, pt_node2, pt_line, pt_node3).scale(0.7).move_to(DOWN*1.5 + RIGHT*3)
            self.play(FadeIn(proof_tree), run_time=tracker.duration * 0.25)

        with self.voiceover(text="So, if we can define what is, and what is not a valid set, then we will have defined what is and what is not part of math.") as tracker:
            self.wait(tracker.duration)

        with self.voiceover(text="But a set is so basic, that is hard to define. If you try to define a set, you will likely say something like a collection of things or a class of objects. But then, how do you define a collection or a class? The axioms of ZFC are a good attempt to precisely define the notion of a set.") as tracker:
            self.play(
                FadeOut(number_sets), FadeOut(abstract_func), FadeOut(graph_group), FadeOut(proof_tree), 
                run_time=tracker.duration * 0.3
            )
            self.wait(tracker.duration * 0.7)

        # --- Scene 3: Words & Axiom Stacking ---
        with self.voiceover(text="Now, when we want to start defining the set theory, we run into a fundamental issue with definitions. Words are defined using other words, so when we want to define the first word, what do we do? So there has to be some sort of a-priori assumptions, which are the axioms.") as tracker:
            def_text = Text("Def: WORD = MORE WORDS", font_size=40, color=YELLOW)
            self.play(FadeIn(def_text), run_time=tracker.duration * 0.2)
            self.wait(tracker.duration * 0.6)
            self.play(FadeOut(def_text), run_time=tracker.duration * 0.2)

        # --- Scene 4: Spine of the Universe ---
        ordinals_x = 2.0
        axioms_x = -4.2
        x_align = ordinals_x + 3.0  # Vertical alignment for the natural numbers labels

        with self.voiceover(text="The first axiom we will look at, is the axiom of existence, which simply asserts that there is some set. Specifically, that there is a set with no members, the so called empty set. So at the base of this whole set theoretic Universe, is that assumption that nothing exists.") as tracker:
            ax_existence = MathTex(r"\text{Existence: } \exists x \forall y (y \notin x)").scale(0.6).move_to(RIGHT * axioms_x + DOWN * 3)
            set_empty = MathTex(r"\emptyset").move_to(RIGHT * ordinals_x + DOWN * 3)
            # Sped up fade in
            self.play(FadeIn(ax_existence, shift=RIGHT), FadeIn(set_empty, shift=UP), run_time=tracker.duration*0.1)

        with self.voiceover(text="We know that the emptyset is unique, due to the axiom of extensionality, which just states that two sets are equal iff they have the same members.") as tracker:
            ax_extensionality = MathTex(r"\text{Extensionality: } \forall x \forall y (x=y \leftrightarrow \forall z (z\in x\leftrightarrow z \in y))").scale(0.6).next_to(ax_existence, UP, buff=0.8).align_to(ax_existence, LEFT)
            # Sped up fade in
            self.play(FadeIn(ax_extensionality, shift=RIGHT*1.1), run_time=tracker.duration*0.5)

        with self.voiceover(text="Once we have sets, we can define other sets, for example using the pairing axiom, which just states that given two sets X and Y, we can form a set with X and Y as members.") as tracker:
            ax_pairing = MathTex(r"\text{Pairing: } \forall x \forall y \exists z (x\in z\land y\in z)").scale(0.6).next_to(ax_extensionality, UP, buff=0.8).align_to(ax_existence, LEFT)
            # Sped up fade in
            self.play(FadeIn(ax_pairing, shift=RIGHT), run_time=tracker.duration*0.5)

        with self.voiceover(text="Applying this with the empty set with itself, gives us the set containing the emptyset. So, we start with nothing, then we can put a bag around it and so we no longer have nothing, we have a bag with nothing in it. ") as tracker:
            # Shifted up to compress vertical spacing
            ord_1 = MathTex(r"\{\emptyset\}").move_to(RIGHT * ordinals_x + DOWN * 1.8)
            self.play(FadeIn(ord_1, shift=UP), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.4)

        with self.voiceover(text="This is obviously pretty dumb, but we are essentially defining the natural numbers.  The emptyset is 0, the set containing the empty set is 1, and then from here, just like Russian Dolls, we will define the successor to be the set of all predecessors.") as tracker:
            # Perfectly aligned labels relying on the Y-coordinate of their respective sets
            label_0 = Text("0", font_size=24, color=YELLOW).move_to(np.array([x_align, set_empty.get_center()[1], 0]))
            label_1 = Text("1", font_size=24, color=YELLOW).move_to(np.array([x_align, ord_1.get_center()[1], 0]))
            
            # Successor function positioned high enough to clear ord_4 later
            succ_func = MathTex(r"S(n) = n \cup \{n\}", color=GOLD).move_to(RIGHT * 3.5 + UP * 3.2)
            ax_union = MathTex(r"\text{Union: } \forall x \exists y \forall z (\dots)").scale(0.6).next_to(ax_pairing, UP, buff=0.8).align_to(ax_existence, LEFT)
            # Sequential fading
            self.wait(tracker.duration * 0.15)
            self.play(FadeIn(label_0), run_time=tracker.duration * 0.15)
            self.play(FadeIn(label_1), run_time=tracker.duration * 0.15)
            self.play(FadeIn(succ_func), run_time=tracker.duration * 0.5)
            self.play(FadeIn(ax_union, shift=RIGHT), run_time=tracker.duration * 0.2)
            

        with self.voiceover(text="So, we can define 2 as the set containing 0 and 1.  Then 3 as the set with 0,1 and 2.  Then we can continue this indefinitely, resulting in the ordinal numbers.") as tracker:
            # Compressing the vertical coordinates to leave room at the top
            ord_2 = MathTex(r"\{\emptyset, \{\emptyset\}\}").scale(0.85).move_to(RIGHT * ordinals_x + DOWN * 0.6)
            ord_3 = MathTex(r"\{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}\}").scale(0.65).move_to(RIGHT * ordinals_x + UP * 0.6)
            ord_4 = MathTex(r"\{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}, \{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}\}\}").scale(0.55).move_to(RIGHT * ordinals_x + UP * 1.8)
            
            label_2 = Text("2", font_size=24, color=YELLOW).move_to(np.array([x_align, ord_2.get_center()[1], 0]))          
            label_3 = Text("3", font_size=24, color=YELLOW).move_to(np.array([x_align, ord_3.get_center()[1], 0]))
            label_4 = Text("4", font_size=24, color=YELLOW).move_to(np.array([x_align, ord_4.get_center()[1], 0]))
            
            self.play(FadeIn(ord_2), FadeIn(label_2), run_time=tracker.duration * 0.2)
            self.play(FadeIn(ord_3, shift=UP), FadeIn(label_3), run_time=tracker.duration * 0.4)
            self.wait(tracker.duration * 0.1)
            self.play(FadeIn(ord_4, shift=UP), FadeIn(label_4), run_time=tracker.duration * 0.4)

        with self.voiceover(text="The ordinals, which are essentially just the natural numbers, will form the spine of the set theoretic Universe.  We will use the following axiom, known as the power set axiom to define more complicated sets") as tracker:
            powerset_str = r"\mathcal{P}(X) = \{\emptyset, \{1\}, \{2\}, \{3\}, \\ \{1, 2\}, \{1, 3\}, \{2, 3\}, \{1, 2, 3\}\}"
            set_px_tex = MathTex(powerset_str).scale(0.8).next_to(set_x_tex, DOWN, aligned_edge=LEFT, buff=0.5)

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
