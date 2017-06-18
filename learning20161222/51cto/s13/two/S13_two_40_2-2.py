#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
装饰器流程制作剖析储备知识

'''

#  s1.py
def outer():
    print('log')

def outer(func):
    def inner():
        print('log')
        ret = func()
        print('after')
        return ret
    return inner

def f1():
    outer()
    print("F1")
def f2():
    outer()
    print("F2")

def f100():
    outer()
    print("F100")

#装饰器
@outer  #函数装饰器功能 不修改原函数功能
def f3():
    print("F3")

@outer
def f4()
    print("F4")