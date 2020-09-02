from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class GridLayoutWidget(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class GridApp(App):
    def build(self):
        return GridLayoutWidget()


if __name__ == "__main__":
    GridApp().run()
