# -*- coding:utf-8 -*-
# 有些登录的接口会有验证码如：短信验证码，图形验证码等，这种登录的话验证码参数可以从后台获取的（或者查数据库最直接）。
# 获取不到也没关系，可以通过添加cookie的方式绕过验证码。

# 原理：
#1.一般登录后会生成一个已登录状态的cookie，只需要直接把这个值添加到cookies里面就可以了。
#2.可以先手动登录一次，然后抓取这个cookie，用抓包工具fiddler 或 charles
#3.然后往session里面添加cookie可以用以下方式

import requests

#打开登录首页，获取部分cookie
url = "https://passport.cnblogs.com/user/signin"
#设置headers
headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
            }

session = requests.session()
r = session.get(url,headers=headers,verify=False)

# 添加登录需要的cookie（手工抓登录后的包查看）
c = requests.cookies.RequestsCookieJar()
c.set('.CNBlogsCookie','EF9FE9F87E0FC33676DE736B7CEFE05A8D640C6A1ED035D648210202CA174F33B38B9E828C0D5FA794C259849E000D82B9E46FA1A6262CFE51DBBC9BB3549432253CA1C7D329D4374E7D5F93A7D8DAC57D3F214E')
c.set('.Cnblogs.AspNetCore.Cookies','CfDJ8PhlBN8IFxtHhqIV3s0LCDlhq4kEiDeRaQj5CK097TNs94h4PJbDxdE8tZeLT26e6k4GH0tfnadn6Q9O4bpogd00_LUhbat-A6cNld0GKCxHWQXOU9-wSVi4E8PTeoRWYEgLMx329_3NoMLfToiZgKrTNzyP4f9pPZfU2_xoRzyswjUI7aO0qOf9t3cQynZrBzHg6n-ZFcyiCk0xiOsq7_9YSb_v0pUwFRYW8SqyOepSarJLGur4vYzWv2BwnJ71gGpIE-A9LCqMW_rQyo0ypbHDzdBhRFF6-I9MQAeYpVyJXU9iU9rds-O4SNPcezlq-A')

session.cookies.update(c)

print session.cookies

#登录成功后发帖子
url_post = "https://i.cnblogs.com/EditPosts.aspx?opt=1"

data_post = {
    "__VIEWSTATE":"",
    "__VIEWSTATEGENERATOR":"FE27D343",
    "Editor$Edit$txbTitle":"title-requests",
    "Editor$Edit$EditorBody":"<p>content</p>",
    "Editor$Edit$Advanced$ckbPublished":"on",
    "Editor$Edit$Advanced$chkDisplayHomePage":"on",
    "Editor$Edit$Advanced$chkComments":"on",
    "Editor$Edit$Advanced$chkMainSyndication":"on",
    "Editor$Edit$lkbDraft": "存为草稿",
}

r1 = session.post(url_post,data=data_post,verify=False)
print r1.url
print r1.content
