#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''

装饰器的参数传递   func（*args,**kwargs)
'''

def outer(func):
    def inner(*args,**kwargs):
        print('before')
        r = func(*args,**kwargs)
        print('after')
        return r
    return inner

# @+函数名
#功能
#1, 自动执行outer 函数 并且将其下面的函数名f1当作参数传递
#2，将outer函数的返回值 重新赋值给f1

# 装饰器   在原函数之前执行  原函数之后执行  ，原函数正常执行
@outer
def f1(arg):
    print(arg)
    return "xxx"

@outer   #多个参数传递  *args,**kwargs
def f2(arg1,arg2):
    print("F2")