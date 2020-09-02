from kivy.app import App
from kivy.uix.recycleview import RecycleView


class RecycleViewWidget(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(100)]


class RecycleViewApp(App):
    def build(self):
        return RecycleViewWidget()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = [.8,.8,.8,1]
    RecycleViewApp().run()
