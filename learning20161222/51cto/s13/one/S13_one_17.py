#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'


# for i in range(10):
#     print(i)


age = 33

for i in range(10):
    if i <3:

        guess_num = int(input("input your guess num:"))

        if guess_num == age:
            print("Got it")
            break
        elif guess_num >age:
            print("Big")
        else:
            print("small")
    else:
        print("error 3 please waiting")
        break
