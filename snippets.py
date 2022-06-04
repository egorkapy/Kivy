from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window


class Red(Widget):
    pass


class Green(Widget):
    pass


class Blue(Widget):
    pass


class MainWidget(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Red(), index=1)
        self.add_widget(Green(), index=1)
        self.add_widget(Blue(), index=2)


class Test2App(App):

    def build(self):
        Window.size = (300, 300)
        self.main_widget = MainWidget()

        return self.main_widget


if __name__ == "__main__":
    Test2App().run()

print('print('')')