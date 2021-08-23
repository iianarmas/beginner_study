from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

card = """

ScrollView:
    #do_scroll_y: True
    MDStackLayout:
        orientation: "lr-tb"
        spacing: "24dp"
        padding: "32dp"
        size_hint_y: None
        height: self.minimum_height
        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            width: "300dp"
            height: "450dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            elevation: 12
            on_release: print("hello")
            border_radius: 20
            radius: [15]
        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            width: "300dp"
            height: "450dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            elevation: 12
            on_release: print("hello")
            border_radius: 20
            radius: [15]
            
        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            width: "300dp"
            height: "450dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            elevation: 12
            on_release: print("hello")
            border_radius: 20
            radius: [15]
        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            width: "300dp"
            height: "450dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            elevation: 12
            on_release: print("hello")
            border_radius: 20
            radius: [15]
            
        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            width: "300dp"
            height: "450dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            elevation: 12
            on_release: print("hello")
            border_radius: 20
            radius: [15]
        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            width: "300dp"
            height: "450dp"
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
