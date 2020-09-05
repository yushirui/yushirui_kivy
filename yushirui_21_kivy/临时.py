# -*- coding:utf-8 -*-
# Author：余时锐
# Date: 2020-06-22
# Message：yushirui0201_Size屏幕尺寸

'''
# 异步图片
image = AsyncImage(source='http://sck.rjkflm.com/images/logo1.png')



# 图片
Image:
    # 图片
	source: '../common/image/yu.ico'



# 遍历添加按钮
        for i in range(25):
            # 按钮
            btn = Button(text=str(i), width=40 + i * 5, size_hint=(None, 0.15))
            # 布局加组件（按钮）
            self.add_widget(btn)



if __name__ == '__main__':
    # 窗口
    from kivy.core.window import Window
    # 页面背景
    Window.clearcolor = [.8, .8, .8, 1]
    # 运行
    Yushirui0201App().run()




# 画布
    canvas:
        # 颜色
        Color:
            # r红色，g绿色，b蓝色，a透明度
            rgba: [1, 1, 1, 1]

        # 矩形
        Rectangle:
            # 绝对大小 = 组件大小
            size: self.size
            # 绝对位置 = 组件位置
            pos: self.pos
            # 图片
            source: 'back.jpg'



 # 画布
    canvas:
        # 颜色
        Color:
            # r红色，g绿色，b蓝色，a透明度
            rgba: [1, 1, 1, 1]

        # 矩形
        Rectangle:
            # 绝对大小 = 组件大小
            size: self.width + 20, self.height + 20
            # 绝对位置 = 组件位置
            pos: self.x - 10, self.y - 10
            # 图片
            source: 'back.jpg'



# 画布
    canvas:
        # 颜色
        Color:
            # r红色，g绿色，b蓝色，a透明度
			rgba: [0, .5, .1, 1]

		# 矩形
		Rectangle:
		    # 具体位置
			pos: self.x+10,self.y+10
		    # 具体大小
			size: self.width*0.2, self.height*0.15





# 设置背景前
        with self.canvas.before:
            # 背景颜色，rgba格式，通常值为0-1之间（具体的值 / 255）
            Color(1, 1, 1, 1)
            # 浮动布局矩形 = 矩形（位置=布局位置，大小=布局大小）
            self.rect = Rectangle(pos=self.pos, size=self.size)
            # 浮动布局绑定（位置=布局矩形位置，大小=设置背景尺寸）
            self.bind(pos=self.update_rect, size=self.update_rect)



画矩形
# 设置背景颜色（可忽略）
        with self.canvas:
            # 背景颜色，rgba格式，通常值为0-1之间（具体的值 / 255）
            Color(0, 0, 1, 0.2)
            # 矩形（位置=位置，大小=大小）
            Rectangle(pos=self.pos, size=(300, 300))

            # 背景颜色，rgba格式，通常值为0-1之间（具体的值 / 255）
            Color(0, 1, 0, 0.4)
            # 矩形（位置=位置，大小=大小）
            Rectangle(pos=(300, 300), size=(300, 300))
'''