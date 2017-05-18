#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
字符串常用操作




【
列表：
索引
切片
追加
删除
长度
循环
包含
】
元组 不可变列表
'''
'''
name = ['a','b','c',3,4,33,5,2,3]

print("The list[name] lens is" ,len(name))
print("The list[name]  is" ,name)

# 元组  不可变列表

r = (1,2,3,4,5,6,2)
count = r.count(2)
print(count)
position_nu = r.index(5)
print(position_nu)
'''
# username = input("user:")
# if username.strip() == 'alex': #脱字符，除去前后空格  table \n等
#     print('welcom')


names = "alex,jack,rain"

name2 = names.split(",") # split 分割 按, 存储到列表
print(name2)

name3 = "|".join(name2)   #用 | 把列表字符串连接起来
print(name3)

name = "axmbl bill"
print(' ' in name)

print(name.capitalize())

msg = "Hell,{name},it is a b long {age},since last...."
msg2 = msg.format(name = 'AM',age=33)
print(msg)
print(msg2)

msg3 = " hell,{0},{1}"
print(msg3.format('AM',33))

#切片
name4 = "alex li"
print(name4[2:4])
print(name4.center(40,'-'))

print(name.find('l'))  # -1 是未找到，找到返回索引

# age = input("your age:")
# if age.isdigit():
#     age = int(age)
# else:
#     print("invalid data")
#
name5 = "aldsfsalsdf"
print(name5.isalnum())
print(name5.endswith('sdf'))
print(name5.startswith('a'))

print(name5.upper())
print(name5.lower())
print(name5.upper().lower())

