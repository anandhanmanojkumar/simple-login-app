from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            error = 'Please enter both username and password.'
    return render_template('login.html', error=error)

@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', name=session['username'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
