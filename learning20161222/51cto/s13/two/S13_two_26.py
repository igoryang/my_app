#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
26--实例 随机验证码 2
'''

#随机验证码

import random

li = []
for i in range(6):
    r = random.randrange(0,5)
    if r == 2 or r == 4 :
        num = random.randrange(0,10)
        li.append(str(num))
    else:
        temp = random.randrange(65,91)
        c = chr(temp)
        li.append(c)

result = "".join(li)
print(result)