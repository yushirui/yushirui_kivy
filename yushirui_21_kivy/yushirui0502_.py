from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class BubbleWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BubbleApp(App):
    def build(self):
        return BubbleWidget()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = [.8,.8,.8,1]
    BubbleApp().run()
