from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Rectangle, Color
from kivy.graphics.instructions import InstructionGroup


class RelativeWidget(RelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(0, 0, 1, 0.2)
            Rectangle(pos=self.pos, size=(300, 300))

            Color(0, 1, 0, 0.4)
            Rectangle(pos=(300, 300), size=(300, 300))


class CanvasApp(App):
    def build(self):
        return RelativeWidget()


if __name__ == '__main__':
    CanvasApp().run()
