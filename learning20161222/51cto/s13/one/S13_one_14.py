#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

#常用模块初识   getpaas 模块  linux下使用
#import 导入模块方法   ogetpass , os ,sys  , tab.py(自己写模块)

import S13_one_13


# import sys,os
# print(sys.path)
# print(os.system("dir"))

'''
import getpass
username = input("username:")
password = getpass.getpass("password:")
print(username,password)
'''
#import os
#os.system("ipconfig")
#os.system("dir")
#os.mkdir("dir")
#cmd_res = os.popen("df -h").read()
#print(cmd_res)

'''
python tab补全模块
tab.py
#!/usr/bin/env python
#python startup file
import sys
import readline
import rlcompleter
import atexit
import os
#tab commpletion
readline.parse_and_bind('tab:complete')
#history file
histfile = os.path.join(os.environ['HOME'],'.pythonhistory')
try:
    readline.read_history_file(histfile)
except IOError:
    pass
atexit.register(readline.write_history_file,histfile)
del os, histfile, readline, rlcompleter

for Linux

'''
