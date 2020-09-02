from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Rectangle, Color


class YushiruiWidget(RelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        # 设置背景
        with self.canvas.before:
            # 设置背景颜色，rgba格式，通常值为0-1之间（具体的值 / 255）
            Color(1, 1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        """设置背尺寸"""
        self.rect.pos = self.pos
        self.rect.size = self.size


class Yushirui0306App(App):
    def build(self):
        return YushiruiWidget()


if __name__ == '__main__':
    Yushirui0306App().run()
