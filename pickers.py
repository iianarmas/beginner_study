MDBoxLayout:
    size_hint: 0.5, 0.5
    pos_hint: {"center_x": 0.5, "center_y": 0.5}
    MDRaisedButton:
        text: "Date Picker"
        on_release: app.show_date()
    MDRaisedButton:
        text: "Time Picker"
        on_release: app.show_time()
    MDRaisedButton:
        text: "Color Picker"
        on_release: app.show_theme()
