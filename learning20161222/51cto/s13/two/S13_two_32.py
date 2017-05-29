#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
32--内置函数补充--7
filter   函数返回True,将元素添加到结果中
map   将函数返回值添加到结果中
'''
#float  转换成浮点型
#format 字符串格式化
#frozenset() 不可变集合

# globals()  #全局变量
# locals() #局部变量

NAME = "ALEX"
def show():
    a =123
    b =33
    print(globals())
    print(locals())
show()

s = "sdlfjsafjldsfjsdsdsdsdferwtrwtsldfj"
print(hash(s))  #一般用于字典的key 存储  转成hash值

s2 = "李杰"  #python2 只能按照字节 李杰=6   #python 3  默认按照字符 李杰=2 /按照字节
s3 = bytes("李杰",encoding="utf-8")
print(len(s2),type(s2))
print(len(s3),type(s3))
