#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

#函数之 内容补充
'''
函数： 定义函数不执行，只有调用函数时，函数体才执行

函数的参数传递的是引用

1,def
2,名字
3，函数体
4，返回值
5，参数
    普通参数
    指定参数
    默认参数
    动态参数
        *args
        **kwargs
    万能参数
        *args,**kwargs
6,补充
    a.函数执行顺序
    b.函数传递的是 -->引用
    c.全局变更---global 定义  全部大写，均可读

'''

def f1(a1,a2):
    return a1 + a2

def f1(a1,a2):
    return a1 * a2
ret = f1(8,8)
print(ret)    #顺序执行 2个f1()

def f2(a1):
    a1.append(999)

li = [11,22,33,44]
f2(li)
print(li)    #函数的参数传递的是引用 li-->a1-->li

#全局变量--- 作用域

NAME = "alex" # 全局变量  所有作用域里面都可以读   全局变量---》全部大写  常量--全部大写
#对全局变量进行 重新赋值---》global
#name = [11,22,33,44]  name是个列表，元组，字典    可以添加值，不可以重新赋值

def f3():
    name = 'ak'   #函数体里 ：自己本身的作用域自己调用
    #global name = 'Jick' #表示name是全局变量  修改全局变量
    print(name)

def f4():
    print(NAME)

f3()
f4()

