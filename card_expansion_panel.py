from kivy.animation import Animation
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivy.lang import Builder

smp = """
MDGridLayout:
    cols: 2
    MDRelativeLayout:
        MDCard:
            orientation: "vertical"
            pos_hint: {"center_x": 0.55, "center_y": 0.5}
            size_hint: 0.8, None
            height: self.minimum_height
            #focus_behavior: True
            MDBoxLayout:
                id: box
                size_hint_y: None
                height: self.minimum_height
                Image:
                    source: "nezuko.png"
                    size_hint: 1, None
                    height: "300dp"
                    allow_stretch: True
                    keep_ratio: False
            MDBoxLayout:
                id: card
                orientation: "vertical"
                size_hint: 1, None
                height: self.minimum_height
                padding: "10dp"



    MDRelativeLayout:
        MDCard:
            orientation: "vertical"
            pos_hint: {"center_x": 0.45, "center_y": 0.5}
            size_hint: 0.8, 0.75
            padding: "10dp"
            spacing: "10dp"
            Image:
                source: "nezuko.png"
                size_hint: 1, 0.8
                allow_stretch: True
                keep_ratio: False
            MDSeparator:
                height: "1dp"
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
            MDBoxLayout:


<Box>:
    #adaptive_height: True
    orientation: "vertical"
    size_hint_y: None
    height: "150dp"        
    MDLabel:
        text: "Sample Layout"
        font_style: "Subtitle1"
    MDBoxLayout:
        spacing: "10dp"
        MDFillRoundFlatButton:
            text: "Continue"
            font_style: "Button"       
        MDRoundFlatButton:
            text: "Cancel"
            font_style: "Button"    
"""


class Box(MDBoxLayout):
    """pass"""


class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(smp)

    def on_start(self):
        content = Box()
        panel = MDExpansionPanel(
            on_open=self.panel_open,
            on_close=self.panel_close,
            icon='language-python',
            content=content,
            panel_cls=MDExpansionPanelOneLine(
                text='Nezuko'
            )

        )
        self.root.ids.card.add_widget(panel)

    def panel_open(self, *args):
        Animation(
            height=(self.root.ids.box.height - self.root.ids.content.height) + self.theme_cls.standard_increment
                   * 2, d=0.2
                    ).start(self.root.ids.box)

    def panel_close(self, *args):
        Animation(
            height=(self.root.ids.box.height - self.root.ids.content.height) +
                   self.theme_cls.standard_increment * 2, d=0.2
                ).start(self.root.ids.box)


if __name__ == "__main__":
    DemoApp().run()
