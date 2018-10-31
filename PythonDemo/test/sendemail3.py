#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

import urllib2,json,sys

reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8') #这个是解决合成中文文本的时候，Unicode和utf-8编码问题的，可以尝试注释掉会不会报错

hemingming = 'hemingming@yftech.com'
wenhuawei = 'wenhuawei@yftech.com'
xupeiqiang = 'xupeiqiang@yftech.com'
libin = 'libin@yftech.com'
zengxianghua = 'zengxianghua@yftech.com'
shanjinhua = 'shanjinhua@yftech.com'
chenguangwen = 'chenguangwen@yftech.com'
huangyanqiang = 'huangyanqiang@yftech.com'
zhizhongbiao = 'zhizhongbiao@yftech.com'
qiyanfu = 'qiyanfu@yftech.com'
huangwencheng='huangwencheng@yftech.com'




my_sender='29867547@qq.com'    # 发件人邮箱账号
my_pass = 'xhebhmsjkackbgff'   # 发件人邮箱密码
my_user='Android Group'      # 收件人邮箱账号，我这边发送给自己
group='yftech.com'

def mail():
    ret=True
    try:
        content='''大佬们，可以提交周报了~ \n  
                 以下是备注:\n
                 每周3下班前提交周报，周报填写在SVN： \n
                http://192.168.29.71/svn/YFIndash/Project/Pm2VM/braches/K257/doc/开发一部软件2组2018工作周报汇总.xlsx  \n
                此外: \n
                公司要求每人把开发的经验集合到一起，方便大家共同学习进步。经验可以是平时的解决bug的心得、开发心得或者客诉问题等等 \n
                要求如下： \n
                1、每人每月更新一次，最低要求一条； \n
                2、更新时间截止到月底 \n
                http://192.168.29.71/svn/YFIndash/Project/Pm2VM/braches/K257/doc/软件设计经验库/设计FMEA经验库(软件).xls '''

        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From']=formataddr(["李斌",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr([my_user,group])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        # 邮件的主题，也可以说是标题
        msg['Subject']="激情提示"
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[hemingming,wenhuawei,xupeiqiang,libin,zengxianghua,shanjinhua,chenguangwen,huangyanqiang,zhizhongbiao,qiyanfu,huangwencheng,],msg.as_string())
        #server.sendmail(my_sender, [libin, ], msg.as_string())
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret
 
ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
