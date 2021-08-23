from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine, MDExpansionPanelLabel, MDExpansionPanelOneLine
from kivy.lang import Builder

smp = """
MDGridLayout:
    
    cols: 2
    MDRelativeLayout:
        MDCard:
            id: box
            orientation: "vertical"
            pos_hint: {"center_x": 0.55, "center_y": 0.5}
            size_hint: 0.8, 0.75
            #adaptive_height: True
            padding: "10dp"
            spacing: "10dp"
            Image:
                source: "nezuko.png"
                size_hint: 1, 0.8
                allow_stretch: True
                keep_ratio: False



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
    adaptive_height: True
    orientation: "vertical"
    MDLabel:
        text: "Sample Layout"
        font_style: "Subtitle1"
    MDBoxLayout:
        spacing: "10dp"
        MDRaisedButton:
            text: "Continue"
            font_style: "Button"
        MDRectangleFlatButton:
            text: "Cancel"
            font_style: "Button"
            
            
        
"""


class Box(MDBoxLayout):
    """pass"""

class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(smp)

    def on_start(self):
        self.root.ids.box.add_widget(
            MDExpansionPanel(
                icon='language-python',
                content=Box(),
                panel_cls=MDExpansionPanelOneLine(
                    text='Nezuko'
                )
            )
        )


if __name__ == "__main__":
    DemoApp().run()
