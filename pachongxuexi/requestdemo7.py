import requests

#r = requests.get('https://kyfw.12306.cn/otn/',verify=True)
r = requests.get('https://kyfw.12306.cn/otn/',verify=False)
print r.text
print r.status_code

