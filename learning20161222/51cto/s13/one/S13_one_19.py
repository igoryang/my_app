#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'


age = 22

counter = 0
for i in range(10):
    print("-->counter:",counter)
    if counter< 3:
        guess_num = int(input("input your guess num:"))
        if guess_num == age:
            print("Welcom right!")
            break
        elif guess_num > age:
            print("big")
        else:
            print("small")
    else:
        # print("error 3,please waiting..")
        # break
        continu_confirm = input("Do you want to continue ?:y/n")
        if continu_confirm ==  'y' or continu_confirm == 'Y':
            counter = 0
            continue
            #pass  占位符
        else:
            print("bye")
            break
    counter +=1

'''
作业一：博客
http://www.cnblogs.com/


作业二：编写登陆接口

1,输入用户名密码
2，认证成功后显示欢迎信息
3，输错三次后锁定

作业三：多级菜单

三级菜单
可依次选择进入各子菜单
所需要知识点：列表、字典
b-->back返回上级菜单
q--》quit
作业需求：
1,流程图 在线processon.com
2,Readme

3,SVN GIT
day1
day2
day3



'''