#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'
'''

'''

def fetch(backend):
    result = []
    with open("HA.cfg",'r',encoding="utf-8") as f:
        flag = False
        for line in f:
            # print(line)
            if line.strip().startswith("backend") and line.strip() == "backend " + backend:
                flag = True
                continue
            if flag and line.strip().startswith("backend") :
                flag = False
                break
            if flag and line.strip():
                result.append(line.strip())
    return result
# ret = fetch('www.oldboy.org')
# print(ret)

def add(backend,record):
    # pass
    #思路一  先检查记录是否存在，读一遍；
    record_list = fetch(backend)
    if not record_list:
        with open("HA.cfg",'r') as old,open("new.cfg",'r') as new:
            for line in old:
                new.write(line)
            new.write("\nbackend " + backend + "\n")
            new.write(" "*8 + record_list + "\n")
    else:
        pass

    # print(record_list)
ret_add = add('www.oldboy.org',"xxxx")
# s = "[11,22,33,44]"
# s1 = '{"k1":"v1"}'    #里面的字符串必须用"" s1 = '{"k1":"v1"}'
# print(s,type(s))
# print(s1,type(s1))
#
# # json 将一个字符串，转换成python的基本数据类型  [],{}
# import json
# n = json.loads(s)
# n1 = json.loads(s1)
# print(n,type(n))
# print(n1,type(n1))