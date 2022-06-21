from random import randint, choice
from kivy.app import App
from kivy.graphics.svg import Svg
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.widget import Widget
from math import hypot

# White background for testing the app
# Window.clearcolor = 0, 0, 0, 0
Window.clearcolor = 1, 1, 1, 1

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
HALF_CAT_WIDTH = 95 // 2
HALF_CAT_HEIGHT = 100 // 2
LIGHT_RADIUS = 50
SAFE_DISTANCE = round(hypot((HALF_CAT_WIDTH + LIGHT_RADIUS), (HALF_CAT_HEIGHT + LIGHT_RADIUS))) + 10

score = 0


def cat_random_position(light_center_x, light_center_y):
    light_center_x = int(light_center_x)
    light_center_y = int(light_center_y)

    light_left_border = light_center_x - SAFE_DISTANCE
    light_right_border = light_center_x + SAFE_DISTANCE
    light_bottom_border = light_center_y - SAFE_DISTANCE
    light_top_border = light_center_y + SAFE_DISTANCE

    coordinates_x = []
    coordinates_y = []

    # Distance on the left from the light.
    if light_left_border > HALF_CAT_WIDTH:
        random_x_left = randint(HALF_CAT_WIDTH, light_left_border)

    # Distance on the right from the light.
    if light_right_border < (Window.width - HALF_CAT_WIDTH):
        random_x_right = randint(light_right_border, Window.width - HALF_CAT_WIDTH)

    # Distance on the bottom from the light.
    if light_bottom_border > HALF_CAT_HEIGHT:
        random_y_bottom = randint(HALF_CAT_HEIGHT, light_bottom_border)

    # Distance on the top from the light.
    if light_top_border < (Window.height - HALF_CAT_HEIGHT):
        random_y_top = randint(light_top_border, Window.height - HALF_CAT_HEIGHT)

    if 'random_x_left' in locals():
        coordinates_x.append(random_x_left)

    if 'random_x_right' in locals():
        coordinates_x.append(random_x_right)

    if 'random_y_bottom' in locals():
        coordinates_y.append(random_y_bottom)

    if 'random_y_top' in locals():
        coordinates_y.append(random_y_top)

    random_x = choice(coordinates_x)
    random_y = choice(coordinates_y)

    return random_x, random_y


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
    diameter = LIGHT_RADIUS * 2

    def __init__(self, sub_light: Widget, **kwargs):
        super(Light, self).__init__(**kwargs)

        self.sub_light = sub_light

        Clock.schedule_interval(self.update, 0)

    def update(self, *args):
        self.center = self.sub_light.center


class SubLight(Widget):
    def __init__(self, **kwargs):
        super(SubLight, self).__init__(**kwargs)

        # self.canvas.clear()

    def on_touch_move(self, touch):
        self.center_x, self.center_y = (touch.x, touch.y)


class Cat(SvgWidget):
    cats = list()

    def __init__(self, filename, sub_light, score_label, **kwargs):
        super(Cat, self).__init__(filename, **kwargs)

        self.sub_light = sub_light
        self.score_label = score_label

        Cat.cats.append(self)

        Clock.schedule_interval(self.touch, 0)

    def touch(self, *args):
        global score

        cats_neighbors = Cat.cats.copy()

        del cats_neighbors[cats_neighbors.index(self)]

        if self.collide_widget(cats_neighbors[0]) or self.collide_widget(cats_neighbors[1]):
            self.center = cat_random_position(self.sub_light.center_x, self.sub_light.center_y)

        if self.collide_widget(self.sub_light):
            self.center = cat_random_position(self.sub_light.center_x, self.sub_light.center_y)
            score += 1
            self.score_label.text = f'Score = {str(score)}'


class GameApp(App):

    def build(self):
        self.title = 'Find the cat :)'
        self.layout = FloatLayout()
        self.sub_light = SubLight()
        self.light = Light(self.sub_light)
        self.score_label = Label(text='Score = 0', pos=(-120, 240), color=(0, 1, 1, 1))

        self.layout.add_widget(self.light)
        self.layout.add_widget(self.sub_light)

        for cat_id in range(1, 4):
            cat = Cat('./img/black_cat.svg', self.sub_light, self.score_label, size_hint=(None, None))
            self.layout.add_widget(cat)
            cat.scale = 1
            cat.center = cat_random_position(self.sub_light.center_x, self.sub_light.center_y)

        self.layout.add_widget(self.score_label)

        return self.layout


if __name__ == '__main__':
    GameApp().run()
