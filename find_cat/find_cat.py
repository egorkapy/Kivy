from random import randint
from kivy.app import App
from kivy.graphics.svg import Svg
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.widget import Widget

# White background for testing the app
Window.clearcolor = 0, 0, 0, 0
# Window.clearcolor = 1, 1, 1, 1

CAT_SIZE = 50
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
score = 0

Window.size = WINDOW_WIDTH, WINDOW_HEIGHT


def cat_random_position():
    return randint(CAT_SIZE, WINDOW_WIDTH - CAT_SIZE), randint(CAT_SIZE, WINDOW_HEIGHT - CAT_SIZE)


Builder.load_file('sprites.kv')


class SvgWidget(Scatter):

    def __init__(self, filename, **kwargs):
        super(SvgWidget, self).__init__(**kwargs)

        self.do_translation = False
        self.do_scale = False
        self.do_rotation = False

        with self.canvas:
            svg = Svg(filename)

        self.size = svg.width, svg.height


class Light(Scatter):
    def __init__(self, sub_light: Widget, **kwargs):
        super(Light, self).__init__(**kwargs)

        self.sub_light = sub_light

        Clock.schedule_interval(self.update, .01)

    def update(self, *args):
        self.center = self.sub_light.center


# TODO
class SubWidget(Widget):
    def __init__(self, **kwargs):
        super(SubWidget, self).__init__(**kwargs)

        self.canvas.clear()

    def on_touch_move(self, touch):
        self.center_x, self.center_y = (touch.x, touch.y)

        print(touch.x, touch.y)


class Cat(SvgWidget):
    cats = list()

    def __init__(self, filename, light, score_label, **kwargs):
        super(Cat, self).__init__(filename, **kwargs)

        self.light = light
        self.score_label = score_label

        Cat.cats.append(self)

        Clock.schedule_interval(self.touch, 0)

    def touch(self, *args):
        global score

        cats_neighbors = Cat.cats.copy()

        del cats_neighbors[cats_neighbors.index(self)]

        if self.collide_widget(cats_neighbors[0]) \
                or self.collide_widget(cats_neighbors[1]) \
                or self.collide_widget(self.light):

            self.center = cat_random_position()

            if not self.light.pos == (0.0, 0.0):
                score += 1
                self.score_label.text = f'Score = {str(score)}'


class GameApp(App):

    def build(self):
        self.layout = FloatLayout()
        self.sub_light = SubWidget()
        self.light = Light(self.sub_light)
        self.score_label = Label(text='Score = 0', pos=(-120, 240), color=(0, 1, 1, 1))

        self.layout.add_widget(self.light)
        self.layout.add_widget(self.sub_light)

        for cat_id in range(1, 4):
            svg = Cat('./img/black_cat.svg', self.sub_light, self.score_label, size_hint=(None, None))
            self.layout.add_widget(svg)
            svg.scale = 1
            svg.center = cat_random_position()

        self.layout.add_widget(self.score_label)

        return self.layout


if __name__ == '__main__':
    GameApp().run()
