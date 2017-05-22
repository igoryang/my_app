#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
lambda表达式   简单的函数写法

'''

#v如果 if 条件 1 == 1 成立
#则 if 前的执行
#否则  else   执行

name = "alex" if 1 == 1 else "SB"
print(name)

def f1(a1):
    return a1 + 100
ret = f1(10)
print(ret)


f2 = lambda a1,a2:a1+a2+100  #简单的赋值操作
ret2 = f2(9,10)
print(ret2)