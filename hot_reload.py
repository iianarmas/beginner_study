# main.py

import os
from kaki.app import App
from kivymd.app import MDApp
from login import LogIn
from kivy.config import Config

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '740')


class MDLive(App, MDApp):
    KV_FILES = {
        os.path.join(os.getcwd(), 'screen.kv')
    }
    CLASSES = {
        'LogIn': 'login'
    }

    AUTORELOADER_PATHS = [
        (os.getcwd(), {'recursive': True})
    ]

    def build_app(self, *args):
        self.login = LogIn()
        return self.login


MDLive().run()

# ===============================================

# login.py

from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager




class LogIn(MDScreen):
    pass

# =============================================
# screen.kv

<LogIn>:
    md_bg_color: 1,1,1,1
    MDFloatLayout:

        MDRelativeLayout:
            pos_hint: {'center_x':0.5, 'top':0.8}
            MDLabel:
                text: 'Welcome'
                font_name: 'fonts/Poppins-Regular.ttf'
                font_size: '26sp'
                text_size: self.size
                valign: 'top'
                halign: 'center'


        MDRelativeLayout:
            pos_hint: {'center_x':0.5, 'top':0.78}
            MDLabel:
                text: 'FFSC'
                font_name: 'fonts/Poppins-SemiBold.ttf'
                font_size: '56sp'
                text_size: self.size
                valign: 'top'
                halign: 'center'

<MyTextField@MDTextFieldRound>:
    normal_color: 1,1,1,1
    color_active: 1,1,1,1
    size_hint: 0.7, 0.064
