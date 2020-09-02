from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class ScaleBoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ScaleApp(App):
    def build(self):
        return ScaleBoxLayoutWidget()


if __name__ == "__main__":
    ScaleApp().run()