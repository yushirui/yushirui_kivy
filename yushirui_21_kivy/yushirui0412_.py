from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class CheckBoxWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 通过id获取到CheckBox部件并绑定方法
        self.ids.first_check_0.bind(active=self.on_checkbox_active)

    @staticmethod
    def on_checkbox_active(checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active')
        else:
            print('The checkbox', checkbox, 'is inactive')


class CheckBoxApp(App):
    def build(self):
        return CheckBoxWidget()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = [.8,.8,.8,1]
    CheckBoxApp().run()
