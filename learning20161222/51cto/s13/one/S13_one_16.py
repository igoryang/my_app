#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
if else 语句
'''
# user = 'admin'
# passwd = 'admin'
#
# username = input("input your name:")
# password = input("password:")
#
# if user == username:
#     print("username is correct...")
#     if password == passwd:
#         print("welcome login...")
#     else:
#         print("password is invalid...")
# else:
#     print("username is error!")

'''
user = 'admin'
passwd = 'admin'

username = input("input your name:")
password = input("password:")

if user == username and password == passwd:
    print("Welcome login")

else:
    print("Invalid username or password!")

'''

age = 22
guess_num = int(input("input your guess num:"))

if guess_num == age:
    print("Got it")
elif guess_num > age:
    print("big")
else:
    print("small")