from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService # Or your preferred TTS service

class SyntaxVsSemantics(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService())

        # ------------------------------------------
        # 1. INTRO: SYNTAX & SEMANTICS (CENTERED)
        # ------------------------------------------
        script_1 = "So we have two ways of looking at math, we have the computational world of syntax, and the platonic world of semantics."
        with self.voiceover(text=script_1) as tracker:
            self.wait(tracker.duration)

        script_2 = "To understand the relation between these two worlds, let's start with a simple language with a single binary relation symbol E."
        l_graph_center = MathTex(r"\mathcal{L}_G = \{E\}", font_size=50)
        with self.voiceover(text=script_2) as tracker:
            self.play(Write(l_graph_center), run_time=1.5)
            self.play(l_graph_center.animate.move_to(UP * 2.5), run_time=1)
            self.wait(max(0, tracker.duration - 2.5))

        script_3 = "We can visualize models in this language by sets of points and arrows between these points."
        # Create a Directed Graph in the center
        vertices = ["a", "b", "c", "d", "e"]
        edges = [("a", "b"), ("a", "c"), ("b", "c"), ("c", "d"), ("d", "e")]
        di_graph = DiGraph(
            vertices, edges, 
            layout="circular", labels=True, 
            vertex_config={"radius": 0.2, "color": BLUE},
            edge_config={"color": WHITE, "stroke_width": 2, "tip_length": 0.2}
        ).scale(0.9).move_to(DOWN * 0.5)

        with self.voiceover(text=script_3) as tracker:
            self.play(Create(di_graph), run_time=1.5)
            self.play(Indicate(di_graph.edges[("a", "b")], color=YELLOW, scale_factor=1.5), run_time=1)
            self.wait(max(0, tracker.duration - 2.5))

        # Fade out intro elements
        self.play(FadeOut(l_graph_center), FadeOut(di_graph))

        # ------------------------------------------
        # 2. SETUP SYNTAX VS SEMANTICS SPLIT
        # ------------------------------------------
        divider = Line(UP * 4, DOWN * 4, stroke_width=2).set_color(WHITE)
        self.play(Create(divider))

        syntax_center = LEFT * 3.5
        semantics_center = RIGHT * 3.5

        g_title_syn = MathTex(r"\mathcal{L}_G = \{E\}", font_size=36).move_to(syntax_center + UP * 3)
        g_title_sem = MathTex(r"\mathcal{G} = (X, E^\mathcal{G})", font_size=36).move_to(semantics_center + UP * 3)

        phi_tex = MathTex(r"\varphi: \forall x,y,z (Exy \land Eyz \to Exz)", font_size=32, color=TEAL).move_to(syntax_center + UP * 1.5)
        psi_tex = MathTex(r"\psi: \forall x \neg Exx", font_size=32, color=ORANGE).next_to(phi_tex, DOWN, buff=0.5)
        chi_tex = MathTex(r"\chi: \forall x,y (Exy \to \neg Eyx)", font_size=32, color=PINK).next_to(psi_tex, DOWN, buff=0.5)

        mod_phi_psi = MathTex(r"Mod(\{\varphi, \psi\})", font_size=40, color=YELLOW).move_to(semantics_center + UP * 2)
        mod_eq = MathTex(r"Mod(\{\varphi, \psi, \chi\}) = Mod(\{\varphi, \psi\})", font_size=32).move_to(semantics_center + DOWN * 2)
        entails = MathTex(r"\{\varphi, \psi\} \models \chi", font_size=36, color=YELLOW).next_to(mod_eq, DOWN, buff=0.3)

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
        
        # Grid Layout
        for i, g in enumerate(all_graphs):
            row = i // 4
            col = i % 4
            shift_x = 0.6 if row != 1 else 0
            g.move_to(semantics_center + UP * 1.5 + DOWN * (row * 1.2) + LEFT * 2.2 + RIGHT * (col * 1.3 + shift_x))

        chaos_dots = MathTex(r"\dots").move_to(semantics_center + UP * 0.3 + RIGHT * 2.8)
        universe_group = VGroup(all_graphs, chaos_dots)

        # ------------------------------------------
        # 3. AXIOMS AND THE UNIVERSE OF MODELS
        # ------------------------------------------
        script_4 = "We need to define axioms to determine the behaviour of this edge relation E."
        with self.voiceover(text=script_4) as tracker:
            self.play(Write(g_title_syn), Write(g_title_sem), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        script_5 = "Without any axioms, every possible combination of points and all possible arrows drawn between them is a model of our empty theory."
        with self.voiceover(text=script_5) as tracker:
            self.play(FadeIn(universe_group, lag_ratio=0.05), run_time=3)
            self.wait(max(0, tracker.duration - 3))

        script_6 = "An axiom can be any FOL sentence."
        with self.voiceover(text=script_6) as tracker:
            self.wait(tracker.duration)

        script_7 = "For example, we can consider this formula phi, expressing transitivity,"
        with self.voiceover(text=script_7) as tracker:
            self.play(Write(phi_tex), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

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

        script_8 = "meaning that if there is some path between nodes, then there is a direct path between these nodes,"
        with self.voiceover(text=script_8) as tracker:
            self.play(universe_group.animate.set_opacity(0.15), run_time=0.5)
            self.play(FadeIn(trans_nodes), GrowArrow(arr_ab), GrowArrow(arr_bc), run_time=1)
            self.play(GrowArrow(arr_ac), run_time=1)
            self.wait(max(0, tracker.duration - 2.5))

        self.play(FadeOut(trans_nodes), FadeOut(arr_ab), FadeOut(arr_bc), FadeOut(arr_ac))

        script_9 = "or this sentence psi expressing irreflexitivity, which enforces that any model of it must not contain any self-referential arrows."
        with self.voiceover(text=script_9) as tracker:
            self.play(Write(psi_tex), run_time=1)
            self.play(universe_group.animate.set_opacity(1), run_time=0.5)
            self.play(Indicate(invalid_graphs[0][1], color=RED, scale_factor=1.5), run_time=1.5)
            invalid_graphs[0][1].set_color(RED)
            self.wait(max(0, tracker.duration - 3))

        # ------------------------------------------
        # 4. FILTERING MOD(PHI, PSI)
        # ------------------------------------------
        script_10 = "Such sentences are true in some of the structures, and false in others."
        with self.voiceover(text=script_10) as tracker:
            self.wait(tracker.duration)

        script_11 = "We can combine the sentences, and consider the collection of all structures which satisfy both phi and psi for example, i.e. the collection of all transitive and irreflexive structures."
        with self.voiceover(text=script_11) as tracker:
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
            self.wait(max(0, tracker.duration - 2))

        script_12 = "We will denote this collection by the model set of phi and psi."
        with self.voiceover(text=script_12) as tracker:
            self.play(Write(mod_phi_psi), run_time=1)
            mod_box = SurroundingRectangle(valid_with_dots, color=YELLOW, buff=0.25)
            self.play(Create(mod_box), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        # ------------------------------------------
        # 5. ASYMMETRY ARGUMENT
        # ------------------------------------------
        script_13 = "If we start to analyze the structures in this collection, we might notice some things in common to all of them."
        with self.voiceover(text=script_13) as tracker:
            self.wait(tracker.duration)

        contra_node_a = Dot(semantics_center + LEFT * 1 + UP * 1.5, color=WHITE)
        contra_node_b = Dot(semantics_center + RIGHT * 1 + UP * 1.5, color=WHITE)
        clabel_a = Text("a", font_size=20).next_to(contra_node_a, DOWN)
        clabel_b = Text("b", font_size=20).next_to(contra_node_b, DOWN)
        contra_nodes = VGroup(contra_node_a, contra_node_b, clabel_a, clabel_b)
        arr_fwd = Arrow(contra_node_a, contra_node_b, buff=0.1, path_arc=-0.3, color=PINK)
        arr_bwd = Arrow(contra_node_b, contra_node_a, buff=0.1, path_arc=-0.3, color=PINK)

        script_14 = "For example we may notice that in none of them do we have an arrow from a to b and from b to a."
        with self.voiceover(text=script_14) as tracker:
            self.play(valid_with_dots.animate.set_opacity(0.15), mod_box.animate.set_color(DARK_GREY), FadeOut(mod_phi_psi), run_time=0.5)
            self.play(FadeIn(contra_nodes), GrowArrow(arr_fwd), GrowArrow(arr_bwd), run_time=1)
            self.wait(max(0, tracker.duration - 1.5))

        script_15 = "We can easily see why, since if we did have an edge from a to b and from b to a in a transitive and irreflexive structure,"
        with self.voiceover(text=script_15) as tracker:
            self.wait(tracker.duration)

        arr_self = Arc(radius=0.3, start_angle=0, angle=3*PI/2, color=YELLOW).next_to(contra_node_a, UP, buff=0).shift(DOWN*0.1)
        arr_self.add_tip()

        script_16 = "then by transitivity we should have a direct path a to a."
        with self.voiceover(text=script_16) as tracker:
            self.play(phi_tex.animate.set_color(YELLOW), run_time=0.5)
            self.play(Create(arr_self), run_time=1)
            self.play(phi_tex.animate.set_color(TEAL), run_time=0.5)
            self.wait(max(0, tracker.duration - 2))

        cross = Cross(arr_self, stroke_color=RED, stroke_width=6)

        script_17 = "But then the structures is not irreflexive, a contradiction."
        with self.voiceover(text=script_17) as tracker:
            self.play(psi_tex.animate.set_color(YELLOW), run_time=0.5)
            self.play(Create(cross), run_time=0.5)
            self.play(psi_tex.animate.set_color(ORANGE), run_time=0.5)
            self.wait(max(0, tracker.duration - 1.5))

        self.play(
            FadeOut(contra_nodes), FadeOut(arr_fwd), FadeOut(arr_bwd), FadeOut(arr_self), FadeOut(cross),
            valid_with_dots.animate.set_opacity(1), mod_box.animate.set_color(YELLOW), FadeIn(mod_phi_psi), run_time=1
        )

        script_18 = "So, we see that adding this sentence chi expressing assymetry, is redundant,"
        with self.voiceover(text=script_18) as tracker:
            self.play(Write(chi_tex), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_19 = "in the sense that Mod(phi,psi,chi)=Mod(phi,psi)."
        with self.voiceover(text=script_19) as tracker:
            self.play(Write(mod_eq), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_20 = "We denote this by {phi,psi} models chi."
        with self.voiceover(text=script_20) as tracker:
            self.play(Write(entails), run_time=1)
            self.wait(max(0, tracker.duration - 1))

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