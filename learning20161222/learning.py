#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#author = 'igor'
''''''
"""
变量
python      python-jenkins   flask  django
可变的量
命名：字母，数字，下划线   不能以数字开头，区分大小写
number = 3    #把3 赋值给变量number

常量：全部大写
NAME
全局变量 global 重新赋值
全部大写


if 3==3:
    pass
else:
    pass
if  elif:  elif: ...else:

for i in rang(10):

while Ture:
    continue
    break


函数：
1，def
2,名称
3，函数体
4,参数：
    普通参数
    指定参数
    动态参数
       *args    列表传输
       *kwargs

       **args   字典传输
       **kwargs
     万能参数
def f1(*args):
     pass

format
print ( "this is format 0 {0},this is format 1 {1}".format(112,222))

三元运算  | 三木运算
name = '3' if 1==1 else '4'
print(name)

lambda 匿名函数

lambda x:print x

内置函数
abs()
bool()
bin()
oct()
hex()
bytes("李李",encoding="utf-8")

文件操作
open()
f = open('db','r')
f = open('db','w')
f = open('db','a')
f = open('db','x')
f = open('db','rb')

文件打开open()
文件操作  只读，只写，追加，
文件关闭

f.close()
with open('d','a') as f:
    pass

file = open("db",'r',encoding="utf-8")  #打开文件  r 只读 ； w  只写 ；a 追加  ; x 文件不存在创建写入，存在报错；b 二进制；
r+ ; w+; a+; x+;可读可写
r+b;w+b;a+b;x+b;
file.write()   #写入文件
file.close()  #关闭文件
file.flush()  #强制刷新
file.seek()  #指针位置
file.truncate()  #截断后面的数据
file.read()  #读取所有
file.readline()   #读取一行
file.readable()   #读取文件的操作模式

"""
file = open('db','r',encoding="utf-8")
n = lambda a,b=5:a+b+10
# bytes(n,encoding="utf-8")
print(n(3))
file.readable()
print(file)


