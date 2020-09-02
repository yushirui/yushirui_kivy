from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color


class BoxLayoutWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 设置背景颜色（可忽略）
        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)

        # 添加两个按钮
        self.add_widget(Button(text='Hello'))
        self.add_widget(Button(text='BoxLayout'))

    def update_rect(self, *args):
        """设置背景尺寸，可忽略"""
        self.rect.pos = self.pos
        self.rect.size = self.size


class BoxApp(App):
    def build(self):
        return BoxLayoutWidget()


if __name__ == "__main__":
    BoxApp().run()
