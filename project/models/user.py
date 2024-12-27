from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from database.dbconnect import get_session
from datetime import date

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'

    uid = Column(Integer, primary_key=True)
    fname = Column(VARCHAR)
    lname = Column(VARCHAR)
    dob = Column(VARCHAR)
    current_weight = Column(Integer)
    target_weight = Column(Integer)
    foodtype = Column(String)
    phone = Column(Integer)
    email = Column(VARCHAR, unique=True)
    password = Column(VARCHAR)
    height = Column(Integer)
    gender = Column(VARCHAR)

def add_user(email, fname, lname, date_of_birth, phone, password):
    session = get_session()
    user = session.query(Person).filter(Person.email == email).first()
    if user is not None:
        return (False, "Already registered!")
    new_user = Person(email=email, fname=fname, lname=lname, dob=date_of_birth, phone=phone, password=password)
    session.add(new_user)
    try:
        session.commit()
    except Exception as e:
        session.rollback() 
        return (False, "Error registering user!")
    return True
def add_info(email, current_weight, target_weight, foodtype, height, gender):
    session = get_session()
    user = session.query(Person).filter(Person.email == email).first()
    if user is None:
        return False
    user.current_weight = current_weight
    user.target_weight = target_weight
    user.foodtype = foodtype
    user.height = height
    user.gender = gender
    try:
        session.commit()
    except:
        return False
    return True

def authn(email, p):
    session = get_session()
    user = session.query(Person).filter(Person.email == email).first()
    if user is None:
        return False
    if user.password != p:
        return False
    return True

def get_info(email):
    session = get_session()
    user = session.query(Person).filter(Person.email == email).first()
    bmi = get_BMI(user.current_weight, user.height)
    bmr = get_BMR(user.current_weight, user.height, user.dob, user.gender)
    return (user, bmi, bmr)

def get_BMI(weight, height):
    return weight / (height**2)
def get_BMR(weight, height, dob, gender):
    birth_year, birth_month, birth_day = int(dob[:4]), int(dob[5:7]), int(dob[8:])
    today = date.today()
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
    height_cm = height * 100
    if gender == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height_cm *100) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height_cm* 100) - (4.330 * age) 
    return bmr


    

