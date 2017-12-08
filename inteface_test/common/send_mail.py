# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendattachmail(file_path):
    '''发送邮件，带附件'''
    # --------1、发件相关参数--------
    smtp_server = "smtp.163.com"        # 发件服务器
    # port = 0                           # 端口
    sender = "puresoul2010@163.com"    # 账号
    pwd = "sunshine0923..."               # 密码
    receiver = "648363313@qq.com"      # 接收人

    # --------2、编辑邮件内容 -------
    # 读文件
    # file_path = os.path.join(os.getcwd(), "result.html")
    # print file_path
    with open(file_path, 'rb') as f:
        mail_body = f.read()

    msg = MIMEMultipart()
    msg['from'] = sender
    msg['to'] = receiver
    msg['subject'] = "接口自动化测试报告"

    # 正文
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)

    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="Inteface_test_report.html"'
    msg.attach(att)

    # --------3、发送邮件 -------
    smtp = smtplib.SMTP()
    smtp.connect(smtp_server)    # 连接服务器
    smtp.login(sender, pwd)     # 登录
    print "start send mail..."
    smtp.sendmail(sender, receiver, msg.as_string())    # 发送
    print "end send..."
    smtp.quit()

if __name__ == "__main__":
    sendattachmail()