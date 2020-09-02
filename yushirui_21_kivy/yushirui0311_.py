from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class RotateGridLayoutWidget(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class RotateApp(App):
    def build(self):
        return RotateGridLayoutWidget()


if __name__ == "__main__":
    RotateApp().run()