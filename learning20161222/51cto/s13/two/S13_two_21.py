#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
本节 作业
文件句柄 = open('文件路径', '模式')

打开文件的模式有：

r ，只读模式【默认】
w，只写模式【不可读；不存在则创建；存在则清空内容；】
x， 只写模式【不可读；不存在则创建，存在则报错】
a， 追加模式【可读；   不存在则创建；存在则只追加内容；】
"+" 表示可以同时读写某个文件

r+， 读写【可读，可写】
w+，写读【可读，可写】
x+ ，写读【可读，可写】
a+， 写读【可读，可写】
 "b"表示以字节的方式操作

rb  或 r+b
wb 或 w+b
xb 或 w+b
ab 或 a+b
 注：以b方式打开时，读取到的内容是字节类型，写入时也需要提供字节类型

修改配置文件 HA

www.cnblogs.com/wupeiqi/articles/4950799.html
同时打开2个文件：
生成一个新的文件：

with open('ha1','r',encoding="utf-8") as f1,open('ha2','w',encoding="utf-8") as f2: #python 2.6以后 支持 打开多个文件
    #pass
    #times = 0
    for line in f1: #读出f1中的
        new_str = line.replace("abc","Replace")
        f2.write(new_str)


1，获取HA记录   如输入：www.oldboy.org
2，添加HA记录   如： {"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}
3，删除HA记录  如： {"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}




如果想要将用户输入的内容转换下格式，

1
2
'{"k1":123, "k2": "wupeiqi"}'       字符串转换成字典类型
"[11,22,33,44]"                     字符串转换成列表类型
################# 当当当当，python的json模块可以搞搞搞 !!!!!!! #################

json模块
json模块的作用之一：根据字符串书写格式，将字符串自动转换成相应格式

import json
inp_str = "[11,22,33,44]"
inp_list = json.loads(inp_str) # 根据字符串书写格式，将字符串自动转换成 列表类型


inp_str = ' {"k1":123, "k2": "wupeiqi"} '  # 正确的输入      切记，内部必须是 双引号 ！！！
#inp_str = " {'k1':123, 'k2': 'wupeiqi'}"   # 错误的输入
inp_dict = json.loads(inp_str) # 根据字符串书写格式，将字符串自动转换成 字典类型
'''
