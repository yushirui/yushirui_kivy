# -*- coding:utf-8 -*-
# Author：余时锐
# Date: 2016-09-01
# Message：自定义按钮

# 导入模块
import sys

# 读取配置，支持中文
from kivy.config import Config

Config.read('kivy_config.ini')

# app对象
from kivy.app import App

# 标题
App.title = '余时锐字符_第三种跨平台'
# 图标
App.icon = 'common/image/yu.ico'

from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.gridlayout import GridLayout

# 字符串
from common.util.yushirui_random_string import YushiruiRandomString

# 剪贴板
from common.util.yushirui_clipboard import YushiruiClipboard

# 找文件
from common.util.yushirui_find_file_or_dir import yushirui_find_file_or_dir


class YushiruiButton(Button):
    def __init__(self, **kwargs):
        # super(YushiruiButton, self).__init__(**kwargs)
        super().__init__(**kwargs)

        # 文本
        self.text = kwargs['text']

        # 字体 = 找文件（当对于data文件夹，/font/simkai.ttf）
        self.font_name = yushirui_find_file_or_dir('/font/simkai.ttf')
