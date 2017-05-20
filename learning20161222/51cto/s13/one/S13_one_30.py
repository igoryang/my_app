#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

'''

完美的购物车程序

#购物小程序
用户启动程序后打印商品列表
允许用户选择购买商品
允许用户不断的购买各种商品

购买时检测  余额是否足够，如果足够，直接扣款，否则打印余额不足

允许用户主动退出 程序  退出 时打印已经购买商品列表

'''

salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
else:
    exit("Invaild data type...")


welcom_msg = "Welcome to Big  Shopping Mall"

print(welcom_msg.center(50,'-'))

product_list = [
    ('Iphone',5888),
    ('Mac Air',8000),
    ('Mac Pro',9000),
    ('XiaoMi 2',19.9),
    ('Coffee',30),
    ('Tesla',820000),
    ('Bike',700),
    ('Cloth',200)
]
shop_car = []

exit_flag = False  #启始符 标位符
while not exit_flag:  #while exit_flag is not True:
    # for product_item in product_list:
    #     p_name,p_price = product_item
    print("product list".center(50,'-'))
    # for p_name,p_price in product_list:
    #     print(p_name,p_price)
    for item in enumerate(product_list): #enumerate 枚举
         index = item[0]
         p_name = item[1][0]
         p_price = item[1][1]
         print(index,'.',p_name,p_price)

    user_choice = input("[q = quit,c = check]What do you want to buy?")
    if user_choice.isdigit(): #肯定是选择商品
        user_choice = int(user_choice)
        if user_choice < len(product_list):
            p_item = product_list[user_choice]
            if p_item[1] <= salary: #买的起
                shop_car.append(p_item)  #放入购物车
                salary -= p_item[1]   #减钱
                print("Added [%s] ,into shop car,your current balance is \033[31;1m[%s]\033[0m"%(p_item,salary))
            else:
                print("your balance is [%s],cannot buy this ..."%salary)

    else:
        if user_choice == 'q' or user_choice =='quit':
            print("purchased products list".center(40,'*'))
            for item in shop_car:
                print(item)
            print("End".center(40,'*'))
            print("Your balance is \033[32;1m[%s]\033[0m"%salary)  #\033[32;1m xxx \033[0m  颜色物理格式
            exit_flag = True
