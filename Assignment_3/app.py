from flask import Flask, render_template, request, session
from models.client import authn, add_client
from models.appointment import make_appointment

app = Flask(__name__)

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
            return render_template('c_dashboard.html')
        else:
            # return render_template('login.html', is_success=is_success)
            return "rejected"

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
        return is_success[1]
    
@app.route('/apointment', methods=['GET', 'POST'])
def appoint():
    if request.method == 'GET':
        return render_template('appointment_form.html')
    elif request.method == 'POST':
        license = request.form['license'] 
        engine = request.form['engine']
        tech = request.form['tech']
        app_day = request.form['appapp_day_day']
        client_id = session.get('id')
        is_success = make_appointment(client_id, license, engine, tech, app_day)
        return is_success[1]

app.run()