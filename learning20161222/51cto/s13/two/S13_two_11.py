#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
三元运算  三目运算
简单的if else语句

# 书写格式
result = 值1 if 条件 else 值2
# 如果条件成立，那么将 “值1” 赋值给result变量，否则，将“值2”赋值给result变量
'''

if 1 == 1:
    name = 'alex'
else:
    name = 'SB'
print(name)

name = 'alex' if 1 == 1 else 'SB'
print(name)
