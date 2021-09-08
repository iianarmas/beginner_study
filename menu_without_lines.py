from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp


CREATE = ['Main Service', 'Outreach Service', 'Event']


class Test(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.create_menu_items = [{
                'viewclass': 'MDLabel',
                'text': f'[ref={i}]    {i}[/ref]',
                'markup': True,  
                'height': dp(52),
                'on_ref_press': lambda x=i: self.create_new_callback(x),
            } for i in CREATE
            ]
        self.create_new_menu = MDDropdownMenu(
                items=self.create_menu_items,
                width_mult=3
            )

    # "Create" Menu
    def create_new(self, button):
        self.create_new_menu.caller = button
        self.create_new_menu.open()

    def create_new_callback(self, text_item):
    
        print('Created!')

class TestApp(MDApp):
    def build(self):
        pass


if __name__ == "__main__":
    TestApp().run()
