# -*- coding:utf-8 -*-

import requests
import json


host = "http://httpbin.org/"
endpoint = "get"

url = ''.join([host,endpoint])

headers = {"User-Agent":"test request headers"}
params = {"show_env":"1"}

r = requests.get(url)
r = requests.get(url,headers=headers,params=params)

#response = r.json()

print (eval(r.text))['headers']['User-Agent']
print r.url
