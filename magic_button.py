from kivymd.app import MDApp
from kivymd.uix.behaviors.magic_behavior import MagicBehavior
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder

magic_button = """
MDFloatLayout:
    ButtonM:
        text: 'Python'
        font_style: 'Button'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_release: self.grow()
"""


class ButtonM(MagicBehavior, MDRaisedButton):
    pass


class DemoApp(MDApp):
    def build(self):
        magic = Builder.load_string(magic_button)
        return magic


if __name__ == "__main__":
    DemoApp().run()
