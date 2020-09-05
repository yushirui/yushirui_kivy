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

# 线布局
from kivy.uix.boxlayout import BoxLayout

# 浮动布局
from kivy.uix.floatlayout import FloatLayout

# 列表布局
from kivy.properties import ListProperty

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
App.title = 'yushirui0201_Size屏幕尺寸'

# 应用
class Yushirui0203App(App):
    # 重构
    def build(self):

        # 设置背景尺寸（布局）
        def update_rect(layout, *args):
            # 布局矩形位置 = 布局位置
            layout.rect.pos = layout.pos
            # 布局矩形大小 = 布局大小
            layout.rect.size = layout.size

        # 浮动布局
        float_layout = FloatLayout()

        # 浮动布局画布锁
        with float_layout.canvas:
            # 背景颜色
            Color(1, 1, 1, 1)
            # 浮动布局矩形 = 矩形（位置=浮动布局位置，大小=浮动布局大小）
            float_layout.rect = Rectangle(pos=float_layout.pos, size=float_layout.size)
            # 浮动布局绑定（位置=布局矩形位置，大小=设置背景尺寸）
            float_layout.bind(pos=update_rect, size=update_rect)

        # 在布局内的300，200处添加一个为布局0.3，0.2大小的按钮
        button = Button(text='Hello FloatLayout', size_hint=(.3, .2), pos=(300, 200))

        # 布局加组件（按钮）
        float_layout.add_widget(button)

        # 返回布局
        return float_layout


if __name__ == "__main__":
    Yushirui0203App().run()
