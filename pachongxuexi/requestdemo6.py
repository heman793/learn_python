import requests

url = 'http://httpbin.org/post'
files = {'file':open('test.txt','rb')}
r = requests.post(url,files=files)

print r.text


