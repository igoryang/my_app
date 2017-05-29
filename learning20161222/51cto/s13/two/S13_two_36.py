#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
36--作业剖析

HA配置文件  增，删，改，查

1,文件全局加载内存 readlines

2,一行一行读取   for line in f:
                  print line

'''

# f = open("HA.cfg","r+",encoding="utf-8")
# f.read()
# for ha_config in f:
#     print(ha_config)
# with open("HA.cfg","r+",encoding="utf-8") as f:
#     for ha_config in f:
#         print(ha_config)

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
ret = fetch('www.oldboy.org')
print(ret)







