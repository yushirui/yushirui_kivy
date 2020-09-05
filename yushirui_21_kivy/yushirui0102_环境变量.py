# -*- coding:utf-8 -*-
# Author：余时锐
# Date: 2020-06-22
# Message：yushirui0102_环境变量
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

# 盒子布局
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
App.title = 'yushirui0102_环境变量'

# 继承网格布局，窗口本身就是网格布局
class YushiruiWidget(GridLayout):
    # 构造方法
    def __init__(self, **kwargs):
        # 父类构造方法
        super(YushiruiWidget, self).__init__(**kwargs)

        # 窗口就是网格布局，2列
        self.cols = 2

        # 用户名标签
        uname_label = Label(text='用户名')
        # 用户名文本框（单行）
        uname_lineedit = TextInput(multiline=False)

        # 密码标签
        pwd_label = Label(text='密码')
        # 密码文本框（加密，单行）
        pwd_lineedit = TextInput(password=True, multiline=False)

        # 窗口加组件（用户名标签）
        self.add_widget(uname_label)
        # 窗口加组件（用户名文本框）
        self.add_widget(uname_lineedit)
        # 窗口加组件（密码标签）
        self.add_widget(pwd_label)
        # 窗口加组件（密码文本框）
        self.add_widget(pwd_lineedit)


# app类
class YushiruiApp(App):
    # 重构
    def build(self):
        # 返回自定义组件
        return YushiruiWidget()


if __name__ == '__main__':
    # 运行
    YushiruiApp().run()
