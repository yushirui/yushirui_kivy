from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color


class FloatLayoutApp(App):
    def build(self):

        def update_rect(layout, *args):
            """设置背景尺寸，可忽略"""
            layout.rect.pos = layout.pos
            layout.rect.size = layout.size

        float_layout = FloatLayout()

        # 设置背景颜色（可忽略）
        with float_layout.canvas:
            Color(1, 1, 1, 1)
            float_layout.rect = Rectangle(pos=float_layout.pos, size=float_layout.size)
            float_layout.bind(pos=update_rect, size=update_rect)

        # 在布局内的300，200处添加一个为布局0.3，0.2大小的按钮
        button = Button(text='Hello FloatLayout', size_hint=(.3, .2), pos=(300, 200))

        # 将按钮添加到布局内
        float_layout.add_widget(button)

        # 返回布局
        return float_layout


if __name__ == "__main__":
    FloatLayoutApp().run()
