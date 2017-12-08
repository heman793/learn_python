#!/usr/bin/python
#-*- coding: utf-8 -*-
#爬取糗事百科
#2017-6-11


import urllib
import urllib2
import re
import thread
import time

class QSBK:
	
	def __init__(self):
	    self.pageIndex = 1
	    self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
	    self.headers = {'User-Agent':self.user_agent}
	    self.stories = []
	    self.enable = False

	def getPage(self,pageIndex):
	    try:
		url = 'https://www.qiushibaike.com/hot/page/' + str(pageIndex) + '/?s=4990275'
		request = urllib2.Request(url,headers=self.headers)
		response = urllib2.urlopen(request)
		pageCode = response.read().decode('utf-8')
		return pageCode
	    except urllib2.URLError,e:
		if hasattr(e,'reason'):	
		    print u"connect QSBK fail,reason:",e.reason
		    return None

	def getPageItems(self,pageIndex):
	    pageCode = self.getPage(pageIndex)
	    if not pageCode:
		 print "load page failed..."
		 return None
	    pattern = re.compile(r'<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?content">.*?<span>(.*?)</span>.*?stats">.*?number">(.*?)</i>.*?dash">.*?number">(.*?)</i>.*?</a>',re.S)
	    items = re.findall(pattern,pageCode)
	    pageStories = []
	    for item in items:
		replaceBR = re.compile(r'<br/>')
		text = re.sub(replaceBR,"\n",item[1])
		pageStories.append([item[0].strip(),text.strip(),item[2].strip(),item[3].strip()])
	    return pageStories

	def loadPage(self):
	    if self.enable == True:
		if len(self.stories) < 2:
		    pageStories = self.getPageItems(self.pageIndex)
		    if pageStories:
			self.stories.append(pageStories)
			self.pageIndex +=1

	def getOneStory(self,pageStories,page):
	    for story in pageStories:
		input = raw_input()
		self.loadPage()
		if input == "Q":
		    self.enable = False
		    return
		print  u"第%d页\t发布人:%s\t内容:%s\t赞:%s\t评论:%s" %(page,story[0],story[1],story[2],story[3])
    
	def start(self):
	    print u'reading QSBK,press a number and enter read new message,Q exit'
	    self.enable = True
	    self.loadPage()
	    nowPage = 0
	    while self.enable:
		if len(self.stories)>0:
		    pageStories = self.stories[0]
		    nowPage +=1
		    del self.stories[0]
		    self.getOneStory(pageStories,nowPage)


spider = QSBK()
spider.start()



