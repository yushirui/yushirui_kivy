# -*- coding:utf-8 -*-
# Author：余时锐
# Date: 2020-06-22
# Message：yushirui0201_Size屏幕尺寸

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

# 文本框
from kivy.uix.textinput import TextInput

# 线布局
from kivy.uix.boxlayout import BoxLayout

# 相对布局
from kivy.uix.relativelayout import RelativeLayout

# 浮动布局
from kivy.uix.floatlayout import FloatLayout

# 列表布局
from kivy.properties import ListProperty

# 锚点布局
from kivy.uix.anchorlayout import AnchorLayout

# 网格布局
from kivy.uix.gridlayout import GridLayout

# 页面布局
from kivy.uix.pagelayout import PageLayout

# 图案库，矩形、颜色
from kivy.graphics import Rectangle, Color

# ======================================== 图标与标题 ========================================
# 查找应用图标
app_icon = yushirui_find_file_or_dir('common/image/yu.ico')

# 图标
App.icon = app_icon

# 标题
App.title = 'yushirui0201_Size屏幕尺寸'




class MyButton(Button):
    """自定义一个按钮，提出公共属性"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.font_size = 20
        self.size_hint = [0.2, 0.2]


class YushiruiWidget(RelativeLayout):
    pass


class YushiruiWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 设置背景颜色（可忽略）
        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)

        # 创建一个RelativeLayout布局
        relative_layout = RelativeLayoutWidget()

        # 使用自定义按钮
        bt0 = MyButton(text='Bt0', pos_hint={"right":1, "top":1}, background_color=(0.1, 0.5, 0.6, 1))
        bt1 = MyButton(text='Bt1', pos_hint={"x": 0, "top": 1}, background_color=(1, 0, 0, 1))
        bt_relative = MyButton(text='Relative', pos_hint={"center_x":.5, "center_y":.5}, background_color=(0.4, 0.5, 0.6, 1))
        bt2 = MyButton(text='Bt2', pos_hint={"x":0, "y":0}, background_color=(0, 0, 1, 1))
        bt3 = MyButton(text='Bt3', pos_hint={"right":1, "y":0}, background_color=(0.8, 0.9, 0.2, 1))

        # 向RelativeLayout布局内遍历添加元素
        for i in [bt0, bt1, bt_relative, bt2, bt3]:
            relative_layout.add_widget(i)

        # 放一个空的BoxLayout占位
        self.add_widget(BoxLayout())
        # 将RelativeLayout添加到布局中
        self.add_widget(relative_layout)

    def update_rect(self, *args):
        """设置背景尺寸，可忽略"""
        self.rect.pos = self.pos
        self.rect.size = self.size


class Yushirui0218App(App):
    def build(self):
        return YushiruiWidget()

if __name__ == "__main__":
    Yushirui0218App().run()