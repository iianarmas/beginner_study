from kivy.config import Config

Config.set('graphics', 'width', '340')
Config.set('graphics', 'height', '480')

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix import Screen

navigation = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            id: screen_manager
            Screen:
                name: 'default'
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Demo App'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10
                    MDLabel:
                        text: 'Hello Python!'
                        halign: 'center'
                    
            Screen:
                name: 'profile'
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Profile'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10
                    Screen:
                        MDRectangleFlatButton:
                            text: 'Home!'
                            font_style: 'Button'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: screen_manager.current = 'default'
                            
            Screen:
                name: 'favorites'
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Favorites'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 10
                    Screen:
                        MDRectangleFlatButton:
                            text: 'Home!'
                            font_style: 'Button'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: screen_manager.current = 'default'
                        
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '10dp'
                padding: '8dp'
                Image:
                    source: 'images/iian-logo-white-circ-bg.png'
                MDLabel:
                    text: 'iian armas'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: 'sample@gmail.com'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                ScrollView:
                    MDList:
                        TwoLineIconListItem:
                            text: 'Python Profile'
                            secondary_text: 'click me'
                            font_style: 'Subtitle2'
                            on_release: screen_manager.current = 'profile'
                            IconLeftWidget:
                                icon: 'language-python'
                        TwoLineIconListItem:
                            text: 'Favorites'
                            secondary_text: 'click me'
                            font_style: 'Subtitle2'
                            on_release: screen_manager.current = 'favorites'
                            IconLeftWidget:
                                icon: 'coffee'
                        OneLineIconListItem:
                            text: 'Logout'
                            font_style: 'Subtitle2'
                            IconLeftWidget:
                                icon: 'logout'
                                
"""


class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(navigation)

        return screen

    def open_nav(self):
        pass


if __name__ == "__main__":
    DemoApp().run()
