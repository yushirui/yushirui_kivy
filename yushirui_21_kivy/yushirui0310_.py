from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Rectangle, Color


class RelativeWidget(RelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CanvasApp(App):
    def build(self):
        return RelativeWidget()


if __name__ == '__main__':
    CanvasApp().run()
