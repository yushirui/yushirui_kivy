from kivy.app import App
from kivy.uix.widget import Widget


class PopupBox(Widget):
    def __int__(self, **kwargs):
        super().__int__(**kwargs)


class PopupApp(App):
    def build(self):
        return PopupBox()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = [.8,.8,.8,1]
    PopupApp().run()
