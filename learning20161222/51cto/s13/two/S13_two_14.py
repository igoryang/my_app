#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
内置函数

Python所有的内置函数
 	 	Built-in Functions
abs()	divmod()	input()	open()	staticmethod()
all()	enumerate()	int()	ord()	str()
any()	eval()	isinstance()	pow()	sum()
basestring()	execfile()	issubclass()	print()	super()
bin()	file()	iter()	property()	tuple()
bool()	filter()	len()	range()	type()
bytearray()	float()	list()	raw_input()	unichr()
callable()	format()	locals()	reduce()	unicode()
chr()	frozenset()	long()	reload()	vars()
classmethod()	getattr()	map()	repr()	xrange()
cmp()	globals()	max()	reversed()	zip()
compile()	hasattr()	memoryview()	round()	__import__()
complex()	hash()	min()	set()	apply()
delattr()	help()	next()	setattr()	buffer()
dict()	hex()	object()	slice()	coerce()
dir()	id()	oct()	sorted()	intern()

'''
'''
常用的内置函数
内置方法	 说明
 __init__(self,...)	 初始化对象，在创建新对象时调用
 __del__(self)	 释放对象，在对象被删除之前调用
 __new__(cls,*args,**kwd)	 实例的生成操作
 __str__(self)	 在使用print语句时被调用
 __getitem__(self,key)	 获取序列的索引key对应的值，等价于seq[key]
 __len__(self)	 在调用内联函数len()时被调用
 __cmp__(stc,dst)	 比较两个对象src和dst
 __getattr__(s,name)	 获取属性的值
 __setattr__(s,name,value)	 设置属性的值
 __delattr__(s,name)	 删除name属性
 __getattribute__()	 __getattribute__()功能与__getattr__()类似
 __gt__(self,other)	 判断self对象是否大于other对象
 __lt__(slef,other)	 判断self对象是否小于other对象
 __ge__(slef,other)	 判断self对象是否大于或者等于other对象
 __le__(slef,other)	 判断self对象是否小于或者等于other对象
 __eq__(slef,other)	 判断self对象是否等于other对象
 __call__(self,*args)	 把实例对象作为函数调用
'''

'''
abs(-9)  #绝对值
bool(1)  #0，None,"",[],()
all(1,2,3,4) #所有为真，才为真
any(0,1,2) #只要有真就为真
ascii(1)#自动执行对象的__str__方法

bin(10)  #10--》2进制  0b
oct(10) #10--》8进制   0o
hex(10)  #10--》16进制  0x

'''
