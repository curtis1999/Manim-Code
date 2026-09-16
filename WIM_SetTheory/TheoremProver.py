from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import random

class PhilosophyAndMechanicsOfMath(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        
        
        # --- PART 2: The Logical Mechanics of Mathematics ---
        # Clear screen to begin next section centrally

        # Function for ZFC axioms text layout
        def create_zfc_item(name, formula):
            name_text = Text(name + ": ", font_size=28, color=TEAL)
            form_tex = MathTex(formula, font_size=32)
            item = VGroup(name_text, form_tex).arrange(RIGHT, aligned_edge=DOWN)
            return item

        # Helper function for the Theorem Prover Box
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

        # --- Scene 1: ZFC Set Theory & Axioms Display ---
        with self.voiceover(text="One modern answer to the question, is simply math is the set of theorems of ZFC set theory.") as tracker:
            zfc_title = Text("ZFC Set Theory", font_size=48, color=YELLOW).to_edge(UP)
            
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
            
            zfc_axioms_full = VGroup()
            zfc_names = VGroup()
            zfc_formulas = VGroup()

            # Construct and arrange the list centrally
            for name, formula in zfc_data:
                name_tex = Text(name + ": ", font_size=28, color=TEAL)
                form_tex = MathTex(formula, font_size=32)
                row = VGroup(name_tex, form_tex).arrange(RIGHT, aligned_edge=DOWN)
                zfc_axioms_full.add(row)
                zfc_names.add(name_tex)
                zfc_formulas.add(form_tex)

            zfc_axioms_full.arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(zfc_title, DOWN, buff=0.5)

            # Display the whole list, larger font
            self.play(Write(zfc_title), run_time=tracker.duration * 0.2)
            self.play(FadeIn(zfc_axioms_full, lag_ratio=0.1), run_time=tracker.duration * 0.8)

        with self.voiceover(text="Where ZFC stands for Zermelo, Fraenkel plus Choice, and is axiomatized by these set of axioms. We will answer why these particular axioms later, but for now just know that these are the best attempt to formalize all of mathematics into a single language.") as tracker:
            self.wait(tracker.duration)

        # --- Scene 2: The Theorem Prover ---
        with self.voiceover(text="The theory of ZFC is every logical consequence of these axioms, which we can think of as all outputs of a certain special theorem proving computer.") as tracker:
            # Shift left, shrink, and fade out names
            self.play(
                FadeOut(zfc_title),
                FadeOut(zfc_names),
                zfc_formulas.animate.arrange(DOWN, aligned_edge=LEFT, buff=0.2).scale(0.6).to_edge(LEFT).shift(DOWN*0.5),
                run_time=tracker.duration * 0.4
            )
            
            # Giant Theorem Prover expecting 9 inputs
            giant_tp = create_tp_box("Theorem\nProver", num_inputs=9, box_height=6.0, box_width=3.0).shift(RIGHT * 1)
            self.play(Create(giant_tp), run_time=tracker.duration * 0.6)

        with self.voiceover(text="So, we feed in the axioms, and it outputs the logical consequences of these axioms, which we call the theorems.") as tracker:
            # Align axioms to inputs
            input_lines = giant_tp[2]
            animations = []
            for i, ax in enumerate(zfc_formulas):
                animations.append(ax.animate.next_to(input_lines[i], LEFT, buff=0.1))
            
            self.play(*animations, run_time=tracker.duration * 0.5)
            
            # Output x = x
            output_line = giant_tp[3]
            thm_group = VGroup()
            thm_1 = MathTex(r"x = x").next_to(output_line, RIGHT, buff=0.2)
            thm_group.add(thm_1)
            self.play(FadeIn(thm_1, shift=RIGHT), run_time=tracker.duration * 0.5)

        with self.voiceover(text="Then we can feed these theorems back in as input, and we continue deriving new mathematical theorems.") as tracker:
            
            # 1st Feedback Loop
            loop_arrow_1 = CurvedArrow(thm_1.get_right() + RIGHT*0.2, input_lines[0].get_left() + LEFT*0.5, angle=-TAU/2.5, color=YELLOW)
            self.play(Create(loop_arrow_1), run_time=tracker.duration * 0.2)
            
            # Prepend x \notin x, moving x=x down
            thm_2 = MathTex(r"x \notin x").move_to(thm_1.get_center()).align_to(thm_1, LEFT)
            
            self.play(
                thm_group.animate.shift(DOWN * 0.8),
                FadeIn(thm_2, shift=DOWN),
                FadeOut(loop_arrow_1),
                run_time=tracker.duration * 0.2
            )
            thm_group.add(thm_2)
            
            # 2nd Feedback Loop
            loop_arrow_2 = CurvedArrow(thm_2.get_right() + RIGHT*0.2, input_lines[-1].get_left() + LEFT*0.5, angle=TAU/2.5, color=ORANGE)
            self.play(Create(loop_arrow_2), run_time=tracker.duration * 0.2)

            # Complex Set Theory Formula (Mutual Subset Equality)
            thm_3 = MathTex(r"\forall a \forall b ((\forall x (x \in a \rightarrow x \in b) \land \forall y (y \in b \rightarrow y \in a)) \rightarrow a = b)")
            thm_3.scale(0.5).move_to(thm_2.get_center()).align_to(thm_2, LEFT)
            
            self.play(
                thm_group.animate.shift(DOWN * 0.8),
                FadeIn(thm_3, shift=DOWN),
                FadeOut(loop_arrow_2),
                run_time=tracker.duration * 0.4
            )
            thm_group.add(thm_3)

        # --- Scene 3: The Tree of Proofs ---
        with self.voiceover(text="So, there is some pre-existing space of all possible proofs from this set of axioms, and the goal of mathematics is to explore as much of this space as possible.") as tracker:
            group_all = VGroup(zfc_formulas, giant_tp, thm_group)
            
            # Visual shrink & move left
            self.play(
                group_all.animate.scale(0.4).to_edge(LEFT),
                run_time=tracker.duration * 0.2
            )
            
            # Create a larger, visible expanding tree, endless illusion
            tree_nodes = VGroup()
            tree_edges = VGroup()
            depths = 8 # Endless illusion
            
            # Store data as: (position_vector, is_main_path)
            start_points = [(group_all.get_right() + UP*(i*0.6 - 0.6), True) for i in range(3)]
            current_layer = start_points
            
            # Lists to store elements for selective highlighting
            all_dots = []
            all_lines = []
            main_dots = []
            main_lines = []
            
            # Generate the tree structure procedurally
            for depth in range(depths):
                next_layer = []
                for pos, is_main in current_layer:
                    # Add node, default dim white
                    dot = Dot(pos, radius=0.03, color=WHITE).set_opacity(0.15)
                    tree_nodes.add(dot)
                    all_dots.append(dot)
                    if is_main:
                        main_dots.append(dot)
                    
                    if depth < depths - 1:
                        # Procedurally generate structure, branching main path vs side
                        children_count = random.randint(1, 3) if is_main else random.randint(0, 2)
                        # Ensure side branches die off visually
                        if not is_main and random.random() < 0.7: 
                            children_count = 0 
                        
                        # Find a main path child
                        main_child_idx = random.randint(0, children_count-1) if is_main else -1
                        
                        for i in range(children_count):
                            # Move right and apply some noise
                            new_pos = pos + RIGHT * 1.2 + UP * random.uniform(-0.8, 0.8) * (1.0 - depth*0.1)
                            child_is_main = (i == main_child_idx)
                            next_layer.append((new_pos, child_is_main))
                            
                            edge = Line(pos, new_pos, stroke_width=1.5, color=WHITE).set_opacity(0.15)
                            tree_edges.add(edge)
                            all_lines.append(edge)
                            if is_main and child_is_main:
                                main_lines.append(edge)
                                
                current_layer = next_layer

            # Add final layer dots
            for pos, is_main in current_layer:
                dot = Dot(pos, radius=0.03, color=WHITE).set_opacity(0.15)
                tree_nodes.add(dot)
                all_dots.append(dot)
                if is_main:
                    main_dots.append(dot)

            # Display tree, already dimmed
            self.play(FadeIn(tree_edges), FadeIn(tree_nodes), run_time=tracker.duration * 0.4)
            
            # Highlight only the main paths (nodes and edges become full white/thicker)
            highlight_anims = [d.animate.set_opacity(1.0) for d in main_dots] + \
                              [l.animate.set_opacity(1.0).set_stroke(width=3) for l in main_lines]
                              
            self.play(*highlight_anims, run_time=tracker.duration * 0.4)

        # --- Scene 4: Inside the Theorem Prover (Hilbert Calculus) ---
        with self.voiceover(text="There are multiple ways of formalizing what the inside of this theorem proving computer.") as tracker:
            # Clear tree part
            self.play(FadeOut(tree_nodes), FadeOut(tree_edges), FadeOut(zfc_formulas), FadeOut(thm_group), run_time=tracker.duration * 0.5)
            
            # Make TP frame the entire screen for 'view change' simulation
            self.play(
                giant_tp[0].animate.stretch_to_fit_width(13).stretch_to_fit_height(7).move_to(ORIGIN),
                FadeOut(giant_tp[1]), FadeOut(giant_tp[2]), FadeOut(giant_tp[3]),
                run_time=tracker.duration * 0.5
            )

        with self.voiceover(text="Perhaps the simplest is with the so called Hilbert Calculus, which is just this set of axioms equipped with modus ponens.") as tracker:
            
            # Hilbert Axioms (image_0.png) - Substring isolation for visual grouping
            hilbert_axioms = VGroup(
                MathTex(r"\mathbf{A1} \ (\varphi \rightarrow (\psi \rightarrow \varphi))", substrings_to_isolate=[r"\rightarrow", r"\neg", r"\forall"]),
                MathTex(r"\mathbf{A2} \ ((\varphi \rightarrow (\psi \rightarrow \chi)) \rightarrow ((\varphi \rightarrow \psi) \rightarrow (\varphi \rightarrow \chi)))", substrings_to_isolate=[r"\rightarrow", r"\neg", r"\forall"]),
                MathTex(r"\mathbf{A3} \ ((\neg\varphi \rightarrow \neg\psi) \rightarrow ((\neg\varphi \rightarrow \psi) \rightarrow \varphi))", substrings_to_isolate=[r"\rightarrow", r"\neg", r"\forall"]),
                MathTex(r"\mathbf{A4} \ (\forall x\varphi \rightarrow \varphi(x/t))", substrings_to_isolate=[r"\rightarrow", r"\neg", r"\forall"]),
                MathTex(r"\mathbf{A5} \ (\forall x(\varphi \rightarrow \psi) \rightarrow (\forall x\varphi \rightarrow \forall x\psi))", substrings_to_isolate=[r"\rightarrow", r"\neg", r"\forall"]),
                MathTex(r"\mathbf{A6} \ (\varphi \rightarrow \forall x\varphi)", substrings_to_isolate=[r"\rightarrow", r"\neg", r"\forall"])
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.7).to_edge(LEFT, buff=1)

            # Display axioms FIRST
            self.play(FadeIn(hilbert_axioms, shift=RIGHT), run_time=tracker.duration * 0.6)
            
            # Then display MP diagram above (image_3.png visual proxy, after axioms)
            mp_rule_top = MathTex(r"\frac{\varphi \quad (\varphi \rightarrow \psi)}{\psi} \quad (\text{MP})", font_size=48).to_edge(UP, buff=1)
            self.play(Write(mp_rule_top), run_time=tracker.duration * 0.4)

        with self.voiceover(text="These axioms determine the behaviour of the logical negation, implication, and universal quantifier, and they turn out to be all that we need to formalize first order logic.") as tracker:
            
            # Sequential display of large font symbols below block, aligned with speech
            sym_neg = MathTex(r"\neg", font_size=120, color=RED).move_to(RIGHT * 3 + UP * 1)
            sym_imp = MathTex(r"\rightarrow", font_size=120, color=YELLOW).move_to(RIGHT * 3)
            sym_forall = MathTex(r"\forall", font_size=120, color=GREEN).move_to(RIGHT * 3 + DOWN * 1)

            self.play(FadeIn(sym_neg, scale=0.5), run_time=tracker.duration * 0.3)
            self.play(FadeIn(sym_imp, scale=0.5), run_time=tracker.duration * 0.3)
            self.play(FadeIn(sym_forall, scale=0.5), run_time=tracker.duration * 0.4)

        # --- Scene 5: Modus Ponens dynamic visual sequence ---
        with self.voiceover(text="Modus ponens, can be seen as the application of a computer program, where phi implies psi means that it takes in phi and outputs psi, so if we then feed in phi we get psi.") as tracker:
            # Clear screen parts for clean derivation visual
            self.play(FadeOut(sym_neg), FadeOut(sym_imp), FadeOut(sym_forall), FadeOut(mp_rule_top), run_time=tracker.duration * 0.1)
            
            # Visual MP structure simulation centrally (using phi/psi)
            # Split rule centrally for perfect alignment of inputs
            rule_bot = MathTex(r"(", r"\varphi", r"\rightarrow", r"\psi", r")").scale(1.2).move_to(RIGHT * 3.5)
            self.play(Write(rule_bot), run_time=tracker.duration * 0.2)
            
            # Input phi appears above, perfectly aligned with bot index [1]
            rule_top = MathTex(r"\varphi").scale(1.2).next_to(rule_bot, UP, buff=1)
            self.play(FadeIn(rule_top, shift=DOWN), run_time=tracker.duration * 0.2)
            
            # Drop input exactly onto slot
            self.play(rule_top.animate.move_to(rule_bot[1].get_center()), run_time=tracker.duration * 0.2)
            
            # Indoctrinating input/output slots (image_3.png style indication)
            self.play(Indicate(rule_bot[1], color=GREEN), Indicate(rule_bot[3], color=YELLOW), run_time=tracker.duration * 0.1)
            
            # Transform from copy outputs result (image_1.png step 3 style logic indication)
            rule_out = MathTex(r"\psi").scale(1.2).set_color(YELLOW).next_to(rule_bot, DOWN, buff=1)
            self.play(TransformFromCopy(rule_bot[3], rule_out), run_time=tracker.duration * 0.2)

        with self.voiceover(text="Not rocket science. But the necessary complexity comes from the fact that we can pass functions as input to other functions.") as tracker:
            # Clear previous derivations
            self.play(FadeOut(rule_top), FadeOut(rule_out), run_time=tracker.duration * 0.2)
            
            # Transform rule_bot into complex formula 1 (image_1.png step 1 substitution visual)
            # Re-creating formula part structure for exact index mapping
            bot_complex = MathTex(r"((", r"\varphi \rightarrow (\varphi \rightarrow \varphi)", r")", r"\rightarrow", r"(\varphi \rightarrow \varphi))").scale(0.8).move_to(RIGHT * 3.5)
            self.play(Transform(rule_bot, bot_complex), run_time=tracker.duration * 0.4)
            
            # Substituted A1 appears above, perfectly aligned as input to bot index [1]
            # (image_1.png step 2 logic indication)
            top_complex = MathTex(r"(\varphi \rightarrow (\varphi \rightarrow \varphi))").scale(0.8).next_to(bot_complex, UP, buff=1)
            self.play(FadeIn(top_complex, shift=DOWN), run_time=tracker.duration * 0.4)

            # Map the complex input perfectly onto slot [1]
            self.play(top_complex.animate.move_to(bot_complex[1].get_center()), run_time=tracker.duration * 0.4)
            
            # Transform from copy outputs complex result (image_1.png step 3 visual)
            out_complex = MathTex(r"(\varphi \rightarrow \varphi)").scale(0.8).set_color(YELLOW).next_to(bot_complex, DOWN, buff=1)
            self.play(TransformFromCopy(bot_complex[4], out_complex), run_time=tracker.duration * 0.4)

        with self.voiceover(text="So we can design or derive, complex interconnect circuits of logical variables using these axioms.") as tracker:
            # Shift Derived output to become new input (Cascade visual complexity)
            # Fade parts, transform derived complex output to clean white white for next step
            self.play(FadeOut(top_complex), FadeOut(rule_bot), out_complex.animate.set_color(WHITE).shift(UP*2), run_time=tracker.duration * 0.3)
            
            # New Complex formula layer 2 (simulating cascading circuitry)
            bot_complex_2 = MathTex(r"((", r"\varphi \rightarrow \varphi", r")", r"\rightarrow", r"(\psi \rightarrow \chi))").scale(0.8).next_to(out_complex, DOWN, buff=1)
            self.play(FadeIn(bot_complex_2), run_time=tracker.duration * 0.2)
            
            # Map cascading input perfectly onto new slot [1]
            self.play(out_complex.animate.move_to(bot_complex_2[1].get_center()), run_time=tracker.duration * 0.2)
            
            # Final cascading output (image_1.png complexity visual cascade)
            final_out = MathTex(r"(\psi \rightarrow \chi)").scale(0.8).set_color(YELLOW).next_to(bot_complex_2, DOWN, buff=1)
            self.play(TransformFromCopy(bot_complex_2[4], final_out), run_time=tracker.duration * 0.3)

        with self.voiceover(text="And this set of axioms is of a special kind, since it can only prove logically valid statements, and as Godel proved in 1929, it can prove all logically valid first order statements.") as tracker:
            self.wait(tracker.duration)

        with self.voiceover(text="So, we can think of these set of axioms, known as the logical axioms, as the operating system of our theorem proving computer.") as tracker:
            # Clear cascading derivation parts
            self.play(FadeOut(out_complex), FadeOut(bot_complex_2), FadeOut(final_out), run_time=tracker.duration * 0.2)
            
            # Surrounding box labeled "Operating System" highlighting the Hilbert axioms centrally
            os_box = SurroundingRectangle(hilbert_axioms, color=YELLOW, buff=0.2)
            os_label = Text("Operating System", color=YELLOW).next_to(os_box, UP)
            self.play(Create(os_box), Write(os_label), run_time=tracker.duration * 0.8)

        # --- Scene 6: Applying to specific theory ---
        with self.voiceover(text="Then we add in new symbols specific to our given theory to the language, add axioms controlling these symbols and we feed in new axioms to our theorem prover and let it run.") as tracker:
            
            # Perform view change shrink: shrinking original box, OS box, and contained axioms (No duplication of blue box)
            os_group = VGroup(giant_tp[0], hilbert_axioms, os_box, os_label)
            self.play(
                os_group.animate.scale(0.3).move_to(DOWN * 1.5),
                run_time=tracker.duration * 0.3
            )
            
            # Swap visuals for scaled down I/O version
            tp_label = Text("Theorem\nProver", font_size=12).move_to(os_group.get_center())
            inputs = VGroup(*[Line(LEFT * 0.2, ORIGIN).next_to(giant_tp[0], LEFT, buff=0).shift(DOWN * (0.3 - i*0.3)) for i in range(3)])
            output = Line(ORIGIN, RIGHT * 0.4).next_to(giant_tp[0], RIGHT, buff=0)
            self.play(FadeIn(tp_label), FadeIn(inputs), FadeIn(output), run_time=tracker.duration * 0.2)
            
            # Theory Language (Groups)
            theory_lang = MathTex(r"\mathcal{L} := \{\cdot, e\}").to_edge(UP).shift(DOWN*0.2)
            self.play(FadeIn(theory_lang, shift=DOWN), run_time=tracker.duration * 0.2)
            
            # Group Theory Axioms (Scaled visual complexity)
            group_axioms = VGroup(
                MathTex(r"\forall x,y,z \ ((x \cdot y) \cdot z = x \cdot (y \cdot z))"),
                MathTex(r"\forall x \ (x \cdot e = x \land e \cdot x = x)"),
                MathTex(r"\forall x \exists y \ (x \cdot y = e \land y \cdot x = e)")
            ).arrange(DOWN, aligned_edge=LEFT).scale(0.5).next_to(inputs, LEFT, buff=1)
            
            self.play(FadeIn(group_axioms, shift=RIGHT), run_time=tracker.duration * 0.15)
            
            # Map input
            self.play(group_axioms.animate.next_to(inputs, LEFT, buff=0.1), run_time=tracker.duration * 0.15)

        with self.voiceover(text="This view of mathematics aligns with the formalist view of math, namely that it is a game being played by meaningless symbols according to certain rules.") as tracker:
            
            # Theorem productionvisual cascade (simulation 'running')
            # Group Theory theorems stacking downward visually (Pushing older ones down)
            theorems = [
                r"e \cdot e = e",
                r"\forall x (x^{-1})^{-1} = x",
                r"\forall x,y (x \cdot y)^{-1} = y^{-1} \cdot x^{-1}",
                r"\forall x (x \cdot x = x \rightarrow x = e)"
            ]
            
            final_thm_group = VGroup().next_to(output, RIGHT, buff=0.5)
            
            # Cascade visual visual stacking (Pushing old downward)
            for thm_str in theorems:
                new_thm = MathTex(thm_str, color=YELLOW).scale(0.6)
                if len(final_thm_group) == 0:
                    new_thm.move_to(output.get_right() + RIGHT*1.5)
                else:
                    new_thm.move_to(final_thm_group[0].get_center()) # Start visual cascade at top slot
                
                # Stack cascade visual visual upward visually downward
                self.play(
                    final_thm_group.animate.shift(DOWN * 0.5),
                    FadeIn(new_thm, shift=DOWN),
                    run_time=tracker.duration / len(theorems)
                )
                final_thm_group.add(new_thm)
            
        self.wait(2)