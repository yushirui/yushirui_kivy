from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class ClockBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ClockApp(App):
    def build(self):
        return ClockBoxLayout()


if __name__ == '__main__':
    # 设置页面背景
    from kivy.core.window import Window
    Window.clearcolor = [.8, .8, .8, 1]
    ClockApp().run()
