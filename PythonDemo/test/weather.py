#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

import urllib2, json, sys

reload(sys)  # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')  # 这个是解决合成中文文本的时候，Unicode和utf-8编码问题的，可以尝试注释掉会不会报错


def getWeather():
    # 调用和风天气的API
    url = 'https://api.seniverse.com/v3/weather/daily.json?key=ageqb19s4vraf28i&location=dongguan&language=zh-Hans&unit=c&start=0&days=3'
    # 用urllib2创建一个请求并得到返回结果
    req = urllib2.Request(url)
    response = urllib2.urlopen(req).read()
    result = json.loads(response)
    # newdata=json.dumps(resp,ensure_ascii=False)
    data = result['results'][0]
    city = data['location']['name']
    # 暂且解析今天的天气,后面的天气怎么循环解析?
    today = data['daily'][0]
    text_day = today['text_day']
    text_night = today['text_night']
    low = today['low']
    high = today['high']
    today_weather = "%s今天天气:白天%s,夜晚%s,最低气温%s℃,最高气温%s℃" % (city, text_day, text_night, low, high)
    print today_weather
    return today_weather


my_sender = '29867547@qq.com'  # 发件人邮箱账号
my_pass = 'xhebhmsjkackbgff'  # 发件人邮箱密码
my_user = '29867547@qq.com'  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:
        msg = MIMEText(getWeather(), 'plain', 'utf-8')
        msg['From'] = formataddr(["colin", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["colin", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "今日资讯"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件,可以多个接受者
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
