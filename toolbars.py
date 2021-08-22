from kivy.config import Config
Config.set('graphics', 'width', '340')
Config.set('graphics', 'height', '480')

from kivymd.app import MDApp
from kivy.lang import Builder

toolbar = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Demo Application'
            left_action_items: [['menu', lambda x: app.navigation_draw()]]
            right_action_items: [['language-python', lambda x: app.navigation_draw()]]
            elevation: 10

        MDLabel:
            text: 'Hello Python!'
            halign: 'center'
        MDBottomAppBar:
            MDToolbar:
                mode: 'center'
                type: 'bottom'
                icon: 'coffee'
                on_action_button: app.navigation_draw()
                
                MDIconButton:
                    icon: 'android'
                    theme_text_color: 'Custom'
                    text_color: 1,1,1,1
            
"""


class DemoAp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        screen = Builder.load_string(toolbar)

        return screen

    def navigation_draw(self):
        print('Navigation')


if __name__ == "__main__":
    DemoAp().run()
