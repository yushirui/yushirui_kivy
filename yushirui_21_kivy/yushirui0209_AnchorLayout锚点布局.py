# -*- coding:utf-8 -*-
# Author：余时锐
# Date: 2020-06-22
# Message：yushirui0209_AnchorLayout锚点布局
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

# 浮动布局
from kivy.uix.floatlayout import FloatLayout

# 列表布局
from kivy.properties import ListProperty

# 锚点布局
from kivy.uix.anchorlayout import AnchorLayout

# 网格布局
from kivy.uix.gridlayout import GridLayout

# 文本框
from kivy.uix.textinput import TextInput

# 图案库，矩形、颜色
from kivy.graphics import Rectangle, Color

# ======================================== 图标与标题 ========================================
# 查找应用图标
app_icon = yushirui_find_file_or_dir('common/image/yu.ico')

# 图标
App.icon = app_icon

# 标题
App.title = 'yushirui0209_AnchorLayout锚点布局'

# 自定义组件（锚点布局）
class YushiruiWidget(AnchorLayout):
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

        # 锚点布局，左上角
        anchor_first = AnchorLayout(anchor_x='left', anchor_y='top')
        # 锚点布局，加按钮
        anchor_first.add_widget(Button(text='左上角', size_hint=[.3, .2]))

        # 锚点布局，右下角
        anchor_second = AnchorLayout(anchor_x='right', anchor_y='bottom')
        # 锚点布局，加按钮
        anchor_second.add_widget(Button(text='右下角', size_hint=[.3, .2]))

        # 加组件（锚点布局，左上角）
        self.add_widget(anchor_first)
        # 加组件（锚点布局，右下角）
        self.add_widget(anchor_second)

    # 设置背景尺寸，可忽略
    def update_rect(self, *args):
        # 布局矩形位置 = 布局位置
        self.rect.pos = self.pos
        # 布局矩形大小 = 布局大小
        self.rect.size = self.size


# app类
class Yushirui0209App(App):
    # 重构
    def build(self):
        # 返回自定义组件
        return YushiruiWidget()


if __name__ == '__main__':
    # 运行
    Yushirui0209App().run()
