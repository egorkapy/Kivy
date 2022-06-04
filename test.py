from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

matrix = [500, 500, 500, 5, 5]


class LoginScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'horizontal'

        self.container_L = MyLayout_L(orientation='vertical', on_touch_down=self.change_label_L)
        self.container_M = BoxLayout(orientation='vertical')
        self.container_R = MyLayout_R(orientation='vertical', on_touch_down=self.change_label_R)

        self.label_L0 = Label(text='3', font_size=30)
        self.label_L1 = Label(text='4', font_size=30)
        self.label_L2 = Label(text='5', font_size=30)
        self.label_L3 = Label(text='6', font_size=30)
        self.label_L4 = Label(text='7', font_size=30)

        label_L_list = [self.label_L0, self.label_L1, self.label_L2, self.label_L3, self.label_L4]
        for item in label_L_list:
            self.container_L.add_widget(item)

        self.label_M0 = Label(text='500', font_size=30)
        label_M_list = [self.label_M0]
        for item in label_M_list:
            self.container_M.add_widget(item)

        self.label_R0 = Label(text='3', font_size=30)
        self.label_R1 = Label(text='4', font_size=30)
        self.label_R2 = Label(text='5', font_size=30)
        self.label_R3 = Label(text='6', font_size=30)
        self.label_R4 = Label(text='7', font_size=30)

        label_R_list = [self.label_R0, self.label_R1, self.label_R2, self.label_R3, self.label_R4]
        for item in label_R_list:
            self.container_R.add_widget(item)

        self.add_widget(self.container_L)
        self.add_widget(self.container_M)
        self.add_widget(self.container_R)

    def change_label_L(self, instance, touch):
        if instance.collide_point(*touch.pos):
            print('L ', matrix)
            counter = matrix[3]
            self.label_L0.text = str(counter - 2)
            self.label_L1.text = str(counter - 1)
            self.label_L2.text = str(counter)
            self.label_L3.text = str(counter + 1)
            self.label_L4.text = str(counter + 2)
            if touch.button == 'scrollup':
                instance.calc_plus()
            elif touch.button == 'scrolldown':
                instance.calc_minus()

    def change_label_R(self, instance, touch):
        if instance.collide_point(*touch.pos):
            print('R ', matrix)
            counter = matrix[4]
            self.label_R0.text = str(counter - 2)
            self.label_R1.text = str(counter - 1)
            self.label_R2.text = str(counter)
            self.label_R3.text = str(counter + 1)
            self.label_R4.text = str(counter + 2)
            if touch.button == 'scrollup':
                instance.calc_plus2()
            elif touch.button == 'scrolldown':
                instance.calc_minus2()


class MyLayout_L(BoxLayout):
    def calc_plus(self):
        matrix[3] += 1

    def calc_minus(self):
        matrix[3] -= 1


class MyLayout_R(BoxLayout):
    def calc_plus2(self):
        matrix[4] += 1

    def calc_minus2(self):
        matrix[4] -= 1


class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
