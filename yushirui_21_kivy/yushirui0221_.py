from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class ScatterLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ScatterApp(App):
    def build(self):
        return ScatterLayoutWidget()


if __name__ == '__main__':
    ScatterApp().run()
