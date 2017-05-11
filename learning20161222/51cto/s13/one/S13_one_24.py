#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'


'''

4,列表  最普遍的数据类型    列表的语法和使用  索引是从0开始。。。
list = [元素1，元素2，。。。，]  [0开始，1，2，3，]
name_list = ['admin','seven','jim']
name_list = list(['admin','seven','jim'])

name = "jim,jik,jii"

作业
写一个列表，列表里包含本组所有成员
往中间插入2个临组成员的名字
取出第3-8个人列表
删除第7个人
把刚才加入的那2个其它组的人一次性删除
把组长的名字加上备注
'''
age = 9
name = ['jim','ko','jack',23,age]
print(name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[-1])
print(name[0:1])
print(name[1:3])
print(name[-4:-1])
print(name[-4:])
print(name[:])
print(name[:4][2:3][0][1])

name.append('KK')
name.remove('jim')
print(name)