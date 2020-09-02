from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton


class ToggleButtonWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        tb = ToggleButton(text='Mixed', group='sex')
        self.add_widget(tb)


class ToggleButtonApp(App):
    def build(self):
        return ToggleButtonWidget()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = [.8,.8,.8,1]
    ToggleButtonApp().run()
