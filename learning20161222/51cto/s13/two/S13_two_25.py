#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
25---随机验证码
'''

#ASCii
#65--90 A-Z;  97--122 a-z;  48--57  0-9;
r = chr(65)
print(r)

n = ord("B")
print(n)

#随机验证码

import random

li = []
for i in range(6):
    temp = random.randrange(65,91)
    c = chr(temp)
    li.append(c)

result = "".join(li)
print(result)
