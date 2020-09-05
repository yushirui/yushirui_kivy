# -*- coding:utf-8 -*-
# Author：余时锐
# Date: 2020-09-05
# Message：yushirui0107_疑难杂症
'''
# ==================== 读取kv文件gbk错误 ====================
# 修改builder.py文件，约第228行
# 打开文件，encoding='utf-8',errors='ignore'

# 余时锐修改标记
# 加入编码支持
with open(filename, 'r',encoding='utf-8',errors='ignore') as fd:
    kwargs['filename'] = filename
    data = fd.read()


'''