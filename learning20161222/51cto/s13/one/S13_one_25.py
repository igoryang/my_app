#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
国际歌
do you hear the people sing
悲惨世界

列表的语法和使用2

'''

name = ['ami','akk','bill','bili','kim','min']

name.insert(-1,'ds2')
name.insert(4,'ds4')

name2 =name[2:7]

print(name)
print(name2)

name.remove('min')
#print(name.remove('min'))
print(name)
#del quanju shanchu
del name[4:6]
print(name)

name[0] = "ami(zuzhang)"
print(name)

print(name[0:-1:1])
print(name[::2])
print('ami' in name)
print('bill' in name)
print(name.count('bill'))
print(name.index('bill'))

name3 = [3,4,9,5,333,999,'ak','pk',999,332,'am','pm',9]

if 9 in name3:
    num_of_ele = name3.count(9)
    print(num_of_ele)
    position_of_ele = name3.index(9)
    print(position_of_ele)
    #name3[position_of_ele] = 888
    print("9 acount is %s \n9 is positon %s" % (num_of_ele,position_of_ele))

name4 = [3,4,9,5,333,999,'ak','pk',999,332,'am','pm',9]

position = name4.index(333)
print(positon)

for i in range(name4.count(9)):
    ele_index = name4.index(9)
    name4[ele_index] = 999999999
print(name4)

name5 = [3,4,9,5,333,999,'ak','pk',999,332,'am','pm',9]
name6 = [6,66,6666]
name6.append(777)  #追加
name5.extend(name6)  #扩展新列表
print(name5)
name6.reverse()  #反转
print(name6)
name6.sort()  #排序
print(name6)
name6.pop() #移除
print(name6)

name7 = [3,4,9,5,333,999,'ak','pk',999,332,'am','pm',9]

name8 = name7.copy() #copy 只COPY第一层
print(name7)
print(name8)

name9 = [3,4,9,5,[333,999],'ak','pk',999,332,'am','pm',9]
name10 = name9.copy()

name9[0] = 333
name9[4][0] = 444
print(name9)
print(name10)

# import copy 模块
# copy.copy() === name9.copy()    软链接
# copy.deepcopy()  #深度COPY      硬链接

