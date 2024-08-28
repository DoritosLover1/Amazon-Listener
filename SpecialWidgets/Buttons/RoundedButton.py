from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        with self.canvas.before:
            Color(255/255, 153/255, 0/255, 1)
            self.background = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[20]
            )
        self.background_color=(0,0,0,0)
        self.bind(pos=self.update_background, size=self.update_background)
        self.bind(on_press=self.on_press, on_release=self.on_release)

    def update_background(self, *args):
        self.background.pos = self.pos
        self.background.size = self.size

    def on_press(self, *args):
        self.color= (0, 0, 0, 0)

    def on_release(self, *args):
        self.color= (1, 1, 1, 1)