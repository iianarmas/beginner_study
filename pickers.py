from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker, MDTimePicker, MDThemePicker


class DemoApp(MDApp):
    def build(self):
        return

    def show_date(self):
        date_dialog = MDDatePicker()
        date_dialog.open()

    def show_time(self):
        time_dialog = MDTimePicker()
        time_dialog.open()

    def show_theme(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

if __name__ == "__main__":
    DemoApp().run()
