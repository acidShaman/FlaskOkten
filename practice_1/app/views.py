from app import app
from flask import render_template
from zipper import zipper
from users import users

@app.route('/')
def main():
    zipped = zipper()
    return render_template('all_users.html', zipped=zipped, users=users)


@app.route('/<userid>')
def user_by_id(userid):
    for user in users:
        if user.get('id') == int(userid):
            return render_template('user.html', user=user)

@app.route('/city/<city_name>')
def user_by_city(city_name):
    for user in users:
        if user.get('address').get('city').lower() == city_name:
            return render_template('user.html', user=user)
