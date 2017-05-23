#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
文件操作--打开操作功能
'''
#open() 函数  文件操作

#打开文件
# file = open("db",'r') #只读
# file = open("db",'w') #清空文件，写
# file = open("db",'x') #如果文件存在报错，不存在创建写内容  python3新加功能
# file = open("db",'a') #追加

#rb,wb,xb,ab -->直接和二进制打交道，字节
#r+b,w+b,x+b,a+b -->直接和二进制打交道，字节

#r+ w+ x+ a+ 可读可写         常用功能 r+

#file.tell()  获取当前指针位置（字节）
#file.seek()  调整当前指针位置（字节）

#2,操作文件
#read()  #无参数，读全部，有参数;   b:按字节
#tell()  获取当前指针位置（字节）
#seek() 调整指定位置（字节）

#wiite() 写数据    有b 只能写字节bytes()
#flush 强刷到文件  在未close()之前

#readable() 是否可读

#readline  只读取一行
#truncate  截断数据

f = open("db","r+",encoding="utf-8")
# f.readline()
# f.readline()
# f.tell()
# f.seek(3)
# f.truncate()
# f.close()

for line in f:  #for 循环 readline
    print(line)

#3，关闭
f.close()