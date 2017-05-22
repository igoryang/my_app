#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
内置函数
'''
bytes()  #判断   UTF-8: 3个字节（一个汉字）  GBK:2个字节(一个汉字)

s = "李杰"   #utf-8  3 +3个字节
#二进制表示
#10进制表示
#8进制表示
#16进制表示

#字符串转换字节类型
#bytes(只要转换的字符串，用什么编码)

n = bytes(s,encoding="utf-8")
print(n)
n = bytes(s,encoding="gbk")
print(n)