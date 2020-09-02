from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class SwitchWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def callback(self):
        print('Callback is running')


class SwitchApp(App):
    def build(self):
        return SwitchWidget()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = [.8,.8,.8,1]
    SwitchApp().run()
