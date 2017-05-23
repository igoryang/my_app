#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
文件操作之打开模式
'''

#open() 函数  文件操作

#打开文件
# file = open("db",'r') #只读
# file = open("db",'w') #清空文件，写
# file = open("db",'x') #如果文件存在报错，不存在创建写内容  python3新加功能
# file = open("db",'a') #追加

#rb,wb,xb,ab -->直接和二进制打交道，字节

f = open('db','r',encoding="utf-8")  #ctrl+open() 进入查看源码功能
data = f.read()
print(data,type(data))
f.close()


f = open('db','rb')  #ctrl+open() 进入查看源码功能
data = f.read()
print(data,type(data))
f.close()

f = open('db','ab')  #ctrl+open() 进入查看源码功能
data = f.write(bytes("\nadd|123",encoding="utf-8"))
print(data,type(data))
f.close()

#操作文件
# file.read()  #通过源码查看功能 ctrl+read()


#关闭文件
# file.close()
#
# with open('db') as f:
#     pass