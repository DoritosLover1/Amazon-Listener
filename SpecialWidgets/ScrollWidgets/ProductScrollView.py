from math import radians
import webbrowser

from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle


class ProductScrollView(ScrollView):
    def __init__(self, **kwargs):
        self.set_of_element = kwargs.pop("element")
        super(ProductScrollView, self).__init__(**kwargs)

        with self.canvas.before:
            Color(102 / 255, 102 / 255, 102 / 255, 1)
            self.background = RoundedRectangle(
                pos=(self.x - 10, self.y - 10),
                size=(self.width + 20, self.height + 20)
            )

        self.bind(pos=self.update_background, size=self.update_background)

        self.size_hint = kwargs.get("size_hint")
        self.pos_hint = kwargs.get("pos_hint")

        self.grid_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))
        self.add_widget(self.grid_layout)

        for element in self.set_of_element:
            product_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=100)
            product_image = Image(source=element["product_photo"], size_hint_x=None, width=100)
            product_info = BoxLayout(orientation='vertical')
            product_url = Label(
                text=f"[ref={element['product_url']}]Ürün Linki[/ref]",
                font_size=16,
                color=(0, 0, 1, 1),
                markup=True
            )

            def open_url(instance, value):
                if value:
                    webbrowser.open(instance.text.split('=')[1].split(']')[0])
            product_url.bind(on_ref_press=open_url)

            product_rate = Label(text=f"Ürün Derecesi:{element["product_star_rating"]}", font_size=16)
            product_price = Label(text=f"Ürün Fiyat: {element["product_price"]}{element["currency"]}", font_size=16)

            product_info.add_widget(product_url)
            product_info.add_widget(product_rate)
            product_info.add_widget(product_price)

            product_layout.add_widget(product_image)
            product_layout.add_widget(product_info)
            self.grid_layout.add_widget(product_layout)

        self.do_scroll_x = False
        self.do_scroll_y = True

    def update_background(self, *args):
        self.background.pos = self.pos
        self.background.size = self.size