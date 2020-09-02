from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color


class AnchorLayoutWidget(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 设置背景颜色（可忽略）
        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)

        # 嵌套第一个布局
        anchor_first = AnchorLayout(anchor_x='left', anchor_y='top')
        # 添加按钮
        anchor_first.add_widget(Button(text='Hello', size_hint=[.3, .2]))

        # 嵌套第二个布局
        anchor_second = AnchorLayout(anchor_x='right', anchor_y='bottom')
        # 添加按钮
        anchor_second.add_widget(Button(text='Anchor', size_hint=[.3, .2]))

        # 添加到父布局中
        self.add_widget(anchor_first)
        self.add_widget(anchor_second)

    def update_rect(self, *args):
        """设置背景尺寸，可忽略"""
        self.rect.pos = self.pos
        self.rect.size = self.size


class AnchorApp(App):
    def build(self):
        return AnchorLayoutWidget()


if __name__ == "__main__":
    AnchorApp().run()
