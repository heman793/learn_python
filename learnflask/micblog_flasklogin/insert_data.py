from blogDemo.model import User, Category
from blogDemo import db


def insert_user(uname, pwd):
    u = User(uname, pwd)
    db.session.add(u)
    db.session.commit()


def insert_category(title, content):
    c = Category(title, content)
    db.session.add(c)
    db.session.commit()



if __name__ == "__main__":

    insert_user("admin", "admin")
    # insert_category("android", "ios")
