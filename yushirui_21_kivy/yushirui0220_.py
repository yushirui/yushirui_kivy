from kivy.app import App
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.graphics import Rectangle, Color


class ScatterLayoutWidget(ScatterLayout):
    pass


class BoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 设置背景颜色（可忽略）
        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)

        # 创建一个ScatterLayout布局
        scatter_layout = ScatterLayoutWidget()
        # 异步加载图片
        image = AsyncImage(source='http://sck.rjkflm.com/images/logo1.png')
        # 将图片添加到ScatterLayout布局中
        scatter_layout.add_widget(image)
        # 将ScatterLayout布局嵌套在BoxLayout布局中
        self.add_widget(scatter_layout)

    def update_rect(self, *args):
        """设置背景尺寸，可忽略"""
        self.rect.pos = self.pos
        self.rect.size = self.size


class ScatterApp(App):
    def build(self):
        return BoxLayoutWidget()


if __name__ == '__main__':
    ScatterApp().run()
