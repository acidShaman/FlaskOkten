from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again'
        else:
            return redirect(url_for('feed'))
    return render_template('login.html', error = error)

@app.route('/about-us')
def about_us():
    return render_template('about_us.html')

@app.route('/feed')
def feed():
    return render_template('base.html')





if __name__ == '__main__':
    app.run()
