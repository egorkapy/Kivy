from kivy.app import App
from kivy.uix.button import Button


class MainApp(App):
    def build(self):
        button = Button(text='Hello from Kivy',
                        size_hint=(.5, .5),
                        pos_hint={'center_x': .3, 'center_y': .7})
        button.bind(on_press=self.on_press_button)

        return button

    def on_press_button(self, instance):
        print(instance.text)


if __name__ == '__main__':
    app = MainApp()
    app.run()
