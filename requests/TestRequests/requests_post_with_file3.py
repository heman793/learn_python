# -*- coding:utf-8 -*-

import requests
import json

host = "http://httpbin.org/"
endpoint = "post"

url = ''.join([host,endpoint])

#多文件上传
files = [
    ('file1',('test.txt',open('test.txt', 'rb'))),
    ('file2', ('test.png', open('test.png', 'rb')))
	]

r = requests.post(url,files=files)
print (r.text)