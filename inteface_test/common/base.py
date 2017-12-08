# -*- coding:utf-8 -*-

from common import config


def get_url(endpoint):
    '''获取url'''
    host = config.get_host()
    url = ''.join([host, endpoint])
    return url

