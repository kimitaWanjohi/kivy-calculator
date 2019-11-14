from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

Builder.load_file("main.kv")

number = ObjectProperty()
base = ObjectProperty()
output =ObjectProperty()


def convert(n, base):
    string = "0123456789ABCDEF"

    if n < base:
        return string[n]

    else:
        return convert(n // base, base) + convert(n % base, base)


class BaseConverter(Screen):
    def output_ui(self):
        try:
            self.output.text = convert(int(self.number.text), int(self.base.text))
        except:
            self.output.text = "check your inputs"

answer = ObjectProperty()


class Calculator(Screen):
    def display(self):
        try:
            self.answer.text = str(eval(self.answer.text))
        except Exception:
            self.answer.text = "Syntax Error"
sm = ScreenManager()
sm.add_widget(BaseConverter(name='base_converter'))
sm.add_widget(Calculator(name='calculator'))


class TestApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()
