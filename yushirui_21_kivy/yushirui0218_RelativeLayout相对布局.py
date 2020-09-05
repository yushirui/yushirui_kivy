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


# 相对大小，相对父布局大小，不是窗口大小

# 自定义按钮，公共属性
class YushiruiButton(Button):
    # 构造方法
    def __init__(self, **kwargs):
        # 父类构造方法
        super().__init__(**kwargs)

        # 按钮字体大小
        self.font_size = 20
        # 按钮相对大小 = 窗口0.2 0.2
        self.size_hint = [0.2, 0.2]


# 自定义组件（线性布局）
class YushiruiWidget(BoxLayout):
    # 构造方法
    def __init__(self, **kwargs):
        # 父类构造方法
        super().__init__(**kwargs)

        # 设置背景颜色（可忽略）
        with self.canvas:
            # 背景颜色
            Color(1, 1, 1, 1)
            # 浮动布局矩形 = 矩形（位置=布局位置，大小=布局大小）
            self.rect = Rectangle(pos=self.pos, size=self.size)
            # 浮动布局绑定（位置=布局矩形位置，大小=设置背景尺寸）
            self.bind(pos=self.update_rect, size=self.update_rect)

        # 按钮，根据相对布局的位置，不是最外层线性布局的位置
        # 自定义按钮1
        bt1 = YushiruiButton(
            # 文本
            text='自定义按钮1',
            # 相对位置
            pos_hint={"right": 1, "top": 1},
            # 背景色
            background_color=(0.1, 0.5, 0.6, 1)
        )
        # 自定义按钮2
        bt2 = YushiruiButton(
            # 文本
            text='自定义按钮2',
            # 相对位置
            pos_hint={"x": 0, "top": 1},
            # 背景色
            background_color=(1, 0, 0, 1)
        )
        # 自定义按钮3
        bt3 = YushiruiButton(
            # 文本
            text='自定义按钮3',
            # 相对位置
            pos_hint={"center_x": .5, "center_y": .5},
            # 背景色
            background_color=(0.4, 0.5, 0.6, 1)
        )
        # 自定义按钮4
        bt4 = YushiruiButton(
            # 文本
            text='自定义按钮4',
            # 相对位置
            pos_hint={"x": 0, "y": 0},
            # 背景色
            background_color=(0, 0, 1, 1)
        )
        # 自定义按钮5
        bt5 = YushiruiButton(
            # 文本
            text='自定义按钮5',
            # 相对位置
            pos_hint={"right": 1, "y": 0},
            # 背景色
            background_color=(0.8, 0.9, 0.2, 1)
        )

        # 相对布局
        relative_layout = RelativeLayout()

        # 遍历加组件
        for i in [bt1, bt2, bt3, bt4, bt5]:
            # 加组件（按钮）
            relative_layout.add_widget(i)

        # 加组件，空的BoxLayout占位
        self.add_widget(BoxLayout())
        # 加组件，相对布局
        self.add_widget(relative_layout)

    # 设置背景尺寸，可忽略
    def update_rect(self, *args):
        # 布局矩形位置 = 布局位置
        self.rect.pos = self.pos
        # 布局矩形大小 = 布局大小
        self.rect.size = self.size


# app类
class Yushirui0218App(App):
    # 重构
    def build(self):
        # 返回自定义组件
        return YushiruiWidget()


if __name__ == "__main__":
    # 运行
    Yushirui0218App().run()
