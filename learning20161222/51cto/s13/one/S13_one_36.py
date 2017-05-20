#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''

先做需求分析---》流程图--》实现功能--》测试完善==》交付产品--修复bug和不断完善
set 集合练习题

old__dict = {
  "1#":8,
   "2#":4,
   "3#":2
}

new__dict = {
   "1#":4,
   "2#":8,
   "4#":2
}

#应该删除哪几个槽位
   1，old_dict 存在，new不存在, key
   old_keys = old_dict.keys()
   old_set = set(old_keys)

   new_keys = new_dict.keys()
   new_set = set(new_keys)



#应该更新哪几个槽位
#应该增加哪几个槽位
'''

old_dict = {
   "1#":8,
   "2#":4,
   "3#":2
}

new_dict = {
   "1#":4,
   "2#":8,
   "4#":2
}

new_set = set(new_dict.keys())
old_set = set(old_dict.keys())

remove_set = old_set.difference(new_set)
add_set = new_set.difference(old_set)
update_set = old_set.intersection(new_set)

print(remove_set)
print(add_set)
print(update_set)