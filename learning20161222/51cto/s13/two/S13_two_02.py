#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
函数之 函数的返回值
'''
#调用发送邮件功能模块
# import sendmail
# ret = sendmail.sendmail()
# print("sendmail sucessful is %s"%ret)

def f1():
    print(123)
    #在函数中，一旦执行return 函数执行过程立即终止
    return "111"
    print(456)

r = f1()
print(r)