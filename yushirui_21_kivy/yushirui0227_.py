from time import strftime

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout


class ClockBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.timing_flag = False
        self.timing_seconds = 0
        self.on_start()

    def on_start(self):
        # 每过0秒执行一次update_time方法
        Clock.schedule_interval(self.update_time, 0)

    def update_time(self, nap):
        if self.timing_flag:
            self.timing_seconds += nap

        # 通过id获取到time_label_id控件，并设置text属性值
        self.ids.time_label_id.text = strftime('[b]%H[/b]:%M:%S')
        m, s = divmod(self.timing_seconds, 60)
        # 同上设置text值
        self.ids.stopwatch.text = ('%02d:%02d.[size=40]%02d[/size]' % (int(m), int(s), int(s * 100 % 100)))

    def start_or_stop(self):
        # 切换状态
        self.ids.start_stop_button_id.text = 'Start' if self.timing_flag else 'Stop'
        self.timing_flag = not self.timing_flag


class ClockApp(App):
    def build(self):
        return ClockBoxLayout()


if __name__ == '__main__':
    # 设置页面背景
    from kivy.core.window import Window
    Window.clearcolor = [.8, .8, .8, 1]
    ClockApp().run()
