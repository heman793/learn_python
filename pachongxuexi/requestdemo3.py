# _*_ coding=utf-8 _*_

import requests

def test1():
	url = 'https://api.github.com'
	params = {'ip':'1.1.1.1'}
	try:
		r = requests.get(url,params=params,timeout=3)
		r.raise_for_status()	#如果响应状态码不是200，主动抛异常
	except requests.RequestExctpiton as e:
		print e
	else:
		result = r.json()
		print type(result)
		print result
		print r.status_code
if __name__ == '__main__':
	test1()
