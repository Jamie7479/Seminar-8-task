

from kivy.app import App
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import  Button

class ShoppingApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.products = [{"name": "Cheese", "price": 12.5}, {"name": "Laptop", "price": 912.95}, {"name": "Plant", "price": 4.75},
         {"name": "Coffee Machine", "price": 2300.00}, {"name": "Guitar", "price": 4399.95}]

    def build(self):
        """Build the Kivy GUI."""
        Window.size = 1000, 800
        self.title = "Shopping App"
        self.root = Builder.load_file("view.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for product in self.products:
            temp_button = Button(text=str(product))
            temp_button.bind(on_release=self.press_entry)
            temp_button.product = product
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        pass


ShoppingApp().run()