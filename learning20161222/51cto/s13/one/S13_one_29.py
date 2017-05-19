#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''
NB数据类型这字典的使用

字典 无序
dict = {key1:value1，key2:value2,.....}   字典可以嵌套字典
dict = {
    key:{
        key:value,
        key2:value2
    },
    key2:{
        key:value,
        key2:value2
    }
}

'''
name = [1,3,4,5,5,6,7,8,'admin']
Position = name.index("admin")
print(Position)

id_db = {

    342222198712010011:{
        'name':"Alex Li",
        'age':22,
        'addr':'shandong'
    },
    342222198712010012:{
        'name': "Alex Tw",
        'age': 32,
        'addr': 'Shanxi'
    },
    342222198712010013:{
        'name': "Alex St",
        'age': 42,
        'addr': 'DongBei'
    }

}

dic2 = {
    342222198712010013: {
        'name': "Alex St",
        'age': 44,
        'addr': 'DongBei'
    },
    342222198712010014: {
        'name': "Alex Ft",
        'age': 42,
        'addr': 'DongBei'
    }
}

print(id_db)   #key：value  key是唯一的
print(id_db[342222198712010013])

id_db[342222198712010013]['name'] = "HAHA"  #修改

print(id_db[342222198712010013])

id_db[342222198712010013]['qq_office_nu'] = 348888888  #插入 新增

id_db[342222198712010013].pop("name")  #删除 pop  del

v = id_db.get(342222198712010013)  #获取
print(v)
print(id_db[342222198712010013])

id_db.update(dic2)  #dic2 to update dic1  相同key被更新，新的插入
print(id_db)

tuple_id_db = id_db.items()  #一般不用 字典转元组
print(tuple_id_db)

print(id_db.values())
print(id_db.keys())
# id_db.has_key()   key in id_db
id_db.setdefault(1,'111')  #取key 有则取出， 如无 则None 或者增加一条记录
print(id_db)

# id_db.fromkeys([1,2,4,5],'abc') #坑 此处有坑
# dict.fromkeys([1,2,4,5],'abc') #坑 此处有坑
#dict.popitem() 随机删除  慎用 不要用

#循环字典
# for k,v in id_db.items():  # 效率低 不要这样写
#     print(k,v)
for key in id_db:  #应该 一定要这样写字典循环
    print(key)
    print(key,id_db[key])