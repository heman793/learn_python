from blogDemo.model.User import User
from blogDemo.model.Category import Category
from blogDemo import app, db
from flask import request, render_template, flash, abort, url_for, redirect, session


@app.route('/')
def show_all():
    categorys = Category.query.all()
    return render_template('show_all.html', entries=categorys)


@app.route('/add', methods=['POST'])
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


# @app.route('/del/<id>', methods=['POST'])
# def del_entry(id):
#     if not session.get('logged_in'):
#         abort(401)
#     id = request.form[id]
#     c = db.session.qu


@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        pwd = User.query.filter_by(password=password).first()

        if user is None:
            error = 'Invalid username'
        elif pwd is None:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_all'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_all'))