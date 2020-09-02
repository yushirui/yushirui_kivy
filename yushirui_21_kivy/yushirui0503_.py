from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp


class CustomDropDown(DropDown):
    """在kv文件中添加下拉选项"""
    pass


class DropDownBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        dropdown = CustomDropDown()
        # 点击该按钮触发下拉框
        main_button = Button(text='SelectItem', size_hint=(0.2, 0.15), pos_hint={'center_x':0.5, 'center_y':0.5})
        main_button.bind(on_release=dropdown.open)
        # 绑定选中后回调的方法：把 main_button 的 text 属性设置为传递过来的 x
        dropdown.bind(on_select=lambda instance, x: setattr(main_button, 'text', x))

        # self.add_widget(main_button)
        # 创建一个MTWindow并将窗口小部件作为根窗口小部件添加到窗口中
        runTouchApp(main_button)


class DropDownApp(App):
    def build(self):
        return DropDownBox()


if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = [.8,.8,.8,1]
    DropDownApp().run()
