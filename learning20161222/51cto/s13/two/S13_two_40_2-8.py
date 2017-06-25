#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'


'''
装饰器的参数传递   func（*args,**kwargs)


装饰器 登陆功能 ：

装饰器  ---  常用功能  权限的验证


'''

LOGIN_USER = {"is_login":False,"courrent_user":user}

def outer(func):
    def inner(*args,**kwargs):
        if LOGIN_USER['is_login']:
            r = func()
            return r
        else:
            print('请登陆')
    return inner

def changpwd():
    pass


def manager():
    if LOGIN_USER['is_login']:
        print('欢迎%s登陆') %LOGIN_USER['current_user']
    else:
        print('请登陆')

def login(user,pwd):
    if user == "alex" and pwd == "123":
        LOGIN_USER['is_login'] = True
        LOGIN_USER['current_user'] = user
        manager()
    pass

def main():
    input("1,后台管理 ; 2,登录")
    if inp == '1':
        manager()
    elif inp == '2':
        username = input("username:")
        pwd = input("password:")
        login(username,pwd)



'''
def outer(func):
    def inner(*args,**kwargs):
        print('before')
        r = func(*args,**kwargs)
        print('after')
        return r
    return inner

# @+函数名
#功能
#1, 自动执行outer 函数 并且将其下面的函数名f1当作参数传递
#2，将outer函数的返回值 重新赋值给f1

# 装饰器   在原函数之前执行  原函数之后执行  ，原函数正常执行
@outer
def f1(arg):
    print(arg)
    return "xxx"

@outer   #多个参数传递  *args,**kwargs
def f2(arg1,arg2):
    print("F2")
    
    
'''