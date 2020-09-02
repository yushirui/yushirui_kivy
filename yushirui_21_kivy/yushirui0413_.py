from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class SliderWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class SliderApp(App):
    def build(self):
        return SliderWidget()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = [.8,.8,.8,1]
    SliderApp().run()
