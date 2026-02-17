from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class MyVoiceRecording(VoiceoverScene):
    def construct(self):
        # 1. Set the service to "RecorderService"
        # This triggers the microphone GUI when you run the file.
        self.set_speech_service(RecorderService(transcription_model=None))

        # SECTION 1
        # The code will pause here and wait for you to record the audio for this block.
        with self.voiceover(text="Welcome to this tutorial on Manim."):
            circle = Circle(color=BLUE)
            self.play(Create(circle))
        
        # SECTION 2
        # Once you finish the first recording, it moves here.
        # You can treat this like a new "take."
        with self.voiceover(text="Now, watch as the circle transforms into a square."):
            square = Square(color=RED)
            self.play(Transform(circle, square))

        # SECTION 3
        with self.voiceover(text="And that is the end of the demonstration."):
            self.play(FadeOut(square))