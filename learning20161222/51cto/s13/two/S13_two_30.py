#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
30===内置函数补充 5

'''
#####one
def f2(a):
    if a < 10:
        return True

li = [1,2,3,5,10,22,33,44]
ret = filter(f2,li)
print(list(ret))

####two
f1 = lambda a:a>30  #lambda  函数表达式 自动return   90 》30 --> Ture
ret2 = f1(90)
print(ret2)  #Ture

li2 = [11,22,33,44]
ret3 = filter(lambda a:a>22,li2)
print(list(ret3))