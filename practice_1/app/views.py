from app import app
from flask import render_template
from zipper import zipper
from users import users


def get_user_by_id(uid):
    for user in users:
        if user.get('id') == uid:
            return user


@app.route('/')
def main():
    zipped = zipper()
    return render_template('all_users.html', zipped=zipped, users=users)


@app.route('/users/<user_id>')
def show_user(user_id):
    for user in users:
        if user.get('id') == user_id:
            return render_template('user_by_id.html', user=user)


