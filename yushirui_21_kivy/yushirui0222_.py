from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Rectangle, Color


class StackLayoutWidget(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 设置背景颜色（可忽略）
        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)

        # 遍历添加按钮
        for i in range(25):
            btn = Button(text=str(i), width=40 + i * 5, size_hint=(None, 0.15))
            self.add_widget(btn)

    def update_rect(self, *args):
        """设置背尺寸，可忽略"""
        self.rect.pos = self.pos
        self.rect.size = self.size


class StackApp(App):
    def build(self):
        return StackLayoutWidget()


if __name__ == '__main__':
    StackApp().run()
