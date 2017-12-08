# -*- coding: utf-8 -*-
# get bugs for F project test tool 

import requests
import json

url = 'http://10.20.11.218:8222/redmine/projects/f_project/issues.json?query_id=452'

response = requests.get(url,auth=('heman793','123456'))

print 'response.status_code:',response.status_code
print 'response.text:\n',response.text

