# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText


'''发送邮件，不带附件'''
def sendmail():

    # --------1、发件相关参数--------
    smtp_server = "smtp.163.com"        # 发件服务器
    port = 0                           # 端口
    sender = "puresoul2010@163.com"    # 账号
    pwd = "sunshine0923..."               # 密码
    receiver = "648363313@qq.com"      # 接收人


    # --------2、编辑邮件内容 -------
    subject = "接口自动化测试报告"
    body = "<p>test content</p>"
    msg = MIMEText(body, "html", "uft-8")   # 定义邮件正文为html格式
    msg['from'] = sender
    msg['to'] = receiver
    msg['subject'] = subject

    # --------3、发送邮件 -------
    smtp = smtplib.SMTP()
    smtp.connect(smtp_server)    # 连接服务器
    smtp.login(sender, pwd)     # 登录
    print "start..."
    smtp.sendmail(sender, receiver, msg.as_string())    # 发送
    print "end"
    smtp.quit()                 # 退出


if __name__ == "__main__":
    sendmail()