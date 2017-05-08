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
            #pass  占位符
        else:
            print("bye")
            break
    counter +=1