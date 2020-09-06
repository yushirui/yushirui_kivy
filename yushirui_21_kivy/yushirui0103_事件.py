# -*- coding:utf-8 -*-
# Author：余时锐
# Date: 2020-06-22
# Message：yushirui0103_事件
# 文件系统
import os

# 系统
import sys

# 追加路径
from common.util.yushirui_path_append import yushirui_path_append

# 追加路径
yushirui_path_append()

# ======================================== kivy ========================================
# kivy
import kivy

# Kivy版本号
kivy.require('1.11.1')

# ======================================== 查找文件 ========================================
# 查找文件
from common.util.yushirui_find_file_or_dir import yushirui_find_file_or_dir

# ======================================== 指定配置文件 ========================================
# 查找配置文件
config_path = yushirui_find_file_or_dir('config/kivy_config.ini')
# 读取配置，支持中文
from kivy.config import Config

# 读取配置文件
Config.read(config_path)

# ======================================== 设置字体 ========================================
# 查找字体文件
font_path = yushirui_find_file_or_dir('font/simkai.ttf')
# 设置字体
from kivy.core.text import LabelBase

# 注册字体
LabelBase.register('.', font_path)

# ======================================== 设置资源目录 ========================================
# 查找资源目录
resource_dir_path = yushirui_find_file_or_dir('res')
# 设置资源目录
from kivy.resources import resource_add_path

# 添加资源目录
resource_add_path(os.path.abspath(resource_dir_path))

# ======================================== kivy应用与组件 ========================================
# app应用
from kivy.app import App

# 组件
from kivy.uix.widget import Widget

# 标签
from kivy.uix.label import Label

# 按钮
from kivy.uix.button import Button

# 线布局
from kivy.uix.boxlayout import BoxLayout

# 列表布局
from kivy.properties import ListProperty

# 网格布局
from kivy.uix.gridlayout import GridLayout

# 文本框
from kivy.uix.textinput import TextInput

# ======================================== 图标与标题 ========================================
# 查找应用图标
app_icon = yushirui_find_file_or_dir('common/image/yu.ico')

# 图标
App.icon = app_icon

# 标题
App.title = 'yushirui0103_事件'

# 线布局
class YushiruiWidget(BoxLayout):
    # 构造方法
    def __init__(self, **kwargs):
        # 父类构造方法
        super(YushiruiWidget, self).__init__(**kwargs)

        # 左边标准按钮
        bt = Button(text='左按钮')
        # 按钮，信号与槽
        bt.bind(on_press=self.yushirui_left_button_do)
        # 布局加组件（左边标准按钮）
        self.add_widget(bt)

        # 中间自定义按钮
        cb = CustomBtn()
        # 按钮，信号与槽
        cb.bind(pressed=self.yushirui_middle_button_do)
        # 布局加组件（中间自定义按钮）
        self.add_widget(cb)

        # 布局加组件（右边标准按钮）
        self.add_widget(Button(text='右按钮'))

    # 左边标准按钮
    def yushirui_left_button_do(self, instance):
        print('左边标准按钮')

    # 中间自定义按钮
    def yushirui_middle_button_do(self, instance, pos):
        print('中间自定义按钮{pos}'.format(pos=pos))


# 中间自定义按钮（继承组件）
class CustomBtn(Widget):
    # 点击 = 列表属性
    pressed = ListProperty([0, 0])

    # 按下（触摸）
    def on_touch_down(self, touch):
        # 触摸点
        if self.collide_point(*touch.pos):
            # 触摸
            self.pressed = touch.pos
            return True
        # 返回父类触摸
        return super(CustomBtn, self).on_touch_down(touch)

    # 这是按钮自带的点击方法，会先运行，打印点击的坐标
    # 后运行按钮绑定的信号与槽
    def on_pressed(self, instance, pos):
        print('先执行按钮自带的on_pressed()，坐标{0}，再执行bind绑定的'.format(pos))


# app类
class Yushirui0103App(App):
    # 重构
    def build(self):
        # 返回自定义组件
        return YushiruiWidget()


if __name__ == '__main__':
    # 运行
    Yushirui0103App().run()
