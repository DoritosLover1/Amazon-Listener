from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle

class SearchBar(FloatLayout):
    def __init__(self, **kwargs):
        super(SearchBar, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0.9, 0.9, 0.9, 1) 
            self.background = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[15]
            )
        self.information = TextInput(
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            hint_text="Enter what you wanna search",
            multiline=False,
            background_color=(0,0,0,0) 
        )
        self.add_widget(self.information)
        self.bind(size=self.update_background, pos=self.update_background)

    def update_background(self, *args):
        self.background.pos = self.pos
        self.background.size = self.size