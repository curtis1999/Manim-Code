from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

# ==========================================
# SCENE 7: AXIOMS AND MODEL SETS
# ==========================================
class GraphAxioms(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # ------------------------------------------
        # 1. SETUP SYNTAX VS SEMANTICS
        # ------------------------------------------
        # Syntax Left
        g_title = MathTex(r"\mathcal{G} = (X, E^\mathcal{G})", font_size=48).to_corner(UL)
        
        # We will place formulas aligned to the left side
        left_align = LEFT * 6
        
        phi_tex = MathTex(r"\varphi: \forall x,y,z (Exy \land Eyz \to Exz)", font_size=36, color=TEAL).next_to(g_title, DOWN, buff=1).align_to(left_align, LEFT)
        psi_tex = MathTex(r"\psi: \forall x \neg Exx", font_size=36, color=ORANGE).next_to(phi_tex, DOWN, buff=0.8).align_to(left_align, LEFT)
        
        sigma_tex = MathTex(r"\Sigma", font_size=48, color=YELLOW).move_to(LEFT * 3 + UP * 1)
        mod_sigma = MathTex(r"Mod(\Sigma)", font_size=48, color=YELLOW).next_to(sigma_tex, DOWN, buff=0.5)

        chi_tex = MathTex(r"\chi: \forall x,y (Exy \to \neg Eyx)", font_size=36, color=PINK).next_to(psi_tex, DOWN, buff=0.8).align_to(left_align, LEFT)
        mod_eq = MathTex(r"Mod(\varphi, \psi, \chi) = Mod(\varphi, \psi)", font_size=36).next_to(chi_tex, DOWN, buff=0.8).align_to(left_align, LEFT)
        entails = MathTex(r"\{\varphi, \psi\} \models \chi", font_size=42, color=YELLOW).next_to(mod_eq, DOWN, buff=0.8).align_to(left_align, LEFT)

        # Semantics Right (The Universe of Models)
        # We create a collection of small graphs
        valid_graphs = VGroup(
            self.get_mini_graph("line").move_to(RIGHT * 2 + UP * 2.5),
            self.get_mini_graph("tree").move_to(RIGHT * 5 + UP * 2),
            self.get_mini_graph("lattice").move_to(RIGHT * 3.5 + UP * 0.5)
        )
        invalid_graphs = VGroup(
            self.get_mini_graph("reflexive").move_to(RIGHT * 5 + DOWN * 1),
            self.get_mini_graph("symmetric").move_to(RIGHT * 2 + DOWN * 1.5),
            self.get_mini_graph("cycle").move_to(RIGHT * 4 + DOWN * 2.5)
        )
        all_graphs = VGroup(valid_graphs, invalid_graphs)

        # ------------------------------------------
        # 2. INTRODUCING MODELS
        # ------------------------------------------
        script_1 = "We need to define axioms to determine the behaviour of this edge relation E. Without any axioms, every possible combination of points and all possible arrows drawn between them is a model of our empty theory."
        with self.voiceover(text=script_1) as tracker:
            self.play(Write(g_title))
            self.play(FadeIn(all_graphs, lag_ratio=0.1), run_time=2)
            self.wait(max(0, tracker.duration - 3))

        # ------------------------------------------
        # 3. TRANSITIVITY (\varphi)
        # ------------------------------------------
        script_2 = "An axiom can be any First Order Logic sentence. For example, we can consider this formula phi, expressing transitivity,"
        with self.voiceover(text=script_2) as tracker:
            self.play(Write(phi_tex), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        # Visualizer for transitivity
        node_a = Dot(RIGHT * 1 + DOWN * 1, color=WHITE)
        node_b = Dot(RIGHT * 3 + DOWN * 1, color=WHITE)
        node_c = Dot(RIGHT * 5 + DOWN * 1, color=WHITE)
        label_a = Text("a", font_size=24).next_to(node_a, DOWN)
        label_b = Text("b", font_size=24).next_to(node_b, DOWN)
        label_c = Text("c", font_size=24).next_to(node_c, DOWN)
        trans_nodes = VGroup(node_a, node_b, node_c, label_a, label_b, label_c)
        
        arr_ab = Arrow(node_a, node_b, buff=0.1, color=TEAL)
        arr_bc = Arrow(node_b, node_c, buff=0.1, color=TEAL)
        arr_ac = Arrow(node_a, node_c, buff=0.1, path_arc=-0.5, color=YELLOW)

        script_3 = "meaning that if there is some path between nodes, then there is a direct path between these nodes."
        with self.voiceover(text=script_3) as tracker:
            # Dim the background graphs to focus on the explanation
            self.play(all_graphs.animate.set_opacity(0.2), run_time=0.5)
            self.play(FadeIn(trans_nodes), run_time=0.5)
            self.play(GrowArrow(arr_ab), run_time=0.5)
            self.play(GrowArrow(arr_bc), run_time=0.5)
            self.play(GrowArrow(arr_ac), run_time=1)
            self.wait(max(0, tracker.duration - 3))

        self.play(FadeOut(trans_nodes), FadeOut(arr_ab), FadeOut(arr_bc), FadeOut(arr_ac))

        # ------------------------------------------
        # 4. IRREFLEXIVITY (\psi)
        # ------------------------------------------
        script_4 = "Or this sentence psi expressing irreflexivity, which enforces that any model of it must not contain any self-referential arrows."
        with self.voiceover(text=script_4) as tracker:
            self.play(Write(psi_tex), run_time=1)
            self.play(all_graphs.animate.set_opacity(1), run_time=0.5)
            
            # Highlight the self-loop on the reflexive graph in red
            self.play(Indicate(invalid_graphs[0][1], color=RED, scale_factor=1.2), run_time=1.5)
            invalid_graphs[0][1].set_color(RED) # Keep it red
            self.wait(max(0, tracker.duration - 3))

        # ------------------------------------------
        # 5. FILTERING THE MODELS
        # ------------------------------------------
        script_5 = "We can combine the sentences, and consider the collection of all structures which satisfy both phi and psi, i.e. the collection of all transitive and irreflexive structures."
        with self.voiceover(text=script_5) as tracker:
            # Shift valid ones to the top, fade out invalid ones
            self.play(
                invalid_graphs.animate.set_opacity(0.1).shift(DOWN * 2),
                valid_graphs.animate.arrange(RIGHT, buff=1).move_to(RIGHT * 3.5 + UP * 1.5),
                run_time=2
            )
            self.wait(max(0, tracker.duration - 2))

        # ------------------------------------------
        # 6. Mod(\Sigma) and Consistency
        # ------------------------------------------
        script_6 = "In general, given any collection of sentences Sigma, this is the model set of Sigma, and it is the set of possible structures which satisfy each of the sentences in Sigma."
        with self.voiceover(text=script_6) as tracker:
            self.play(FadeOut(phi_tex), FadeOut(psi_tex), FadeIn(sigma_tex), run_time=1)
            self.play(FadeIn(mod_sigma, shift=DOWN), run_time=1)
            # Create a box bounding the valid models
            mod_box = SurroundingRectangle(valid_graphs, color=YELLOW, buff=0.3)
            self.play(Create(mod_box), run_time=1)
            self.wait(max(0, tracker.duration - 3))

        script_7 = "Note that if Sigma contains an unsatisfiable sentence, such as x does not equal x, then Mod Sigma will be empty."
        with self.voiceover(text=script_7) as tracker:
            unsat_tex = MathTex(r"\exists x (x \neq x)", color=RED).next_to(sigma_tex, DOWN, buff=0.5)
            self.play(FadeIn(unsat_tex), FadeOut(mod_sigma), run_time=0.5)
            self.play(FadeOut(valid_graphs), FadeOut(mod_box), FadeOut(invalid_graphs), run_time=1.5)
            self.wait(max(0, tracker.duration - 2))

        script_8 = "And the soundness of First order logic, tells us that if our set of sentences Sigma is consistent, meaning that one cannot prove phi and not phi for any formula phi as hard as you try, then there is at least one model out there which satisfies every formula in Sigma."
        with self.voiceover(text=script_8) as tracker:
            self.play(FadeOut(unsat_tex), FadeIn(mod_sigma), run_time=0.5)
            self.play(FadeIn(valid_graphs[0].move_to(RIGHT * 3.5)), run_time=1) # Bring just one back
            self.wait(max(0, tracker.duration - 1.5))

        script_9 = "We see that this is based on a platonistic vision of mathematics, where mathematical structures are pre-existing, and we can characterize them using first order sentences."
        with self.voiceover(text=script_9) as tracker:
            self.wait(tracker.duration)

        # ------------------------------------------
        # 7. ASYMMETRY PROOF (\chi)
        # ------------------------------------------
        script_10 = "If we start to study the general structure of the models satisfying phi and psi, we might notice some things in common to all of these structures."
        with self.voiceover(text=script_10) as tracker:
            self.play(FadeOut(sigma_tex), FadeOut(mod_sigma), FadeIn(phi_tex), FadeIn(psi_tex), run_time=1)
            self.play(FadeIn(valid_graphs[1]), FadeIn(valid_graphs[2]), run_time=1)
            self.play(valid_graphs.animate.arrange(RIGHT, buff=1).move_to(RIGHT * 3.5 + UP * 1.5), run_time=1)
            self.wait(max(0, tracker.duration - 3))

        # Visualizer for Asymmetry contradiction
        contra_node_a = Dot(RIGHT * 2 + DOWN * 2, color=WHITE)
        contra_node_b = Dot(RIGHT * 5 + DOWN * 2, color=WHITE)
        clabel_a = Text("a", font_size=24).next_to(contra_node_a, DOWN)
        clabel_b = Text("b", font_size=24).next_to(contra_node_b, DOWN)
        contra_nodes = VGroup(contra_node_a, contra_node_b, clabel_a, clabel_b)

        arr_fwd = Arrow(contra_node_a, contra_node_b, buff=0.1, path_arc=-0.3, color=PINK)
        arr_bwd = Arrow(contra_node_b, contra_node_a, buff=0.1, path_arc=-0.3, color=PINK)
        
        script_11 = "For example we may notice that in none of them do we have aEb and bEa."
        with self.voiceover(text=script_11) as tracker:
            self.play(FadeIn(contra_nodes), run_time=0.5)
            self.play(GrowArrow(arr_fwd), GrowArrow(arr_bwd), run_time=1)
            self.wait(max(0, tracker.duration - 1.5))

        arr_self = Arc(radius=0.3, start_angle=0, angle=3*PI/2, color=YELLOW).next_to(contra_node_a, UP, buff=0).shift(DOWN*0.1)
        arr_self.add_tip()

        script_12 = "We can easily see why, since if we did have such an edge in a transitive and irreflexive structure, then by transitivity we should have a direct path from a to a."
        with self.voiceover(text=script_12) as tracker:
            self.play(phi_tex.animate.set_color(YELLOW), run_time=0.5)
            self.play(Create(arr_self), run_time=1.5)
            self.play(phi_tex.animate.set_color(TEAL), run_time=0.5)
            self.wait(max(0, tracker.duration - 2.5))

        cross = Cross(arr_self, stroke_color=RED, stroke_width=6)

        script_13 = "But then the structure is not irreflexive, a contradiction."
        with self.voiceover(text=script_13) as tracker:
            self.play(psi_tex.animate.set_color(YELLOW), run_time=0.5)
            self.play(Create(cross), run_time=0.5)
            self.play(psi_tex.animate.set_color(ORANGE), run_time=0.5)
            self.wait(max(0, tracker.duration - 1.5))

        script_14 = "So, we see that adding this sentence chi expressing asymmetry, is redundant, in the sense that Mod(phi, psi, chi) is exactly equal to Mod(phi, psi)."
        with self.voiceover(text=script_14) as tracker:
            self.play(Write(chi_tex), run_time=1.5)
            self.play(Write(mod_eq), run_time=1.5)
            self.wait(max(0, tracker.duration - 3))

        script_15 = "We denote this by saying the set phi, psi models chi."
        with self.voiceover(text=script_15) as tracker:
            self.play(Write(entails), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        self.wait(2)


    # ---------------------------------------------------
    # Helper Function for Mini-Graphs
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
            
        elif g_type == "lattice":
            n1, n2, n3, n4 = Dot(UP*0.4), Dot(LEFT*0.4), Dot(RIGHT*0.4), Dot(DOWN*0.4)
            e1, e2 = Arrow(n1, n2, buff=0.05), Arrow(n1, n3, buff=0.05)
            e3, e4 = Arrow(n2, n4, buff=0.05), Arrow(n3, n4, buff=0.05)
            e5 = Arrow(n1, n4, buff=0.05, path_arc=0.3) # Transitive edge
            group.add(n1, n2, n3, n4, e1, e2, e3, e4, e5)
            
        elif g_type == "reflexive":
            n1, n2 = Dot(LEFT*0.3), Dot(RIGHT*0.3)
            e1 = Arrow(n1, n2, buff=0.05)
            e2 = Arc(radius=0.15, start_angle=0, angle=3*PI/2).next_to(n2, UP, buff=0).shift(DOWN*0.05)
            e2.add_tip(tip_length=0.1)
            group.add(n1, n2, e1, e2)
            
        elif g_type == "symmetric":
            n1, n2 = Dot(LEFT*0.4), Dot(RIGHT*0.4)
            e1 = Arrow(n1, n2, buff=0.05, path_arc=-0.3)
            e2 = Arrow(n2, n1, buff=0.05, path_arc=-0.3)
            group.add(n1, n2, e1, e2)
            
        elif g_type == "cycle":
            n1, n2, n3 = Dot(UP*0.3), Dot(LEFT*0.3 + DOWN*0.2), Dot(RIGHT*0.3 + DOWN*0.2)
            e1 = Arrow(n1, n2, buff=0.05)
            e2 = Arrow(n2, n3, buff=0.05)
            e3 = Arrow(n3, n1, buff=0.05)
            group.add(n1, n2, n3, e1, e2, e3)
            
        return group.scale(0.8)