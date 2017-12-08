import json
import requests

url = 'http://httpbin.org/post'
data = {'some':'thing'}
#r = requests.post(url,data=data)
r = requests.post(url,data=json.dumps(data))
print r.text
