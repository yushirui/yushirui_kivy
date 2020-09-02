from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout


class PageLayoutWidget(PageLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 创建两个按钮
        bt0 = Button(text='bt0', background_color=[0.3, .9, .3, 1])
        bt1 = Button(text='bt1', background_color=[0.9, .3, .3, 1])

        # 添加到布局中
        self.add_widget(bt0)
        self.add_widget(bt1)


class PageApp(App):
    def build(self):
        return PageLayoutWidget()


if __name__ == "__main__":
    PageApp().run()
