#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# -*- coding:utf-8 -*-
# author Y.G
__author__ = 'YangGang'

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
        return False
    else:
        return True


'''
from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header

def send_email(SMTP_host, from_addr, password, to_addrs, subject, content):
    email_client = SMTP(SMTP_host)
    email_client.login(from_addr, password)
    # create msg
    msg = MIMEText(content,'plain','utf-8')
    msg['Subject'] = Header(subject, 'utf-8')#subject
    msg['From'] = 'main<xxxxx@163.com>'
    msg['To'] = "xxxxx@126.com"
    email_client.sendmail(from_addr, to_addrs, msg.as_string())

    email_client.quit()

if __name__ == "__main__":
    send_email("smtp.163.com","xxxxx@163.com","password","xxxxx@126.com","test","hellow")
'''