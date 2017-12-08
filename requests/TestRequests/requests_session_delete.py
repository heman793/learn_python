# -*- coding:utf-8 -*-

import requests
import json

host = "http://httpbin.org/"
endpoint = "headers"

url = ''.join([host,endpoint])

header1 = {"testA":"AAA"}
header2 = {"testB":"BBB"}

s = requests.session()    #初始化一个session对象
s.headers.update(header1)   #已经存在于服务中的信息
r = s.get(url,headers=header2) #发送新的信息

print r.text

print '--------'

s.headers['testA'] = None   #删除会话里的信息testA
r1 = s.get(url,headers = header2)
print r1.text

