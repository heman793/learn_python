# -*- coding: utf-8 -*-
# get a bug info

import requests
import json

url = 'http://10.20.11.218:8222/redmine/issues/47938.json'

response = requests.get(url,auth=('heman793','123456'))

data = response.text
print 'data type:',type(data)

print 'response.status_code:',response.status_code
print 'response.text:\n',data
ddata = json.loads(data)
print 'ddata type:',type(ddata)

print 'issue_ID:',ddata["issue"]["id"]
