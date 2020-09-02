from kivy.app import App
from kivy.graphics import Line, Color
from kivy.uix.widget import Widget


class DrawCanvasWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 设置默认颜色
        self.canvas.add(Color(rgb=[0,0,0]))
        self.line_width = 2

    def on_touch_down(self, touch):
        """触摸显示轨迹"""
        if Widget.on_touch_down(self, touch):
            return
        with self.canvas:
            touch.ud['current_line'] = Line(points=(touch.x, touch.y), width=self.line_width)

    def on_touch_move(self, touch):
        """连线"""
        if 'current_line' in touch.ud:
            touch.ud['current_line'].points += (touch.x, touch.y)


class PaintApp(App):
    def build(self):
        self.draw_canvas_widget = DrawCanvasWidget()
        return self.draw_canvas_widget


if __name__ == '__main__':
    PaintApp().run()
