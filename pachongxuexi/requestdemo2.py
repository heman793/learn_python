import requests
import json

def get_method():
	url = 'https://api.github.com/some/endpoint'
	params = {'wd':'python'}
	r = requests.get(url,params=params)

	print r.text
	print r.url
	print r.status_code
	print r.request.headers


def post_method():
	url = 'https://api.github.com/some/endpoint'
	data = {'comment':'test post'}
	r = requests.post(url,data=data)

	print r.text
	print r.url
	print r.status_code
	print r.headers

def post_method_json():
	url = 'https://api.github.com/some/endpoint'
	r = requests.post(url,data=json.dumps({'some':'thing'}))

	print r.json()

def post_setheader():
	url = 'https://api.github.com/some/endpoint'
	data = {'some':'thing'}
	headers = {'USER-Agent':'TEST',
			'content-type':'application/json'}
	r = requests.post(url,data=data,headers=headers)
	print r.text
	print r.request.headers


if __name__ == '__main__':
	print "please enter number:"
	input = raw_input('get_method:1,post_method:2,post_method_json:3,post_setheader:4:')
	if input == '1':
		get_method()
	elif input == '2':
		post_method()

	elif input == '3':
		post_method_json()
	else:
		post_setheader()





