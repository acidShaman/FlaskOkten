from app import app
from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user
from app import db
from app.owners.models import UserModel


@app.route('/')
def main():
    return redirect(url_for('owners.show_owners'))


@app.route('/login')
def login():
    user = UserModel.query.get(2)
    login_user(user)
    return render_template('login.html')
