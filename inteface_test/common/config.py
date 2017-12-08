# -*- coding:utf-8 -*-


def get_host():
    host = 'http://httpbin.org/'
    return host


sql_conn_dict = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'inteface',
    'charset': 'utf8'
}


if __name__ == '__main__':
    print get_host()