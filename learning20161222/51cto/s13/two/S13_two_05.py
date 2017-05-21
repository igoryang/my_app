#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

#函数之动态参数

#def f1():--->

#4.*  接收任意个参数  存放在元组中  f1(*[11,22,33,44])
#4.**  接收任意个参数  存放在字典中  f1(**{'k1':'v1','k2':'v2'})
def f1(*args):
    print(args,type(args))

f1(11,22,33,44)
li = [11,22,33,44,'ak']
f1(li,'mm')
f1(*li,'mm')
