# -*- coding: utf-8 -*-

from blogDemo.model.User import User
from blogDemo.model.Category import Category
from blogDemo import app, db
from flask import request, render_template, flash, abort, url_for, redirect, session
from flask_login import login_required, login_user, logout_user, current_user
from flask_login import LoginManager

login_manager = LoginManager()  # 声明login对象
login_manager.init_app(app)     # 初始化绑定到应用
# 声明默认视图函数为login，当我们进行@require_login时，如果没登陆会自动跳到该视图函数处理
login_manager.login_view = "login"


@app.route('/')
@login_required
def show_all():
    categorys = Category.query.all()
    return render_template('show_all.html', entries=categorys)


@app.route('/add', methods=['POST'])
@login_required
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    title = request.form['title']
    content = request.form['text']
    category = Category(title, content)
    db.session.add(category)
    db.session.commit()
    flash("New entry was successfully posted")
    return redirect(url_for('show_all'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        error = None
        if request.method == 'POST':
            user = User.query.filter_by(username=request.form['username']).first()
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('show_all'))

    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('show_all'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()
