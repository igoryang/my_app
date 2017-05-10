#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
.pyc是什么鬼？ 内存中的 PyCodeObject    字节码文件：二进制文件

固定的.py文件 补引用 会生成固定.pyc的文件 加快执行

__pycache__/*.pyc  python3
*.pyc  __pycache__  python2

编译型语言   C ; C++
解释弄语言   Ruby;Python;

JAVA --编译--解释   虚拟机JVM   Eclipse -IDE


Python Java C#  一门基于虚拟机的语言  Pycharm-IDE


Python 是先编译 --再解释的语言

'''

username = input("input username:")
print(username)