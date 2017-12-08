# -*- coding:utf-8 -*-

import requests
import json

host = "http://httpbin.org/"
endpoint = "post"

url = ''.join([host,endpoint])

#流式上传
with open( 'test.txt' ) as f:
	r = requests.post(url,data = f)

print (r.text)


