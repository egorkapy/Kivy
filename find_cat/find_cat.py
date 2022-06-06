from random import randint
from kivy.app import App
from kivy.graphics.svg import Svg
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget

# White background for testing the app
# Window.clearcolor = 0, 0, 0, 0
Window.clearcolor = 1, 1, 1, 1

CAT_SIZE = 50
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
Window.size = WINDOW_WIDTH, WINDOW_HEIGHT

Builder.load_file('sprites.kv')


class SvgWidget(Scatter):

    def __init__(self, filename, **kwargs):
        super(SvgWidget, self).__init__(**kwargs)
        with self.canvas:
            svg = Svg(filename)
        self.size = svg.width, svg.height

class Light(Scatter):
    pass


class Cat(SvgWidget):

    def on_touch_move(self, touch):
        print(f'Touch: {touch}')


class GameApp(App):

    def build(self):
        self.layout = FloatLayout()
        self.light = Light()

        self.layout.add_widget(self.light)

        for cat_id in range(1, 4):
            svg = Cat('./img/black_cat.svg', size_hint=(None, None))
            self.layout.add_widget(svg)
            svg.scale = 1
            svg.center = randint(CAT_SIZE, WINDOW_WIDTH - CAT_SIZE), randint(CAT_SIZE, WINDOW_HEIGHT - CAT_SIZE)

        return self.layout


if __name__ == '__main__':
    GameApp().run()
