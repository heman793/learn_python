# -*- coding:utf-8 -*-

import requests
import json


host = "http://httpbin.org/"
endpoint = "post"

url = ''.join([host,endpoint])

headers = {"User-Agent":"test request headers"}

# r = requests.post(url)
r = requests.post(url,headers=headers)

#response = r.json()

print (r.text)