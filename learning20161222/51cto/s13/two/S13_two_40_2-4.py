#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'


'''
1，定义函数 未调用 不执行

2，函数名 》 代指函数体


'''

def outer(func):
    def inner():
        print('before')
        func()
        print('after')
    return inner

# @+函数名
#功能
#1, 自动执行outer 函数 并且将其下面的函数名f1当作参数传递
#2，将outer函数的返回值 重新赋值给f1
@outer
def f1():
    print("F1")



