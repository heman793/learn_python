使用说明：
1、修改setting.py文件里面的SQLALCHEMY_DATABASE_URI为自己的数据库
2、执行脚本create_db.py创建数据库表结构
3、在数据库表b_user中随便添加一个用户(比如:root/root)
4、执行脚本runserver.py程序运行起来



主要依赖包：
flask
flask_sqlalchemy