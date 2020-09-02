from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color


class GridLayoutWidget(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 设置背景颜色（可忽略）
        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)

        # 指定列数(行数使用rows)
        self.cols = 3

        # 添加按钮
        for i in range(5):
            btn = Button(text=str(i))
            self.add_widget(btn)

    def update_rect(self, *args):
        """设置背尺寸，可忽略"""
        self.rect.pos = self.pos
        self.rect.size = self.size


class GridApp(App):
    def build(self):
        return GridLayoutWidget()


if __name__ == "__main__":
    GridApp().run()
