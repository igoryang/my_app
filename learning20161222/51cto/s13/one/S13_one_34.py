#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''

set 集合   {key1,key2,key3,.....}

无序，不重复序列

a.创建
li =[]
dic = {key:value}
se = {key,key2,key3}
type(xx)  #类型查看

b.功能
li = [] --->list()  __init__ --》一个for循环 ==》特殊方法
__init__

c.操作
操作集合
'''

# li = [11,22,33,44,55,66,11]
# print(li)
# se = {"123","456"}
# print(se)
# print(type(se))
#
# s = set()  #创建集合
# lii = [11,22,11,22]
# s1 = set(lii)   #转换集合
# print(s1)

s = set()
s.add(123)  #添加元素
s.add(123)
s.add(124)
print(s)

s1 = {11,22,33}
s2 = {22,44,55}
df = s1.difference(s2)  #A中存在，B中不存在
print(df)
df_2 = s1.symmetric_difference(s2)  #A B 中重复的去掉后合拼
print(df_2)

# s1.discard(11)  #移除元素 ，不存在也不会报错
# s1.remove(111)  #移除元素 ，不存在会报错
# # s1.pop()  #随机移除元素 ，并且存储 ret = s1.pop()

df_3 = s1.intersection(s2)  #交集
print(df_3)

df_4 = s1.isdisjoint(s2)  #判断是否有交集
print(df_4)
df_5 = s1.union(s2)  #联合
print(df_5)

ab = "sadlfjad"

df_6 = s1.update(ab)
print(df_6)


li = [55,66,77]  #list __init__
li()           #list  __call__
li[0]             #list __getitem__
li[0] = 123        #list __setitem__