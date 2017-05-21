#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

# 函数之基本参数

#def sendmail(arg):  arg是形式参数

#ret = sendmail(ak) #ak 是 实际参数

#1,普通参数
#2，默认参数 放到最后
#3.指定参数

def sendmail(addr,content,xx = "ok"):  #addr 收件箱邮箱地址
    #pass
    try:
        import smtplib #发邮件模块
        from email.mime.text import MIMEText
        from email.utils import formataddr

        #msg = MIMEText('邮件内容！你好！','plain','utf-8')
        msg = MIMEText(content,'plain','utf-8')
        msg['From'] = formataddr(["杨岗",'yanggang1025@126.com'])
        #msg['To'] = formataddr(["Igor",'345223200@qq.com'])
        msg['To'] = formataddr(["Igor",addr])
        msg['Subject'] = "主题- Python -sendmail"

        server = smtplib.SMTP("smtp.126.com",25)
        server.login("yanggang1025@126.com","yg1314520")
        server.sendmail('yanggang1025@126.com',[addr,],msg.as_string())
        server.quit()
    except:
        return False
    else:
        return True


while True:
    em = input("请输入收件邮箱地址：")
    content = input("请输入发送内容：")
    print(em)
    print(content)
    result = sendmail(em,content)
    if result == True:
        print("发送成功！")
    else:
        print("发送失败")