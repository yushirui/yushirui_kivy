from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class LabelBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LabelApp(App):
    def build(self):
        return LabelBoxLayout()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = [1,1,1,1]
    LabelApp().run()
