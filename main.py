from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.config import Config

from SpecialWidgets.Buttons.RoundedButton import RoundedButton
from SpecialWidgets.DropDownButtons.DropDownButton import DropDownButton
from SpecialWidgets.ScrollWidgets.ProductScrollView import ProductScrollView
from SpecialWidgets.SearchBars.SearchBar import SearchBar

from APISource.User.User import User

Config.set('graphics', 'resizable', False)
Window.size = (500, 600)
Window.resizable = False

Builder.load_string('''
<MainPage>:
    canvas.before:
        Color:
            rgba: 34/255, 34/255, 34/255, 1
        Rectangle:
            pos: self.pos
            size: self.size
''')


class MainPage(FloatLayout):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)

        self.search_box = SearchBar(
            size_hint=(0.7, 0.05),
            pos_hint={'center_x': 0.5, 'center_y': 0.95}
        )

        self.search_button = RoundedButton(
            text="Search",
            size_hint=(0.25, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.81}
        )
        self.search_button.bind(on_press=self.buttonClicked)

        self.screen_widget = None

        self.country_drop_down = DropDownButton(kind="country")
        self.country_drop_down_button = RoundedButton(text='Select Country', size_hint=(0.2, 0.05), pos_hint={'center_x': 0.28, 'center_y': 0.89}, font_size=12)
        self.country_drop_down_button.bind(on_release=self.country_drop_down.open)
        self.country_drop_down.bind(on_select=lambda instance, x: setattr(self.country_drop_down_button, 'text', x))

        self.condition_drop_down = DropDownButton(kind="condition")
        self.condition_drop_down_button = RoundedButton(text='Select Condition', size_hint=(0.2, 0.05), pos_hint={'center_x': 0.5, 'center_y': 0.89}, font_size=12)
        self.condition_drop_down_button.bind(on_release=self.condition_drop_down.open)
        self.condition_drop_down.bind(on_select=lambda instance1, x: setattr(self.condition_drop_down_button, "text", x))

        self.relevance_drop_down = DropDownButton(kind="relevance")
        self.relevance_drop_down_button = RoundedButton(text="Select Relevance", size_hint=(0.2, 0.05), pos_hint={'center_x': 0.72, 'center_y': 0.89}, font_size=12)
        self.relevance_drop_down_button.bind(on_release=self.relevance_drop_down.open)
        self.relevance_drop_down.bind(on_select=lambda instance2, x: setattr(self.relevance_drop_down_button, "text", x))

        self.add_widget(self.search_box)

        self.add_widget(self.search_button)

        self.add_widget(self.country_drop_down_button)

        self.add_widget(self.condition_drop_down_button)

        self.add_widget(self.relevance_drop_down_button)

    def buttonClicked(self, button):

        country_text = self.country_drop_down_button.text
        condition_text = self.condition_drop_down_button.text
        relevance_text = self.relevance_drop_down_button.text

        if country_text != "Select Country" or condition_text != "Select Condition" or relevance_text != "Select Relevance":
            obj = User(self.search_box.information.text ,country_text, relevance_text, condition_text)
            set_of_element = obj.search()

            self.screen_widget = ProductScrollView(
                size_hint = (0.8, 0.7),
                pos_hint = {'center_x': 0.5, 'center_y': 0.4},
                element = set_of_element
            )
            self.add_widget(self.screen_widget)


            for element in set_of_element:
                print(element["product_price"])

class TheAmazonApp(App):
    def build(self):
        Config.write()
        return MainPage()

if __name__ == "__main__":
    TheAmazonApp().run()