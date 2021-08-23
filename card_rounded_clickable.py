from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

card = """
MDCard:
    orientation: 'vertical'
    size_hint: 0.5, 0.5
    pos_hint: {"center_x": 0.5, "center_y": 0.5}
    elevation: 12
    on_release: print("hello")
    border_radius: 20
    radius: [15]
    
"""


class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(card)


if __name__ == "__main__":
    DemoApp().run()
