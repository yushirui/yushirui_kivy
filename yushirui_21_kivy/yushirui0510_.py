from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.vkeyboard import VKeyboard


class VKeyboardTest(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        vk = VKeyboard()
        vk.bind(on_key_up=self.key_up)
        self.add_widget(vk)

    def key_up(self, *args):
        print('You have pressed the key is:',args[2])


class VKeyboardApp(App):
    def build(self):
        return VKeyboardTest()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = [.8,.8,.8,1]
    VKeyboardApp().run()