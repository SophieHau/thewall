from flask import Flask
from flask import render_template, request, redirect, url_for

from message import Message
from user import User

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def show_wall():
    
    m = Message()

    if request.method == 'POST':
        new_message = request.form.get('message')
        m.add_message(new_message, 'Frank Sinatra')
    
    messages = m.get_messages()
    
    m.close()   

    return render_template('index.html', messages=messages)
    

@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        u = User()
        username = request.form.get('username')
        password = request.form.get('password')
        if u.login(username, password) == True:
            return redirect(url_for('show_wall'))
    return render_template('login.html')

@app.route("/signup/", methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        u = User()
        new_username = request.form.get('new_username')
        new_password = request.form.get('new_password')
        u.signup(new_username, new_password)
    return render_template('signup.html')