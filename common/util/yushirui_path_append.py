# -*- coding:utf-8 -*-
# Author：余时锐
# Date: 2016-09-01
# Message：追加路径

import os
import sys

def yushirui_path_append():
    ''' 追加路径 '''

    # 当前目录
    xpath = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(xpath)
    # 上一级目录
    xpath = os.path.dirname(xpath)
    sys.path.append(xpath)
    # 上上一级目录
    xpath = os.path.dirname(xpath)
    sys.path.append(xpath)
    sys.path.append('./')
    sys.path.append('../')
    sys.path.append('../../')
    sys.path.append('../../../')
    sys.path.append('../../../../')