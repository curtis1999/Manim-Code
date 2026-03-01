from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class TermsAndFormulas(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(transcription_model=None))

        # --- SCENE DEFINITIONS ---
        COLOR_DEF = BLUE
        COLOR_TERM = YELLOW
        COLOR_FORMULA = GREEN
        
        # 1. Random Strings Analogy
        str_1 = Tex(r"$\{ \text{hjr} \}$", font_size=40)
        str_2 = Tex(r"$\{ \text{asue}, \text{hjr} \}$", font_size=40)
        str_3 = Tex(r"$\{ \text{qwx}, \text{asue}, \text{hjr} \}$", font_size=40)
        str_4 = Tex(r"$\{ \text{\textbf{cat}}, \text{qwx}, \text{asue}, \text{hjr} \}$", font_size=40)
        
        # 2. Terms Definition
        term_title = Tex(r"Set of Terms $\mathcal{T}$:", font_size=40, color=COLOR_DEF)
        term_1 = Tex(r"1. All constants in the language ($c$)", font_size=32)
        term_2 = Tex(r"2. All variables in the language ($v$)", font_size=32)
        term_3 = Tex(r"3. $F(t_1, \dots, t_n)$ whenever $F$ is $n$-ary and $t_i \in \mathcal{T}$", font_size=32)
        term_def_group = VGroup(term_title, term_1, term_2, term_3).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        term_def_group.to_edge(UP+LEFT, buff=0.5)

        # 3. Term Examples
        t_ex1 = MathTex("5", font_size=36) # Closed
        t_ex2 = MathTex("x", font_size=36)
        t_ex3 = MathTex("(x+y) \cdot 7", font_size=36)
        t_ex4 = MathTex("2+4", font_size=36) # Closed
        t_ex5 = MathTex("y+1", font_size=36)
        t_ex6 = MathTex("x \cdot (y+2)", font_size=36)
        
        all_terms = VGroup(t_ex1, t_ex2, t_ex3, t_ex4, t_ex5, t_ex6).arrange_in_grid(rows=2, cols=3, buff=1)
        all_terms.next_to(term_def_group, DOWN, buff=1).shift(RIGHT * 1)
        
        closed_terms = VGroup(t_ex1, t_ex4)
        open_terms = VGroup(t_ex2, t_ex3, t_ex5, t_ex6)

        # 4. Number Line for Closed Terms
        num_line = NumberLine(x_range=[0, 8, 1], length=7, include_numbers=True, font_size=24)
        num_line.to_edge(DOWN, buff=1)

        # 5. Formulas Definition
        form_title = Tex(r"Set of Formulas $\Phi$:", font_size=40, color=COLOR_FORMULA)
        form_base = Tex(r"Base: $R(t_1, \dots, t_n)$ where $R$ is $n$-ary and $t_i \in \mathcal{T}$", font_size=32)
        form_def_group = VGroup(form_title, form_base).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        form_def_group.move_to(LEFT * 2 + UP * 1)
        
        atom_1 = MathTex(r"1+1=3", font_size=32)
        atom_2 = MathTex(r"3 \cdot 5 < 2+(8 \cdot 12)", font_size=32)
        atom_group = VGroup(atom_1, atom_2).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        atom_group.next_to(form_def_group, RIGHT, buff=1.5)

        # Inductive Formulas
        ind_title = Tex(r"If $\varphi, \psi \in \Phi$ and $x$ is a variable, then:", font_size=32).set_color(COLOR_FORMULA)
        ind_1 = MathTex(r"\neg \varphi", font_size=36)
        ind_2 = MathTex(r"(\varphi \land \psi)", font_size=36)
        ind_3 = MathTex(r"(\varphi \lor \psi)", font_size=36)
        ind_4 = MathTex(r"(\varphi \to \psi)", font_size=36)
        ind_5 = MathTex(r"\forall x \varphi", font_size=36)
        ind_6 = MathTex(r"\exists x \varphi", font_size=36)
        
        ind_formulas = VGroup(ind_1, ind_2, ind_3, ind_4, ind_5, ind_6).arrange(RIGHT, buff=0.6)
        ind_group = VGroup(ind_title, ind_formulas).arrange(DOWN, buff=0.4).next_to(form_def_group, DOWN, buff=1).align_to(form_def_group, LEFT)


        # --- ANIMATIONS ---

        script_1a = "Once we have fixed our vocabulary, we can define the well-formed terms and well-formed formulas. This is somewhat similar to English."
        with self.voiceover(text=script_1a) as tracker:
            self.wait(tracker.duration)

        script_1b = "If we image the set of all possible combinations of letters in the alphabet, most will be meaningless."
        with self.voiceover(text=script_1b) as tracker:
            self.play(FadeIn(str_1), run_time=0.5)
            self.play(ReplacementTransform(str_1, str_2), run_time=0.5)
            self.play(ReplacementTransform(str_2, str_3), run_time=0.5)
            self.wait(max(0, tracker.duration - 1.5))

        script_1c = "However, some combinations of letters form words."
        with self.voiceover(text=script_1c) as tracker:
            self.play(ReplacementTransform(str_3, str_4), run_time=0.5)
            self.play(str_4[0][1:4].animate.set_color(COLOR_TERM), run_time=0.5) # Highlights 'cat'
            self.wait(max(0, tracker.duration - 1))

        script_2a = "Here we define the terms recursively,"
        with self.voiceover(text=script_2a) as tracker:
            self.play(FadeOut(str_4), run_time=0.5)
            self.play(Write(term_title), run_time=0.5)
            self.wait(max(0, tracker.duration - 1))

        script_2b = "where in the base case we say that the set of terms consists of: 1. All constants in the language,"
        with self.voiceover(text=script_2b) as tracker:
            self.play(FadeIn(term_1, shift=RIGHT*0.3), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_2c = "and 2. All variables in the language."
        with self.voiceover(text=script_2c) as tracker:
            self.play(FadeIn(term_2, shift=RIGHT*0.3), run_time=1)
            self.wait(max(0, tracker.duration - 1))

        script_3 = "Then if we have a function symbol F, which expects n-inputs, then given n terms t_1 through t_n, the term Ft_1 through t_n is also a term."
        with self.voiceover(text=script_3) as tracker:
            self.play(FadeIn(term_3, shift=RIGHT*0.3), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        script_4 = "So all of the following are examples of terms in the language of arithmetic."
        with self.voiceover(text=script_4) as tracker:
            self.play(FadeIn(all_terms, lag_ratio=0.1), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        script_5a = "Note that terms without variables, which are known as closed terms simply point to specific elements of the structure."
        with self.voiceover(text=script_5a) as tracker:
            # Reorganize terms: Closed terms at top, open terms dimmed below
            self.play(
                closed_terms.animate.arrange(RIGHT, buff=2).move_to(LEFT * 1 + DOWN * 0.5),
                open_terms.animate.arrange(RIGHT, buff=1).move_to(LEFT * 1 + DOWN * 1.5).set_opacity(0.3),
                run_time=1.5
            )
            self.play(closed_terms.animate.set_color(COLOR_TERM), run_time=0.5)
            self.wait(max(0, tracker.duration - 2))

        script_5b = "So in the theory of arithmetic, they simply point to numbers."
        with self.voiceover(text=script_5b) as tracker:
            self.play(FadeIn(num_line), run_time=1)
            
            # Arrows pointing from the math text to the actual point on the number line
            arrow_5 = CurvedArrow(t_ex1.get_bottom(), num_line.n2p(5), angle=PI/4, color=COLOR_TERM)
            arrow_6 = CurvedArrow(t_ex4.get_bottom(), num_line.n2p(6), angle=PI/4, color=COLOR_TERM)
            
            self.play(Create(arrow_5), Create(arrow_6), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        script_6a = "Once we have our terms, we can combine them to create well-formed formulas. Similar to English, well-formed formulas are special combinations of terms that are grammatically correct."
        with self.voiceover(text=script_6a) as tracker:
            self.play(
                FadeOut(all_terms), FadeOut(num_line), FadeOut(arrow_5), FadeOut(arrow_6),
                run_time=1
            )
            # Scale down and push terms definition out of the way
            self.play(
                term_def_group.animate.scale(0.6).to_edge(UP+LEFT, buff=0.2),
                run_time=1.5
            )
            self.wait(max(0, tracker.duration - 2.5))

        script_6b = "Again, these are defined recursively, where in the base case we have the relation terms, of the form: R t_1 through t_n, where R is n-ary."
        with self.voiceover(text=script_6b) as tracker:
            self.play(Write(form_title), run_time=1)
            self.play(FadeIn(form_base, shift=RIGHT*0.3), run_time=1)
            self.wait(max(0, tracker.duration - 2))

        script_6c = "Note we are being general here, and most relations are binary. In form, these are the same as the functional terms, but instead of pointing to specific elements of the structure, they make a claim about the structure, which may or may not be true."
        with self.voiceover(text=script_6c) as tracker:
            self.wait(tracker.duration)

        script_7 = "For example, the following are atomic formulas in the theory of arithmetic: 1+1=3. And 3 times 5 is less than 2 plus 8 times 12."
        with self.voiceover(text=script_7) as tracker:
            self.play(FadeIn(atom_group, lag_ratio=0.3), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        script_8a = "Then we can inductively define the non-atomic formulas using the Boolean connectives and the quantifiers. So if phi and psi are terms,"
        with self.voiceover(text=script_8a) as tracker:
            self.play(FadeIn(ind_title), FadeIn(ind_formulas), run_time=1.5)
            self.wait(max(0, tracker.duration - 1.5))

        script_8b = "then so is phi and psi,"
        with self.voiceover(text=script_8b) as tracker:
            self.play(ind_2.animate.set_color(YELLOW).scale(1.2), run_time=0.5)
            self.play(ind_2.animate.set_color(WHITE).scale(1/1.2), run_time=0.5)
            self.wait(max(0, tracker.duration - 1))

        script_8c = "so is for all x phi, etc."
        with self.voiceover(text=script_8c) as tracker:
            self.play(ind_5.animate.set_color(YELLOW).scale(1.2), run_time=0.5)
            self.play(ind_5.animate.set_color(WHITE).scale(1/1.2), run_time=0.5)
            self.wait(max(0, tracker.duration - 1))

        script_9 = "Now we are ready to define what a mathematical structure is, and how we construct a bridge between the worlds of syntax and semantics."
        with self.voiceover(text=script_9) as tracker:
            self.wait(max(0, tracker.duration - 1))
            self.play(
                FadeOut(term_def_group), FadeOut(form_def_group), 
                FadeOut(atom_group), FadeOut(ind_group),
                run_time=1
            )
            
        self.wait(1)