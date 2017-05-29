#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

"""
33--内置函数补充 8
"""

#2，7 for "李杰"
#3,5 for "李杰"

#max()   最大值
#main()  最小值
#sum()   求和

r = max([11,22,33,44])
r2 = min(11,22,33,44)
r3 = sum([11,22,33,44])
print(r)
print(r2)
print(r3)

#object() 类
#chr()  ord()   数字 字符

r4 = pow(2,10)  # 求次方 2**10=1024
print(r4)

# *args,**kwargs  参数可能不对的  python3 参数显示不友好，Python2.7的友好
#property() 面向对象 特性
#range()

#repr()
#reversed()  反转

li5 = [11,22,33,44]
li5.reverse()
reversed(li5)

r = round(1,8) #round 四舍五入
print(r)

#set() 集合
# slice()  切片功能
ss = "sla;dfa;ldfxxxxxssssss"
print(ss[0:5])

#sort() 排序
li6 = [2,3,5,0]
li6.sort()

#str()  字符串
#super()  面向对象
#tuple()  元组
#type()  类型
#vars() 模块有哪些变更使用

#zip()  元素集合
l1 =["ak",11,22,33]
l2 =["is",44,55,66]
l3 =["good",77,88,99]

r = zip(l1,l2,l3)
# print(list(r))
temp = list(r)[0]
ret = ' '.join(temp)
print(ret)

#__import__()  导入模块