from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from database.dbconnect import get_session
from datetime import date

Base = declarative_base()

class reminder(Base):
    __tablename__ = 'reminder'

    appointment_id = Column(Integer, primary_key=True)
    appointment_name = Column(VARCHAR)
    lnadateme = Column(VARCHAR)
    a_time = Column(VARCHAR)
    reminder_date = Column(VARCHAR)


def add_reminder():
    pass

def edit_reminder():
    pass

def delete_reminder():
    pass

def set_reminder_done():
    pass