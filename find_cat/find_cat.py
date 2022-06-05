from kivy.app import App
from kivy.graphics import Rectangle
from kivy.graphics.svg import Svg
from kivy.uix.scatter import Scatter
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.clearcolor = 1, 1, 1, 1

Builder.load_file('sprites.kv')


class Light(Scatter):
    pass


# https://kivy.org/doc/stable/api-kivy.graphics.svg.html
# https://github.com/kivy/kivy
# https://github.com/kivy/kivy/blob/master/examples/svg/main.py
# https://stackoverflow.com/questions/65332722/extremely-bad-svg-quality-kivy
class Cat(Widget):

    def start(self):
        # self.cat = Svg('./img/black_cat.svg')
        self.cat = Rectangle(source='./img/black_cat.png', size=self.size)

        self.canvas.add(self.cat)

    def on_touch_move(self, touch):
        print(f'Touch: {touch}')


class GameApp(App):

    def build(self):
        self.layout = AnchorLayout()
        self.light = Light()
        self.cat = Cat()

        self.layout.add_widget(self.light)
        self.layout.add_widget(self.cat)

        self.cat.start()

        return self.layout


if __name__ == '__main__':
    GameApp().run()
