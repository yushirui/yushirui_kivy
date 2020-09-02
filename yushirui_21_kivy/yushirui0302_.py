from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class YushiruiWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Yushirui0302App(App):
    def build(self):
        return YushiruiWidget()


if __name__ == '__main__':
    Yushirui0302App().run()
