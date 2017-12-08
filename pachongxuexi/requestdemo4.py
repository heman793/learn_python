import requests

r = requests.get('http://www.baidu.com/')

print (r.cookies['BDORZ'])
print (tuple(r.cookies))
