from app import app
from flask import render_template, request, redirect, url_for
from app.user_dict import Users


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again'
        else:
            return redirect(url_for('feed'))
    return render_template('login.html', error=error)

@app.route('/sign_up', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        if request.form['username'] in Users.dict_users:
            error = 'User with such name already exists, please try another one!'
        if len(request.form['password']) < 5 :
            error = 'Password too short, please try another one!'
        if request.form['password'].islower() or request.form['password'].isupper() or request.form['password'].isalpha() or request.form['password'].isdigit():
            error = 'Password is not OK. Password must me longer 5 chars, has lower and upper case letters and digits'
        else:
            Users.dict_users.update({request.form['username']: request.form['password']})
            return redirect(url_for('feed'))
    return render_template('register.html', error=error)



@app.route('/about-us')
def about_us():
    return render_template('about_us.html')


@app.route('/feed')
def feed():
    return render_template('base.html')