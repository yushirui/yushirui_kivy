from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class SpinnerBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class SpinnerApp(App):
    def build(self):
        return SpinnerBox()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = [.8,.8,.8,1]
    SpinnerApp().run()
