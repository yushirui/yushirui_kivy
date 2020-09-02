# -*- coding:utf-8 -*-
# Author：余时锐
# Date: 2017-08-26
# Message：找文件、目录

import os
import sys


# 是否存在文件、目录
def yushirui_path_exists(path):
    ''' 是否存在文件、目录 '''
    return os.path.exists(path)


# 找文件或文件夹（文件名，目录名），找到，返回相对路径，找不到，抛文件找不到异常
def yushirui_find_file_or_dir(file_name='', dir_name='data'):
    ''' 找文件或文件夹（文件名，目录名），找到，返回相对路径，找不到，抛文件找不到异常 '''

    # 路径列表，相对路径，支持GUI、test、app等
    xpaths = ['./data/', '../data/', '../../data/', '../../../data/', '../../../../data/', './', '../', '../../']

    # 文件路径
    xpath = ''

    # 循环路径，看是否能找到文件或文件夹
    for xpath in xpaths:
        # 完整路径 = 相对路径 + 文件名
        xpath = xpath.replace('data', dir_name) + file_name
        # print(xpath)

        # 文件存在
        # 调用自定义，是否存在文件、目录方法
        if yushirui_path_exists(xpath):
            # 返回找到的路径
            return xpath

    # 未找到文件异常
    raise FileNotFoundError('有幺蛾子，方法 {}，没找到文件 {}'.format(sys._getframe().f_code.co_name, xpath))


if __name__ == '__main__':
    b = yushirui_find_file_or_dir('yushirui_file.py')
    print(b)

    b = yushirui_find_file_or_dir('余时锐_其它.xlsx')
    print(b)

    b = yushirui_find_file_or_dir('util', 'common')
    print(b)

    b = yushirui_find_file_or_dir('/util', 'common')
    print(b)

    b = yushirui_find_file_or_dir('util/yushirui_excel.py', 'common')
    print(b)

    b = yushirui_find_file_or_dir('util/yushirui_excel2.py', 'common')
    print(b)
