# -*- coding:utf-8 -*-
# Author：余时锐
# Date: 2020-06-22
# Message：yushirui0105_打包ios
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

'''
目前只能Python2.7打包，3.3以上的支持还在开发中
sudo brew install autoconf automake libtool pkg-config
brew link libtool
sudo easy_install pip3
sudo pip install cython==0.29.10

下载kivy-ios项目
git clone git://github.com/kivy/kivy-ios
cd kivy-ios
./toolchain.py build kivy


创建初始Xcode项目。把Touchtracer这个换成你的项目名字。名字一定不能有空格或者其他非法字符
./toolchain.py create yushirui <app_directory>
./toolchain.py create Touchtracer ~/code/kivy/examples/demo/yushirui
    
打开这个项目
open yushirui-ios/yushirui.xcodeproj

若要添加numpy库
./toolchain.py build numpy
./toolchain.py update yushirui-ios
'''


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
