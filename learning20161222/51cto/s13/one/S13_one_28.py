#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'


'''
海枯石烂死循环


while loop


'''

count = 0
while True:
    count +=1
    if count > 50 and count < 60:
        continue
    print("xxxxx.....xxxxxx",count)
    #count +=1
    if count == 100:
        print("oh ",count)
        break