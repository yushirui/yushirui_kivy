from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class ButtonFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def press_button(self):
        """按下按钮触发事件的回调函数"""
        print('press_button is running')

    def release_button(self):
        """"按下按钮并释放时触发事件的回调函数"""
        print('release_button is running')

class ButtonApp(App):
    def build(self):
        return ButtonFloatLayout()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = [1,1,1,1]
    ButtonApp().run()
