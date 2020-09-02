from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class CheckBoxWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CheckBoxApp(App):
    def build(self):
        return CheckBoxWidget()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = [.8,.8,.8,1]
    CheckBoxApp().run()
