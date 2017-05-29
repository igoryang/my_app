#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'
'''
HA
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

def add()
    pass