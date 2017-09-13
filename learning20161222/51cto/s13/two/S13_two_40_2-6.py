#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'



def outer(func):
    def inner(a):
        print('before')
        r = func(a)
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

def f2():
    pass