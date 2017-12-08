# -*- coding:utf-8 -*-
#获取cookie

import requests
import json

# host = "http://httpbin.org/"
# endpoint = "cookies"
#
# url = ''.join([host,endpoint])

url = "https://www.baidu.com/"
r = requests.get(url)

#将RequestsCookieJar转换成字典
c = requests.utils.dict_from_cookiejar(r.cookies)

print r.cookies
print c

for a in r.cookies:
    print a.name,a.value