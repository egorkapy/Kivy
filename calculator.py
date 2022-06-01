from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):

    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.is_last_operator_button = None
        self.text_input = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout = BoxLayout(orientation="vertical")
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]

        main_layout.add_widget(self.text_input)

        for row in buttons:

            h_layout = BoxLayout()

            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)

            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current_input_text = self.text_input.text
        button_text = instance.text
        new_input_text = current_input_text + button_text
        is_operator_button = button_text in self.operators

        if button_text == "C":
            self.text_input.text = ""

        else:
            # Не добавляет два оператора подряд
            if is_operator_button and self.is_last_operator_button:
                return

            # Первый символ не может быть оператором
            elif current_input_text == "" and is_operator_button:
                return

            else:
                self.text_input.text = new_input_text

        self.is_last_operator_button = is_operator_button

    def on_solution(self, instance):

        last_character = self.text_input.text[len(self.text_input.text) - 1]

        if self.text_input.text:
            if last_character in self.operators:
                self.text_input.text = self.text_input.text[:len(self.text_input.text) - 1]

            try:
                self.text_input.text = str(eval(self.text_input.text))

            except ZeroDivisionError:
                self.text_input.text = 'YOU CAN\'T DIVIDE BY ZERO!'

            except SyntaxError:
                self.text_input.text = 'ERROR'


MainApp().run()