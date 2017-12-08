#!/usr/bin/python
# _*_ coding: utf-8 _*_
#模拟登录知乎

import requests
from lxml import etree

url = 'https://www.zhihu.com/#signin'

#伪装成浏览器
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

response = requests.get(url,headers=headers)
print 'url:',response.status_code

#获取页面隐藏变量 _xsrf 的值
html = etree.HTML(response.text)
_xsrf = html.xpath('//input[@name="_xsrf"]/@value')[0]

print _xsrf

#开始模拟登录
login_url = 'https://www.zhihu.com/login/email'
data = {
	'email':'puresoul2010@163.com',
	'password':'870502',
	'captcha_type':'cn',
	'_xsrf':_xsrf
	}

res = requests.post(url=login_url,data=data,headers=headers)
print 'login_url:',res.status_code
print res.text

print 'res type:',type(res)
print res.json()['msg']
