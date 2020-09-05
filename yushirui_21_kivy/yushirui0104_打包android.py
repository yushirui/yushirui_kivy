# -*- coding:utf-8 -*-
# Author：余时锐
# Date: 2020-06-22
# Message：yushirui0104_打包android
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class IndexPage(BoxLayout):
    def __init__(self, **kwargs):
        super(IndexPage, self).__init__(**kwargs)
        self.join = Button(text="91")
        self.add_widget(self.join)


class TestApp(App):
    def build(self):
        return IndexPage()


if __name__ == "__main__":
    TestApp().run()
