# -*- coding:utf-8 -*-
# Author：余时锐
# Date: 2020-06-22
# Message：yushirui0406_Label标签
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

# 开关
from kivy.uix.togglebutton import ToggleButton

# 开关改变状态
from kivy.uix.behaviors import ToggleButtonBehavior

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

# 图案库，矩形、颜色、线
from kivy.graphics import Rectangle, Color, Line

# 图片指示组
from kivy.graphics.instructions import InstructionGroup

# 十六进制颜色
from kivy.utils import get_color_from_hex

# ======================================== 图标与标题 ========================================
# 查找应用图标
app_icon = yushirui_find_file_or_dir('common/image/yu.ico')

# 图标
App.icon = app_icon

# 标题
App.title = 'yushirui0406_Label标签'


# 自定义组件（线布局）
class YushiruiWidget(BoxLayout):
    # 构造方法
    def __init__(self, **kwargs):
        # 父类构造方法
        super().__init__(**kwargs)

        # 设置引用时markup属性必须设置为真（True、1等）
        # Label文本标记
        # 单击【不该沉默时沉默，该勇敢时软弱】触发绑定的事件
        # 单击【全都怪我，】无事件
        label_ref = Label(text='全都怪我，[ref=label]不该沉默时沉默，该勇敢时软弱[/ref]', markup=True, color=(.9, .2, .1, 1))

        # 绑定触发事件，回调方法
        label_ref.bind(on_ref_press=self.print_it)

        # 布局加组件（按钮）
        self.add_widget(label_ref)

    # 未使用到self，建议设置为静态方法
    @staticmethod
    def print_it(*args):
        # 打印文本
        print('不该沉默时沉默，该勇敢时软弱')


# app类
class Yushirui0406App(App):
    # 重构
    def build(self):
        # 返回自定义组件
        return YushiruiWidget()


if __name__ == '__main__':
    # 窗口
    from kivy.core.window import Window

    # 页面背景
    Window.clearcolor = [1, 1, 1, 1]
    # 运行
    Yushirui0406App().run()
