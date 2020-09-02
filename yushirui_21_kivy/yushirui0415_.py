from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout


class ProgressBarWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.i = 0

    def clicked(self):
        # 每0.5s调用update_bar方法一次
        self.update_bar_trigger = Clock.schedule_interval(self.update_bar, 0.5)

    def update_bar(self, dt):
        if self.i <= 100:
            # 赋值
            self.ids.progress_bar.value += self.i
            self.i += 1
            self.update_bar_trigger()


class ProgressBarApp(App):
    def build(self):
        return ProgressBarWidget()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = [.8,.8,.8,1]
    ProgressBarApp().run()
