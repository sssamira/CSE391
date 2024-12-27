from flask import Flask, request, render_template, session, redirect, url_for

from models.user import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "blablabla"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = request.args.get('error')
    if request.method == 'GET':
        return render_template('login.html', error=error)
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        is_success = authn(email, password)
        if is_success:
            session[email] = email
            data = get_info(email)
            return render_template('userdashboard.html', user=data[0], bmi=data[1], bmr=data[2])
        else:
            return render_template('login.html', error="Wrong email or password!")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        email = request.form['email']
        fname = request.form['fname']
        lname = request.form['lname']
        date_of_birth = request.form['dob']
        password = request.form['password']
        phone = request.form['phone']
        is_success = add_user(email, fname, lname, date_of_birth, phone, password)
        if is_success:
            session['user_email'] = email
            return redirect(url_for('datacollection', success="User registered!"))
        else:
            return render_template('signup.html', error="Error registering user!")
    

@app.route('/datacollection', methods=['GET', 'POST'])
def datacollection():
    if request.method == 'GET':
        if 'user_email' not in session:
            return redirect(url_for('signup'))
        return render_template('datacollection.html')
    elif request.method == 'POST':
        email = session['user_email']
        current_weight = request.form['currentweight']
        target_weight = request.form['targetweight']
        foodtype = request.form['dietPreference']
        restriction = request.form['dietRestriction']
        height = request.form['height']
        gender = request.form['gender']
        is_success = add_info(email, current_weight, target_weight, foodtype, height, gender)
        if is_success:
            return render_template('login.html')
        else:
            return render_template('datacollection.html', error="Error registering user!")

@app.route('/userdashboard', methods=['GET', 'POST'])
def userdashboard():
    if request.method == 'GET':
        if 'user_email' not in session:
            return redirect(url_for('login'))
        


@app.route('/logout' , methods=['GET', 'POST'])
def logout():
    session.pop('user_email', None)
    return redirect(url_for('home'))

app.run(debug=True)