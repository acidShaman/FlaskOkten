from app import app
from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user
from app import db
from app.owners.models import UserModel
from app.forms import LoginForm, RegisterForm


@app.route('/')
def main():
    return redirect(url_for('owners.show_owners'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        email = request.form['email']
        password = request.form['password']
        user = UserModel.query.filter_by(email=email).first()
        print(user)
        if user.password == password:
            login_user(user)
            if user.is_admin:
                return redirect('/admin')
            else:
                return redirect(url_for('owners.show_owners'))
    return render_template('login.html', form=form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        email = request.form['email']
        password = request.form['password']
        user = UserModel(email=email, password=password, is_admin=False)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



