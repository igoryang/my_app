#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
31--内置函数补充6
'''

#fileter(函数，循环）  筛选符合函数的参数
#map(函数，可以迭代的对象（可以for循环的东西））

li = [11,22,33,44,55]

def f1(args):
    result = []
    for i in args:
        result.append(100+i)
    return result

r = f1(li)
print(r)

def f2(a):
    return a + 100
li2 = [11,22,33,44]
re = map(f2,li2)
re2 = map(lambda a:a+101,li2)
print(list(re))
print(list(re2))
