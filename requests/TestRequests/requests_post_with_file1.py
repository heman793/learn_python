# -*- coding:utf-8 -*-

import requests
import json

host = "http://httpbin.org/"
endpoint = "post"

url = ''.join([host,endpoint])

#普通上传
files = {
            'file':open('test.txt','rb')
        }

r = requests.post(url,files=files)
print (r.text)