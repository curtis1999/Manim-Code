from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

# ==========================================
# SCENE 7: AXIOMS, MODEL SETS, AND THEORIES
#CONTAINS IMPROVED VERSION OF THE COMPUTER ENGINE SYNTAX
# ==========================================
class GraphAxiomsAndTheories(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # ------------------------------------------
        # 1. SETUP SYNTAX VS SEMANTICS
        # ------------------------------------------
        divider = Line(UP * 4, DOWN * 4, stroke_width=2).set_color(WHITE)
        self.add(divider)

        syntax_center = LEFT * 3.5
        semantics_center = RIGHT * 3.5

        # Syntax Left Elements
        g_title_syn = MathTex(r"\mathcal{L}_{graphs} = \{E\}", font_size=36).move_to(syntax_center + UP * 3)
        
        phi_tex = MathTex(r"\varphi: \forall x,y,z (Exy \land Eyz \to Exz)", font_size=32, color=TEAL).move_to(syntax_center + UP * 1.5)
        psi_tex = MathTex(r"\psi: \forall x \neg Exx", font_size=32, color=ORANGE).next_to(phi_tex, DOWN, buff=0.5)
        
        sigma_tex = MathTex(r"\Sigma = \{\varphi, \psi\}", font_size=40, color=YELLOW).move_to(syntax_center + UP * 2)
        
        unsat_part1 = MathTex(r"x \neq x \in ", font_size=40, color=RED)
        unsat_part2 = MathTex(r"\Sigma", font_size=40, color=RED)
        unsat_group = VGroup(unsat_part1, unsat_part2).arrange(RIGHT, buff=0.1).move_to(syntax_center + UP * 2)

        chi_tex = MathTex(r"\chi: \forall x,y (Exy \to \neg Eyx)", font_size=32, color=PINK).next_to(psi_tex, DOWN, buff=0.5)
        provable = MathTex(r"\{\varphi, \psi\} \vdash \chi", font_size=36, color=YELLOW) 

        # Semantics Right Elements
        g_title_sem = MathTex(r"\mathcal{G} = (X, E^\mathcal{G})", font_size=36).move_to(semantics_center + UP * 3)
        
        # 12 Total Structures (6 Valid, 6 Invalid)
        valid_graphs = VGroup(
            self.get_mini_graph("line"), self.get_mini_graph("tree"), self.get_mini_graph("bool_alg"),
            self.get_mini_graph("disconnected"), self.get_mini_graph("lattice"), self.get_mini_graph("pentagon_dag")
        )
        invalid_graphs = VGroup(
            self.get_mini_graph("reflexive"), self.get_mini_graph("symmetric"), self.get_mini_graph("cycle"),
            self.get_mini_graph("dense_dag"), self.get_mini_graph("square_cycle"), self.get_mini_graph("non_transitive_line")
        )

        all_graphs = VGroup(*valid_graphs, *invalid_graphs)
        
        # Domino Pattern Layout for 12 items (3 rows, 4 cols) - Middle row shifted left
        for i, g in enumerate(all_graphs):
            row = i // 4
            col = i % 4
            shift_x = 0.6 if row != 1 else 0
            g.move_to(semantics_center + UP * 1.5 + DOWN * (row * 1.2) + LEFT * 2.2 + RIGHT * (col * 1.3 + shift_x))

        # Ellipses for the infinite rightward span (only on the middle row now)
        chaos_dots = MathTex(r"\dots").move_to(semantics_center + UP * 0.3 + RIGHT * 2.8)
        universe_group = VGroup(all_graphs, chaos_dots)

        mod_sigma = MathTex(r"Mod(\Sigma)", font_size=40, color=YELLOW).move_to(semantics_center + UP * 2)
        
        mod_eq = MathTex(r"Mod(\{\varphi, \psi, \chi\}) = Mod(\{\varphi, \psi\})", font_size=32)
        entails = MathTex(r"\{\varphi, \psi\} \models \chi", font_size=36, color=YELLOW)

        # ------------------------------------------
        # 2. INTRODUCING MODELS
        # ------------------------------------------
        script_1 = "We need to define axioms to determine the behaviour of this edge relation E."
        with self.voiceover(text=script_1) as tracker:
            self.play(Write(g_title_syn), Write(g_title_sem), run_time=1.5)
            self.wait(max(0.1, tracker.duration - 1.5))

        script_2 = "Without any axioms, every possible combination of points and all possible arrows drawn between them is a model of our empty theory."
        with self.voiceover(text=script_2) as tracker:
            self.play(FadeIn(universe_group, lag_ratio=0.05), run_time=3)
            self.wait(max(0.1, tracker.duration - 3))

        # ------------------------------------------
        # 3. FILTERING WITH AXIOMS
        # ------------------------------------------
        script_3 = "An axiom can be any FOL sentence."
        with self.voiceover(text=script_3) as tracker:
            self.wait(tracker.duration)

        script_3b = "For example, we can consider this formula phi, expressing transitivity,"
        with self.voiceover(text=script_3b) as tracker:
            self.play(Write(phi_tex), run_time=1.5)
            self.wait(max(0.1, tracker.duration - 1.5))

        node_a = Dot(semantics_center + LEFT * 2 + DOWN * 2, color=WHITE)
        node_b = Dot(semantics_center + DOWN * 2, color=WHITE)
        node_c = Dot(semantics_center + RIGHT * 2 + DOWN * 2, color=WHITE)
        label_a = Text("a", font_size=20).next_to(node_a, DOWN)
        label_b = Text("b", font_size=20).next_to(node_b, DOWN)
        label_c = Text("c", font_size=20).next_to(node_c, DOWN)
        trans_nodes = VGroup(node_a, node_b, node_c, label_a, label_b, label_c)
        arr_ab = Arrow(node_a, node_b, buff=0.1, color=TEAL)
        arr_bc = Arrow(node_b, node_c, buff=0.1, color=TEAL)
        arr_ac = Arrow(node_a, node_c, buff=0.1, path_arc=-0.5, color=YELLOW)

        script_4 = "meaning that if there is some path between nodes, then there is a direct path between these nodes."
        with self.voiceover(text=script_4) as tracker:
            self.play(universe_group.animate.set_opacity(0.15), run_time=0.5)
            self.play(FadeIn(trans_nodes), GrowArrow(arr_ab), GrowArrow(arr_bc), run_time=1)
            self.play(GrowArrow(arr_ac), run_time=1)
            self.wait(max(0.1, tracker.duration - 2.5))

        self.play(FadeOut(trans_nodes), FadeOut(arr_ab), FadeOut(arr_bc), FadeOut(arr_ac))

        script_5 = "Or this sentence psi expressing irreflexivity, which enforces that any model of it must not contain any self-referential arrows."
        with self.voiceover(text=script_5) as tracker:
            self.play(Write(psi_tex), run_time=1)
            self.play(universe_group.animate.set_opacity(1), run_time=0.5)
            self.play(Indicate(invalid_graphs[0][1], color=RED, scale_factor=1.5), run_time=1.5)
            invalid_graphs[0][1].set_color(RED)
            self.wait(max(0.1, tracker.duration - 3))

        script_6 = "We can combine the sentences, and consider the collection of all structures which satisfy both phi and psi, i.e. the collection of all transitive and irreflexive structures."
        with self.voiceover(text=script_6) as tracker:
            # Re-arrange valid graphs into Domino Pattern (3 rows, 2 cols)
            for i, g in enumerate(valid_graphs):
                row = i // 2
                col = i % 2
                shift_x = 0.7 if row != 1 else 0
                g.generate_target()
                g.target.move_to(semantics_center + UP * 1 + DOWN * (row * 1.2) + LEFT * 1 + RIGHT * (col * 1.6 + shift_x))
            
            mod_dots = MathTex(r"\dots").move_to(semantics_center + DOWN * 0.2 + RIGHT * 2)
            valid_with_dots = VGroup(valid_graphs, mod_dots)
            
            self.play(
                invalid_graphs.animate.set_opacity(0).shift(DOWN * 2),
                FadeOut(chaos_dots),
                *[MoveToTarget(g) for g in valid_graphs],
                FadeIn(mod_dots),
                run_time=2
            )
            self.wait(max(0.1, tracker.duration - 2))

        # ------------------------------------------
        # 4. MOD(SIGMA) & CONSISTENCY
        # ------------------------------------------
        script_7 = "In general, given any collection of sentences Sigma, this is the model set of Sigma, and it is the set of possible structures which satisfy each of the sentences in Sigma."
        with self.voiceover(text=script_7) as tracker:
            self.play(ReplacementTransform(VGroup(phi_tex, psi_tex), sigma_tex), Write(mod_sigma), run_time=1.5)
            mod_box = SurroundingRectangle(valid_with_dots, color=YELLOW, buff=0.25)
            self.play(Create(mod_box), run_time=1)
            self.wait(max(0.1, tracker.duration - 2.5))

        script_8 = "Note that if Sigma contains an unsatisfiable sentence, such as x is not equal to x, then Mod Sigma will be empty."
        with self.voiceover(text=script_8) as tracker:
            self.play(ReplacementTransform(sigma_tex, unsat_group), FadeOut(mod_sigma), run_time=1)
            self.play(FadeOut(valid_with_dots), run_time=1) # Keep mod_box on screen!
            self.wait(max(0.1, tracker.duration - 2))

        script_9 = "And the soundness of First order logic, tells us that if our set of sentence Sigma is consistent..."
        with self.voiceover(text=script_9) as tracker:
            # Fade out x != x \in, and change Sigma back to yellow
            self.play(FadeOut(unsat_part1), unsat_part2.animate.set_color(YELLOW), FadeIn(mod_sigma), run_time=1)
            self.wait(max(0.1, tracker.duration - 1))

        m_model = MathTex(r"\mathcal{M}", font_size=60, color=BLUE).move_to(mod_box.get_center())
        # Anchor arrow to the newly isolated yellow Sigma
        soundness_arrow = Arrow(unsat_part2.get_right(), mod_box.get_left(), color=BLUE, buff=0.2)
        soundness_label = Text("Soundness", font_size=24, color=BLUE).next_to(soundness_arrow, UP)

        script_10 = "then there is at least one model out there which satisfies every formula in Sigma."
        with self.voiceover(text=script_10) as tracker:
            self.play(GrowArrow(soundness_arrow), FadeIn(soundness_label), run_time=1)
            self.play(FadeIn(m_model), run_time=1)
            self.wait(max(0.1, tracker.duration - 2))

        # ------------------------------------------
        # 5. PLATONISTIC VISION
        # ------------------------------------------
        script_11 = "We see that this is based on a platonistic vision of mathematics, where mathematical structures are pre-existing,"
        with self.voiceover(text=script_11) as tracker:
            self.play(FadeOut(soundness_arrow), FadeOut(soundness_label), FadeOut(m_model), FadeOut(mod_box))
            # Restore all graphs to the domino grid
            for i, g in enumerate(all_graphs):
                row = i // 4
                col = i % 4
                shift_x = 0.6 if row != 1 else 0
                g.move_to(semantics_center + UP * 1.5 + DOWN * (row * 1.2) + LEFT * 2.2 + RIGHT * (col * 1.3 + shift_x))
            self.play(FadeIn(universe_group.set_opacity(1)), run_time=2)
            self.wait(max(0.1, tracker.duration - 2))

        script_12 = "and we can characterize them using first order sentences."
        with self.voiceover(text=script_12) as tracker:
            valid_box_group = VGroup(*[SurroundingRectangle(g, color=YELLOW, buff=0.1) for g in valid_graphs])
            self.play(Create(valid_box_group), run_time=1.5)
            self.wait(max(0.1, tracker.duration - 1.5))

        # Reset to clean filtered view for the next proof
        self.play(FadeOut(universe_group), FadeOut(valid_box_group))
        for i, g in enumerate(valid_graphs):
            row = i // 2
            col = i % 2
            shift_x = 0.7 if row != 1 else 0
            g.move_to(semantics_center + UP * 1 + DOWN * (row * 1.2) + LEFT * 1 + RIGHT * (col * 1.6 + shift_x))
        mod_dots.move_to(semantics_center + DOWN * 0.2 + RIGHT * 2)
        
        valid_with_dots = VGroup(valid_graphs, mod_dots)
        mod_box.move_to(valid_with_dots.get_center())
        self.play(FadeIn(valid_with_dots), Create(mod_box), run_time=1)

        # ------------------------------------------
        # 6. ASYMMETRY ARGUMENT & COMPLETENESS
        # ------------------------------------------
        phi_tex = MathTex(r"\varphi: \forall x,y,z (Exy \land Eyz \to Exz)", font_size=32, color=TEAL).move_to(syntax_center + UP * 1.5)
        psi_tex = MathTex(r"\psi: \forall x \neg Exx", font_size=32, color=ORANGE).next_to(phi_tex, DOWN, buff=0.5)

        script_13 = "If we start to study the general structure of the models in Mod({phi,psi}), we might notice some things in common to all of these structures."
        with self.voiceover(text=script_13) as tracker:
            self.play(ReplacementTransform(unsat_part2, VGroup(phi_tex, psi_tex)), FadeOut(mod_sigma), run_time=1)
            self.wait(max(0.1, tracker.duration - 1))

        contra_node_a = Dot(semantics_center + LEFT * 1 + UP * 2, color=WHITE)
        contra_node_b = Dot(semantics_center + RIGHT * 1 + UP * 2, color=WHITE)
        clabel_a = Text("a", font_size=20).next_to(contra_node_a, DOWN)
        clabel_b = Text("b", font_size=20).next_to(contra_node_b, DOWN)
        contra_nodes = VGroup(contra_node_a, contra_node_b, clabel_a, clabel_b)
        arr_fwd = Arrow(contra_node_a, contra_node_b, buff=0.1, path_arc=-0.3, color=PINK)
        arr_bwd = Arrow(contra_node_b, contra_node_a, buff=0.1, path_arc=-0.3, color=PINK)

        script_14 = "For example we may notice that in none of them do we have aEb and bEa."
        with self.voiceover(text=script_14) as tracker:
            self.play(valid_with_dots.animate.set_opacity(0.15), mod_box.animate.set_color(DARK_GREY), run_time=0.5)
            self.play(FadeIn(contra_nodes), GrowArrow(arr_fwd), GrowArrow(arr_bwd), run_time=1)
            self.wait(max(0.1, tracker.duration - 1.5))

        script_15a = "We can easily see why, since if we did have such an edge in a transitive and irreflexive structure,"
        with self.voiceover(text=script_15a) as tracker:
            self.wait(tracker.duration)

        arr_self = Arc(radius=0.3, start_angle=0, angle=3*PI/2, color=YELLOW).next_to(contra_node_a, UP, buff=0).shift(DOWN*0.1)
        arr_self.add_tip()

        script_15b = "then by transitivity we should have a direct path a to a."
        with self.voiceover(text=script_15b) as tracker:
            self.play(phi_tex.animate.set_color(YELLOW), run_time=0.5)
            self.play(Create(arr_self), run_time=1)
            self.play(phi_tex.animate.set_color(TEAL), run_time=0.5)
            self.wait(max(0.1, tracker.duration - 2))

        cross = Cross(arr_self, stroke_color=RED, stroke_width=6)

        script_16 = "But then the structure is not irreflexive, a contradiction."
        with self.voiceover(text=script_16) as tracker:
            self.play(psi_tex.animate.set_color(YELLOW), run_time=0.5)
            self.play(Create(cross), run_time=0.5)
            self.play(psi_tex.animate.set_color(ORANGE), run_time=0.5)
            self.wait(max(0.1, tracker.duration - 1.5))

        self.play(
            FadeOut(contra_nodes), FadeOut(arr_fwd), FadeOut(arr_bwd), FadeOut(arr_self), FadeOut(cross),
            valid_with_dots.animate.set_opacity(1), mod_box.animate.set_color(YELLOW), run_time=1
        )

        script_17 = "So, we see that adding this sentence chi expressing assymetry, is redundant,"
        with self.voiceover(text=script_17) as tracker:
            self.play(Write(chi_tex), run_time=1)
            self.wait(max(0.1, tracker.duration - 1))

        script_18 = "in the sense that Mod(phi,psi,chi) = Mod(phi,psi)."
        with self.voiceover(text=script_18) as tracker:
            mod_eq.next_to(mod_box, DOWN, buff=0.4)
            self.play(Write(mod_eq), run_time=1)
            self.wait(max(0.1, tracker.duration - 1))

        script_18b = "We denote this by {phi,psi} models chi."
        with self.voiceover(text=script_18b) as tracker:
            entails.next_to(mod_eq, DOWN, buff=0.3)
            self.play(Write(entails), run_time=1)
            self.wait(max(0.1, tracker.duration - 1))

        script_19 = "Recall that the deductive completeness of our calculus gives us a guarantee that there is a proof of chi from the axioms using phi,psi as assumptions."
        with self.voiceover(text=script_19) as tracker:
            provable.move_to(syntax_center).set_y(entails.get_y())
            self.play(Write(provable), run_time=1)
            
            comp_arrow = Arrow(entails.get_left(), provable.get_right(), color=YELLOW, buff=0.2)
            comp_label = Text("Completeness", font_size=20, color=YELLOW).next_to(comp_arrow, UP, buff=0.1)
            self.play(GrowArrow(comp_arrow), FadeIn(comp_label), run_time=1)
            self.wait(max(0.1, tracker.duration - 2))

        # ------------------------------------------
        # 7. DEDUCTIVE ENGINE (Tight Black Box, Slowed Down 2x)
        # ------------------------------------------
        self.play(FadeOut(comp_arrow), FadeOut(comp_label), FadeOut(provable), FadeOut(chi_tex), FadeOut(psi_tex), FadeOut(phi_tex))
        
        engine_label = Text("Deductive\nEngine", font_size=16)
        engine_box = SurroundingRectangle(engine_label, color=BLUE, buff=0.15, fill_opacity=0.2)
        engine = VGroup(engine_box, engine_label)
        
        arr_1 = Arrow(LEFT, RIGHT, buff=0.1, color=WHITE).scale(0.5)
        arr_2 = Arrow(LEFT, RIGHT, buff=0.1, color=WHITE).scale(0.5)

        in_1 = MathTex(r"\{", r"\varphi, \psi", r"\}", font_size=28)
        out_chi = MathTex(r"\chi", font_size=28, color=PINK)
        sys_1 = VGroup(in_1, arr_1, engine, arr_2, out_chi).arrange(RIGHT, buff=0.2).move_to(syntax_center + UP * 1)

        in_2 = MathTex(r"\{", r"\varphi, \psi", r", \chi", r"\}", font_size=28)
        out_xi = MathTex(r"\xi", font_size=28, color=PURPLE)
        sys_2 = VGroup(in_2, arr_1.copy(), engine.copy(), arr_2.copy(), out_xi).arrange(RIGHT, buff=0.2).move_to(syntax_center + UP * 1)

        in_3 = MathTex(r"\{", r"\varphi, \psi", r", \chi, \xi", r"\}", font_size=28)
        out_th = MathTex(r"\theta", font_size=28, color=TEAL)
        sys_3 = VGroup(in_3, arr_1.copy(), engine.copy(), arr_2.copy(), out_th).arrange(RIGHT, buff=0.2).move_to(syntax_center + UP * 1)

        in_4 = MathTex(r"\{", r"\varphi, \psi", r", \chi, \xi, \theta", r"\}", font_size=28)
        out_ze = MathTex(r"\zeta", font_size=28, color=GREEN)
        sys_4 = VGroup(in_4, arr_1.copy(), engine.copy(), arr_2.copy(), out_ze).arrange(RIGHT, buff=0.2).move_to(syntax_center + UP * 1)
        
        in_final = MathTex(r"\{", r"\varphi, \psi", r", \chi, \xi, \theta, \zeta, \dots", r"\}", font_size=28)
        sys_final = VGroup(in_final, arr_1.copy(), engine.copy()).arrange(RIGHT, buff=0.2).move_to(syntax_center + UP * 1)

        script_20 = "Moving back to the world of syntax, as mentioned earlier, this can be seen as a computational process, where at first the axioms are put in, and derive a new formula like chi."
        with self.voiceover(text=script_20) as tracker:
            # 2X Slower
            self.play(FadeIn(in_1), FadeIn(engine), run_time=2)
            self.play(GrowArrow(arr_1), run_time=1)
            self.play(engine_box.animate.set_fill(opacity=0.6), run_time=1)
            self.play(engine_box.animate.set_fill(opacity=0.2), GrowArrow(arr_2), FadeIn(out_chi, shift=RIGHT), run_time=2)
            self.wait(max(0.1, tracker.duration - 6))

        script_21 = "Once we have derived chi, we can use it to prove more theorems and so on."
        with self.voiceover(text=script_21) as tracker:
            # 2X Slower
            self.play(ReplacementTransform(sys_1, sys_2), run_time=1.6)
            self.play(sys_2[2][0].animate.set_fill(opacity=0.6), run_time=0.6)
            self.play(sys_2[2][0].animate.set_fill(opacity=0.2), run_time=0.6)
            
            self.play(ReplacementTransform(sys_2, sys_3), run_time=1.6)
            self.play(sys_3[2][0].animate.set_fill(opacity=0.6), run_time=0.6)
            self.play(sys_3[2][0].animate.set_fill(opacity=0.2), run_time=0.6)
            
            self.play(ReplacementTransform(sys_3, sys_4), run_time=1.6)
            self.play(sys_4[2][0].animate.set_fill(opacity=0.6), run_time=0.6)
            self.play(sys_4[2][0].animate.set_fill(opacity=0.2), run_time=0.6)
            
            self.play(ReplacementTransform(sys_4, sys_final), run_time=1.6)
            self.wait(max(0.1, tracker.duration - 10.2))

        script_22 = "In this scenario, we would say that phi and psi are axioms,"
        with self.voiceover(text=script_22) as tracker:
            self.play(in_final[1].animate.set_color(YELLOW), run_time=1)
            self.wait(max(0.1, tracker.duration - 1))

        script_23 = "and the consequences of phi and psi are theorems."
        with self.voiceover(text=script_23) as tracker:
            self.play(in_final[1].animate.set_color(WHITE), in_final[2].animate.set_color(PINK), run_time=1)
            self.wait(max(0.1, tracker.duration - 1))

        script_24 = "The theory of {phi,psi} is the set of all such theorems."
        with self.voiceover(text=script_24) as tracker:
            theory_tex = MathTex(
                r"Th(\{\varphi, \psi\}) = \{\varphi, \psi, \chi, \xi, \theta, \zeta, \dots\}", 
                font_size=32, color=BLUE
            ).move_to(syntax_center + DOWN * 0.5)
            self.play(ReplacementTransform(sys_final, theory_tex), run_time=1.5)
            self.wait(max(0.1, tracker.duration - 1.5))

        # ------------------------------------------
        # 8. FINAL SOUNDNESS CONNECTION
        # ------------------------------------------
        final_sound_arrow = Arrow(theory_tex.get_right(), mod_box.get_left(), color=BLUE, buff=0.2)
        final_sound_label = Text("Soundness", font_size=20, color=BLUE).next_to(final_sound_arrow, UP, buff=0.1)

        script_25 = "And note that as a consequence of soundness, all of these theorems are satisfied in every model which satisfy phi and psi."
        with self.voiceover(text=script_25) as tracker:
            self.play(GrowArrow(final_sound_arrow), FadeIn(final_sound_label), run_time=1.5)
            self.wait(max(0.1, tracker.duration - 1.5))

        script_26 = "I.e. each theorem is satisfied in every transitive and irreflexive structure. So we can see that the theorems of a given set of sentences Sigma are exactly the set of sentences satisfied by every model of Sigma."
        with self.voiceover(text=script_26) as tracker:
            self.wait(tracker.duration)

        self.wait(2)


    # ---------------------------------------------------
    # Helper Function for 12 Extended Mini-Graphs
    # ---------------------------------------------------
    def get_mini_graph(self, g_type):
        group = VGroup()
        if g_type == "line": 
            n1, n2, n3 = Dot(LEFT*0.5), Dot(ORIGIN), Dot(RIGHT*0.5)
            e1, e2 = Arrow(n1, n2, buff=0.05), Arrow(n2, n3, buff=0.05)
            e3 = Arrow(n1, n3, buff=0.05, path_arc=-0.6)
            group.add(n1, n2, n3, e1, e2, e3)
        elif g_type == "tree": 
            n1, n2, n3 = Dot(UP*0.3), Dot(LEFT*0.4 + DOWN*0.3), Dot(RIGHT*0.4 + DOWN*0.3)
            e1, e2 = Arrow(n1, n2, buff=0.05), Arrow(n1, n3, buff=0.05)
            group.add(n1, n2, n3, e1, e2)
        elif g_type == "bool_alg": 
            n0 = Dot(DOWN*0.5)
            n1a, n1b, n1c = Dot(LEFT*0.5), Dot(ORIGIN), Dot(RIGHT*0.5)
            n3 = Dot(UP*0.5)
            edges = [Arrow(n0,n1a,buff=0), Arrow(n0,n1b,buff=0), Arrow(n0,n1c,buff=0),
                     Arrow(n1a,n3,buff=0), Arrow(n1b,n3,buff=0), Arrow(n1c,n3,buff=0),
                     Arrow(n0,n3,buff=0.05, path_arc=0.8, stroke_opacity=0.5)]
            group.add(n0, n1a, n1b, n1c, n3, *edges)
        elif g_type == "disconnected": 
            n1, n2 = Dot(LEFT*0.4), Dot(RIGHT*0.4)
            n3, n4 = Dot(UP*0.4), Dot(DOWN*0.4)
            e1 = Arrow(n3, n4, buff=0.05)
            group.add(n1, n2, n3, n4, e1)
        elif g_type == "lattice": 
            n1, n2, n3, n4 = Dot(UP*0.4), Dot(LEFT*0.4), Dot(RIGHT*0.4), Dot(DOWN*0.4)
            e1, e2 = Arrow(n1, n2, buff=0.05), Arrow(n1, n3, buff=0.05)
            e3, e4 = Arrow(n2, n4, buff=0.05), Arrow(n3, n4, buff=0.05)
            e5 = Arrow(n1, n4, buff=0.05, path_arc=0.3)
            group.add(n1, n2, n3, n4, e1, e2, e3, e4, e5)
        elif g_type == "pentagon_dag": 
            n1, n2, n3 = Dot(UP*0.4), Dot(LEFT*0.4 + UP*0.1), Dot(RIGHT*0.4 + UP*0.1)
            n4, n5 = Dot(LEFT*0.2 + DOWN*0.4), Dot(RIGHT*0.2 + DOWN*0.4)
            edges = [Arrow(n1,n2,buff=0.05), Arrow(n1,n3,buff=0.05), Arrow(n2,n4,buff=0.05), Arrow(n3,n5,buff=0.05),
                     Arrow(n1,n4,buff=0.05), Arrow(n1,n5,buff=0.05)]
            group.add(n1, n2, n3, n4, n5, *edges)
        elif g_type == "reflexive": 
            n1 = Dot(ORIGIN)
            e1 = Arc(radius=0.2, start_angle=0, angle=3*PI/2).next_to(n1, UP, buff=0).shift(DOWN*0.1)
            e1.add_tip(tip_length=0.1)
            group.add(n1, e1)
        elif g_type == "symmetric": 
            n1, n2 = Dot(LEFT*0.4), Dot(RIGHT*0.4)
            e1 = Arrow(n1, n2, buff=0.05, path_arc=-0.3)
            e2 = Arrow(n2, n1, buff=0.05, path_arc=-0.3)
            group.add(n1, n2, e1, e2)
        elif g_type == "cycle": 
            n1, n2, n3 = Dot(UP*0.4), Dot(LEFT*0.4 + DOWN*0.3), Dot(RIGHT*0.4 + DOWN*0.3)
            e1, e2, e3 = Arrow(n1, n2, buff=0.05), Arrow(n2, n3, buff=0.05), Arrow(n3, n1, buff=0.05)
            group.add(n1, n2, n3, e1, e2, e3)
        elif g_type == "dense_dag": 
            n1, n2, n3, n4 = Dot(LEFT*0.5+UP*0.5), Dot(RIGHT*0.5+UP*0.5), Dot(LEFT*0.5+DOWN*0.5), Dot(RIGHT*0.5+DOWN*0.5)
            e1, e2 = Arrow(n1, n3, buff=0.05), Arrow(n2, n4, buff=0.05)
            e3, e4 = Arrow(n1, n4, buff=0.05), Arrow(n2, n3, buff=0.05)
            group.add(n1, n2, n3, n4, e1, e2, e3, e4)
        elif g_type == "square_cycle": 
            n1, n2, n3, n4 = Dot(UL*0.3), Dot(UR*0.3), Dot(DR*0.3), Dot(DL*0.3)
            e1, e2, e3, e4 = Arrow(n1,n2,buff=0.05), Arrow(n2,n3,buff=0.05), Arrow(n3,n4,buff=0.05), Arrow(n4,n1,buff=0.05)
            group.add(n1, n2, n3, n4, e1, e2, e3, e4)
        elif g_type == "non_transitive_line": 
            n1, n2, n3 = Dot(LEFT*0.4), Dot(ORIGIN), Dot(RIGHT*0.4)
            e1, e2 = Arrow(n1, n2, buff=0.05), Arrow(n2, n3, buff=0.05)
            group.add(n1, n2, n3, e1, e2)
            
        return group.scale(0.55)