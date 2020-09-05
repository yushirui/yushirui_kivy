# -*- coding:utf-8 -*-
# Author：余时锐
# Date: 2020-06-22
# Message：yushirui0101_环境安装
# kivy
import kivy

# Kivy版本号
kivy.require('1.11.1')

# 从kivy.app包里面导入App类
from kivy.app import App
Label控件
from kivy.uix.label import Label

'''
# 安装kivy
pyhon版本3.7以下


# 下载whl安装
# pip install *.whl

# 或者
pip install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com --upgrade pip wheel setuptools
pip install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
pip install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com kivy.deps.gstreamer
pip install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com kivy.deps.angle
pip install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com kivy


# 从kivy.uix.label包中导入

# 打包虚拟机
下载打包虚拟机
链接：http://pan.baidu.com/s/1gf5S8lP 密码：buj4
1.先安装虚拟机：VirtualBox-4.3.12-93733-Win.exe
2.安装插件：Oracle_VM_VirtualBox_Extension_Pack-4.3.12-93733.vbox-extpack
3.安装系统：kivydev.ova（安装好1，2之后直接双击）
需要注意的是共享文件夹（win不能直接拖动到虚拟机内），设置方法
1.点击设置，进入设置界面
2.点击设置，在右边有一个添加按钮，选择文件夹后勾选自动挂载（其余的不要选择）
直接启动虚拟机，打开File System ， sf_(你共享的文件名)，这就是你的共享目录
将你要打包的文件复制到/home/kivydev/kivy/accordion/目录下，在/home/kivydev/kivy/accordion/下启动终端（右击第4个选项），输入以下命令：
buildozer android_new debug
success成功后，在/home/kivydev/kivy/accordion/bin目录下会生成一个apk
'''


class YushiruiApp(App):
	# 重构
	def build(self):
		# 标签
		label = Label(text='yushirui_kivy')

		# label组件
		return label


if __name__ == '__main__':
	# 运行
	YushiruiApp().run()
