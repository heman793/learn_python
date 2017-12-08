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

#百度贴吧爬虫
class BDTB():
	"""抓取百度贴吧内容"""
	#初始化
	def __init__(self, baseURL,seeLZ):
		self.baseURL = baseURL
		self.seeLZ = '?see_lz='+str(seeLZ)
		self.tool = Tool()
		self.file = None
		self.defaultTitle = u"百度贴吧"
		self.floor = 1


	#传入页码，获取当页帖子的HTML code
	def getPage(self,pageNum):
		try:
			url = self.baseURL + self.seeLZ + '&pn='+ str(pageNum)
			#print url
			reuquest = urllib2.Request(url)
			response = urllib2.urlopen(reuquest)
			return response.read()
		except urllib2.URLError,e:
			if hasattr(e,"reason"):
				print u"connect bai_du_tie_ba failed,reason:",e.reason
				return None

	#获取贴子标题
	def getTitle(self,pageCode):
		pattern = re.compile('<h3.*?core_title_txt pull-left text-overflow.*?>(.*?)</h3>',re.S)
		title = re.search(pattern,pageCode)
		if title:
			return title.group(1).strip()
		else:
			return None

	#获取帖子一共有多少页
	def getPageNum(self,pageCode):
		pattern = re.compile('共<span class="red">(.*?)</span>页</li>',re.S)
		pageNum = re.search(pattern,pageCode)
		#print "pageNum:"+str(pageNum)
		if pageNum:
			return pageNum.group(1).strip()
		else:
			return None
	

	#获取楼层内容，传入参数：页面html code
	def getContent(self,pageCode):
		pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
		items = re.findall(pattern,pageCode)
		contents = []
		for item in items:
			content = "\n" + self.tool.replaceContent(item) + "\n"
			contents.append(content)
		return contents

	def setFileTitle(self,title):
		if title is not None:
			self.file = open(title + ".txt","w+")
		else:
			self.file =  open(self.defaultTitle + ".txt","w+")

	def writeData(self,contents):
		for item in contents:
			floorLine = "\n"+ u"-----------------------------------------------------------------------------------------\n"
			self.file.write(floorLine)
			self.file.write(item)

	def start(self):
		indexPage = self.getPage(1)
		pageNum = self.getPageNum(indexPage)
		title = self.getTitle(indexPage)
		self.setFileTitle(title)
		if pageNum == None:
			print u"URL 已失效，请重试"
			return
		try:
			print "该帖子共有" + str(pageNum) + "页"
			for i in range(1,int(pageNum)+1):
				print "正在写入第" + str(i) + "页数据"
				pageCode = self.getPage(i)
				contents = self.getContent(pageCode)
				self.writeData(contents)
		except IOError, e:
			print "写入异常，原因：" + e.message
		finally:
			print "写入任务完成"




print u"请输入帖子代号"
baseURL = 'http://tieba.baidu.com/p/' + str(raw_input('http://tieba.baidu.com/p/'))
#baseURL = "https://tieba.baidu.com/p/3138733512"
seeLZ = raw_input('是否只获取楼主发言，是：1，否：0\n')
bdtb = BDTB(baseURL,seeLZ)
bdtb.start()



