#!/usr/bin/python
# _*_ coding: utf-8 _*_

__author__ = "heman793"
__date__ = "2017-7-31"

import requests
import re
import time
import os

# 构造 Request headers
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent':"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36"
}

session = requests.session()

# 获取_xsrf的值
def get_xsrf():
    '''_xsrf 是一个动态变化的参数'''
    index_url = "https://www.zhihu.com/"
    index_page = session.get(url=index_url,headers=headers)
    html = index_page.text
    pattern = r'name="_xsrf" value="(.*?)"'
    _xsrf = re.findall(pattern,html)
    return _xsrf[0]

# 获取验证码
def get_captcha():
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    # 用pillow 的 Image 显示验证码
    # 如果没有安装 pillow 到源代码所在的目录去找到验证码然后手动输入
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input("please input the captcha\n>")
    return captcha

#判断是否已经登录
def isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    setting_url = "https://www.zhihu.com/settings/profile"
    #allow_redirects 默认值为Ture，允许挑战
    response = session.get(url=setting_url,headers=headers,allow_redirects=False)
    login_code = response.status_code
    print response.url

    if login_code == 200:
        return True
    else:
        return False

def login(secret,account):
    _xsrf = get_xsrf()
    headers['X-Xsrftoken'] = _xsrf
    headers['X-Requested-With'] = 'XMLHttpRequest'
    post_url = 'https://www.zhihu.com/login/email'
    postdata = {
        '_xsrf':_xsrf,
        'password':secret,
        'email':account,
        'captcha_type':'cn'
    }

    # 不需要验证码直接登录成功
    login_page = session.post(post_url,data=postdata,headers=headers)
    login_code = login_page.json()
    if login_code['r'] == 1:
        # 不输入验证码登录失败
        # 使用需要输入验证码的方式登录
        postdata['captcha'] = get_captcha()
        login_page=session.post(post_url,data=postdata,headers=headers)
        #login_code = login_page.json()
       # print(login_code['msg'])
        print login_page.text

try:
    input = raw_input
except:
    pass

if __name__ == '__main__':
   if isLogin():
       print '您已经登录'
   else:
       account = input('请输入你的用户名\n>  ')
       secret = input('请输入你的密码\n>  ')
       login(secret, account)
