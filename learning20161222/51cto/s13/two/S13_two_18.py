#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
文件操作--打开模式2

'''
#open() 函数  文件操作

#打开文件
# file = open("db",'r') #只读
# file = open("db",'w') #清空文件，写
# file = open("db",'x') #如果文件存在报错，不存在创建写内容  python3新加功能
# file = open("db",'a') #追加

#rb,wb,xb,ab -->直接和二进制打交道，字节

#r+ w+ x+ a+ 可读可写         常用功能 r+

#file.tell()  获取当前指针位置（字节）
#file.seek()  调整当前指针位置（字节）

f = open("db","r+",encoding="utf-8")    # r+ 按照字符读取； r+b 按照字节读取
data = f.read(1)  #只要读，默认写就在最后添加
print(data,type(data))
print(f.tell())  #tell()是获取当前指针的位置（字节）
#f.seek(1)  #seek() 调整指针位置  字节的位置（字节）
f.seek(f.tell()) #从当前指针位置开始覆盖数据
f.write("888")
f.close()