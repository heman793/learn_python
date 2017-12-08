# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 创建项目对象
app = Flask(__name__)

# 加载配置文件内容
app.config.from_object('blogDemo.setting')  # 模块下的setting文件名，不用加py后缀
# app.config.from_envvar('FLASKR_SETTINGS')   # 环境变量，指向配置文件setting的路径

# 创建数据库对象
# db = SQLAlchemy(app)
db = SQLAlchemy()
db.init_app(app)

'''
在__init__.py 文件添加 from blog2.model import User,Category 时，直接放在文件的顶部，
这样就出现循环导入的问题， ImportError: cannot import name db 
把这句导入包的语句放在文件的最后就正常
'''
from blogDemo.model import User, Category
from blogDemo.controller import blog_message


