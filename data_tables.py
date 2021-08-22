from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        table = MDDataTable(size_hint=(0.9, 0.6),
                            pos_hint={'center_x': 0.5, 'center_y': 0.5},
                            check=True,
                            rows_num=10,
                            column_data=[
                                ('Number', dp(30)),
                                ('Food', dp(30)),
                                ('Calories', dp(30))
                            ],
                            row_data=[
                                ('1', 'Burger', '300'),
                                ('2', 'Fries', '200'),
                                ('3', 'Spaghetti', '100'),
                                ('4', 'Oats', '150'),
                                ('5', 'Ice Cream', '250'),
                                ('6', 'Cereal', '150'),
                                ('7', 'Fried Chicken', '280'),
                                ('8', 'Chocolate', '240'),
                                ('9', 'Steak', '325'),
                                ('10', 'Tuna', '230')
                            ]
                            )
        table.bind(on_check_press=self.check_press)
        table.bind(on_row_press=self.row_press)
        screen.add_widget(table)
        return screen

    def check_press(self, instance_table, current_row):
        print(instance_table, current_row)

    def row_press(self, instance_table, instance_row):
        pass


if __name__ == "__main__":
    DemoApp().run()
