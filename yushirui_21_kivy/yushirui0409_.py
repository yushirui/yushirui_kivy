from kivy.app import App
from kivy.uix.widget import Widget


class TextInputWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TextInputApp(App):
    def build(self):
        return TextInputWidget()


if __name__ == '__main__':
    TextInputApp().run()
