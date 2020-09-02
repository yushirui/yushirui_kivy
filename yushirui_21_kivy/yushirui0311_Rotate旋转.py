# -*- coding:utf-8 -*-
# Author：余时锐
# Date: 2020-06-22
# Message：yushirui0201_Size屏幕尺寸

# ======================================== 标准库 ========================================
# 文件系统
import os

# 系统
import sys

# 时间
from time import strftime

# ======================================== 追加路径 ========================================
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

# ======================================== kivy应用 ========================================
# app应用
from kivy.app import App

# ======================================== kivy组件 ========================================
# 组件
from kivy.uix.widget import Widget

# 标签
from kivy.uix.label import Label

# 按钮
from kivy.uix.button import Button

# 文本框
from kivy.uix.textinput import TextInput

# 异步图片
from kivy.uix.image import AsyncImage

# ======================================== kivy布局 ========================================
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

# 缩放布局
from kivy.uix.scatterlayout import ScatterLayout

# 堆栈布局
from kivy.uix.stacklayout import StackLayout

# ======================================== kivy其他 ========================================
# 定时器
from kivy.clock import Clock

# 图案库，矩形、颜色
from kivy.graphics import Rectangle, Color
# ？？？
from kivy.graphics.instructions import InstructionGroup

# ======================================== 图标与标题 ========================================
# 查找应用图标
app_icon = yushirui_find_file_or_dir('common/image/yu.ico')

# 图标
App.icon = app_icon

# 标题
App.title = 'yushirui0201_Size屏幕尺寸'



class YushiruiWidget(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Yushirui0311App(App):
    def build(self):
        return YushiruiWidget()

if __name__ == "__main__":
    Yushirui0311App().run()