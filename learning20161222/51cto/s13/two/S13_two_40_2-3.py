#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''

装饰器流程剖析
'''

#
# def outer(func):
#     def inner():
#         print('log')
#     return

def outer(func):
    def inner():
        print('before')
        func()
        print('after')
    return inner

#@ +函数名  放在某个函数功能上面
# 功能1：自动执行outer函数 并且将其下面的函数名f 1当作参数传递
# 功能2，将outer函数的返回值，重复赋值给f1
@outer
def f1():
    print("F1")


