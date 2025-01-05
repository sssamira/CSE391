from flask import Flask, request, render_template, session, redirect, url_for,jsonify
import requests
from models.user import *
from models.reminder import *
from models.exercise import *
from flask_mailman import Mail, EmailMessage
from models.sceduler import sched
from datetime import datetime
from models.email import sendemail 


app = Flask(__name__)
app.config["SECRET_KEY"] = "blablabla"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'shinzzzo123@gmail.com'
app.config['MAIL_PASSWORD'] = 'hjso bcdl odek hfbm'
mail = Mail()
mail.init_app(app)


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
            session['user_email'] = email
            return redirect('/userdashboard')
        else:
            return render_template('login.html', error="Wrong email or password!")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = request.args.get('error')
    if request.method == 'GET':
        if 'user_email' in session:
            return redirect(url_for('userdashboard'))
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
    error = request.args.get('error')
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
            return redirect(url_for('login', error= "Please login first!"))
        email = session['user_email']
        data = get_info(email)
        return render_template('userdashboard.html', user=data[0], bmi=data[1], bmi_category=data[2], bmr=data[3])
    
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'GET':
        if 'user_email' not in session:
            return redirect(url_for('login'))
        email = session['user_email']
        data = get_info(email)
        return render_template('profile.html', user=data[0], bmi=data[1], bmi_category=data[2], bmr=data[3])
        

@app.route('/reminder', methods=['GET', 'POST'])
def reminder():
    if request.method == 'GET':
        if 'user_email' not in session:
            return redirect(url_for('login'))
        rem = get_reminders(session['user_email'])
        return render_template('reminder.html', reminders=rem)
    elif request.method == 'POST':
        email = session['user_email']
        reminder_name = request.form['name']
        due_date = request.form['due_date']
        due_time = request.form['due_time']
        future_datetime = datetime.strptime(due_date + " " + due_time, "%Y-%m-%d %H:%M")
        job_time = future_datetime.strftime("%Y-%m-%dT%H:%M:%S")
        sched.add_job(sendemail, 'date', run_date=future_datetime, args=[reminder_name, email])
        is_success = add_reminder(email, reminder_name, due_date, due_time)
        if is_success:
            return redirect(url_for('reminder'))
        else:
            return redirect(url_for('reminder'))



@app.route('/editreminder', methods=['POST'])
def editreminder():
    if request.method == 'POST':
        id = request.form['edit_id']
        name = request.form['editname']
        date = request.form['edit_due_date']
        time = request.form['edit_due_time']
        is_success = edit_reminder(id, name, date, time)
        if is_success:
            return redirect(url_for('reminder'))
        else:
            return  redirect(url_for('reminder'))

@app.route('/deletereminder', methods=['POST'])
def deletereminder():
    if request.method == 'POST':
        id = request.form['edit_id']
        is_success = delete_reminder(id)
        if is_success:
            return redirect(url_for('reminder'))
        else:
            return  redirect(url_for('reminder'))


@app.route('/exercise', methods=['GET'])
def exercise():
    return render_template('exercise1.html')
@app.route('/meal', methods=['GET'])
def food():
    return render_template('food1.html')

# @app.route('/personalized-exercise', methods=['GET'])
# def personalized_exercise():
#     return render_template('quote.html')

@app.route('/arm-exercise', methods=['GET'])
def arm_exercise():
    result = get_exerciseby_typ("arms")
    return render_template('arm-exercise.html')


@app.route('/leg-exercise', methods=['GET'])
def leg_exercise():
    bodypart = ["lower legs", "upper legs"]
    return render_template('leg-exercise.html')

@app.route('/abdominal-exercise', methods=['GET'])
def abdominal_exercise():
    bodypart = ["chest","back","waist"]
    return render_template('abdominal-exercise.html')

@app.route('/cardio', methods=['GET'])
def cardio():
    bodypart = ["cardio"]
    return render_template('cardio.html')
@app.route('/extra', methods=['GET'])
def extra():
    bodypart = ["neck" ]
    return render_template('extra.html')





    



@app.route('/logout' , methods=['GET', 'POST'])
def logout():
    session.pop('user_email', None)
    return redirect(url_for('home'))

app.run(debug=True)
