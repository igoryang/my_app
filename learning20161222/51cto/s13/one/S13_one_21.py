#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
本节内容
Python介绍
发展史
Python 2 or 3?
安装
Hello World程序
变量
用户输入
模块初识
.pyc是个什么鬼？
数据类型初识
数据运算
表达式if ...else语句
表达式for 循环
break and continue
表达式while 循环
作业需求


usrname = raw_input() 2.x  字符串
usrname = input()  2.x  整数

useranme = input()   3.x 字符串 整数。。。。。。
'''

'''
import getpass
user,passwd = 'amin','123'
username = input("username:")
password = getpass.getpass("passwd:")
if username == user and password == passwd:
    print("Welcom login!")
else:
    print("Wrong!")

'''

'''
real_age = 33

guess_age = int(input("guess:"))

for i in range(10):
    # if i >=3:
    #     break
    if i >=3:break
    if guess_age > real_age:
        print("big")
    elif guess_age < real_age:
        print("small")
        break
        # pass  #占位符
    else:
        print("xxx")
        break
'''

name = 'jim'
age = 33
job = 'IT'
msg = '''
information of name:
name: %s
age : %d
job : %s
'''%(name,age,job)
print(msg)

#变量
name = 'admin'
#常量  大写字母  不会更改
MYSQL_CONNECTION = '192.168.1.100'
print(name,MYSQL_CONNECTION)
#导入模块  import
import os,sys,time

#pip  安装python 各种模块命令   pip install  mysql

#pip list
os.system("dir")
res = os.popen("ipconfig").read()
print(res)

print(sys.path)

#lib/site-packages;dist-packages;

