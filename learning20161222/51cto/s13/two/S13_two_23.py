#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''

1,python 基础
2，基本数据类型 ：str,dict,list,tuple,int,float,
3,函数式编程
    函数定义 def f1():
    内置函数：文件处理open()  abs() bin() otc() hex()
4，三元运算   列表  name = "a" if 1==1: else "b"
  lambda表达式  函数  f = lambda a1: a1+1



'''

# with open("HA.cfg","r+",encoding="utf-8") as file:
#     print(file.read())

li = [11,22,33,44]    #函数默认返回None   传递参数是：引用
def f1(arg):
    arg.append(55)
    #print(arg)
li = f1(li)
#f1(li)
print(li)

li = [11,22,33,44]
def f1(arg):
    arg.append(55)
    #print(arg)
#li = f1(li)
f1(li)
print(li)

f = bytes("李杰",encoding="utf-8")  #字符串转字节
print(f,type(f))

f1 = f.decode()  #字节转字符串
print(f1,type(f1))
