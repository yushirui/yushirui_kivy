from kivy.app import App
from kivy.graphics import Color, Line
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex


class FrameToggleButton(ToggleButton):
    """当前按钮添加边框"""
    def do_press(self):
        """点击改变状态"""
        if self.state == 'normal':
            ToggleButtonBehavior.do_press(self)


class DrawCanvasWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 设置默认颜色
        self.change_color(get_color_from_hex('#19caad'))
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

    def change_color(self, new_color):
        """调色"""
        self.last_color = new_color
        self.canvas.add(Color(*new_color))

    def change_line_width(self, line_width='Normal'):
        """线宽"""
        self.line_width = {'Thin': 1, 'Normal': 2, 'Thick': 4}[line_width]


class PaintApp(App):
    def build(self):
        self.canvas_widget = DrawCanvasWidget()
        return self.canvas_widget


if __name__ == '__main__':
    PaintApp().run()
