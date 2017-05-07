#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
基本if判断
'''
user = 'admin'
passwd = '123'

username = input("username:")
password = input("password:")
if user == username:
    print("username is right!")
    break
    if passwd == password:
        print("You can login")
else:
    print("login error")
#     else:
#         print("password is erro")
#         break
# else:
#     print("username is  erro")