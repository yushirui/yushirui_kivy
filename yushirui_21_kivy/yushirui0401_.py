from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class ButtonFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        bt = Button(text='Button 01')
        self.add_widget(bt)


class ButtonApp(App):
    def build(self):
        return ButtonFloatLayout()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = [1,1,1,1]
    ButtonApp().run()
