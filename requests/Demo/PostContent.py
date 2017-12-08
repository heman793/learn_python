# -*- coding:utf-8 -*-
# 模拟登录博客园后自动发帖子

import requests

url = "https://passport.cnblogs.com/user/signin"

#设置headers
headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/json; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "Content-Length":"385",
            "Cookie":"__utma=226521935.1731082838.1498201221.1499744466.1499744466.1; __utmz=226521935.1499744466.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); UM_distinctid=15d5822e3f496d-0da565aedf34f5-3066780a-fa000-15d5822e3f57a2; pgv_pvi=6394449920; _ga=GA1.2.1731082838.1498201221; _gid=GA1.2.532869340.1502782706; _gat=1; SERVERID=227b087667da6f8e99a1165002db93f6|1502866116|1502862739",
            "Connection":"keep-alive"
            }
data_login = {
        "input1":"cPTebVDmqsAlAgBmoCXgvlaoVy4nvdZE4emHcILZhdhYfoatbCLyxw0LfRYbLvmYbrqvqhJR+Mns9kBBs30TLQvl4XMQrN1OeN65nlkTLBIus0qcRoDRAE4OyvEXDcMqZLYrl/cAW1zIbpnnudLZ7KwPOXix/tAbUSfc570VDRg=",
        "input2":"lfs+oOTYdkMOJLlcnUgptmh0uhm3asWcKED0agEsNw7dD3SOEBwsma/5GvNQqqoq1nbp7jWOmSaE6tGOYzdhInM3pfup+KG+ETekP2XwI8kv5ezKubvPcTPMPVVanYZi/4k2kjjIRMB33R5A1RAb+v7n0L4rviWefRj4V0fTkZY=",
        "remember":True
        }

session = requests.session()
r = session.post(url,json=data_login,headers=headers,verify=False)

print r.json()

#发帖
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
print r1.content