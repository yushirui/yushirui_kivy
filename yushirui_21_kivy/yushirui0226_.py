from time import strftime

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout


class ClockBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.on_start()

    def on_start(self):
        # 每过0秒执行一次update_time方法
        Clock.schedule_interval(self.update_time, 0)

    def update_time(self, nap):
        # 通过id获取到time_label_id控件，并设置text属性值
        self.ids.time_label_id.text = strftime('[b]%H[/b]:%M:%S')


class ClockApp(App):
    def build(self):
        return ClockBoxLayout()


if __name__ == '__main__':
    # 设置页面背景
    from kivy.core.window import Window
    Window.clearcolor = [.8, .8, .8, 1]
    ClockApp().run()
