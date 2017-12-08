from lxml import etree

html = etree.parse('demo.html')
print type(html)
li = html.xpath("//li")
print li
print len(li)
print type(li)
print type(li[0])
