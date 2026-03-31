from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

# ==========================================
# SCENE 8: FROM "GOAL OF MATH IS TO ADD ENOUGH..." to "ADDING ONE MORE MAKES INCONS."
# ==========================================
class CompleteTheories(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # ------------------------------------------
        # 1. RECREATE SCENE 7 END STATE
        # ------------------------------------------
        divider = Line(UP * 4, DOWN * 4, stroke_width=2).set_color(WHITE)
        self.add(divider)

        syntax_center = LEFT * 3.5
        semantics_center = RIGHT * 3.5

        # Syntax Left
        sigma_tex = MathTex(r"\Sigma = \{\varphi, \psi\}", font_size=40, color=YELLOW).move_to(syntax_center + UP * 2)
        self.add(sigma_tex)

        # Semantics Right (The Filtered Valid Models)
        valid_graphs = VGroup(
            self.get_mini_graph("line"), self.get_mini_graph("tree"), self.get_mini_graph("bool_alg"),
            self.get_mini_graph("disconnected"), self.get_mini_graph("lattice"), self.get_mini_graph("pentagon_dag")
        )
        
        for i, g in enumerate(valid_graphs):
            row = i // 2
            col = i % 2
            shift_x = 0.7 if row != 1 else 0
            g.move_to(semantics_center + UP * 1 + DOWN * (row * 1.2) + LEFT * 1 + RIGHT * (col * 1.6 + shift_x))
            
        mod_dots = MathTex(r"\dots").move_to(semantics_center + DOWN * 0.2 + RIGHT * 2)
        valid_with_dots = VGroup(valid_graphs, mod_dots)
        mod_box = SurroundingRectangle(valid_with_dots, color=YELLOW, buff=0.25)
        
        self.add(valid_with_dots, mod_box)

        # ------------------------------------------
        # 2. NARROWING DOWN TO ONE STRUCTURE
        # ------------------------------------------
        sigma_expanded = MathTex(r"\Sigma = \{\varphi, \psi, \chi, \theta, \dots\}", font_size=40, color=YELLOW).move_to(syntax_center + UP * 2)

        script_1a = "In some sense the goal of mathematics is to add enough axioms such that there is "
        with self.voiceover(text=script_1a) as tracker:
            self.play(ReplacementTransform(sigma_tex, sigma_expanded), run_time=tracker.duration)

        script_1b = "exactly one structure which satisfies them."
        with self.voiceover(text=script_1b) as tracker:
            # Fade out everything except the leftmost graph in the middle row (valid_graphs[2])
            graphs_to_fade = VGroup(valid_graphs[0], valid_graphs[1], valid_graphs[3], valid_graphs[4], valid_graphs[5], mod_dots)
            self.play(
                FadeOut(graphs_to_fade),
                mod_box.animate.surround(valid_graphs[2], buff=0.2),
                run_time=1
            )
            
            # Increase the size of the isolated model
            isolated_model = VGroup(valid_graphs[2], mod_box)
            self.play(
                isolated_model.animate.scale(2).move_to(semantics_center + DOWN * 0.5), 
                run_time=1.5
            )
            self.wait(max(0.1, tracker.duration - 2.5))

        th_sigma = MathTex(r"Th(\Sigma)", font_size=40, color=BLUE).next_to(sigma_expanded, DOWN, buff=0.5)

        script_2 = "In this case, the theory of Sigma is a perfect description of the structure, it contains everything we could possibly say about the structure in first order logic in the language of the structure."
        with self.voiceover(text=script_2) as tracker:
            self.play(Write(th_sigma), run_time=1.5)
            self.wait(max(0.1, tracker.duration - 1.5))

        # ------------------------------------------
        # 3. FINITE VS INFINITE CHARACTERIZATION
        # ------------------------------------------
        # Explicit, massive finite characterization formula
        finite_formula = VGroup(
            MathTex(r"\varphi_{fin} \equiv \forall x,y,z (Exy \land Eyz \to Exz)", font_size=24),
            MathTex(r"\land \ \forall x \neg Exx", font_size=24),
            MathTex(r"\land \ \exists x_1, x_2, x_3, x_4, x_5 \left(\bigwedge_{i \neq j} x_i \neq x_j\right)", font_size=24),
            MathTex(r"\land \ \forall x_1, x_2, x_3, x_4, x_5, x_6 \left(\bigvee_{i \neq j} x_i = x_j\right)", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(syntax_center + DOWN * 1.5)

        script_3 = "If a theory has a finite model, then there is a single sentence phi which fully characterizes the theory, and therefore there is exactly one model up to isomorphism."
        with self.voiceover(text=script_3) as tracker:
            self.play(Write(finite_formula), run_time=2)
            self.wait(max(0.1, tracker.duration - 2))

        script_4 = "However, in the third video, we will see why this is impossible for a theory with infinite models."
        with self.voiceover(text=script_4) as tracker:
            self.play(FadeOut(finite_formula), FadeOut(th_sigma), run_time=1)
            self.wait(max(0.1, tracker.duration - 1))

        # Re-center Sigma
        sigma_simple = MathTex(r"\Sigma", font_size=48, color=YELLOW).move_to(syntax_center + UP * 1)

        # Infinite Models Box
        inf_models = MathTex(r"\mathcal{M}, \mathcal{N}, \dots", font_size=40).move_to(semantics_center + UP * 1)
        inf_box = SurroundingRectangle(inf_models, color=YELLOW, buff=0.4)

        script_5 = "But we can still achieve something weaker, namely that all models of our set Sigma satisfy the same sentences."
        with self.voiceover(text=script_5) as tracker:
            self.play(
                ReplacementTransform(sigma_expanded, sigma_simple),
                FadeOut(isolated_model),
                run_time=1
            )
            self.play(FadeIn(inf_models), Create(inf_box), run_time=1.5)
            self.wait(max(0.1, tracker.duration - 2.5))

        script_6 = "You may ask how we can know that two models M and N are actually different if they satisfy the same sentences. Again, we will see this in the third video, but for now just know that this has to do with the inability of First Order Logic to deal with the complexities of infinity."
        with self.voiceover(text=script_6) as tracker:
            self.wait(tracker.duration)

        # ------------------------------------------
        # 4. COMPLETENESS (SEMANTIC & SYNTACTIC)
        # ------------------------------------------
        script_7 = "However, if we have such a set Sigma, then we cannot differentiate any of its models using a single first order sentence."
        with self.voiceover(text=script_7) as tracker:
            self.wait(tracker.duration)

        alpha_tex = MathTex(r"\alpha", font_size=40, color=TEAL).move_to(syntax_center + DOWN * 0.5)

        # 4-Line display for Semantic Completeness
        either_text = Text("Either:", font_size=24, color=WHITE)
        model_alpha = MathTex(r"\mathcal{M} \models \alpha \quad \text{and} \quad \mathcal{N} \models \alpha", font_size=32)
        or_text = Text("Or:", font_size=24, color=WHITE)
        model_not_alpha = MathTex(r"\mathcal{M} \models \neg \alpha \quad \text{and} \quad \mathcal{N} \models \neg \alpha", font_size=32)
        
        comp_group = VGroup(either_text, model_alpha, or_text, model_not_alpha).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(semantics_center + DOWN * 1.5)

        script_8 = "So, given any sentence alpha we can write, either every model satisfies it, or every model satisfies its negation."
        with self.voiceover(text=script_8) as tracker:
            self.play(Write(alpha_tex), run_time=1)
            self.play(FadeIn(comp_group[0]), FadeIn(comp_group[1], shift=DOWN), run_time=1)
            self.play(FadeIn(comp_group[2]), FadeIn(comp_group[3], shift=DOWN), run_time=1)
            self.wait(max(0.1, tracker.duration - 3))

        complete_text = Text("Complete Theory", font_size=36, color=GREEN).next_to(sigma_simple, UP, buff=0.5)

        script_9 = "In this case we say that the theory is complete."
        with self.voiceover(text=script_9) as tracker:
            self.play(Write(complete_text), run_time=1)
            self.wait(max(0.1, tracker.duration - 1))

        syn_comp = MathTex(r"\forall \alpha: \quad \alpha \in \Sigma \quad \lor \quad \neg \alpha \in \Sigma", font_size=36).move_to(syntax_center + DOWN * 2)

        script_10 = "Syntactically, completeness means that the theory is maximally consistent, in the sense that for every formula alpha, either alpha is in Sigma, or not alpha is in Sigma."
        with self.voiceover(text=script_10) as tracker:
            self.play(FadeOut(alpha_tex))
            self.play(Write(syn_comp), run_time=2)
            self.wait(max(0.1, tracker.duration - 2))

        script_11 = "Thus, it decides everything that it possibly can."
        with self.voiceover(text=script_11) as tracker:
            self.wait(tracker.duration)

        # Inconsistency climax
        new_alpha = MathTex(r"\cup \ \{\alpha_{new}\}", font_size=40, color=RED).next_to(sigma_simple, RIGHT, buff=0.2)

        script_12 = "If we added even a single new formula alpha to a complete theory, it would then become inconsistent, and it would therefore have no models."
        with self.voiceover(text=script_12) as tracker:
            self.play(FadeIn(new_alpha, shift=LEFT), run_time=1)
            # The model box turns red, shakes, and the models inside vanish
            self.play(inf_box.animate.set_color(RED), run_time=0.5)
            self.play(inf_box.animate.shift(LEFT * 0.1), run_time=0.1)
            self.play(inf_box.animate.shift(RIGHT * 0.2), run_time=0.1)
            self.play(inf_box.animate.shift(LEFT * 0.1), FadeOut(inf_models, scale=0.5), run_time=0.5)
            self.wait(max(0.1, tracker.duration - 2.2))

        self.wait(2)


    # ---------------------------------------------------
    # Helper Function to Rebuild Valid Graphs
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
            
        return group.scale(0.55)