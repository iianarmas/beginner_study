from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.app import MDApp
from kivy.lang import Builder
from text_helper import *
from kivymd.uix.dialog import MDDialog


class DemoApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Screen()
        self.username = Builder.load_string(username_helper)

        close_button = MDFlatButton(text='Close', font_style='Button', on_release=self.close_dialog)
        more_button = MDFlatButton(text='More', font_style='Button')
        close_err_button = MDFlatButton(text='Try Again', font_style='Button',
                                        on_press=self.close_err_dialog)

        self.dialog_welcome = MDDialog(title='Verified User', text=f'Welcome! You will now be redirected.',
                                       buttons=[close_button, more_button])
        self.dialog_err = MDDialog(title='Error!', text='Please enter your username', buttons=[close_err_button])

    def on_button_release(self, obj):

        if self.username.text:
            self.dialog_welcome.open()
        else:
            self.dialog_err.open()

    def close_dialog(self, obj):
        self.dialog_welcome.dismiss()

    def close_err_dialog(self, obj):
        self.dialog_err.dismiss()

    def build(self):
        self.theme_cls.primary_palette = 'Green'

        login_label = MDLabel(text='Login', halign='center', font_style='H4', theme_text_color='Custom',
                              pos_hint={'center_x': 0.5, 'center_y': 0.62},
                              text_color=(71 / 255, 139 / 255, 64 / 255, 1))

        button = MDRectangleFlatButton(text='Show', pos_hint={'center_x': 0.5, 'center_y': 0.38},
                                       on_release=self.on_button_release)

        self.screen.add_widget(login_label)
        self.screen.add_widget(self.username)
        self.screen.add_widget(button)
        return self.screen


if __name__ == "__main__":
    DemoApp().run()
