#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
利用动态参数实现  format 功能
'''

# str--》format 格式化输出
# 格式化输出：%s %d

s = "i am {0},age{1}".format("alex",18)
s2 = "i am {0},age{1}".format(*["alex",18])
print(s)
print(s2)

li = ['Tom',18]

s3 = "i am {name},age {age}".format(name = 'Jim',age = 20)
print(s3)

dic = {'name':'alex','age':20}
s4 = "i am {name},age {age}".format(**dic)
print(s4)