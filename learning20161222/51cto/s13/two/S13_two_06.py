#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
'''
#函数之 动态参数2
# 4,动态参数
# *  默认将传入的参数，全部放置在元组中 f1(*[11,22,33,'a'])
#  **  默认将传入的参数，全部放置在字典中 f1(**{'k1':'v1','k2':'v2'})

# 5万能参数  *args,**kwargs

def f2(*args,**kwargs):  #万能参数 *args,**kwargs
    print(args)
    print(kwargs)
f2(11,22,33,44,k1='v1',k2='v2')

def f1(**args):
    print(args,type(args))

# f1('ak')  #error
f1(name = 'Jim')
f1(name2 = 'Tom',age2 = 22)

dic = {'k1':'v1','k2':'v2'}
f1(kk = dic)
f1(**dic)

