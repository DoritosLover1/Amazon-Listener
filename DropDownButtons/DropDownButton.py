from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.graphics import Color, RoundedRectangle

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        with self.canvas.before:
            Color(255/255, 153/255, 0/255, 1)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[15], padding=(20,10))

        # Buton boyutu veya konumu değiştiğinde arka planı güncellemek için bind işlemi
        self.bind(pos=self.update_rect, size=self.update_rect)
        self.background_color=(0,0,0,0)
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class DropDownButton(DropDown):
    def __init__(self, **kwargs):
        self.list = []
        self.country_list = ['US', 'AU', 'BR', 'CA', 'CN', 'FR', 'DE', 'IN', 'IT']
        self.condition_list = ['ALL', 'NEW', 'USED', 'RENEWED', 'COLLECTIBLE']
        self.relevance_list = ['RELEVANCE', 'LOWEST_PRICE', 'HIGHEST_PRICE', 'REVIEWS', 'NEWEST', 'BEST_SELLERS']

        match kwargs.pop("kind"):
            case "country":
                self.list.extend(self.country_list)
            case "condition":
                self.list.extend(self.condition_list)
            case "relevance":
                self.list.extend(self.relevance_list)

        super(DropDownButton, self).__init__(**kwargs)

        for option in self.list:
            selection_button = RoundedButton(text=option, size_hint_y=None, height=30, font_size=12)
            selection_button.bind(on_release=lambda btn=selection_button: self.select(btn.text))
            self.add_widget(selection_button)

    def update_background(self, *args):
        self.background.pos = self.pos
        self.background.size = self.size