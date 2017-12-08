#!/usr/bin/python
# -*- coding: utf-8 -*-
#爬取糗事百科
#2017-6-11


import urllib
import urllib2
import re

page = 1
url = 'https://www.qiushibaike.com/hot/page/' + str(page) + '/?s=4990275'
#print url

#make browser
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
headers = {'User-Agent':user_agent}

try:
	request = urllib2.Request(url,headers=headers)
	response = urllib2.urlopen(request)
	content = response.read().decode('utf-8')
	#print content
	pattern = re.compile(r'<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?content">.*?<span>(.*?)</span>.*?stats">.*?number">(.*?)</i>.*?dash">.*?number">(.*?)</i>.*?</a>',re.S)
	items = re.findall(pattern,content)
	for item in items:
		print item[0]+"\n"+item[1]+"\n"+item[2]+"\n"+item[3]+"\n"

except urllib2.URLError,e:
	if hasattr(e,'code'):
		print e.code
	if hasattr(e,'reason'):
		print e.reason
