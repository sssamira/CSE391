from flask import Flask, render_template, request, session, redirect, url_for
from models.client import *
from models.appointment import *
from database.dbconnect import *
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "blablabla"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'i' in session:
            if get_role(session['i']):
                return redirect(url_for('admin'))
            return render_template('c_dashboard.html')
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        is_success = authn(email, password)
        if is_success:
            session['i'] = get_userid(email)[0][0]
            if get_role(session['i']):
                return redirect(url_for('admin'))
            return render_template('c_dashboard.html')
        else:
            return render_template('login.html', error="Wrong email or password!")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        if 'i' in session:
            if get_role(session['i']):
                return redirect(url_for('admin'))
            return render_template('c_dashboard.html')
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
    
@app.route('/apointment', methods=['GET', 'POST'])
def appoint():
    if request.method == 'POST':
        license = request.form['license'] 
        engine = request.form['engine']
        app_day = request.form['app_day']
        client_id = session.get('i')
        total = all_mechanics()
        data = []
        for i in total:
            data.append((i[0], i[1], free_slots(app_day, i[0])))
        return render_template('appointment.html', client_id = client_id, license = license, engine = engine, app_day = app_day, data=data)
    
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'GET':
        if get_role(session['i']):   
            appointment = get_all_appointments()
            total = all_mechanics()
            all_infos = []
            data = []
            for i in total:
                data.append((i[0], i[1]))
            for j in appointment:
                client = get_client_info(j[1])
                mecha= get_mecha_name(j[4])[0][0]
                all_infos.append((j[0],client[0][0], client[0][1], j[2], j[3], mecha, j[5]))
            return render_template('admin.html', data= data, all_infos = all_infos)
        return redirect(url_for('login'))
    elif request.method == 'POST':
        id = request.form['appointment_id'] 
        tech = request.form['tech']
        app_day = request.form['app_day']
        is_success = change_appointment(id, tech, app_day)
        if is_success[0]:
            return redirect(url_for('admin', success="Appointment Changed Successfully!"))
        else:
            return redirect(url_for('admin', error=is_success[1]))

@app.route('/book' , methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        client_id = session.get('i')
        license = request.form['license']
        engine = request.form['engine']
        tech = request.form['tech']
        app_day = request.form['app_day']
        is_success = make_appointment(client_id, license, engine, tech, app_day)
        return is_success[1]  
        
@app.route('/logout')
def logout():
    session.pop('i', None)
    return redirect(url_for('login'))

app.run()