from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from database.dbconnect import get_session
from datetime import date

Base = declarative_base()

class reminder(Base):
    __tablename__ = 'reminder'

    appointment_id = Column(Integer, primary_key=True)
    appointment_name = Column(VARCHAR)
    date = Column(VARCHAR)
    time = Column(VARCHAR)
    reminder_date = Column(VARCHAR)
    # reminder_time = Column(VARCHAR)
    user_email = Column(VARCHAR)


def add_reminder(email, reminder_name, due_date, due_time):
    session = get_session()
    new_reminder = reminder(appointment_name=reminder_name, date=due_date, time=due_time, user_email=email)
    session.add(new_reminder)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return False
    return True

def edit_reminder(id, name, date, time):
    session = get_session()
    my_reminder = session.query(reminder).filter(reminder.appointment_id == id).first()
    my_reminder.appointment_name = name
    my_reminder.date = date
    my_reminder.time = time
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return False
    return True

    

def delete_reminder():
    pass

def get_reminders(email):
    session = get_session()
    reminders = session.query(reminder).filter(reminder.user_email == email).all()
    return reminders