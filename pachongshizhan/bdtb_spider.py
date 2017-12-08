#!/usr/bin/python
# _*_ coding: utf-8 _*_
#爬取百度贴吧
#2017-6-13

import urllib
import urllib2
import re

class Tool():
	"""删除无用的字符"""
	removeImg = re.compile('<img.*?>')
	removeBlank = re.compile(' {3,7}')
	removeAddr = re.compile('<a.*?>|</a>')
	removeBR = re.compile('<br>')

	def replaceContent(self,content):
		content = re.sub(self.removeImg,"",content)
		content = re.sub(self.removeBlank,"",content)
		content = re.sub(self.removeAddr,"",content)
		content = re.sub(self.removeBR,"\n",content)
		return content.strip()

class BDTB():
	"""抓取百度贴吧内容"""
	#初始化
	def __init__(self, baseURL,seeLZ):
		self.baseURL = baseURL
		self.seeLZ = '?see_lz='+str(seeLZ)
		self.tool = Tool()

	#获取帖子的HTML code
	def getPage(self,pageNum):
		try:
			url = self.baseURL + self.seeLZ + '&pn='+ str(pageNum)
			reuquest = urllib2.Request(url)
			response = urllib2.urlopen(reuquest)
			return response.read()
		except urllib2.URLError,e:
			if hasattr(e,"reason"):
				print u"connect baidutieba failed,reason:",e.reason
				return None

	#获取贴子标题
	def getTitle(self):
		pageCode = self.getPage(1)
		pattern = re.compile('<h3.*?core_title_txt pull-left text-overflow.*?>(.*?)</h3>',re.S)
		title = re.search(pattern,pageCode)
		if title:
			return title.group(1).strip()
		else:
			return None

	#获取帖子页数
	def getPageNum(self):
		pageCode = self.getPage(1)
		#pattern = re.compile('<li class="l_reply_num" style="margin-left:8px" >.*?class="red">(.*?)</span>页</li>',re.S)
		pattern = re.compile('共<span class="red">(.*?)</span>页</li>',re.S)
		pageNum = re.search(pattern,pageCode)
		if pageNum:
			return pageNum.group(1).strip()
		else:
			return None

	#获取楼层内容，传入参数：页面html code
	def getContent(self,pageCode):
		pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
		items = re.findall(pattern,pageCode)
		floor = 1
		for item in items:
			print "\n"
			print str(floor) + u"_楼--------------------------------------------------------------------------------------------------------------\n"
			print self.tool.replaceContent(item)
			floor = floor + 1
		#print self.tool.replaceContent(items[0])


baseURL = "https://tieba.baidu.com/p/3138733512"
bdtb = BDTB(baseURL,1)
#print bdtb.getPage(1)
print  "title:" + bdtb.getTitle()
print "共:" + bdtb.getPageNum() + "页"
#bdtb.getContent(bdtb.getPage(1))



