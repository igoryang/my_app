#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
24  -- 内置函数补充

'''
#callable()  是否可以被执行 /调用
def f1():
    pass

f2 = 123
print(callable(f1))
print(callable(f2))

#ASCii表   65 --90 A-Z;
print(chr(65))
print(ord("A"))