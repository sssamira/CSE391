from flask import Flask, request, render_template, session, redirect, url_for
from models.temp import *
app = Flask(__name__)
app.config["SECRET_KEY"] = "blablabla"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        is_success = authn(email, password)
        if is_success:
            return render_template('userdashboard.html')
        else:
            return render_template('login.html', error="Wrong email or password!")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        date_of_birth = request.form['dob']
        address = request.form['address']
        password = request.form['password']
        phone = request.form['phone']
        is_success = add_client(email, name, address, password, phone)
        if is_success[0]:
            return redirect(url_for('login', success="User registered!"))
        else:
            return render_template('signup.html', error=is_success[1])
    

@app.route('/datacollection', methods=['GET', 'POST'])
def datacollection():
    pass


app.run(debug=True)