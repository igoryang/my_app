#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
28--内置函数补充3

'''
# python s1.py
# 1,读取文件内容open，str到内存
# 2,python,把字符串--.>编译-->特殊代码
# 3，执行代码
#
# compile()  #把字符串 ---》编译成代码
# eval()
# exec()

s = "print(123)"
#将字符串编译成python代码
r = compile(s,"<string>","exec")  #编译 single,eval,exec  单行，表达式，和pythons代码一样的内容
print(s,type(s))
#执行python 代码
exec(r) #执行代码  无返回值

s = "8*8"
ret = eval(s) #执行 表达式 有返回值
print(ret)

print(dir(dict))  #dir 快速查看，对象提供了哪些功能
print(dir(list))

help(list) #查看 对象 功能 明细  读源码

#divmod(x,y)
#共97条； 每页显示10条；需要多少页
r = divmod(97,10)
print(r[0])
print(r[1])

n1,n2 = divmod(100,10)
print(n1,n2)

# 对象和类关系
s = "alex" #对象，"alex"==>str   每一个都是一个类

#对象是类的实例
 # list = [11,22,33 ]   ["s"]
 # 类的实例      对象           对象
s2 = [11,22,33]
 #用来判断，对象是否是某个类的实例
r = isinstance(s2,list)
print(r)
r = isinstance(s2, dict)
print(r)
