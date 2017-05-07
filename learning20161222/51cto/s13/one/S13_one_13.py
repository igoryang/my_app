#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# author Y.G
__author__ = 'YangGang'

name = input("input your name:")
age = input("input your age:")
job = input("input your job:")
print("name is:",name)
print("age is:",age)
print("job is:",job)

#print("name is %s,age is %s,job is %s",%(name,age,job))
#格式化字符串  %s 字符串  %d 整数  %f 浮点数
msg = '''
information of user %s:
Name :%s
Age  :%s
Job  :%s
=====end===
''' %(name,name,age,job)

print(msg)