#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
实例：  函数式编程实现登录和注册
'''
def login(username,password):
    """
    用于用户登陆：
    :param username: 用户名
    :param password: 用户密码
    :return: True 登陆成功 False登录失败
    """
    #pass
    f = open("db",'r')
    for line in f:
        line_list = line.strip().split("|")  #strip() 移除 换行符 空格
        if line_list[0] == username and line_list[1] == password:
            return True
        else:
            return False

def register(username,password):
    """
    用于用户注册
    :param username:用户名
    :param password:用户密码
    :return:
    """
    # pass
    f = open("db",'a')
    temp = "\n" + username + "|" + password
    f.write(temp)
    f.close()
    print("欢迎注册本系统！")

def main():
    t = input("1:登录；2：注册")
    if t == "1":
        user = input("请输入用户名:")
        pwd = input("请输入密码:")
        r = login(user,pwd)
        if r:
            print("登录成功！")
        else:
            print("登录失败！")
    elif t == "2":
        user = input("请输入注册用户名：")
        pwd = input("请输入注册用户密码：")
        register(user,pwd)

main()