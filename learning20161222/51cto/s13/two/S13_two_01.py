#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'


'''
2-Python高级自动化开发工程师微职位:函数和常用模块（培训班课程，请勿购买）98
课程目录记笔记提问题
1 函数之初识函数23:33
2 函数之函数的返回值10:14
3 函数之函数的返回值 201:30
4 函数之基本参数25:27
5 函数之动态参数09:31
6 函数之动态参数 213:38
7 利用动态参数实现format功能08:12
8 函数之内容补充29:22
9 函数之内容补充 256
10 实例：函数式编程实现登录和注册17:12
11 三元运算02:00
12 瞎扯淡13:42
13 lambda表达式06:25
14 内置函数13:4
15 内置函数 208:31
16 内置函数 304:57
17 文件操作之打开模式19:55
18 文件操作之打开模式 219:24
19 文件操作之文件操作功能14:17
20 文件操作之with处理上下文08:25
21 本节作业08:49
22 今日内容介绍02:04
23 上节内容回顾11:25
24 内置函数补充06:48
25 实例：随机验证码06:57
26 实例：随机验证码 205:50
27 内置函数补充 222:38
28 内置函数补充 314:29
29 内置函数补充 410:57
30 内置函数补充 505:55
31 内置函数补充 606:50
32 内置函数补充 710:08
33 内置函数补充 822:16
34 内置函数补充 903:37
35 Alex鸡汤18:00
36 上节作业剖析24:56
37 上节作业剖析 226:30
38 上节作业剖析 321:38
39 装饰器概要13:38
40 装饰器流程剖析储备知识04:25
41 装饰器流程剖析17:57
42 装饰器流程剖析 206:23
43 装饰器流程剖析之返回值12:43
44 装饰器流程剖析之参数04:09
45 装饰器流程剖析之参数06:14
46 实例：用户管理程序13:28
47 今日作业07:39
48 上节作业概况03:46
49 今日内容介绍03:35
50 上节内容回顾05:33
51 双层装饰器实现用户登录和权限验证12:23
52 双层装饰器实现用户登录和权限验证 215:31
53 多层装饰器原理04:02
54 python字符串格式化25:26
55 python字符串格式化 224:44
56 python生成器17:17
57 基于生成器实现range功能07:00
58 Alex鸡汤来袭31:45
59 python迭代器08:28
60 思考题01:02
61 python函数递归13:49
62 python模块介绍13:56
63 python模块介绍 223:26
64 安装第三方模块07:48
65 python序列化之json07:31
66 基于天气API获取天气相关JSON数据05:47
67 python序列化之json 208:41
68 扩展：博客小知识分享05:11
69 python序列化之pickle10:35
70 python时间处理之time模块37:21
71 python日志处理之logging模块40:08
72 今日作业以及代码目录23:00
73 今日内容概要01:19
74 ATM作业分析32:30
75 利用递归实现阶乘实例07:28
76 Python反射23:08
77 Python反射 218:36
78 Python反射 307:19
79 Python模块模块中特殊变量18:05
80 Python模块模块中特殊变量 208:23
81 Python之sys模块14:11
82 Python之sys模块 201:46
83 Python之os模块05:51
84 Python之加密模块08:13
85 Python之正则表达式30:20
86 Python之正则表达式 233:10
87 Python之正则表达式之分组19:31
88 本周作业13:58
89 今日内容概要01:13
90 计算器作业分析07:13
91 configparser模块15:31
92 XML模块32:15
93 XML模块 204:44
94 XML模块 315:54
95 XML模块 425:27
96 Alex鸡汤29:43
97 shutil模块以及压缩包处理28:05
98 subprocess模块15:18


================================================================================================
常用函数
2. Built-in Functions¶
The Python interpreter has a number of functions and types built into it that are always available. They are listed here in alphabetical order.

Built-in Functions
abs()	dict()	help()	min()	setattr()
all()	dir()	hex()	next()	slice()
any()	divmod()	id()	object()	sorted()
ascii()	enumerate()	input()	oct()	staticmethod()
bin()	eval()	int()	open()	str()
bool()	exec()	isinstance()	ord()	sum()
bytearray()	filter()	issubclass()	pow()	super()
bytes()	float()	iter()	print()	tuple()
callable()	format()	len()	property()	type()
chr()	frozenset()	list()	range()	vars()
classmethod()	getattr()	locals()	repr()	zip()
compile()	globals()	map()	reversed()	__import__()
complex()	hasattr()	max()	round()
delattr()	hash()	memoryview()	set()
abs(x)

================================================================================================
'''

#函数之初识函数
# 函数  def
# -自定义函数
# -内置函数

name = "alex"
print(name)

#def 创建函数  函数名称：f1()  ：结尾
#1，def 关键字 创建函数
#2,数了数名
#3，()
#4，功能  函数体   默认不补执行  调用函数体才执行
#5，返回值

# def f1():
#     pass

def sendmail():
    #pass
    try:
        import smtplib #发邮件模块
        from email.mime.text import MIMEText
        from email.utils import formataddr

        msg = MIMEText('邮件内容！你好！','plain','utf-8')
        msg['From'] = formataddr(["杨岗",'yanggang1025@126.com'])
        msg['To'] = formataddr(["Igor",'345223200@qq.com'])
        msg['Subject'] = "主题- Python -sendmail"

        server = smtplib.SMTP("smtp.126.com",25)
        server.login("yanggang1025@126.com","yg1314520")
        server.sendmail('yanggang1025@126.com',['345223200@qq.com',],msg.as_string())
        server.quit()
    except:
        return False  #发送失败
    else:
        return True   #发送成功


ret = sendmail() #调用函数 执行函数体
print("sendmail is %s"%ret)

if ret == True:
    print("发送成功！！")
else:
    print("发送失败！")