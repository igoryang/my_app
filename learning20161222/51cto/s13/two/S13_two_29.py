#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'
'''


29 --内置函数补充4

'''

 # filter,map
 #filter 函数 ，可以迭代的对象

# def f1(args):
#     result = []
#     for item in args:
#
#         if item > 22:
#             result.append(item)
#     return result
# li = [ 11,22,33,44,55]
# ret = f1(li)
# print(ret)

# filter(函数，可迭代的对象（列表，元组，字典）)

# li = [44,55,66,77]
# ret = filter(None,li)
# print(list(ret))

li2 = [1,2,33,10,33,44,55,66]
#filter内部，循环第二个参数
def f2(a):
    if a > 22:
        return True

ret2 = filter(f2,li2)  #filter 循环第二个参数，让每个循环元素执行 函数，如果函数返回值True,表示合法存入ret2
print(list(ret2))