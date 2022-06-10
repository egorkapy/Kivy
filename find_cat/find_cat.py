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
# Window.clearcolor = 0, 0, 0, 0
Window.clearcolor = 1, 1, 1, 1

CAT_SIZE = 50
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
Window.size = WINDOW_WIDTH, WINDOW_HEIGHT
score = 0

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
    cats = list()

    def __init__(self, filename, light, score_label, **kwargs):
        super(Cat, self).__init__(filename, **kwargs)

        self.score_label = score_label
        self.score = score

        Cat.cats.append(self)

        while self.collide_widget(light):
            self.center = randint(CAT_SIZE, WINDOW_WIDTH - CAT_SIZE), randint(CAT_SIZE, WINDOW_HEIGHT - CAT_SIZE)

        Clock.schedule_interval(self.touch, .01)

    def touch(self, *args):
        cats = Cat.cats.copy()

        del cats[cats.index(self)]

        if self.collide_point(Window.mouse_pos[0], Window.mouse_pos[1]) or\
                self.collide_widget(cats[0]) or self.collide_widget(cats[1]):
            self.center = randint(CAT_SIZE, WINDOW_WIDTH - CAT_SIZE), randint(CAT_SIZE, WINDOW_HEIGHT - CAT_SIZE)
            self.score += 1
            self.score_label.text = f'Score = {self.score}'


class GameApp(App):

    def build(self):
        self.layout = FloatLayout()
        self.light = Light()
        self.score_label = Label(text=f'Score = {score}', pos=(-120, 240), color=(0, 1, 1, 1))

        self.layout.add_widget(self.light)

        for cat_id in range(1, 4):
            svg = Cat('./img/black_cat.svg', self.light, self.score_label, size_hint=(None, None))
            self.layout.add_widget(svg)
            svg.scale = 1
            svg.center = randint(CAT_SIZE, WINDOW_WIDTH - CAT_SIZE), randint(CAT_SIZE, WINDOW_HEIGHT - CAT_SIZE)

        self.layout.add_widget(self.score_label)

        return self.layout


if __name__ == '__main__':
    GameApp().run()
