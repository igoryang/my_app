#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
内置函数3

用utf-8编码
'''
#字符串转换字节类型
#bytes(只要转换的字符串,按照什么编码)
n = bytes("李杰",encoding="utf-8")
print(n)
n = bytes("李杰",encoding='gbk')
print(n)

#字节转换成字符串
str()
s = "李杰"
s = str(bytes("李杰",encoding="utf-8"),encoding="utf-8")
print(s)
s1 = str(bytes(s,encoding="utf-8"),encoding="utf-8")
print(s1)

s2 = b'\xe6\x9d\x8e\xe6\x9d\xb0'
print(s2.decode('utf-8'))
# print(str(bytes(s2,encoding="utf-8"),encoding="utf-8"))

# name = 'zifuchuang'
# nameBytes = name.encode('utf-8')   # 字节
# nameStr = nameBytes.decode('utf-8')# 字符串
# print(name)
# print(nameBytes)
# print(nameStr)