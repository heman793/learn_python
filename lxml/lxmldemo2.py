from lxml import etree

html = etree.parse('demo.html')
result = etree.tostring(html,pretty_print=True)
print result

