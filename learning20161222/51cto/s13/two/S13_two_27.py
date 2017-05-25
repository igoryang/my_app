#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
27--内置函数补充2

'''

# python s1.py
# 1,读取文件内容open，str到内存
# 2,python,把字符串--.>编译-->特殊代码
# 3，执行代码
#
# compile()  #把字符串 ---》编译成代码
# eval()  #执行 把字符串转换成表达式   有返回值
# exec()  #执行python代码   无返回值

s = "print(123)"
#将字符串编译成python代码
r = compile(s,"<string>","exec")  #编译 single,eval,exec  单行，表达式，和pythons代码一样的内容
print(s,type(s))
#执行python 代码
exec(r) #执行代码

s = "8*8"
ret = eval(s)  #字符串转换成pthon表达式
print(ret)

