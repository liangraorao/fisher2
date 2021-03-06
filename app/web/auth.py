from app.form.auth import RegisterForm, LoginForm
from app.models.user import User
from . import web
from flask import render_template, request, redirect, url_for, flash
from app.models.base import db
from flask_login import login_user


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        res = user.check_password(form.password.data)
        if user and res:
            login_user(user, remember=True)
            # 如果不是以‘/’开头，跳转到首页
            next = request.args.get('next')
            if not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash("账号和密码不正确")
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
