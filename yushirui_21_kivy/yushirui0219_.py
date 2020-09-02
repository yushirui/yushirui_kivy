from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class RelativeLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class RelativeApp(App):
    def build(self):
        return RelativeLayoutWidget()


if __name__ == "__main__":
    RelativeApp().run()
