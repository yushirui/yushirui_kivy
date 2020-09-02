from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel


class TabbedPanelTest(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TabbedPanelApp(App):
    def build(self):
        return TabbedPanelTest()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = [.8,.8,.8,1]
    TabbedPanelApp().run()
