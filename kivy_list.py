from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, ThreeLineListItem, ThreeLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        scroll = ScrollView()
        list_view = MDList()

        scroll.add_widget(list_view)

        for i in range(20):
            icon = IconLeftWidget(icon='android')
            item = ThreeLineIconListItem(text=f'item {i+1}', secondary_text='Hello World', tertiary_text='Python')

            item.add_widget(icon)
            list_view.add_widget(item)

        screen.add_widget(scroll)
        return screen


if __name__ == "__main__":
    DemoApp().run()
