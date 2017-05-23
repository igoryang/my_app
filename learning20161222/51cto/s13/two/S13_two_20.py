#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'
'''
文件操作---with处理上下文
'''

#3.关闭文件
#file.close()
#with

with open("db") as f:   #python 2.7以后 支持 打开多个文件
    pass

with open('db1','r',encoding="utf-8") as f1,open('db2','w',encoding="utf-8") as f2: #python 2.7以后 支持 打开多个文件
    #pass
    times = 0
    for line in f1: #读出f1中的
        times += 1
        if times <= 10:
            f2.write(line)  #写入到f2中
        else:
            break

with open('db1','r',encoding="utf-8") as f1,open('db2','w',encoding="utf-8") as f2: #python 2.6以后 支持 打开多个文件
    #pass
    #times = 0
    for line in f1: #读出f1中的
        new_str = line.replace("abc","Replace")
        f2.write(new_str)